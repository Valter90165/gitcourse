# La regressione — ripasso completo

**Il blocco piu' richiesto dell'esame: circa 20 delle 37 domande di econometria
uscite all'orale.**

Questo documento tiene insieme i quattro blocchi (A basi, B risultati, C
multipla e stimatore, D ipotesi e violazioni) in **un solo filo**. Non e' un
riassunto: e' la stessa materia esposta **nell'ordine in cui ogni pezzo nasce da
una domanda aperta dal pezzo precedente** — ed e' quell'ordine la cosa da
possedere, perche' permette di ricostruire e non solo di ricordare.

Otto movimenti. In fondo, **le dieci frasi che tengono tutto**.

---

# Movimento 1 — Che cos'e', e a che domanda risponde

**La regressione e' la tecnica che stima la relazione fra una variabile
dipendente e una o piu' variabili esplicative.** Non e' una retta: **la retta e'
lo strumento** con cui la relazione viene rappresentata, **il coefficiente e' il
risultato**.

**A quale domanda risponde: non «esiste un legame?» ma «di quanto?»**.
Restituisce un numero, non un si' o un no. Questa e' la prima cosa da dire
sempre, perche' definisce la natura dello strumento.

**La variabile dipendente e' quella che il modello vuole spiegare. La variabile
esplicativa, o indipendente, e' quella che si usa per spiegare la dipendente.**
Non si memorizzano i due nomi: si chiede **chi spiega chi**, e i nomi vengono
dietro. Attenzione: l'esplicativa **spiega la dipendente**, non «spiega il
modello» — il modello e' l'attrezzo, non l'oggetto da spiegare.

**Due assi distinti, e non vanno mescolati.** **Semplice contro multipla**
riguarda **quante** esplicative ci sono: una sola, oppure due o piu'. **Lineare
contro non lineare** riguarda **la forma** della relazione: una retta, oppure
una curva. Non sono un'alternativa: si combinano, e la multipla di cui si parla
**e'** lineare.

**Il modello si compone di due parti**, e la domanda che le genera e' *quanto
spiego e quanto no?*: **la parte sistematica, cioe' cio' che il modello spiega**,
e **la parte stocastica, cioe' il termine di errore**, che raccoglie tutto cio'
che influenza la dipendente e non e' nel modello — variabili omesse, errori di
misura, casualita' intrinseca. **L'errore non e' un difetto: e' il modello che
dichiara di non spiegare tutto.**

**Errore e residuo non sono la stessa cosa. L'errore e' teorico, sta nella
popolazione, non e' osservabile. Il residuo e' quanto la stima si discosta
dall'osservazione, e si osserva nel campione.**

---

# Movimento 2 — Come si trova la retta

Domanda aperta dal movimento 1: *i punti non stanno su una retta — quale retta
si scegle?*

**Il residuo e' la distanza verticale fra il punto osservato e la retta**, cioe'
di quanto la retta sbaglia su quel caso.

**Il metodo si chiama minimi quadrati ordinari, in inglese OLS, in italiano
MQO. E' il metodo, non la retta**: la retta si chiama retta di regressione.

**Il criterio: fra tutte le rette possibili si scegle quella che rende minima la
somma dei quadrati dei residui.** Senza la parola «somma» la frase e'
tecnicamente sbagliata, perche' i residui non si possono minimizzare tutti
insieme uno per uno: si minimizza il loro totale.

**Perche' al quadrato — due ragioni.** I residui dei punti sopra e sotto la retta
hanno **segno opposto** e sommandoli si cancellerebbero: si avrebbe somma zero
anche con una retta pessima. E al quadrato **gli errori grandi pesano molto piu'
dei piccoli**, cosa desiderabile: meglio una retta che sbaglia poco su tutti che
una che azzecca quasi tutto e sbaglia enormemente su qualcuno.

*Tenere a mente questo secondo motivo: nel movimento 8 torna rovesciato, come
difetto.*

---

# Movimento 3 — I quattro numeri

Domanda aperta dal movimento 2: *trovata la retta, che cosa restituisce?*

**Quattro numeri, e ciascuno risponde a una domanda diversa. Le prime tre
riguardano un coefficiente; la quarta riguarda il modello intero.** Tenere
separate queste due cose e' meta' del movimento.

