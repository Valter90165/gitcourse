# La retta di regressione in sette gradini

*26 novembre 2026. Piano di studio completo: che cos'e', di che cosa e' fatta,
come si costruisce, come si giudica, come si specifica, quando e' valida,
che cosa non puo' dire. Con le risposte pronte per l'orale.*

| | Gradino | La domanda |
|---|---|---|
| 1 | Che cos'e' una regressione | *Che cosa sto facendo quando traccio quella retta?* |
| 2 | I pezzi della retta | *Di che cosa e' fatta?* |
| 3 | Come si trova la retta | *Perche' proprio quella?* |
| 4 | Quanto e' buona la retta | *Come dico se funziona?* |
| 5 | Da una a piu' variabili | *E se le cause sono tante?* |
| 6 | Quando ci si puo' fidare | *A quali condizioni e' valida?* |
| 7 | Che cosa non puo' dire | *Ho trovato una causa o no?* |

---

## 1 — CHE COS'E'

Strumento che studia come una variabile **dipendente** varia al variare di una o piu'
**esplicative**, sintetizzando la relazione in una funzione.

Tre decisioni dentro la definizione:
- **decidi tu chi dipende da chi** — la correlazione e' simmetrica, la regressione no;
  la scelta la da' la **teoria**, non il dato
- **accetti di semplificare** — la retta non descrive i punti, ne sintetizza la tendenza
- **spezzi la realta' in due** — *valore osservato = parte spiegata + parte non spiegata*.
  **Questa scomposizione E' la regressione.**

> «La regressione e' lo strumento che studia come una variabile dipendente varia al
> variare di una o piu' variabili esplicative, sintetizzando la relazione in una
> funzione, nel caso lineare una retta. Si distingue dalla correlazione per due
> aspetti: la correlazione e' simmetrica e misura soltanto l'intensita' del legame
> lineare, mentre la regressione e' asimmetrica, perche' presuppone una scelta teorica
> su quale variabile dipenda dalle altre, e consente di quantificare l'effetto. L'idea
> di fondo e' la scomposizione di ciascun valore osservato in una componente
> sistematica, spiegata dal modello, e una componente accidentale, che il modello non
> spiega.»

---

## 2 — I PEZZI

**Intercetta.** Valore atteso di Y quando le esplicative valgono zero. Ha significato
sostanziale **solo se lo zero e' plausibile**; altrimenti posiziona soltanto la retta.

**Coefficiente.** Di quanto varia Y all'aumentare di **una unita'** di X. Due parole
obbligatorie: **in media** e **a parita' delle altre**. E' il numero che interessa in
econometria.

**Termine di errore.** Tutto cio' che influenza Y e non e' nel modello. Non e' uno
sbaglio: e' la **parte non osservata** del fenomeno.

**COPPIA GEMELLA**

| | che cos'e' | dove vive |
|---|---|---|
| **errore** | distanza dal valore **vero** della popolazione | **teorico**, non osservabile |
| **residuo** | distanza dal valore **stimato** sul campione | **osservato**, calcolabile |

*L'errore appartiene al modello vero, il residuo alla mia stima.*

> «La retta di regressione e' definita da un'intercetta e da uno o piu' coefficienti,
> cui si aggiunge il termine di errore. L'intercetta e' il valore atteso della
> variabile dipendente quando le esplicative valgono zero, e ha significato sostanziale
> solo se lo zero e' un valore plausibile. Il coefficiente indica di quanto varia in
> media la variabile dipendente all'aumentare di un'unita' dell'esplicativa, a parita'
> delle altre variabili incluse nel modello. Il termine di errore raccoglie tutto cio'
> che influisce sulla variabile dipendente e non e' compreso fra le esplicative: non e'
> un errore di misurazione, ma la componente non osservata del fenomeno. Va distinto
> dal residuo, che e' la sua controparte empirica.»

---

## 3 — COME SI TROVA: I MINIMI QUADRATI

Si sceglie la retta che rende **minima la somma dei quadrati dei residui**.

