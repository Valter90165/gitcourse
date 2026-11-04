# Il blocco regressione — le dodici domande, spiegate

Su 37 domande di econometria uscite all'orale, circa **una ventina riguardano la
regressione**: e' il blocco che decide il voto della materia.

Questa scheda spiega, **nell'ordine delle dodici domande d'interrogazione**, tutto
cio' che serve per risponderle. Solo definizioni, nessun esempio.

---

# Blocco A — le basi

## 1. Che cos'e' la regressione e a che domanda risponde

La regressione e' la **tecnica** che stima la relazione fra una grandezza che si
vuole spiegare e una o piu' grandezze usate per spiegarla. Non e' una retta: la
retta e' lo strumento con cui la relazione viene rappresentata, il coefficiente
e' il risultato.

Risponde a una domanda di forma precisa: **non «c'e' un legame?» ma «di
quanto?»**. Restituisce un numero, non un si' o un no.

Il nome viene dagli studi ottocenteschi di Galton sull'ereditarieta' della
statura, dove i figli di genitori molto alti «regredivano» verso la media. Il
nome e' rimasto allo strumento.

## 2. Variabile dipendente e variabile esplicativa

La domanda generatrice e' una sola: **questa colonna la voglio spiegare, o la uso
per spiegare?** Ci sono solo due risposte possibili, quindi solo due tipi.

La **variabile dipendente** e' quella che il modello vuole spiegare, e si chiama
cosi' perche' il modello la fa dipendere dalle altre. La **variabile
esplicativa**, detta anche indipendente, e' quella che il modello usa per
spiegare.

Non si memorizzano i due nomi: si chiede **chi spiega chi**, e i nomi vengono
dietro.

## 3. La regressione lineare semplice

Stima la relazione fra la dipendente e **una sola** esplicativa. «Lineare»
perche' la relazione e' rappresentata da una retta, «semplice» perche'
l'esplicativa e' una sola.

Il modello si compone sempre di due parti, e la domanda che le genera e' *quanto
spiego e quanto no?*: una **parte sistematica**, cio' che il modello spiega, e
una **parte stocastica** — il **termine di errore** — che raccoglie tutto cio'
che influenza la dipendente e non e' nel modello: variabili omesse, errori di
misura, casualita' intrinseca. L'errore non e' un difetto del modello: e' il
modello che dichiara di non spiegare tutto.

**Errore e residuo non sono la stessa cosa**, ed e' una domanda d'orale.
L'errore e' teorico, sta nella popolazione, **non e' osservabile**. Il **residuo**
e' la sua controparte empirica: la differenza fra il valore osservato e il valore
stimato dal modello, e **si osserva**.

## 4. Il criterio con cui si individua la retta

Il metodo si chiama **minimi quadrati ordinari**, in inglese **OLS** — *Ordinary
Least Squares* —, in italiano anche **MQO**. E' il metodo, non la retta: la retta
si chiama retta di regressione.

Il criterio: per ogni punto osservato il residuo e' **la distanza verticale fra
il punto e la retta**; fra tutte le rette possibili si scegle quella che **rende
minima la somma dei quadrati dei residui**.

**Perche' al quadrato**, che e' la domanda immediatamente successiva. Per due
ragioni. I residui dei punti sopra e sotto la retta hanno **segno opposto** e
sommandoli si cancellerebbero: si avrebbe somma zero anche con una retta
pessima. E al quadrato **gli errori grandi pesano molto piu' dei piccoli**, cosa
desiderabile: meglio una retta che sbaglia poco su tutti che una che azzecca
quasi tutto e sbaglia enormemente su qualcuno.

---

# Blocco B — leggere i risultati

## 5. Coefficiente ed errore standard

Vanno trattati **come una coppia**, e la domanda che li genera entrambi e':
**«quanto, e quanto ci credo?»**

Il **coefficiente** risponde alla prima meta': dice **di quanto varia la
dipendente quando l'esplicativa aumenta di una unita'**. Si legge su tre piani:
il **segno** da' la direzione, la **grandezza** da' l'intensita', l'**unita' di
misura** da' il significato.

