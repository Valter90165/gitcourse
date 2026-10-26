# SE-1 — I numeri indici · scheda di sintesi

Manuale, Parte IV cap. 1, pp. 575-582. Costruita in sei passi il 26 ottobre.
Copre le domande 90, 94, 258 e 287 del repertorio (numeri indici, base fissa
e base mobile, indici di quantita').

---

## 0. Dove siamo

La statistica si divide in **metodologica** — la parte teorica, fondata sui
metodi per raccogliere e classificare i dati — e **applicata**, che prende
nomi diversi secondo la materia a cui si applica. La **statistica
economica** e' statistica applicata all'economia: il manuale ne dice che il
contributo e' stato fondamentale per **costruire modelli rappresentativi ed
esplicativi del sistema macroeconomico**.

**L'ISTAT** e' un **ente pubblico di ricerca**, sottoposto alla **vigilanza
della Presidenza del Consiglio dei ministri**, dotato di autonomia
**scientifica, statutaria e regolamentare, organizzativa, finanziaria,
patrimoniale e contabile**. Compiti principali: **censimenti generali**
(popolazione e abitazioni, industria e servizi, agricoltura) · predisposizione
ed esecuzione della maggior parte delle indagini del **programma statistico
nazionale** · **indirizzo e coordinamento** delle attivita' statistiche degli
enti del **SISTAN** · partecipazione al potenziamento del sistema statistico
europeo e internazionale.

## 1. Il numero indice e' un rapporto statistico

**I rapporti statistici** consentono di confrontare **intensita' o frequenze**
di due fenomeni, ed **eliminano l'effetto dell'unita' di misura**, dando
luogo a **numeri puri**. (La sottrazione no: resta dentro l'unita' di misura.)

- **frequenza** = il **numero di volte** in cui una modalita' si presenta
- **intensita'** = **l'ammontare o la misura** di un carattere additivo

Le quattro famiglie, distinte da **cosa sta al denominatore**:

| Rapporto | Al denominatore | Esempio |
|---|---|---|
| di **composizione** (parte al tutto) | il **totale** | quota degli alimentari sui consumi |
| di **densita'** | una dimensione **spaziale o temporale** | densita' della popolazione |
| di **durata** | il **flusso di rinnovo** (num.: consistenza media) | giacenza media in magazzino |
| di **ripetizione** | la **consistenza media** (num.: flusso di rinnovo) | rotazioni annue del magazzino |

Durata e ripetizione sono **l'una il reciproco dell'altra**.

**Il numero indice si distingue da tutti**: si costruisce ponendo al
denominatore **un'intensita' — detta base — della stessa natura del fenomeno
che e' al numeratore**. Prezzo su prezzo, quantita' su quantita'.

> Gli altri rapporti confrontano **due cose diverse** e creano una misura
> nuova. Il numero indice confronta **la stessa cosa in due situazioni**.

## 2. Come si legge

Indice **100** = nessuna variazione · **115** = **+15%** · **92** = **−8%**.
**Sottrai 100 e hai la variazione percentuale.**

Misura la **variazione relativa**, non la differenza assoluta: trenta
centesimi su due euro valgono il doppio di trenta centesimi su quattro.

## 3. Le due classi fondamentali

| | Confrontano | Esempio |
|---|---|---|
| **temporali** | lo stesso luogo in **due momenti** — dinamica temporale per variazioni relative | il pane a Roma, gennaio contro oggi |
| **spaziali** (o territoriali) | lo stesso momento in **due luoghi** | il pane oggi, Roma contro Milano |

**Temporali = quando · spaziali = dove.**

In economia le categorie principali sono tre: **prezzi, quantita', valori**.

## 4. Base fissa e base mobile

| | Denominatore | Cosa misura |
|---|---|---|
| **base fissa** | **un'unica intensita' che resta costante** | la **distanza dal punto di partenza** |
| **base mobile** (o **concatenati**) | **il termine precedente** | la **velocita' del cambiamento** |

Esempio, prezzo del pane: gen 2,00 · feb 2,10 · mar 2,10 · apr 2,40.

| | gen | feb | mar | apr |
|---|---|---|---|---|
| base fissa (gen) | 100 | 105 | **105** | 120 |
| base mobile | — | 105 | **100** | 114,3 |

**Marzo vale 105 a base fissa e 100 a base mobile**, e hanno ragione
entrambi: a marzo il pane costa il 5% in piu' che a gennaio, e non e'
cambiato rispetto a febbraio.

Le due serie sono **convertibili**: da base mobile a base fissa si dice
**concatenamento** (da cui il nome «concatenati»); mutare il periodo di
riferimento di una serie a base fissa si dice **cambiamento di base**.

## 5. Semplici e complessi, e i tre nomi

| Tipo | Cos'e' | Esempio |
|---|---|---|
| **semplici** (elementari) | rapporto fra misurazioni di **un unico fenomeno** | il prezzo di un prodotto |
| **complessi** (ponderati) | rapporto fra **due o piu' fenomeni eterogenei** | — |
| → **sintetici** | combinano **indici semplici** | il prezzo di una categoria |
| → **composti** | combinano **indici sintetici** | — |

Con piu' beni serve **ponderare**, perche' la media semplice tratterebbe il
caffe' come il pane. I pesi sono le **quantita'** — ma di quale anno?

| | **Laspeyres** | **Paasche** |
|---|---|---|
| pesi | quantita' dell'**anno base** | quantita' dell'**anno dato** |
| metodo | **dell'anno base** | **dell'anno dato** |
| i pesi nel tempo | **costanti** | **variabili** |
| pregio | semplice, **serie confrontabili** | **aggiornato e fedele** |
| difetto | **il paniere invecchia** | **complica il calcolo** |

**Paasche** conviene dove si dispone **congiuntamente e simultaneamente** di
prezzi e quantita' (esempio del manuale: le **contrattazioni borsistiche**).

**L'ISTAT usa Laspeyres**, per la **costanza nel tempo del paniere**: misura
variazioni di prezzi **a paniere costante**. Il difetto si corregge
**aggiornando il paniere ogni anno**.

**Fisher** e' la **media geometrica** di Laspeyres e Paasche. Ma il manuale
annota che nella pratica si preferiscono Laspeyres e Paasche, **soprattutto
il primo**.

## 6. Le proprieta'

**Indici semplici — quattro:**

- **identita'**: confronto con se stesso → 1 (o 100)
- **reversibilita' delle basi**: scambiando numeratore e denominatore si ottiene il **reciproco**
- **reversibilita' dei fattori** (o **decomposizione delle cause**): poiche' **valore = prezzo × quantita'**, l'indice di valore e' il prodotto degli indici di prezzo e di quantita' → **noti due dei tre, il terzo e' determinato**
- **transitivita'** (o **circolarita'**): permette di **cambiare la base** e di **concatenare**