**Perche' i quadrati — due ragioni, entrambe da dire:**
1. senza il quadrato positivi e negativi **si compenserebbero** e il criterio non
   distinguerebbe nulla
2. il quadrato **penalizza di piu' gli scostamenti grandi**: la retta non tollera
   punti molto lontani

*(E' la stessa logica dell'RMSE: lo stesso principio una volta per **costruire** la
retta, una volta per **giudicarla**.)*

**Due proprieta':** passa per il punto delle medie; la somma dei residui e' zero.
**Un avvertimento:** proprio perche' penalizza gli scostamenti grandi, il metodo e'
**sensibile agli outlier**, che vanno cercati **prima** di stimare.

---

## 4 — QUANTO E' BUONA

Due domande diverse, da tenere separate:
- **quanto spiega il modello nel complesso?** -> **R quadro**
- **quanto e' affidabile il singolo coefficiente?** -> **errore standard e significativita'**

### R quadro

Quota della variabilita' **della variabile dipendente** che il modello **spiega**.
Nasce dalla scomposizione *variabilita' totale = spiegata + residua*; e' il rapporto
fra spiegata e totale. Varia **fra 0 e 1**: 0 = non fa meglio della previsione della
media; 1 = tutti i punti sulla retta.

**L'idea in una frase:** *l'R quadro dice quanto il modello batte la media.*

**Perche' non puo' essere negativo dentro il campione:** la retta piatta all'altezza
della media e' **una delle rette fra cui i minimi quadrati scelgono**. Non puoi perdere
contro un avversario che sei libero di diventare. **Fuori campione puo' esserlo**,
perche' li' la scelta e' gia' stata fatta, sui vecchi dati.

**Limiti:** e' bonta' di **adattamento**, non bonta' del modello. Non garantisce
correttezza della specificazione, non autorizza conclusioni causali, non assicura
capacita' predittiva (e' calcolato dentro il campione). **Non diminuisce mai**
all'aggiunta di una variabile -> per confrontare modelli serve l'**R quadro corretto**,
che penalizza il numero di regressori, e' sempre <= R quadro e **puo' essere negativo**.

| | minimo | massimo |
|---|---|---|
| R quadro dentro il campione | **0** | 1 |
| R quadro corretto | **puo' essere negativo** | 1 |
| R quadro fuori campione | **puo' essere negativo** | 1 |

**Non esiste una soglia assoluta:** 0,2 su dati individuali puo' essere ottimo; 0,9 su
serie storiche macro e' ordinario.

### Errore standard e significativita'

**Errore standard:** di quanto la stima varierebbe da campione a campione.
*Il coefficiente e' il valore, l'errore standard e' quanto posso fidarmi del valore.*
Cresce con: poche osservazioni, poca variabilita' nella X, molto rumore residuo,
multicollinearita'.

**Significativita':** ipotesi nulla = coefficiente pari a zero nella popolazione; si
costruisce il rapporto fra coefficiente ed errore standard.
- **«non significativo» non vuol dire «nessun effetto»**: vuol dire prove insufficienti
  (asimmetria del processo penale)
- **significativita' statistica != rilevanza sostanziale**: su campioni enormi anche
  effetti minimi risultano significativi; su campioni piccoli effetti importanti no
- preferibile presentare l'**intervallo di confidenza**: valore e incertezza insieme

**SEGNALE DIAGNOSTICO:** R quadro alto + nessun coefficiente significativo =
**multicollinearita'**.

---

## 5 — LA MULTIPLA

Le variabili lasciate fuori **non spariscono**: finiscono nell'errore.

**Il ceteris paribus.** Nella multipla il coefficiente misura l'effetto di X
**a parita' delle altre variabili incluse**. Non cambia solo valore: **cambia
significato**. E vale **solo per le variabili effettivamente incluse**.

**Il controllo statistico.** Includere = controllare per. Stesso limite del matching:

| | che cosa controlla |
|---|---|
| **RCT** | **tutto**, anche il non osservato (sorteggio) |
| **Regressione multipla / matching** | **solo l'osservato e incluso** |