## «Quanto?» — il coefficiente

**Il coefficiente, cioe' di quanto varia la dipendente quando l'esplicativa
aumenta di una unita'.** **Si legge su tre elementi**: il **segno** da' la
direzione, la **grandezza** da' l'intensita', l'**unita' di misura** da' il
significato — e va sempre detta, perche' un coefficiente senza unita' di misura
non si puo' interpretare.

**L'intercetta, cioe' il valore che il modello attribuisce alla dipendente quando
l'esplicativa vale zero. Serve a posizionare la retta in altezza, non a essere
interpretata**, perche' lo zero dell'esplicativa spesso non ha senso economico.

## «Quanto mi fido?» — l'errore standard

Il coefficiente da solo e' muto: il modello ha lavorato su **un** campione.

**L'errore standard del coefficiente, cioe' la precisione della stima**: quanto
il coefficiente oscillerebbe se la stima fosse ripetuta su altri campioni
simili. **Si legge sempre in rapporto al coefficiente, mai da solo.** Piccolo:
stima affidabile. Grande: stima instabile, su un altro campione si poteva
trovare un valore molto diverso, perfino di segno opposto.

**Coefficiente ed errore standard si dicono sempre insieme**: la domanda e'
*«quanto, e quanto ci credo?»*, e all'orale li chiedono in coppia.

## «C'e' o non c'e'?» — la significativita'

**La statistica t, cioe' il rapporto fra il coefficiente e il proprio errore
standard.**

**Un coefficiente e' significativo quando e' grande rispetto alla propria
incertezza, cioe' quando si puo' escludere che il suo vero valore sia zero.**
Zero e' il valore che conta perche' corrisponderebbe all'**assenza di effetto**:
se il vero coefficiente fosse zero, quello che si vede nei dati sarebbe solo
rumore.

**Due trappole, simmetriche.** **Significativo non vuol dire importante**: un
coefficiente puo' essere significativissimo e minuscolo — la significativita'
riguarda la **certezza**, la grandezza riguarda la **rilevanza**. E **non
significativo non vuol dire assenza di effetto**: vuol dire che **con questi dati
non si puo' concludere nulla**. Non sapere e sapere che non c'e' sono cose
diverse.

## «E il modello?» — la bonta' di adattamento

Qui **cambia l'oggetto**. La domanda generatrice: *in quanti modi si puo' chiedere
«quanto si adatta»?*

*«Quanto spiega?»* → **l'R quadro, o coefficiente di determinazione, cioe' la
quota della variabilita' della dipendente spiegata dal modello**, fra zero e uno.

*«Quanto spiega, scontato il numero di variabili?»* → **l'R quadro corretto**,
che esiste perche' l'R quadro semplice **non diminuisce mai** aggiungendo
variabili, anche inutili, e quindi non serve a scegliere fra modelli; il corretto
**penalizza il numero di esplicative**.

*«Quanto sbaglia, nell'unita' di misura della dipendente?»* → **l'errore standard
della regressione, cioe' la dispersione dei residui**. *Nome simile a quello del
coefficiente, oggetto diverso: quello misura la precisione di una stima, questo
quanto sbaglia il modello intero.*

E per confrontare modelli diversi, **i criteri di informazione AIC e BIC**, che
bilanciano adattamento e numero di parametri.

## La domanda che viene subito dopo, ed e' uscita

*«Un modello con R quadro alto prevede bene?»* — **No. L'R quadro misura quanto
il modello aderisce ai dati con cui e' stato costruito, non quanto prevede su
dati nuovi.** Il perche': un modello puo' adattarsi quasi perfettamente ai dati
di partenza proprio perche' ha inseguito anche **le loro irregolarita'
casuali** — e quelle, nei dati nuovi, non ci sono. Un adattamento altissimo puo'
essere perfino il **sintomo** di un modello che non generalizzera'. **La capacita'
predittiva si verifica solo fuori campione.**

---

# Movimento 4 — Perche' una sola esplicativa non basta

Domanda aperta dal movimento 1: *le cause che restano fuori dove finiscono?*
Nell'errore. E finche' ci restano tranquille non e' un dramma.