**Indici sintetici — le quattro di sopra, piu' tre:**

- **commensurabilita'**: l'indice non varia al variare dell'**unita' di misura**
- **determinatezza**: non si annulla ne' tende all'infinito se un termine elementare si annulla o tende all'infinito
- **proporzionalita'**: se i prezzi variano **proporzionalmente**, l'indice varia **secondo lo stesso coefficiente**

> ⚠️ **Laspeyres e Paasche NON soddisfano**: **reversibilita' delle basi** ·
> **transitivita'** (per cui *il confronto fra due termini qualunque della
> serie non e' attuabile*) · **decomposizione delle cause**.
>
> Le proprieta' valgono per gli **indici semplici**: appena si introduce la
> **ponderazione**, il risultato dipende anche dal paniere scelto e tre
> proprieta' si perdono. **E' il prezzo della sintesi.**

## 7. Gli indici di quantita'

I ruoli si scambiano, il meccanismo e' lo stesso:

| | Cosa misura | Cosa usa come peso |
|---|---|---|
| indice di **prezzo** | i prezzi | le **quantita'** |
| indice di **quantita'** | le quantita' | i **prezzi** |

| | **Laspeyres** | **Paasche** |
|---|---|---|
| indice di **prezzo** | quantita' dell'anno **base** | quantita' dell'anno **dato** |
| indice di **quantita'** | prezzi dell'anno **base** | prezzi dell'anno **dato** |

**Laspeyres guarda sempre alla base, Paasche sempre all'anno dato**: cambia
solo *cosa* si tiene fermo.

**A cosa servono**: alla **decomposizione delle cause**. Se una spesa cresce
del 10%, puo' essere perche' i prezzi sono saliti o perche' si consuma di
piu'. L'indice di valore non lo distingue; prezzo e quantita' separati si'.
Per un funzionario e' *la* domanda, perche' la risposta cambia la politica.

---

## La sera prima — gli otto fatti

1. il numero indice ha al denominatore **un'intensita' della stessa natura**, detta **base**
2. **indice − 100 = variazione percentuale**
3. **temporali = quando · spaziali = dove**
4. **base fissa = distanza dal punto di partenza · base mobile = velocita' del cambiamento**
5. **base mobile → base fissa = concatenamento**
6. **Laspeyres pesa alla base · Paasche all'anno dato · Fisher e' la media geometrica**
7. **l'ISTAT usa Laspeyres, a paniere costante, aggiornato ogni anno**
8. **Laspeyres e Paasche perdono tre proprieta': reversibilita' delle basi, transitivita', decomposizione delle cause**
