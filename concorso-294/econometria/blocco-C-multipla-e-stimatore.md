# Blocco C — la multipla e lo stimatore

Spiegato passo per passo, nell'ordine in cui i concetti si reggono l'uno
sull'altro. **L'ordine delle ultime due domande e' invertito** rispetto
all'elenco d'interrogazione: BLUE si definisce usando distorsione e varianza,
quindi quelle vengono prima.

Ogni termine e' scritto **gia' attaccato al suo pezzo di definizione**: il nome
nudo e' la cosa che si stacca.

---

## Passo 1 — Il problema da cui nasce la multipla

La regressione semplice usa **una sola** esplicativa, mentre i fenomeni
economici hanno **piu' cause insieme**. Le cause che restano fuori finiscono nel
termine di errore.

Il problema nasce quando una di quelle cause escluse e' **correlata con
l'esplicativa inclusa**: il coefficiente della variabile inclusa **si prende
anche l'effetto di quella esclusa**, e il numero che si legge e' sbagliato.

**Distorsione da variabili omesse, cioe' il coefficiente incluso assorbe
l'effetto di una variabile rilevante lasciata fuori.**

**Servono due condizioni insieme**, e dirlo vale punti: la variabile omessa deve
essere **rilevante** per la dipendente **e** **correlata con l'esplicativa
inclusa**. Se e' rilevante ma non correlata con quella inclusa, **non c'e'
distorsione**: il coefficiente resta corretto, aumenta solo la parte non
spiegata.

## Passo 2 — Il guadagno: il ceteris paribus

**Regressione multipla, cioe' quella in cui le esplicative sono due o piu',
stimate simultaneamente.**

Il guadagno non e' aritmetico: **nella multipla ogni coefficiente si legge a
parita' di tutte le altre variabili incluse.** Il coefficiente dice di quanto
varia la dipendente per una unita' in piu' di quella variabile, **tenendo ferme
le altre**. La multipla **separa** i contributi.

Dire «usa piu' variabili» e' il *come*. Dire «permette di leggere ogni
coefficiente a parita' delle altre, e quindi isola l'effetto di ciascuna» e' il
*perche'*.

*Frase: «la multipla serve perche' i fenomeni hanno piu' cause, e permette di
leggere ogni coefficiente a parita' delle altre variabili, isolando l'effetto di
ciascuna.»*

## Passo 3 — Il costo: le due domande generatrici

**Cosa guadagno aggiungendo variabili? e cosa perdo?**

**Includere una variabile irrilevante, cioe' che non ha effetto sulla dipendente,
non distorce i coefficienti** — restano centrati sul valore giusto — **ma aumenta
la loro varianza**: gli errori standard si gonfiano e coefficienti veri rischiano
di risultare non significativi.

Va detto **in coppia con l'errore opposto**: **omettere una variabile rilevante
distorce**, includerne una irrilevante **non distorce ma rende imprecisi**.

Il primo errore e' piu' grave del secondo, **ma il secondo non e' gratuito**: e'
il motivo per cui un modello non si costruisce buttandoci dentro tutto.

## Passo 4 — La multicollinearita'

**Multicollinearita', cioe' quando due o piu' esplicative sono fortemente
correlate fra loro** — fra loro, non con la dipendente.

Conseguenza: **i coefficienti diventano instabili e gli errori standard si
gonfiano**, perche' i dati non contengono l'informazione per separare l'effetto
dell'una da quello dell'altra.

**Tre cose da dire, e la seconda e' la trappola.** Primo: **il modello nel
complesso puo' restare buono** — R quadro alto, previsioni che tengono. Secondo:
**la multicollinearita' non produce distorsione** — i coefficienti restano non
distorti, diventano solo imprecisi; il problema e' di precisione, non di
correttezza. Terzo: il modello resta usabile **per prevedere e non per
interpretare** i singoli coefficienti.