### La variabile omessa — il nemico

Variabile rilevante non inclusa, che resta nell'errore. Distorce se ricorrono
**due condizioni insieme**: (1) influenza Y; (2) e' correlata con una X inclusa.
La distorsione e' **sistematica** e **non si riduce aumentando il campione**.
Viola l'**esogeneita'** -> OLS non e' piu' corretto, non e' piu' BLUE.

### L'errore opposto (quesito 119)

| | effetto |
|---|---|
| variabile **omessa** | **distorce** -> problema di **correttezza** |
| variabile **irrilevante** | non distorce, **gonfia la varianza** -> **efficienza** |

*L'omessa sposta la stima, l'irrilevante la rende incerta.*

**Non si mette dentro tutto:** multicollinearita', e **controlli sbagliati** (includere
una variabile che e' essa stessa un effetto di X sottrae il canale che volevi misurare).
**Le variabili si scelgono con la teoria, non con i dati.**

---

## 6 — LE IPOTESI E LE VIOLAZIONI

Le cinque ipotesi di **Gauss-Markov**: **linearita'** nei parametri · **esogeneita'** ·
**omoschedasticita'** · assenza di **auto**correlazione · assenza di multicollinearita'
**perfetta**. Se valgono, OLS e' **BLUE**.

*(La normalita' degli errori NON serve per il BLUE: serve per l'inferenza esatta su
campioni piccoli.)*

**Attenzione ai due qualificatori**, che sono proprio l'ipotesi:
*auto*correlazione (errori fra loro, non variabili) · multicollinearita' *perfetta*
(quella non perfetta lascia BLUE, gonfia solo gli errori standard; quella perfetta
rende il modello **non stimabile**).

| Ipotesi violata | Che cosa si rompe | Corretto? | Gravita' |
|---|---|---|---|
| **Esogeneita'** (omessa, simultaneita', errore di misura) | **CORRETTEZZA** | **NO** | gravissima |
| **Linearita'** | correttezza | **NO** | grave |
| **Omoschedasticita'** | **EFFICIENZA** + errori standard | si' | media |
| **Autocorrelazione** | **EFFICIENZA** + errori standard | si' | media |
| **Multicollinearita'** non perfetta | efficienza | si' | gestibile |

> **L'endogeneita' attacca la STIMA. L'eteroschedasticita' e l'autocorrelazione
> attaccano l'INFERENZA.**

**COPPIA GEMELLA:** **corretto** = centrato sul vero (dove sta la stima) ·
**efficiente** = a varianza minima (quanto balla). Ed e' **efficiente**, non *efficace*.

### L'autocorrelazione