**Il problema nasce quando una causa esclusa e' correlata con l'esplicativa
inclusa: il coefficiente della variabile inclusa si prende anche l'effetto di
quella esclusa, e il numero che si legge e' sbagliato. E' la distorsione da
variabili omesse.**

**Servono due condizioni insieme**, e dirlo vale punti: la variabile omessa deve
essere **rilevante** per la dipendente **e** **correlata con l'esplicativa
inclusa**. Se e' rilevante ma non correlata, **non c'e' distorsione**: il
coefficiente resta corretto, aumenta solo la parte non spiegata.

**La regressione multipla, cioe' quella in cui le esplicative sono due o piu',
stimate simultaneamente.** Il guadagno non e' aritmetico: **ogni coefficiente si
legge a parita' di tutte le altre variabili incluse.** La multipla **isola
l'effetto di ciascuna dalle altre**. Dire «usa piu' variabili» e' il *come*; dire
«a parita' delle altre» e' il *perche'*.

**Le due domande generatrici: cosa guadagno aggiungendo variabili, e cosa perdo?**
Il guadagno e' il ceteris paribus e meno distorsione. Il costo, tre cose.

**Includere una variabile irrilevante non distorce** — i coefficienti restano
centrati — **ma aumenta la loro varianza**, cioe' fa perdere precisione. Va detto
**in coppia con l'errore opposto**: **omettere una rilevante distorce**,
includerne una irrilevante **non distorce ma rende imprecisi**. Il primo errore
e' piu' grave, **ma il secondo non e' gratuito**.

**La multicollinearita', cioe' quando due o piu' esplicative sono fortemente
correlate fra loro** — fra loro, non con la dipendente. I coefficienti diventano
instabili e gli errori standard si gonfiano, perche' i dati non contengono
l'informazione per separarli. **Tre cose, e la seconda e' la trappola**: il
modello **nel complesso puo' restare buono**; **la multicollinearita' non produce
distorsione**, e' un problema di precisione e non di correttezza; quindi il
modello resta usabile **per prevedere e non per interpretare** i singoli
coefficienti. Caso estremo: **la multicollinearita' perfetta, cioe' quando una
esplicativa e' esattamente ricostruibile dalle altre — il modello non e' nemmeno
stimabile.**

**Le variabili dummy, cioe' variabili che valgono uno se la caratteristica e'
presente e zero se e' assente**, servono a inserire i caratteri qualitativi. **Con
k categorie se ne inseriscono k meno una**, e la categoria esclusa diventa il
**riferimento**. **Perche' una va esclusa**: inserendole tutte si ricade nella
multicollinearita' perfetta, perche' sommate darebbero sempre uno. E' la
**trappola delle dummy**, e collegarla alla collinearita' invece di citarla a
memoria vale punti.

---

# Movimento 5 — Che cosa si vuole dallo stimatore

Cambio di oggetto: non piu' il modello, ma **lo stimatore**, cioe' lo strumento
che produce le stime.

**In quanti modi uno stimatore puo' sbagliare? Due, indipendenti.**

**La distorsione, cioe' l'errore sistematico: lo stimatore e' centrato nel posto
sbagliato**, e ripetendo la stima si sbaglierebbe **sempre nella stessa
direzione**. E' il difetto grave: non si corregge con piu' dati dello stesso tipo.

**La varianza, cioe' l'instabilita': lo stimatore e' centrato bene ma oscilla
molto** da campione a campione. Mediamente azzecca, singolarmente balla.

**Il trade-off**: poiche' quello che interessa e' **sbagliare poco in totale**,
**a volte conviene accettare un po' di distorsione in cambio di una forte
riduzione della varianza.**

**Uno stimatore con grande varianza, cioe' che su un altro campione simile
avrebbe dato un valore molto diverso**: errore standard grande, coefficiente non
significativo, e **non si puo' concludere nulla**.

**BLUE, cioe' Best Linear Unbiased Estimator: il migliore stimatore lineare non
distorto.** Si legge all'indietro. **Estimator**: e' uno stimatore. **Linear**:
dentro la famiglia degli stimatori lineari. **Unbiased**: non distorto, centrato
sul valore vero — il primo difetto escluso. **Best**: a **varianza minima** — il
secondo difetto ridotto al minimo in quella famiglia. **BLUE e' la risposta
formale alle due cose che si vogliono da uno stimatore.**