Caso estremo: **la multicollinearita' perfetta, cioe' quando una esplicativa e'
esattamente ricostruibile dalle altre: il modello non e' nemmeno stimabile.**

## Passo 5 — Le variabili dummy

**Variabile dummy, cioe' una variabile che vale uno se la caratteristica e'
presente e zero se e' assente.** Serve a inserire nel modello i caratteri
qualitativi.

**La regola, e nasce dal passo 4:** con *k* categorie si inseriscono **k meno
una** dummy, e la categoria lasciata fuori diventa il **riferimento**, cioe'
quella rispetto a cui si leggono i coefficienti delle altre.

**Perche' una va esclusa:** inserendole tutte si ricade nella multicollinearita'
perfetta — le dummy sommate darebbero sempre uno, quindi una sarebbe
ricostruibile dalle altre. Si chiama **trappola delle dummy**. Collegare la
regola alla multicollinearita', invece di citarla a memoria, vale punti.

## Passo 6 — Distorsione e varianza

Cambio di oggetto: non piu' il modello, ma **lo stimatore**, cioe' lo strumento
che produce le stime.

**In quanti modi uno stimatore puo' sbagliare?** Due, indipendenti.

**La distorsione, cioe' l'errore sistematico: lo stimatore e' centrato nel posto
sbagliato.** Ripetendo la stima su molti campioni si sbaglierebbe **sempre nella
stessa direzione**. E' il difetto grave: non si corregge con piu' dati dello
stesso tipo.

**La varianza, cioe' l'instabilita': lo stimatore e' centrato bene ma oscilla
molto** da campione a campione. Mediamente azzecca, singolarmente balla.

**Il trade-off**: poiche' quello che interessa e' **sbagliare poco in totale**, e
non essere formalmente non distorti, **a volte conviene accettare un po' di
distorsione in cambio di una forte riduzione della varianza.** L'errore
complessivo combina le due componenti, e minimizzarne una sola non minimizza il
totale.

**Stimatore con grande varianza, cioe' che su un altro campione simile avrebbe
dato un valore molto diverso.** Conseguenza: errore standard grande, coefficiente
non significativo, e **non si puo' concludere nulla** — che non e' la stessa cosa
che concludere l'assenza di effetto.

## Passo 7 — BLUE

**BLUE, cioe' Best Linear Unbiased Estimator: il migliore stimatore lineare non
distorto.**

Si legge all'indietro. **Estimator**: e' uno stimatore. **Linear**: dentro la
famiglia degli stimatori lineari. **Unbiased**: non distorto, cioe' centrato sul
valore vero — il primo difetto del passo 6 e' escluso. **Best**: il migliore, e
«migliore» significa **a varianza minima** — il secondo difetto e' ridotto al
minimo dentro quella famiglia.

BLUE e' quindi **la risposta formale alle due cose che si vogliono da uno
stimatore**: non sbagliare il centro, e ballare il meno possibile.

**La condizione, e va sempre detta**: lo stimatore dei minimi quadrati e' BLUE
**se valgono le ipotesi del modello classico** sull'errore — media nulla,
varianza costante, assenza di correlazione fra gli errori, assenza di
correlazione fra errore ed esplicative. Quando una cade, la proprieta' si perde.

**Precisione che fa colpo:** la **normalita'** dell'errore **non serve** per
BLUE. Serve per i test e gli intervalli di confidenza, non per la proprieta' di
essere il migliore stimatore lineare non distorto.

---

## La frase d'attacco

*«La multipla esiste perche' omettere una causa rilevante correlata con
l'esplicativa distorce il coefficiente; il suo guadagno e' che ogni coefficiente
si legge a parita' delle altre, il suo costo e' la perdita di precisione, e lo
stimatore dei minimi quadrati, se valgono le ipotesi classiche, e' il migliore
stimatore lineare non distorto — cioe' centrato e col minimo di oscillazione.»*