L'**errore standard** risponde alla seconda meta': misura la **precisione** della
stima, cioe' quanto il coefficiente oscillerebbe se la stima fosse ripetuta su
altri campioni. Piccolo rispetto al coefficiente, la stima e' affidabile; grande,
la stima e' instabile e su un altro campione si sarebbe potuto trovare un valore
molto diverso, perfino di segno opposto.

C'e' anche il secondo coefficiente, l'**intercetta**: il valore che il modello
attribuisce alla dipendente quando l'esplicativa vale zero. Serve a posizionare
la retta in altezza; spesso non ha significato economico **e non va
interpretata**.

## 6. Quando un coefficiente e' significativo

Un coefficiente e' significativo quando e' **grande rispetto alla propria
incertezza**, cioe' quando si puo' escludere che il suo vero valore sia zero.

Zero e' il valore che conta perche' corrisponderebbe all'**assenza di effetto**:
se il vero coefficiente fosse zero, quello che si vede nei dati sarebbe solo
rumore. Lo strumento che serve a deciderlo e' la **statistica t**, cioe' il
rapporto fra il coefficiente e il proprio errore standard.

**La trappola, ed e' una domanda d'orale: significativo non vuol dire
importante.** Un coefficiente puo' essere significativissimo e minuscolo. La
significativita' riguarda la **certezza** del risultato, la grandezza riguarda la
sua **rilevanza**: sono due giudizi distinti.

## 7. Le misure della bonta' di adattamento

La domanda chiede un plurale, quindi servono piu' misure, e la domanda
generatrice e': **in quanti modi si puo' chiedere «quanto si adatta»?**

«**Quanto spiega?**» → l'**R quadro**, o coefficiente di determinazione: la quota
della variabilita' della dipendente spiegata dal modello, fra zero e uno.

«**Quanto spiega, scontato il numero di variabili?**» → l'**R quadro corretto**,
o aggiustato. Serve perche' l'R quadro semplice **non diminuisce mai** quando si
aggiungono variabili, anche inutili, e quindi non puo' servire a scegliere fra
modelli; il corretto **penalizza il numero di esplicative**.

«**Quanto sbaglia, nell'unita' di misura della dipendente?**» → l'**errore
standard della regressione**, cioe' la dispersione dei residui.

Per il confronto fra modelli diversi si usano inoltre i **criteri di
informazione**, AIC e BIC, che bilanciano l'adattamento e il numero di parametri.

## 8. Gli indici di bonta' di adattamento misurano la capacita' predittiva?

**No**, e questa e' la risposta che va avuta pronta perche' la domanda e'
realmente uscita.

L'R quadro misura quanto il modello **aderisce ai dati con cui e' stato
costruito**; non misura quanto prevede su **dati nuovi**. Sono due cose diverse.

Il motivo: un modello puo' adattarsi quasi perfettamente ai dati di partenza
proprio perche' ha inseguito anche le loro **irregolarita' casuali** — e quelle
irregolarita', nei dati nuovi, non ci sono. Per sapere se un modello prevede
bisogna provarlo **fuori dal campione** su cui e' stato stimato.

---

# Blocco C — la multipla e lo stimatore

## 9. La regressione multipla, e perche' non basta la semplice

La **multipla** stima la relazione fra la dipendente e **due o piu'** esplicative
simultaneamente.

**Perche' non basta la semplice**: perche' i fenomeni economici hanno piu' cause
insieme. Se una causa rilevante resta fuori dal modello ed e' correlata con
l'esplicativa inclusa, il coefficiente di quest'ultima **assorbe anche l'effetto
di quella omessa** e risulta sbagliato. Si chiama **distorsione da variabili
omesse**.

**Il guadagno vero della multipla**, ed e' la frase che distingue la risposta
buona: nella multipla ogni coefficiente si legge **a parita' di tutte le altre
variabili**. La multipla non serve a guardare piu' variabili per comodita':
serve a **isolare l'effetto di ciascuna dalle altre**.

Le due domande generatrici del blocco: *cosa guadagno aggiungendo variabili?* —
il ceteris paribus e la riduzione della distorsione. *Cosa perdo?* — precisione, e
il rischio di multicollinearita'.