---

# Movimento 6 — A quali condizioni tutto questo vale

Domanda aperta dal movimento 5: *lo stimatore dei minimi quadrati e' BLUE
sempre?* No. **Che cosa deve valere perche' i minimi quadrati funzionino?**
Cinque cose, piu' una che serve ad altro.

**Linearita' nei parametri**, cioe' la relazione deve essere lineare nei
coefficienti da stimare.

**Esogeneita', cioe' il termine di errore non deve essere correlato con le
esplicative.** E' la piu' importante: se cade, cade la correttezza.

**Omoschedasticita', cioe' la varianza dell'errore deve essere costante.**

**Assenza di autocorrelazione, cioe' gli errori non devono essere correlati fra
loro.**

**Assenza di multicollinearita' perfetta.**

E la sesta, che **non serve a BLUE**: **la normalita' dell'errore**. Serve per i
test e gli intervalli di confidenza, non per la proprieta' BLUE. Tenerle distinte
fa colpo, perche' molti le accorpano.

---

# Movimento 7 — Che cosa va storto quando non valgono

**Non si memorizza una lista di violazioni: si memorizzano le ipotesi, e poi ci
si chiede «quale ipotesi e' caduta?»**

## La frase che vale tutto il movimento

**Eteroschedasticita' e autocorrelazione rompono l'efficienza e i test;
l'endogeneita' rompe la correttezza.**

## Cade l'omoschedasticita' → eteroschedasticita'

**Eteroschedasticita', cioe' la varianza dell'errore non e' costante ma cambia al
variare delle esplicative.** Conseguenze, due e separate: lo stimatore **resta
non distorto**; ma **non e' piu' a varianza minima** e **gli errori standard
calcolati sono sbagliati**, quindi t e test non sono affidabili. **Il problema non
e' il coefficiente, e' il giudizio sul coefficiente.** Rimedi: **errori standard
robusti**, o minimi quadrati ponderati.

## Cade l'assenza di autocorrelazione → autocorrelazione

**Autocorrelazione, cioe' gli errori di periodi diversi sono correlati fra
loro.** Tipica delle **serie storiche**. Conseguenze **identiche**: non distorto,
non efficiente, errori standard sbagliati — quasi sempre **sottostimati**, quindi
si rischia di dichiarare significativo cio' che non lo e'.

## Cade l'esogeneita' → endogeneita'

**Endogeneita', cioe' una esplicativa e' correlata con il termine di errore.**
**E' la violazione grave: lo stimatore diventa distorto e inconsistente.**
«Inconsistente» significa che **la distorsione non si attenua aumentando i
dati**. Nelle altre due i coefficienti erano giusti e i test sbagliati; **qui e'
il coefficiente a essere sbagliato**, e non e' piu' interpretabile come effetto.

**Perche' una esplicativa puo' essere correlata con l'errore? Tre risposte:
variabili omesse** — una causa rilevante nell'errore e correlata con
l'esplicativa; **errori di misura** nell'esplicativa; **simultaneita' o causalita'
inversa** — la dipendente influenza a sua volta l'esplicativa.

## Il rimedio: le variabili strumentali

**Variabile strumentale, cioe' una variabile usata per isolare la parte esogena
di un'esplicativa endogena. Due condizioni, e vanno dette entrambe. Rilevanza:
correlata con l'esplicativa endogena. Esogeneita', o condizione di esclusione:
non correlata con il termine di errore**, cioe' non influenza la dipendente se
non passando per l'esplicativa endogena.

**La logica**: lo strumento fornisce una variazione dell'esplicativa che e'
pulita, perche' non dipende dall'errore; si usa solo quella, e il coefficiente
torna interpretabile.

---

# Movimento 8 — Le domande di coda

**Cambiare la scala di una variabile, cioe' cambiarne l'unita' di misura: non
cambia nulla di sostanziale.** Il coefficiente cambia in modo proporzionale, ma
**t, significativita' e R quadro restano identici**. **E' proprio per questo che
il coefficiente va sempre letto con la sua unita' di misura.** I **coefficienti
standardizzati** servono al problema opposto: confrontare l'importanza relativa
di variabili misurate in unita' diverse.