Errori di osservazioni successive correlati fra loro; tipica delle serie storiche.
**Cause:** inerzia del fenomeno · variabile omessa persistente · forma funzionale
sbagliata (spesso e' **sintomo di cattiva specificazione**).
**Effetti:** corretto si', efficiente no, **errori standard sottostimati** -> si
conclude per la significativita' quando non ci sono prove.
**Diagnosi:** esame dei residui nel tempo; test di **Durbin-Watson**.
**Rimedi:** prima la specificazione, poi errori standard robusti, poi modellare la
dinamica.

*Eteroschedasticita' = errori di dimensione diversa. Autocorrelazione = errori che si
ricordano del passato.*

---

## 7 — CHE COSA NON PUO' DIRE

Il coefficiente misura un'**associazione condizionata**, non una causa. Per leggerlo
causalmente serve una condizione in piu': l'**esogeneita'**.

**Le tre fonti di endogeneita'** — stessa firma: X correlata con l'errore.
1. **variabile omessa** (confondente)
2. **causalita' inversa o simultaneita'** — anche Y influenza X
3. **errore di misura** nelle esplicative

**L'esogeneita' non si verifica sui dati: si argomenta.** E' un'assunzione che si
difende con il **disegno**, non un risultato del calcolo.

### Le variabili strumentali

Uno **strumento** Z influenza X ma **non influenza Y se non attraverso X**.
Due proprieta':
- **rilevanza** — Z correlata con X: **verificabile sui dati**
- **esogeneita' / esclusione** — Z non correlata con l'errore: **NON verificabile, si argomenta**

**Due stadi:** si stima X in funzione di Z; si usa solo **la parte di X spiegata da Z**
— la porzione di variazione «innocente» — per stimare l'effetto su Y.

### La gerarchia dei disegni

| Disegno | Da dove viene l'esogeneita' |
|---|---|
| **RCT** | dal **sorteggio**: vale anche sul non osservato |
| **RDD, differenza-nelle-differenze, variabili strumentali** | da una fonte di variazione **quasi casuale** |
| **Regressione multipla, matching** | **assunta** sugli osservati — l'ipotesi piu' forte |

> **La causalita' non viene dallo stimatore: viene dal disegno.**

---

# I QUESITI ATTESTATI, GRADINO PER GRADINO

*Incrocio della scala con i 375 quesiti. Venticinque domande attestate ricadono
nei gradini 1-6.* ✅ prodotta · ◐ spiegata, mai testata · **–** mai aperta

| Gradino | N. | Quesito | |
|---|---|---|---|
| **1** | 113 | Che cos'e' un modello econometrico e a che serve per valutare le politiche | ✅ |
| | 114 | Che cosa sono la variabile dipendente e la variabile esplicativa | ✅ |
| | 115 | Che cos'e' la regressione lineare semplice | ✅ |
| | 130 | Differenza tra modello teorico e modello stimato | **–** |
| | 317 | Perche' una correlazione vicina a zero puo' coesistere con una relazione | **–** |
| **2** | 117 | Che cosa sono il coefficiente e l'errore standard | ✅ |
| | 290 | Come si interpreta l'intercetta | ✅ |
| **3** | — | **nessuna domanda attestata sui minimi quadrati** | |
| **4** | 211 | **Quali sono le misure della bonta' di adattamento** | **–** |
| | 212 | Un buon adattamento garantisce buone previsioni? | **–** |
| | 123 | Che cosa significa che uno stimatore ha una varianza grande | ✅ |
| | 172 | I risultati restano uguali su campioni diversi? | **–** |
| | 232 | Perche' confrontare valori osservati, stimati e previsti | **–** |
| | 244 | Differenza tra distorsione e varianza; il loro compromesso | ✅ |
| | 371 | Come si valuta una regressione fuori campione | ✅ |
| **5** | 118 | Che cos'e' la regressione lineare multipla | ✅ |
| | 119 | Che cosa succede se aggiungo una variabile irrilevante | ✅ |
| | 296 | Che cosa sono le variabili dummy | ✅ |
| | 120 | Che cosa significa cambiare la scala di una variabile | **–** |
| | 121 | Che effetto hanno gli outlier sui risultati | ◐ |
| | 352 | Che cosa sono gli outlier e quali effetti possono avere *(statistica)* | ◐ |
| | 233 | Come si costruisce un modello a partire dai valori osservati | **–** |
| | 223 | Che cosa significa «regressione sui residui» | **–** |
| **6** | 116 | Quali ipotesi devono essere rispettate in un modello di regressione | ✅ |
| | 124 | Che cosa indica la proprieta' BLUE | ✅ |
| | 173 | Che cosa significa BLUE per uno stimatore | ✅ |
| | 127 | Che cosa significa autocorrelazione in una serie storica | ◐ |

## Tre cose che l'incrocio rivela

1. **Il BLUE e' chiesto due volte** (124 e 173). E' la nozione a resa piu' alta
   di tutta la scala. Gia' a 28.
2. **Minimi quadrati, eteroschedasticita' e multicollinearita': zero domande
   attestate.** Restano utili come rilanci, ma non meritano altro tempo.
3. **Il gradino 4 e' il piu' battuto** — sette domande attestate — ed e' anche
   quello con piu' buchi: 211, 212, 172 e 232 mai aperte.
