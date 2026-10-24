#!/bin/sh
# OCR di scansioni miste: decide foglio per foglio rotazione (0/270) e
# taglio (pagina intera o doppia pagina da separare), scegliendo la
# variante che produce piu' parole italiane riconoscibili.
# uso: ocr_mixed.sh <pdf> <nome> <dir_base>
set -e
export OMP_THREAD_LIMIT=1
SRC="$1"; NAME="$2"; BASE="$3"
W="$BASE/mx_$NAME"; rm -rf "$W"; mkdir -p "$W"
DICT='\b(della|delle|degli|dello|pubblica|bilancio|Stato|entrate|spese|che|non|per|sono|anche|art|legge|comma)\b'

python3 -I - "$SRC" "$W" <<'PY'
import pymupdf, sys, os
d=pymupdf.open(sys.argv[1]); out=sys.argv[2]
for i,p in enumerate(d):
    for ang in (0,270):
        m=pymupdf.Matrix(300/72,300/72).prerotate(ang)
        p.get_pixmap(matrix=m).save(os.path.join(out,f"f{i+1:03d}_{ang}.png"))
print(len(d))
PY
cd "$W"
for f in f*_*.png; do b="${f%.png}"; convert "$f" -crop 50%x100% +repage "${b}h-%d.png"; done
ls f*.png | xargs -P 4 -I{} sh -c 'tesseract "{}" "$(basename {} .png)" -l ita --psm 6 2>/dev/null'

: > "$BASE/$NAME.txt"
N=$(ls f*_0.png | wc -l)
i=1
while [ "$i" -le "$N" ]; do
  p=$(printf "%03d" "$i")
  BESTN=-1; BESTF=""
  for ang in 0 270; do
    # pagina intera
    cand="f${p}_${ang}.txt"
    n=$(grep -c -i -o -E "$DICT" "$cand" 2>/dev/null | wc -l)
    n=$(grep -o -i -E "$DICT" "$cand" 2>/dev/null | wc -l)
    [ "$n" -gt "$BESTN" ] && { BESTN=$n; BESTF="$cand"; }
    # doppia pagina separata
    cat "f${p}_${ang}h-0.txt" "f${p}_${ang}h-1.txt" > "f${p}_${ang}split.txt" 2>/dev/null || true
    n=$(grep -o -i -E "$DICT" "f${p}_${ang}split.txt" 2>/dev/null | wc -l)
    [ "$n" -gt "$BESTN" ] && { BESTN=$n; BESTF="f${p}_${ang}split.txt"; }
  done
  printf "\n=== foglio %s [%s, %d parole] ===\n" "$p" "$BESTF" "$BESTN" >> "$BASE/$NAME.txt"
  cat "$BESTF" >> "$BASE/$NAME.txt"
  i=$((i+1))
done
echo "  $NAME.txt: $(wc -c < "$BASE/$NAME.txt") bytes"