**Il modello teorico, cioe' la relazione come si suppone valga nella
popolazione**, con i parametri veri non osservabili: contiene **l'errore**. **Il
modello stimato, cioe' quello ottenuto sui dati del campione**: contiene i
**residui**. **Il teorico e' cio' che si vuole conoscere, lo stimato e' cio' che
si riesce a misurare** — la stessa distinzione di errore e residuo, al livello del
modello intero.

**Dati di stima e dati di verifica**: si stima su una parte e si controlla su
una parte tenuta da parte, perche' l'adattamento sui dati di stima non dice
nulla sulla previsione. **Confrontare valori osservati e previsti misura l'errore
di previsione**, che e' cio' che l'R quadro in-sample non misura.

**L'analisi di robustezza, cioe' rifare la stima cambiando specificazione,
campione o periodo, e verificare se il risultato tiene.** Se il coefficiente
cambia segno o perde significativita', **il risultato non e' robusto**.

**Il bootstrap, cioe' una tecnica di ricampionamento: dal campione osservato si
estraggono molti campioni con reinserimento, si ristima su ciascuno, e dalla
distribuzione delle stime si ricavano errore standard e intervalli di
confidenza.** Serve **quando la formula teorica dell'errore standard non e'
disponibile o le sue ipotesi non valgono**.

**Gli outlier, cioe' osservazioni molto distanti dal resto della
distribuzione.** **Qui torna il movimento 2 rovesciato**: poiche' i minimi
quadrati minimizzano la **somma dei quadrati**, un'osservazione molto lontana
pesa in modo sproporzionato e **puo' spostare la retta da sola**. Lo stesso
elevamento al quadrato che punisce gli errori grandi rende un dato anomalo capace
di dettare la retta. Cosa si fa: identificarli, verificare se sono **errori di
misura**, e confrontare la stima **con e senza** — che e' a sua volta un'analisi
di robustezza.

---

# Il confine, e con questo si chiude sempre

**La regressione misura associazione, non causalita'.** Due ragioni: puo'
esistere una **terza variabile** che muove entrambe, e il **verso** della
relazione puo' essere invertito.

Per passare alla causalita' serve il **paradigma controfattuale**, cioe'
chiedersi che cosa sarebbe accaduto allo stesso soggetto in assenza
dell'intervento, con esperimenti randomizzati, differenza-nelle-differenze e
regression discontinuity. **E' il secondo grande blocco di domande della
materia**, quindi questa chiusura apre la porta sull'argomento successivo.

---

# Le dieci frasi che tengono tutto

Se restasse tempo per una cosa sola, queste. Una per movimento, piu' due.

1. **La regressione e' la tecnica che stima di quanto la dipendente varia al
   variare dell'esplicativa: risponde non a «si' o no» ma a «di quanto».**
2. **L'esplicativa spiega la dipendente; semplice o multipla dipende da quante
   esplicative, lineare o non lineare dipende dalla forma.**
3. **La retta si trova coi minimi quadrati, cioe' si scegle quella che rende
   minima la somma dei quadrati dei residui: al quadrato perche' i segni opposti
   si cancellerebbero e perche' gli errori grandi devono pesare di piu'.**
4. **Il coefficiente dice quanto, l'errore standard dice quanto fidarsi, la
   significativita' decide se l'effetto c'e', l'R quadro giudica il modello
   intero.**
5. **Significativo non vuol dire importante, e non significativo non vuol dire
   assenza di effetto.**
6. **Adattarsi bene non e' prevedere bene: la capacita' predittiva si verifica
   solo fuori campione.**
7. **La multipla esiste perche' omettere una causa rilevante correlata con
   l'esplicativa distorce il coefficiente, e il suo guadagno e' leggere ogni
   coefficiente a parita' delle altre.**
8. **Da uno stimatore si vogliono due cose, non sbagliare il centro e ballare
   poco: BLUE e' esattamente questo, sotto le ipotesi del modello classico.**
9. **Eteroschedasticita' e autocorrelazione rompono l'efficienza e i test;
   l'endogeneita' rompe la correttezza, e si rimedia con le variabili
   strumentali.**
10. **Tutto questo misura associazione, non causalita': per la causalita' serve
    il paradigma controfattuale.**
