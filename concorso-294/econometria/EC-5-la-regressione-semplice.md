# EC-5 — La regressione lineare semplice

**Manuale, Parte III.** Blocco che pesa piu' di ogni altro in econometria: su 37
domande di econometria uscite all'orale, circa una ventina riguardano la
regressione.

**Forma di questa scheda**: solo definizioni. Nessun esempio. Gli esempi si
chiedono a parte quando servono.

---

**Regressione lineare semplice.** Tecnica che stima la relazione lineare fra una
variabile dipendente e **una sola** variabile esplicativa. «Lineare» perche' la
relazione e' rappresentata da una retta, «semplice» perche' l'esplicativa e' una
sola. Con due o piu' esplicative si chiama multipla.

**Variabile dipendente.** La variabile che il modello vuole spiegare.

**Variabile esplicativa** (o indipendente). La variabile che il modello usa per
spiegare.

**Parte sistematica e parte stocastica.** Ogni modello econometrico si divide in
due: la parte sistematica e' cio' che il modello spiega, la parte stocastica e'
cio' che non spiega.

**Termine di errore** (o disturbo stocastico). La componente non spiegata:
raccoglie tutto cio' che influenza la dipendente e non e' nel modello —
variabili omesse, errori di misura, casualita' intrinseca. E' teorico e **non
osservabile**.

**Residuo.** La differenza fra il valore osservato della dipendente e il valore
stimato dal modello. E' la controparte **empirica e osservabile** dell'errore.
La distinzione errore/residuo e' una domanda d'orale: l'errore e' nella
popolazione, il residuo e' nel campione.

**Metodo dei minimi quadrati.** Criterio con cui si sceglie la retta: fra tutte
le rette possibili si prende quella che **minimizza la somma dei quadrati dei
residui**. Al quadrato per due ragioni: i residui di segno opposto non si
cancellano, e gli errori grandi pesano piu' dei piccoli.

**Coefficiente angolare** (beta). La stima che interessa. Esprime **di quanto
varia la variabile dipendente quando l'esplicativa aumenta di una unita'**. Si
legge su tre piani: il segno da' la direzione, la grandezza da' l'intensita',
l'unita' di misura da' il significato.

**Intercetta** (alfa). Il valore che il modello attribuisce alla dipendente
quando l'esplicativa vale zero. Serve a posizionare la retta in altezza; spesso
non ha significato economico e non va interpretata.

**Errore standard del coefficiente.** Misura la **precisione** della stima: e' la
variabilita' che il coefficiente avrebbe se la stima fosse ripetuta su altri
campioni. Piccolo rispetto al coefficiente, la stima e' affidabile; grande, la
stima e' instabile.

**Statistica t.** Il rapporto fra il coefficiente e il proprio errore standard.
Serve a stabilire la significativita'.

**Significativita'.** Un coefficiente e' significativo quando e' **grande
rispetto alla propria incertezza**, cioe' quando si puo' escludere che il suo
vero valore sia zero. Zero e' il valore che conta perche' corrisponderebbe
all'assenza di effetto. **Significativo non vuol dire importante**: riguarda la
certezza del risultato, non la sua rilevanza.

**R quadro** (coefficiente di determinazione). La **quota della variabilita'
della dipendente spiegata dal modello**. Varia fra zero e uno.

**Adattamento e capacita' predittiva.** Non coincidono. L'R quadro misura quanto
il modello aderisce ai dati su cui e' stato stimato; non misura la capacita' di
prevedere su dati nuovi. Un modello che insegue anche le irregolarita' casuali
del campione si adatta benissimo e prevede male. La capacita' predittiva si
verifica **fuori campione**.

**Associazione e causalita'.** La regressione misura associazione, non
causalita'. Due ragioni: puo' esistere una terza variabile che muove entrambe, e
il verso della relazione puo' essere invertito. Per la causalita' serve il
**paradigma controfattuale** — esperimenti randomizzati,
differenza-nelle-differenze, regression discontinuity.

---

## La frase d'attacco

*«La regressione risponde non a "si' o no" ma a "di quanto": il coefficiente
dice di quanto varia la dipendente per una unita' in piu' dell'esplicativa,
l'errore standard dice quanto ci si puo' fidare di quel numero, e il confine e'
che misura associazione, non causalita'.»*

## Le tre domande

1. Che cos'e' la regressione lineare semplice e con quale criterio si sceglie la retta?
2. Che cosa si intende per coefficiente ed errore standard?
3. Le misure di bonta' di adattamento dicono anche se il modello prevede bene?

## Dove continua

Le risposte a voce su questo blocco sono gia' scritte in
`concorso-294/ripetizione/02-la-regressione.md` (undici domande uscite
all'orale) e in `ripetizione/01-econometria-blocco-1.md` (dodici domande).
Non e' materiale nuovo da produrre: e' materiale da dire a voce.