## 10. Che cosa accade inserendo una variabile irrilevante

Va risposto **in coppia con l'errore opposto**, perche' sono i due errori
simmetrici e la commissione li confronta.

**Includere una variabile irrilevante non distorce** i coefficienti: restano
centrati sul valore giusto. Ma **aumenta la varianza** delle stime, cioe' fa
perdere precisione: gli errori standard si gonfiano e i coefficienti rischiano di
risultare non significativi.

**Omettere una variabile rilevante, invece, distorce**: la stima sbaglia
sistematicamente.

Quindi il primo errore e' meno grave del secondo, **ma non e' gratuito**.

**Multicollinearita'.** Caso in cui due o piu' esplicative sono fortemente
correlate **fra loro**. I coefficienti diventano instabili e gli errori standard
si gonfiano. Il punto da dire: **il modello nel complesso puo' restare buono** —
R quadro alto, previsioni che tengono — **ma i coefficienti presi uno per uno non
sono piu' interpretabili**, perche' i dati non contengono l'informazione per
separarli.

**Variabili dummy.** Variabili che valgono zero o uno, con cui si inseriscono nel
modello i caratteri qualitativi. Con *k* categorie si inseriscono *k meno una*
dummy, e la categoria esclusa diventa il **riferimento** rispetto a cui si
leggono le altre; inserirle tutte rende il modello non stimabile.

## 11. La proprieta' BLUE

Significa **Best Linear Unbiased Estimator**: il **migliore stimatore lineare non
distorto**. Vale per lo stimatore dei minimi quadrati **a condizione che valgano
le ipotesi del modello classico** sull'errore — media nulla, varianza costante,
assenza di correlazione fra gli errori, assenza di correlazione fra errore ed
esplicative.

La domanda generatrice: **cosa si vuole da uno stimatore?** Due cose sole. Che
**non sbagli sistematicamente il centro** — ed e' la **non distorsione**. Che
**balli il meno possibile** fra campione e campione — ed e' la **varianza
minima**. «Migliore» significa appunto varianza minima, dentro la famiglia degli
stimatori lineari non distorti.

## 12. Distorsione e varianza, e il trade-off

Sono i **due difetti indipendenti** di uno stimatore, e la domanda generatrice e'
*in quanti modi uno stimatore puo' sbagliare?*

La **distorsione** e' l'errore **sistematico**: lo stimatore e' centrato nel
posto sbagliato, e ripetendo la stima su molti campioni si sbaglierebbe sempre
nella stessa direzione.

La **varianza** e' l'**instabilita'**: lo stimatore e' centrato bene ma oscilla
molto da campione a campione.

**Il trade-off**: poiche' cio' che interessa e' sbagliare poco **in totale**, e
non essere formalmente non distorti, **a volte conviene accettare un po' di
distorsione per ridurre molto la varianza**.

**Stimatore con grande varianza — cosa significa.** Che su un altro campione
simile si sarebbe ottenuto un valore molto diverso. Conseguenza: errore standard
grande, coefficiente non significativo, e **non si puo' concludere nulla** — che
non e' la stessa cosa che concludere l'assenza di effetto.

---

# Il confine del blocco

La regressione misura **associazione, non causalita'**. Due ragioni: puo'
esistere una **terza variabile** che muove entrambe, e il **verso** della
relazione puo' essere invertito.

Per passare alla causalita' serve il **paradigma controfattuale** — chiedersi
cosa sarebbe accaduto allo stesso soggetto in assenza dell'intervento — con
esperimenti randomizzati, differenza-nelle-differenze, regression discontinuity.
E' il secondo grande blocco di domande della materia.

# La frase d'attacco del blocco

*«La regressione risponde non a "si' o no" ma a "di quanto": il coefficiente dice
di quanto varia la dipendente per una unita' in piu' dell'esplicativa, l'errore
standard dice quanto ci si puo' fidare di quel numero, la multipla permette di
leggere ogni coefficiente a parita' delle altre, e il confine e' che tutto questo
misura associazione, non causalita'.»*
