# Econometria

## Sintesi ragionata sul manuale, per la prova orale

*Concorso RIPAM 294 unità — Codice 02, Area dei funzionari — prova orale del 27 novembre 2026*

Questa dispensa è costruita sulla **Parte III del manuale** — *Econometria e metodi qualitativi e quantitativi* (Simone, edizione per il concorso RIPAM 294) — **pagine stampate 261-571**, lette integralmente. Sono **sedici capitoli**, dalla statistica descrittiva alla valutazione controfattuale delle politiche pubbliche.

> **La regola che hai fissato, e che ho seguito alla lettera.** Dalle testimonianze raccolte all'orale **non chiedono formule**. Quindi: **nessuna derivazione, nessuna dimostrazione, nessun passaggio algebrico**. Le formule che contano davvero sono raccolte **tutte insieme alla fine**, nel riquadro *«Le venti formule fondamentali»*, così le valuti in blocco e decidi tu quali memorizzare. Nel corpo della dispensa compaiono solo quando **scriverle è più chiaro che descriverle a parole**, e sempre accompagnate da ciò che davvero conta: **che cosa significano e come si leggono**.
>
> Il criterio che ho usato per selezionarle: una formula entra solo se **saperla rende la risposta migliore**. Tutte le altre — e nel manuale ce ne sono centinaia — le ho **tradotte in italiano**, perché a un funzionario si chiede di saper interpretare un output, non di ricavarlo.

**Come è organizzata.** Le parti seguono i capitoli del manuale, ma il peso non è uniforme: ho dato più spazio a ciò che una commissione chiede davvero — **il significato delle ipotesi classiche, che cosa succede quando cadono, come si legge un output di regressione, e tutta la parte finale sulla valutazione delle politiche**, che è il ponte diretto con l'altra materia del tuo bando. Alla statistica descrittiva e al calcolo delle probabilità, che sono premesse strumentali, ho dato lo spazio che serve a non essere colti impreparati, non uno di più.

---

# Parte I — Statistica descrittiva

*(Capitolo 1 del manuale, pp. 261-300 circa)*

## 1. Il vocabolario di base

Un'**indagine statistica** è un'operazione condotta, mediante l'osservazione, su elementi di un determinato collettivo, con l'obiettivo di distinguerli e classificarli secondo le **modalità** di uno o più **caratteri**.

- l'**unità statistica** è la componente elementare del collettivo, quella su cui si acquisiscono le informazioni. Si distingue in **semplice** (una persona, un'impresa), **composta** (insieme di unità semplici simili, esistenti anche a prescindere: la famiglia, un edificio) e **complessa** (insieme di unità semplici *diverse*, che la caratterizzano nella loro totalità: un processo produttivo);
- i **caratteri** sono gli aspetti del fenomeno rilevato e si distinguono in **qualitativi** (professione, genere di attività) e **quantitativi** (reddito, età, produzione);
- le **fasi** dell'indagine sono quattro: **identificazione del collettivo**, **rilevazione** (totale o campionaria), **elaborazione** (classificazione in tabelle e grafici, sintesi), **interpretazione**.

**Distribuzione statistica** è l'insieme delle determinazioni del carattere e delle rispettive frequenze. Si chiama **variabile statistica** se il carattere è quantitativo, **mutabile statistica** se è qualitativo. Le mutabili si distinguono in **rettilinee** (esiste un ordine naturale o logico: gli operai per livello), **serie storiche** (il principio regolatore è il tempo), **cicliche** (il tempo è inteso come periodicità: non c'è né una modalità iniziale né una finale), **sconnesse** (nessun ordine: i voti ai partiti).

Le **frequenze** sono **assolute**, **relative** (divise per il totale), **percentuali**, **cumulate** (quante osservazioni hanno un valore minore o uguale a una data modalità).

> **Il punto che vale un'osservazione all'orale.** La distinzione fra carattere qualitativo e quantitativo — e, dentro i qualitativi, fra ordinabili e sconnessi — **non è una classificazione scolastica: decide quali statistiche siano lecite**. Su una mutabile sconnessa la media non ha alcun senso, sulla rettilinea ha senso la mediana ma non la media, e solo sulle variabili quantitative si può calcolare tutto. È lo stesso principio che ritroverai nelle scale di misura della data science: **è la natura del dato a vincolare l'analisi, non la disponibilità del software**.

## 2. Gli indici di posizione

Le **medie** si distinguono in **analitiche** — che considerano *tutti* i valori: aritmetica, quadratica, armonica, geometrica — e **lasche**, che ne considerano solo alcuni: mediana e moda.

| Media | Invarianza che la definisce | Quando si usa |
|---|---|---|
| **Aritmetica** | lascia invariata la **somma** delle intensità | è la media per eccellenza; l'unica **traslativa** |
| **Quadratica** | lascia invariata la **somma dei quadrati** | quando contano le grandezze in valore assoluto (errori, scarti) |
| **Armonica** | lascia invariata la **somma dei reciproci** | medie di **rapporti**: velocità, prezzi unitari, produttività |
| **Geometrica** | lascia invariato il **prodotto** delle intensità | **tassi di variazione**, saggi di crescita composti |

**La relazione fondamentale fra le medie** — vale sempre, ed è una di quelle cose che conviene sapere a memoria:

> **M<sub>armonica</sub> ≤ M<sub>geometrica</sub> ≤ M<sub>aritmetica</sub> ≤ M<sub>quadratica</sub>**

L'uguaglianza vale solo se tutte le intensità sono uguali fra loro.

**Le proprietà della media aritmetica** (quattro, e sono quelle che la rendono lo strumento privilegiato): è **interna** (compresa fra il minimo e il massimo); è **traslativa** (se a tutti i valori si somma una costante, la media aumenta della stessa costante); è **omogenea** (se tutti i valori si moltiplicano per una costante, la media si moltiplica per la stessa costante); è **associativa** (la media generale è la media ponderata delle medie parziali). Le altre tre medie sono interne, omogenee e associative **ma non traslative**.

**Le due proprietà degli scarti dalla media** — e queste sono importanti perché tornano in tutta l'econometria:

- la **somma algebrica degli scarti dalla media aritmetica è zero**;
- la **somma dei quadrati degli scarti è minima** quando gli scarti si calcolano dalla media aritmetica.

> **Tienile a mente: la seconda è la ragione per cui esiste il metodo dei minimi quadrati.** Quando in econometria si stimerà una retta «minimizzando la somma dei quadrati dei residui», si starà applicando a due dimensioni esattamente questa proprietà. Dirlo all'orale, quando arrivi alla regressione, mostra che hai visto il filo che lega il primo capitolo al settimo.

**Moda** — la modalità con la frequenza più alta. Può non esistere e può non essere unica (distribuzioni *unimodali*, *plurimodali*, *zeromodali*). Attenzione al caso delle **classi di diversa ampiezza**: la classe modale non è quella con più casi, ma quella con la **densità di frequenza più alta** (frequenza divisa per ampiezza della classe). Il manuale dedica a questo un esempio, perché è l'errore classico.

**Mediana** — il valore che **bipartisce** la distribuzione, lasciando metà dei casi a sinistra e metà a destra. Le sue due proprietà: il numero degli scarti positivi uguaglia quello dei negativi; la **somma dei valori assoluti degli scarti dalla mediana è minima**.

**Percentili** — intensità che dividono la distribuzione lasciando da un lato una data percentuale di casi. **Terzili** (2), **quartili** (3, di cui il secondo coincide con la mediana), **decili** (9), **centili** (99).

> **Media o mediana?** È la domanda che una commissione può fare per capire se ragioni. La risposta: la **media** usa tutta l'informazione ma è **sensibile ai valori estremi**; la **mediana** è **robusta** ma ignora la struttura interna. Su dati fortemente asimmetrici — e i **redditi** lo sono sempre — la media è tirata verso l'alto dalla coda dei valori alti e **descrive male l'individuo tipico**: è la ragione per cui l'ISTAT pubblica il reddito *mediano* delle famiglie e non solo quello medio.

## 3. Gli indici di variabilità

Sapere dov'è il centro non basta: serve sapere quanto i dati si disperdono intorno ad esso.

**Indici di posizione (grezzi):** il **campo di variazione** (massimo − minimo) e la **differenza interquartilica** (terzo quartile − primo quartile, che racchiude il 50% centrale dei casi). Entrambi hanno il difetto di **non tenere conto della struttura interna** della distribuzione; il campo di variazione, in più, è influenzato dai valori anomali e non è calcolabile se le classi estreme sono aperte.

**Indici analitici (di dispersione):**

- **scostamento semplice medio** dalla media aritmetica o dalla mediana: la media dei **valori assoluti** degli scarti;
- **devianza**: la somma dei quadrati degli scarti dalla media;
- **varianza**: la devianza divisa per la numerosità;
- **scarto quadratico medio (deviazione standard)**: la radice della varianza. È l'indice principe, ed è espresso **nella stessa unità di misura** del fenomeno.

**Il coefficiente di variazione** è il rapporto fra scarto quadratico medio e media aritmetica (di solito in percentuale). È un **numero puro**, e serve a una cosa precisa: **confrontare la variabilità di distribuzioni espresse in unità di misura diverse**, o con ordini di grandezza molto diversi. Se ti chiedono «è più variabile il reddito o l'altezza?», la risposta passa di qui.

**La standardizzazione** — dividere gli scarti dalla media per lo scarto quadratico medio — produce valori adimensionali a media 0 e varianza 1. È l'operazione che consente il confronto fra grandezze eterogenee, e la stessa che in data science si chiama *z-score*.

**Differenze medie** (con e senza ripetizione): misurano la **disuguaglianza media fra le intensità**, confrontando tutti i termini a due a due. A differenza degli scostamenti, non guardano a un centro ma **ai dati fra loro**: è un'idea diversa di variabilità, ed è quella che porta agli indici di concentrazione.

**Gli indici di concentrazione.** La concentrazione ha senso solo per caratteri **trasferibili e additivi** — reddito, ricchezza, capitale — cioè quando l'ammontare globale può essere posseduto in quote diverse dalle unità. Un carattere è **equidistribuito** se frazioni uguali di unità possiedono frazioni uguali dell'ammontare. Da qui la **curva di Lorenz** e il **rapporto di concentrazione di Gini**, che vale **0 in caso di equidistribuzione perfetta e 1 in caso di concentrazione massima**.

> **Il collegamento da tenere pronto.** L'indice di Gini è **l'unico strumento di questo capitolo che si incontra ogni giorno nel dibattito pubblico** — ed è anche uno degli indicatori BES allegati ai documenti di finanza pubblica. Se la commissione tocca disuguaglianza, politiche redistributive o scienza delle finanze, farlo comparire qui è naturale e fa una buona impressione.

## 4. Indici di forma, rapporti statistici, distribuzioni doppie

Gli **indici di forma** descrivono la sagoma della distribuzione: **asimmetria** (la coda più lunga è a destra o a sinistra) e **curtosi** (quanto è appuntita o piatta rispetto alla normale). Si costruiscono a partire dai **momenti**.

I **rapporti statistici** mettono in relazione due grandezze e sono il pane quotidiano di un'amministrazione: rapporti di **composizione** (una parte sul totale), di **derivazione** (un fenomeno rapportato a quello che lo genera: nati per 1.000 abitanti), di **coesistenza** (due parti fra loro: maschi su femmine), di **densità** (abitanti per km²), **numeri indice** a base fissa o mobile.

Le **distribuzioni doppie** (o bivariate) incrociano due caratteri e introducono i concetti che reggeranno tutto il resto del volume: **distribuzioni marginali** (i totali di riga e di colonna), **distribuzioni condizionate** (una riga o una colonna presa da sola), **indipendenza statistica**.

La **connessione** misura il legame fra due **mutabili** (caratteri qualitativi) e si valuta con il **chi-quadrato** e gli indici che ne derivano; la **concordanza o discordanza** riguarda due **variabili** e si misura con **covarianza** e **coefficiente di correlazione lineare**.

## 5. La regressione nella statistica descrittiva

Il capitolo si chiude con un primo sguardo alla **regressione**, che il manuale riprenderà poi in chiave econometrica nei capitoli 7 e 8.

L'idea è semplice: **interpolare** i dati con una funzione che ne sintetizzi l'andamento. Nella **regressione lineare semplice** si cerca la retta che meglio approssima la nuvola di punti; il criterio di «meglio» è quello dei **minimi quadrati** — la retta che rende minima la somma dei quadrati delle distanze verticali fra i punti osservati e la retta stessa.

> **La differenza fra i due sguardi, da dire esplicitamente.** In **statistica descrittiva** la regressione è **interpolazione**: sintetizza i dati che ho davanti, non pretende di dire nulla su altro. In **econometria** la stessa retta diventa la stima di una **relazione causale ipotizzata dalla teoria economica**, con un **termine di errore stocastico**, e su di essa si fanno **inferenza, test e previsioni**. Stessa matematica, statuto completamente diverso. Chi coglie questo passaggio ha capito che cos'è l'econometria.

---

# Parte II — Calcolo delle probabilità

*(Capitolo 2, pp. 300-310 circa)*

## 6. Incertezza e ripetibilità

Il calcolo delle probabilità nasce da due concetti: l'**incertezza** del risultato e la **ripetibilità** dell'esperimento. È importante notarlo subito, perché — come vedremo — **è proprio la ripetibilità che manca ai dati economici**, e da lì nasce la specificità dell'econometria.

**Gli eventi e l'algebra booleana.** Lo **spazio campione** è l'insieme di tutti i risultati possibili; un **evento** è un suo sottoinsieme. Le operazioni: **unione** (somma logica: si verifica almeno uno dei due), **intersezione** (prodotto logico: si verificano entrambi), **negazione** (evento complementare). Una **partizione** dello spazio campione è una famiglia di eventi **incompatibili** la cui unione è l'evento certo.

## 7. Le tre definizioni di probabilità

Il manuale le presenta come alternative, ed è utile saperle distinguere perché ciascuna ha un limite preciso:

| Definizione | Formulazione | Limite |
|---|---|---|
| **Classica** (*a priori*) | casi favorevoli / casi possibili | richiede che i casi siano **equiprobabili** e in numero finito: è una definizione **circolare** (usa la probabilità per definirla) |
| **Frequentista** (*a posteriori*) | limite della frequenza relativa al crescere delle prove | richiede la **ripetibilità** dell'esperimento in condizioni identiche: inapplicabile agli eventi singolari |
| **Soggettivista** | il grado di fiducia che un individuo coerente attribuisce al verificarsi dell'evento, misurato dalla quota che è disposto a scommettere | è **soggettiva**, ma è l'unica applicabile a eventi non ripetibili |

Per superare i limiti delle tre definizioni si ricorre all'**assiomatizzazione** (Kolmogorov): la probabilità è una funzione che soddisfa tre assiomi — **non negatività**, **normalizzazione** (la probabilità dell'evento certo è 1), **additività** per eventi incompatibili. Da essi si deduce tutto il resto.

## 8. Probabilità condizionata, composte, totali e il teorema di Bayes

- **probabilità condizionata**: la probabilità di A **sapendo che** si è verificato B. È il concetto che introduce l'**informazione** nel calcolo;
- **probabilità composte**: la probabilità che si verifichino **entrambi** gli eventi. Due eventi sono **indipendenti** quando il verificarsi dell'uno non modifica la probabilità dell'altro;
- **teorema delle probabilità totali**: se gli eventi formano una partizione, la probabilità di un evento si ottiene sommando le probabilità condizionate pesate;
- **teorema di Bayes**: consente di **invertire il condizionamento**, passando dalla probabilità dell'effetto data la causa alla probabilità della causa dato l'effetto.

> **Perché Bayes merita di essere raccontato bene.** È il teorema che formalizza **l'aggiornamento delle credenze alla luce dell'evidenza**: si parte da una probabilità *a priori*, si osserva un dato, si ottiene una probabilità *a posteriori*. È il fondamento dei classificatori bayesiani della data science, ed è anche la struttura logica di qualunque **attività di controllo**: l'amministrazione parte da una probabilità di irregolarità, osserva un indizio, e aggiorna. L'esempio che colpisce sempre — e che puoi usare — è quello del **test diagnostico su una malattia rara**: anche un test molto accurato, applicato a una popolazione in cui la malattia è rarissima, produce **più falsi positivi che veri positivi**. La ragione è che la probabilità *a priori* conta quanto l'accuratezza del test. È la stessa logica che rende inefficiente un controllo fiscale fatto a caso invece che sul rischio.

---

# Parte III — Le variabili casuali

*(Capitolo 3, pp. 310-322 circa)*

Una **variabile casuale** (o aleatoria) associa un numero a ciascun risultato di un esperimento. È **discreta** se assume un'infinità numerabile di valori, **continua** se ne assume infiniti in un intervallo. Si descrive con la **funzione di probabilità** (o di densità, nel continuo) e con la **funzione di ripartizione**, che dà la probabilità cumulata fino a un certo valore.

I due parametri che riassumono una variabile casuale sono il **valore atteso** (la media della popolazione, indicata con **μ**) e la **varianza** (indicata con **σ²**).

> **Attenzione a una distinzione che il manuale segnala espressamente:** la media di una **variabile statistica** si indica con **M**, quella di una **variabile casuale** con **μ**. Non è pedanteria: è la differenza fra **ciò che si osserva in un campione** e **ciò che caratterizza la popolazione**, ed è il cuore di tutta l'inferenza.

## 9. Le variabili casuali discrete

| Variabile | Descrive | Da ricordare |
|---|---|---|
| **Bernoulli** | un singolo esperimento con **due soli esiti** (successo/insuccesso) | è il mattone elementare di tutto il resto |
| **Binomiale** | il numero di successi in **n prove indipendenti** con probabilità costante | somma di n bernoulliane; è il modello del campionamento **con** reinserimento |
| **Poisson** | il numero di eventi **rari** in un intervallo di tempo o spazio | media e varianza **coincidono**; è il limite della binomiale quando n è grande e p piccolo — il modello degli arrivi, dei guasti, degli incidenti |
| **Ipergeometrica** | il numero di successi estraendo **senza reinserimento** da una popolazione finita | è il modello del **collaudo** e del **controllo di qualità**: le estrazioni non sono indipendenti |

## 10. Le variabili casuali continue

**La normale (di Gauss)** è la distribuzione centrale di tutta la statistica. È **simmetrica e campanulare**, completamente individuata da media e varianza; ha la proprietà notevole che una sua trasformazione lineare è ancora normale, il che consente la **standardizzazione** in una **normale standard** a media 0 e varianza 1. Da ricordare la regola pratica: circa il **68%** dei valori cade entro una deviazione standard dalla media, il **95%** entro due, il **99,7%** entro tre.

Le tre distribuzioni **derivate dalla normale** sono quelle che incontrerai in ogni output econometrico, ed è importante sapere **a che cosa serve ciascuna**:

| Distribuzione | Nasce da | Serve a |
|---|---|---|
| **Chi-quadrato (χ²)** | somma di quadrati di normali standard | test sulla **varianza**, test di **indipendenza** e di **adattamento**; compare nei test diagnostici del modello di regressione |
| **t di Student** | rapporto fra una normale standard e la radice di un chi-quadrato | test sulla **media** e sui **singoli coefficienti** di regressione **quando la varianza è incognita**. Ha code più pesanti della normale, e vi tende al crescere dei gradi di libertà |
| **F di Fisher-Snedecor** | rapporto fra due chi-quadrato | **confronto fra varianze** e test su **ipotesi congiunte** — la significatività complessiva di un modello di regressione |

**La variabile uniforme** attribuisce uguale densità a tutti i valori di un intervallo: è il modello dell'assenza totale di informazione.

## 11. Il teorema del limite centrale

È il risultato più importante della statistica, e va saputo enunciare con precisione:

> **La somma (o la media) di un numero sufficientemente grande di variabili casuali indipendenti, comunque distribuite, tende a distribuirsi come una normale.**

**Perché è decisivo.** Perché rende la distribuzione normale **applicabile anche quando non sappiamo nulla della distribuzione di partenza**: qualunque sia la forma della popolazione, la **media campionaria** è approssimativamente normale, purché il campione sia abbastanza grande. È questo teorema — non un'ipotesi di comodo — che giustifica l'uso dei test basati sulla normale in tutta l'inferenza e in tutta l'econometria.

> **Se ti chiedono perché la distribuzione normale è così importante, questa è la risposta migliore:** non perché i fenomeni siano «naturalmente normali», ma perché **la normalità emerge dall'aggregazione**. Un fenomeno determinato dalla somma di tanti piccoli fattori indipendenti tende a distribuirsi normalmente **a prescindere** da come si distribuiscono i singoli fattori. Ed è anche la ragione teorica per cui, nel modello di regressione, si assume che il termine di errore — che rappresenta la somma di innumerevoli cause trascurate — sia normale.

---

# Parte IV — La teoria della stima

*(Capitolo 4, pp. 317-324 circa)*

## 12. Dal campione alla popolazione

La **rilevazione campionaria** si contrappone a quella totale: si osserva un sottoinsieme e da esso si inferisce sulla popolazione. I vantaggi sono evidenti — costo, tempo, talvolta è l'unica via possibile (il collaudo distruttivo) — il prezzo è l'**errore di campionamento**, che però, se il campione è **probabilistico**, è **quantificabile**.

Un **parametro** è una caratteristica ignota della popolazione (μ, σ², una proporzione). Uno **stimatore** è una funzione delle osservazioni campionarie usata per approssimarlo; il valore che assume su un campione concreto è la **stima**.

> **Distinzione da tenere ferma:** lo **stimatore** è una **variabile casuale** — cambia da campione a campione e ha una propria distribuzione; la **stima** è un **numero**. Tutte le proprietà che seguono riguardano lo stimatore, non la stima.

## 13. Le proprietà desiderabili di uno stimatore

Sono cinque, e il manuale le elenca in quest'ordine. Vale la pena saperle spiegare **in italiano**, perché è così che le chiederanno.

| Proprietà | Che cosa significa |
|---|---|
| **Correttezza** (non distorsione) | il **valore atteso** dello stimatore **coincide con il parametro**. In media, su infiniti campioni, non sbaglia né per eccesso né per difetto |
| **Consistenza** | **al crescere della numerosità campionaria** lo stimatore converge al vero valore del parametro. È una proprietà **asintotica**: riguarda ciò che accade con molti dati |
| **Efficienza** | fra due stimatori corretti, è più efficiente quello con **varianza minore**: sbaglia meno da campione a campione |
| **Sufficienza** | lo stimatore **utilizza tutta l'informazione** campionaria rilevante per il parametro: nessun'altra funzione dei dati aggiungerebbe informazione |
| **Normalità asintotica** | al crescere del campione, la distribuzione dello stimatore tende alla normale: è ciò che consente di costruire test e intervalli anche quando la distribuzione esatta è ignota |

> **Correttezza e consistenza non sono la stessa cosa**, ed è un chiarimento che colpisce. Uno stimatore può essere **corretto ma non consistente** (non migliora all'aumentare dei dati) oppure **distorto ma consistente** (sbaglia sistematicamente su campioni piccoli, ma la distorsione svanisce al crescere di n). Quando in econometria si dirà che uno stimatore è «inconsistente», si starà dicendo la cosa peggiore possibile: **nemmeno con infiniti dati troverebbe il valore vero**.

## 14. Gli intervalli di confidenza

Uno stimatore fornisce una **stima puntuale**; l'**intervallo di confidenza** fornisce un **intervallo di valori plausibili**, associato a un **livello di confidenza** (tipicamente 95%).

Il manuale tratta separatamente il caso della media di una popolazione normale **con varianza nota** (si usa la **normale standard**) e **con varianza non nota** (si usa la **t di Student** con n−1 gradi di libertà, sostituendo alla varianza incognita la sua stima campionaria).

> **L'interpretazione corretta — ed è una domanda-trappola classica.** Un intervallo al 95% **non** significa che «il parametro ha il 95% di probabilità di stare lì dentro»: il parametro è un numero fisso, non una variabile casuale. Significa che **se ripetessimo il campionamento infinite volte, il 95% degli intervalli così costruiti conterrebbe il vero parametro**. È una proprietà della *procedura*, non di quell'intervallo specifico. Chi dà questa risposta ha studiato inferenza; chi dà l'altra l'ha memorizzata.

**Da che cosa dipende l'ampiezza di un intervallo?** Da tre cose, e saperle elencare è utile: cresce al crescere della **variabilità** del fenomeno; cresce al crescere del **livello di confidenza** richiesto (più sicurezza = intervallo più largo); **diminuisce al crescere della numerosità campionaria** — ma solo con la radice di n, il che significa che **per dimezzare l'ampiezza occorre quadruplicare il campione**. Quest'ultimo è un fatto con implicazioni di bilancio molto concrete per chi progetta un'indagine.

---

# Parte V — La verifica delle ipotesi

*(Capitolo 5, pp. 325-334 circa)*

## 15. La logica del test

Si formulano due ipotesi:

- l'**ipotesi nulla (H₀)**, che «rispecchia la situazione acquisita prima dell'osservazione campionaria» — l'assenza di effetto, l'uguaglianza, lo *status quo*;
- l'**ipotesi alternativa (H₁)**, che ne afferma una diversa specificazione.

Si sceglie una **statistica-test**, di cui si conosce la distribuzione **sotto l'ipotesi nulla**; si fissa un **livello di significatività α**; si individua la **regione critica** (o di rifiuto); si rifiuta H₀ se il valore osservato della statistica cade in quella regione.

**La regione critica dipende dall'ipotesi alternativa**, ed è un punto che il manuale sottolinea con cura:

| Ipotesi alternativa | Regione critica |
|---|---|
| **H₁: μ < μ₀** | **coda di sinistra** (test unilaterale sinistro) |
| **H₁: μ > μ₀** | **coda di destra** (test unilaterale destro) |
| **H₁: μ ≠ μ₀** | **entrambe le code**, con α ripartito a metà (test bilaterale) |

## 16. I due errori, e perché non sono simmetrici

| | **H₀ è vera** | **H₀ è falsa** |
|---|---|---|
| **Rifiuto H₀** | **errore di I specie** (probabilità **α**) | decisione corretta (**potenza = 1−β**) |
| **Accetto H₀** | decisione corretta | **errore di II specie** (probabilità **β**) |

- l'**errore di prima specie** è **rifiutare un'ipotesi nulla vera**: è il falso allarme. La sua probabilità è α, ed è quella che **noi fissiamo**;
- l'**errore di seconda specie** è **accettare un'ipotesi nulla falsa**: non accorgersi di un effetto reale. La sua probabilità β **non la fissiamo**: dipende da quanto il vero valore si discosta da quello ipotizzato, dalla variabilità e dalla numerosità;
- la **potenza del test** è **1−β**: la capacità di rilevare un effetto quando c'è.

> **I tre punti che fanno la differenza su questa domanda, e che porterei senz'altro all'orale.**
>
> **Primo — il trade-off.** A parità di numerosità campionaria, **ridurre α aumenta β**: chiedere più prove per condannare significa assolvere più colpevoli. L'unico modo per ridurre entrambi è **aumentare i dati**.
>
> **Secondo — «accettare» non significa «dimostrare».** Non rifiutare H₀ vuol dire soltanto che **i dati non forniscono evidenza sufficiente** contro di essa: è il «non provato», non l'«innocente». Per questo si dovrebbe dire *non si rifiuta*, non *si accetta*.
>
> **Terzo — significatività statistica non è rilevanza sostanziale.** Con un campione abbastanza grande **qualunque** differenza, anche minuscola e priva di interesse pratico, risulta «statisticamente significativa». È l'errore più costoso che un'amministrazione possa fare nel leggere una valutazione: la domanda giusta non è *«l'effetto è significativo?»* ma *«quanto è grande, e vale quello che è costato?»*.

**Il parallelo che rende tutto memorizzabile** è quello con il **processo penale**: H₀ è la presunzione di innocenza; l'errore di prima specie è **condannare un innocente**; quello di seconda specie è **assolvere un colpevole**; α è lo standard di prova richiesto («oltre ogni ragionevole dubbio» significa α molto piccolo); l'ordinamento sceglie deliberatamente di **tenere bassissimo l'errore di prima specie**, accettando in cambio un errore di seconda specie più alto.

I test trattati dal manuale: sulla **media** con varianza nota (statistica **Z**, normale standard) e non nota (statistica **t**, con n−1 gradi di libertà); sulla **varianza** (statistica **chi-quadrato**) e sul confronto fra varianze (statistica **F**).

---

# PARTE VI — I MODELLI ECONOMETRICI

## 25. Che cosa distingue l'econometria dalla statistica

Fino a qui abbiamo parlato di statistica: descrivere dati, calcolare probabilità, stimare parametri, verificare ipotesi. L'econometria comincia nel momento in cui si aggiunge un ingrediente ulteriore: **la teoria economica**. Un modello econometrico non è una curva tirata attraverso una nuvola di punti, ma la **traduzione formale di una teoria** in un sistema di relazioni quantitative, i cui parametri vengono poi stimati su dati reali e sottoposti a verifica.

Questa è la risposta che conviene dare in commissione se ti chiedono «che cos'è l'econometria»: *la disciplina che misura le relazioni economiche mettendo insieme tre componenti — la teoria economica, che dice quali variabili contano e in che direzione va la causalità; la matematica, che trasforma una relazione generica in una relazione determinata; e la statistica inferenziale, che assegna ai parametri un valore numerico e ne misura l'attendibilità*. Nessuna delle tre da sola basta. La teoria non dice se la funzione è lineare o logaritmica; la matematica non dice quale variabile è causa e quale effetto; la statistica non dice nulla sul significato economico dei numeri che produce.

C'è poi una difficoltà che l'econometria ha e che le scienze sperimentali non hanno: **i dati economici non sono ripetibili**. L'economista non può rifare il 2008 cambiando i tassi d'interesse per vedere che cosa succede. Lavora su dati **non sperimentali**, prodotti dal sistema economico e non da un laboratorio. È questa la ragione profonda per cui l'econometria è così ossessionata dalle ipotesi: non potendo controllare l'esperimento, deve controllare le assunzioni. Ed è anche la ragione per cui l'ultimo capitolo del manuale — la valutazione controfattuale delle politiche pubbliche — è così importante: è il tentativo, in un mondo senza laboratorio, di ricostruire artificialmente la condizione sperimentale.

## 26. I tipi di dati: serie storiche, cross section, panel

Tre categorie, da conoscere con precisione perché la commissione le chiede spesso come domanda d'apertura.

Le **serie storiche** (*time series*) osservano **la stessa unità in momenti diversi**: il PIL italiano dal 1970 al 2024, il tasso d'inflazione mensile, le entrate tributarie trimestrali. Il dato è ordinato nel tempo e l'ordine conta: il PIL del 2023 non è indipendente da quello del 2022. È proprio qui che nasce il problema dell'**autocorrelazione**, di cui parleremo al capitolo 12.

I **dati cross section** (o *sezionali*, o *trasversali*) osservano **unità diverse nello stesso momento**: la spesa sanitaria di tutte le Regioni italiane nel 2024, il reddito di 5.000 famiglie in un'indagine campionaria. Qui il tempo è congelato e la variabilità è tra i soggetti. Il problema tipico di questi dati non è l'autocorrelazione ma l'**eteroschedasticità**: famiglie ricche e famiglie povere hanno dispersioni di spesa molto diverse.

I **dati panel** (o *longitudinali*) sono la combinazione delle due: **più unità osservate in più momenti**. Le 20 Regioni italiane, ciascuna dal 2010 al 2024. È il tipo di dato più ricco, perché consente di separare ciò che varia tra i soggetti da ciò che varia nel tempo, e soprattutto di **controllare le caratteristiche non osservate ma costanti nel tempo** di ciascun soggetto — un punto cruciale, e il motivo per cui il capitolo 15 sui panel e il capitolo 16 sulla valutazione delle politiche sono strettamente imparentati.

> **Come lo dici all'orale.** «I dati economici si presentano in tre forme. Le serie storiche seguono una stessa unità nel tempo, e il loro problema tipico è l'autocorrelazione. I dati cross section fotografano unità diverse nello stesso istante, e il loro problema tipico è l'eteroschedasticità. I dati panel combinano le due dimensioni, e proprio per questo permettono di controllare l'eterogeneità individuale non osservata: è la ragione per cui sono lo strumento privilegiato nella valutazione degli effetti delle politiche pubbliche.»

## 27. I quattro stadi della costruzione di un modello

Il manuale organizza tutto il capitolo 6 attorno a quattro stadi. Impararli nell'ordine ti dà una scaletta pronta per qualunque domanda generale sull'econometria.

**Primo stadio: la specificazione.** Si individua il fenomeno, si sceglie la variabile dipendente e le variabili esplicative, si stabilisce la **forma funzionale** che le lega, si scrive il modello. Qui entrano in gioco la teoria economica (quali variabili, quale direzione di causalità) e le **ipotesi di specificazione** (lineare? logaritmica? con quali ritardi?). È lo stadio più delicato, perché un errore commesso qui non si corregge con nessuna tecnica di stima successiva.

**Secondo stadio: la stima.** Si attribuisce un valore numerico ai parametri ignoti, usando un campione di osservazioni. Il metodo di elezione è quello dei **minimi quadrati ordinari (OLS)**, ma vedremo che quando cadono le ipotesi classiche servono metodi alternativi (minimi quadrati generalizzati, massima verosimiglianza, variabili strumentali, doppi minimi quadrati).

**Terzo stadio: la verifica.** Si sottopone il modello stimato a una batteria di controlli, che il manuale articola su tre piani distinti:

- la **verifica della significatività statistica** dei parametri, tramite statistiche-test con distribuzione nota (normale standardizzata, *t* di Student, chi-quadrato, *F* di Fisher). Se il test cade nella regione critica si rifiuta l'ipotesi nulla; altrimenti «non si rifiuta»;
- la **verifica della capacità descrittiva**: il modello riproduce con accuratezza i valori osservati delle variabili endogene? Si confrontano valori storici e valori stimati. Attenzione a una precisazione che il manuale sottolinea: in un modello **uniequazionale** bastano le misure classiche di adattamento (l'indice di determinazione R² e simili); in un modello **multiequazionale** il fatto che le singole equazioni funzionino bene *non garantisce affatto* l'attendibilità del sistema nel suo insieme;
- la **verifica della conformità alle aspettative teoriche**: i segni e gli ordini di grandezza dei coefficienti sono coerenti con quanto la teoria economica prevede? Questa analisi usa la nozione di **moltiplicatore**, che misura l'entità dell'effetto prodotto su una variabile endogena da una variazione unitaria di una variabile esogena. Se il modello stima una propensione marginale al consumo pari a 1,4, è statisticamente significativa quanto si vuole, ma è teoricamente assurda.

A queste si aggiunge la **capacità previsionale**, valutabile con tecniche di **previsione ex post** (si stima il modello su una parte del campione e se ne verifica la capacità di prevedere la parte restante, di cui si conosce già l'esito).

**Quarto stadio: l'utilizzo.** Subordinato alla corretta specificazione, a una stima con tecniche adeguate e all'esito favorevole delle verifiche. Il modello può poi servire a tre scopi:

- **descrittivo** — rappresentare la realtà osservata. Il manuale avverte che è un «ruolo riduttivo», perché formalizzare un fenomeno non può ridursi a riprodurlo;
- **interpretativo** — mettere in evidenza i nessi causali e la dinamica del sistema. L'esempio è classicamente di politica economica: *quantificare gli effetti sul PIL o sull'inflazione di un aumento di un punto percentuale del tasso praticato dalla BCE*;
- **previsionale** — valutare i valori futuri delle variabili endogene. Qui il manuale segnala il punto critico: la previsione richiede la **«soluzione» del modello** per istanti temporali esterni al periodo di osservazione, e implica necessariamente **l'ipotesi di stabilità della struttura osservata**. Se la struttura economica cambia (una crisi, una riforma, una pandemia), la previsione salta.

> **Domanda tipica.** «Come si costruisce un modello econometrico?» — Rispondi con i quattro stadi, e all'interno del terzo distingui le tre verifiche (significatività, capacità descrittiva, conformità teorica). È una risposta completa che mostra metodo.

## 28. Modelli per serie storiche e modelli di regressione

I modelli si dividono in due grandi famiglie, che presuppongono assunzioni e conoscenze diverse.

I **modelli per serie storiche** basano la loro conoscenza **sulla storia del fenomeno stesso**: non cercano una causa esterna, ma estrapolano dal passato. Si fondano sull'ipotesi che i fattori che hanno influenzato l'andamento della serie nel passato e nel presente eserciteranno effetti analoghi anche nel futuro. Sono la famiglia degli ARIMA e di Box-Jenkins (capitolo 14).

I **modelli di regressione** si incentrano invece sull'esistenza di una **relazione causa-effetto** tra il fenomeno osservato e una o più variabili esplicative. Sono costituiti da una o più equazioni, lineari o non lineari nei parametri.

All'interno dei modelli di regressione il manuale distingue:

- **regressione semplice**: una sola variabile esplicativa (il «regressore») spiega la variabile dipendente;
- **regressione multipla**: le variabili esplicative sono più di una;
- **regressione multivariata multipla**: anche le variabili dipendenti (o «variabili risposta») sono più di una.

## 29. Variabili esogene ed endogene, forma strutturale e forma ridotta

Una distinzione che la commissione chiede volentieri perché è semplice da formulare e discrimina bene chi ha studiato.

Le **variabili endogene** sono quelle **spiegate dal modello**, determinate al suo interno; in linguaggio matematico le «variabili dipendenti». Le **variabili esogene** sono quelle che **spiegano**, determinate fuori dal modello; le «variabili indipendenti» o «esplicative». Il manuale aggiunge un criterio pratico per scegliere quale variabile mettere da che parte: **si sceglie come indipendente la variabile logicamente antecedente rispetto all'altra**. Non è una scelta arbitraria, è una scelta teorica.

Da qui la distinzione fra le due forme in cui un modello può essere scritto.

Un modello è in **forma strutturale** quando le variabili endogene sono espresse in funzione **delle variabili esogene e delle altre variabili endogene**. La connessione fra le grandezze economiche deriva direttamente dalla teoria: la forma strutturale è la fotografia formale della teoria. Ma proprio per questo è un **«modello di analisi»**: non consente di calcolare immediatamente i valori delle endogene in corrispondenza di ogni livello delle esogene, perché le endogene compaiono su entrambi i lati.

Un modello è in **forma ridotta** quando ciascuna variabile endogena corrente è espressa in funzione **dei soli parametri, delle variabili esogene e delle variabili esogene ritardate**. Si ottiene risolvendo algebricamente il sistema strutturale. La forma ridotta è un **«modello di strategia»**: è quella che si usa operativamente per simulare, prevedere e valutare politiche.

> **La formula mnemonica.** *Forma strutturale = modello di analisi (la teoria). Forma ridotta = modello di strategia (l'operatività).* Tienila a mente: tornerà identica al capitolo 13 sulle equazioni simultanee, dove il passaggio dalla forma strutturale a quella ridotta diventa il cuore del problema dell'identificazione.

## 30. L'esempio guida: il modello di Keynes

Il manuale costruisce un modello econometrico completo partendo dalla teoria keynesiana del consumo. È l'esempio da avere pronto: mostra in concreto tutti e quattro gli stadi ed è economicamente familiare.

**Il punto di partenza teorico.** La «legge psicologica fondamentale» di Keynes: *«di norma e in media, gli uomini sono disposti ad accrescere il loro consumo con l'aumentare del reddito, ma non tanto quanto l'aumento del reddito»*.

**Le ipotesi da formalizzare.** Quattro:

1. la spesa per consumi (C) dipende dal reddito disponibile (Y);
2. il livello degli investimenti privati (I) dipende dalla variazione del reddito disponibile corrente e dal tasso d'interesse di mercato (r);
3. esiste una spesa pubblica autonoma (G);
4. il reddito lordo è la somma di consumi, investimenti privati e investimenti pubblici.

**La traduzione formale.** Il consumo è funzione crescente del reddito: la sua derivata rispetto al reddito è positiva, ed è la **propensione marginale al consumo**. Keynes non precisa la forma della funzione, ma impone due vincoli teorici che l'econometria dovrà rispettare:

- la **propensione marginale al consumo è compresa fra 0 e 1**: se il reddito nazionale aumenta di un'unità monetaria, il consumo aumenta, ma meno di un'unità;
- la **propensione media al consumo** (il rapporto C/Y) **diminuisce al crescere del reddito**.

**La forma funzionale scelta.** Nella letteratura successiva alla *Teoria generale* si è affermata, come semplificazione utilizzabile per le stime empiriche, la funzione **lineare**:

> **C = α₀ + α₁ Y**

dove **α₀ > 0** è la **componente autonoma** del consumo — quella parte di domanda di beni di consumo che non dipende dal reddito corrente, graficamente l'**intercetta** della retta — e **0 < α₁ < 1** è la **propensione marginale al consumo**, graficamente il **coefficiente angolare**, cioè la tangente dell'angolo che la retta forma con l'asse delle ascisse. La condizione α₀ > 0 è esattamente ciò che rende decrescente la propensione media al consumo: il vincolo teorico si traduce in un vincolo di segno su un parametro stimato. Questo è il punto didattico dell'esempio.

Il manuale osserva anche che il consumo potrebbe essere rappresentato da una funzione **esponenziale** anziché lineare: la scelta della forma funzionale è una decisione, non un dato.

**La struttura dei ritardi.** Formalizzate le ipotesi, l'econometria deve dare veste funzionale alle relazioni tenendo conto della **struttura dei ritardi** (*lags*): le scelte di consumo e di investimento possono dipendere dal reddito corrente o da quello passato, dai tassi correnti o passati. Convenzionalmente si ragiona su periodi annuali, indicando con *t* l'anno corrente, *t−1* il precedente e così via.

**Il modello in forma strutturale.** Con questi elementi si arriva a un sistema di tre relazioni:

> **Cₜ = α₀ + α₁Yₜ + α₂rₜ**  con α₀ > 0, 0 < α₁ < 1, α₂ < 0
> **Iₜ = β₀ + β₁(Yₜ₋₁ − Yₜ₋₂) + β₂rₜ₋₁**  con β₀ > 0, 0 < β₁ < 1, β₂ < 0
> **Yₜ = Cₜ + Iₜ + Gₜ**  (identità contabile)

Le scelte di consumo dipendono dalle endogene correnti Y e r; le scelte d'investimento dalle endogene ritardate. Nota che i segni attesi sono **dichiarati prima della stima**: sono le «aspettative teoriche» contro cui si farà la verifica del terzo stadio.

**Il dilemma della selezione delle variabili.** Il manuale segnala un conflitto che è bene citare all'orale perché è il cuore del capitolo 10 sulla multicollinearità: la realizzazione di un modello persegue **due obiettivi fra loro in conflitto**. Il primo è includere *quante più variabili possibile*, perché ciascuna può influire sui valori attesi della dipendente. Il secondo è includere *quante meno variabili possibile*, perché **la varianza dei valori stimati della variabile dipendente aumenta al crescere del numero di variabili**. È il *trade-off* fra distorsione da omissione e perdita di precisione. E il manuale chiude con un'avvertenza di realismo: **nessuna procedura di selezione delle variabili garantisce equazioni «migliori in assoluto»** per una certa serie di dati.

**Stima e verifica.** La stima attribuisce un numero a ciascun α e a ciascun β. Si parla di *stima* e non di misurazione perché le osservazioni non riguardano tutti i consumatori — l'intera popolazione — ma un **campione** estratto da essa: siamo nel campo dell'inferenza statistica, con il **rischio casuale** tipico del metodo induttivo, legato al numero limitato di unità e alla loro natura casuale. Da cui il requisito della **rappresentatività del campione**: esso deve avere, in media, le stesse caratteristiche della popolazione (stessa proporzione di uomini e donne, equivalente ripartizione per classi di età e così via). Segue la verifica: le relazioni specificate sono valide? il modello regge su tutto il periodo di osservazione? i parametri sono stabili?

## 31. Perché un modello «fallisce»

Il manuale dedica un passaggio specifico — molto utile come chiusura di una risposta — alle cause per cui un modello non supera la fase di verifica (si parla allora di **«fallimento del modello»**). Sono tre:

1. **la teorizzazione non regge alla prova dei fatti**: il modello elaborato non si adatta alla realtà osservata. È la fonte di errore più difficile da individuare, perché ogni modello è per definizione una semplificazione della realtà e di solito si assume valido fino a prova contraria;
2. **la teorizzazione è corretta ma la formulazione-identificazione è errata**: per esempio si usa un modello lineare quando le relazioni sono non lineari. I risultati sono scadenti;
3. **i dati non sono idonei** — per qualità o per quantità — **oppure il metodo di stima non è idoneo**.

Il ciclo logico della costruzione di un modello è dunque iterativo: individuazione del fenomeno → scelta delle variabili e raccolta dei dati → formulazione del modello → stima → verifica → uso (descrizione, previsione, interpretazione, controllo); e se la verifica fallisce, si torna all'inizio.

---

# PARTE VII — IL MODELLO DI REGRESSIONE SEMPLICE

Questo è **il capitolo decisivo** dell'intera materia. Se all'orale ti chiedono una sola cosa di econometria, con altissima probabilità è questa. Tutto ciò che viene dopo — regressione multipla, multicollinearità, eteroschedasticità, autocorrelazione, equazioni simultanee, panel — è o un'estensione o la diagnosi di una patologia di questo modello. Vale la pena padroneggiarlo davvero.

## 32. Che cos'è la regressione

La regressione è la ricerca di un modello che descriva **la relazione esistente fra una variabile dipendente e una o più variabili indipendenti**. Nel modello di regressione le variabili esplicative (o regressori) «spiegano, prevedono, simulano e controllano» la variabile dipendente.

Un dettaglio storico che fa sempre una buona impressione: il termine **regressione** fu coniato da **Francis Galton**, il quale, misurando la relazione fra la statura dei padri e quella dei figli, osservò una *regressione* dei valori delle altezze dei figli **verso la media** — i figli di padri altissimi tendevano a essere meno alti dei padri, quelli di padri bassissimi meno bassi. Il nome della tecnica nasce dunque da un fenomeno — la regressione verso la media — che con la tecnica stessa c'entra poco.

I modelli teorici di riferimento possono essere lineari, parabolici, esponenziali, logaritmici. Il **modello di regressione semplice** è quello in cui una variabile endogena è spiegata da **una sola** variabile esogena, con un legame **lineare nei parametri**.

## 33. La componente deterministica e la componente stocastica

Ecco il passaggio concettuale più importante del capitolo, quello che separa la matematica dall'econometria.

Verrebbe naturale scrivere la relazione fra due variabili come **Y = f(X)**, una funzione matematica esatta. Ma questo è impossibile, per tre ragioni che il manuale elenca:

- non si dispone di tutte le informazioni sul fenomeno, ma **solo di un campione** di coppie ordinate (x₁,y₁), (x₂,y₂), …, (xₙ,yₙ), che esprimono la relazione della popolazione **solo in termini probabilistici**;
- esistono **fenomeni imprevedibili, errori di misurazione e scarti accidentali**;
- nella realtà esistono **interrelazioni fra variabili che non possono essere compendiate in alcuna scrittura**: affermare che Y è spiegato da X è comunque una semplificazione.

Per questo il modello di riferimento è:

> **Y = f(X) + ε**

dove Y è una variabile casuale risultante dalla somma di una **componente deterministica** f(X) e di una **componente stocastica** ε. La variabile casuale ε è l'**errore** (o **scarto**, o **disturbo aleatorio**): ha «funzione compensativa» per tutte le discrepanze fra il modello e la realtà. Formalmente ε = Y − f(X).

Assumendo la linearità nei parametri, il modello diventa:

> **Yᵢ = β₀ + β₁xᵢ + εᵢ**   per i = 1, 2, …, n

dove **β₀ + β₁xᵢ** è la **parte sistematica** e **εᵢ** la **parte stocastica**. Il senso profondo è questo: in corrispondenza di ogni valore fissato di X non abbiamo un solo valore di Y, ma **un'intera distribuzione di possibili valori**.

## 34. Le sei ipotesi classiche — il cuore della materia

Le ipotesi «classiche» sono ipotesi **semplificatrici della realtà**. Tutto ciò che segue nel manuale — i capitoli 10, 11, 12, 13 — consiste nel domandarsi *che cosa succede quando una di queste ipotesi cade*. Imparale come un elenco chiuso, con il nome, il contenuto in parole e la patologia corrispondente. Questa tabella, memorizzata, è probabilmente il singolo pezzo di econometria che rende di più all'orale.

| # | Ipotesi | Che cosa dice | Se cade… |
|---|---|---|---|
| 1 | **Linearità** | La variabile dipendente è funzione lineare del regressore tramite il coefficiente β₁, più una manifestazione non osservabile di ε | Errore di specificazione della forma funzionale (cap. 8) |
| 2 | **Non sistematicità degli errori** | Gli errori sono **mediamente nulli**: E(ε) = 0. Scarti positivi e negativi si compensano in media | Stima distorta dell'intercetta; variabili rilevanti omesse |
| 3 | **Omoschedasticità** | La **varianza dell'errore resta costante** al variare delle osservazioni: Var(ε) = σ². Il modello non può essere più accurato per una parte della popolazione e meno per un'altra | **Eteroschedasticità** (cap. 12) |
| 4 | **Covarianza nulla fra errori di osservazioni diverse** | Cov(εᵢ, εⱼ) = 0 per i ≠ j. Sapere che il modello sottostima Y in un caso non deve dire nulla sul comportamento del modello in un altro caso | **Autocorrelazione** (cap. 12), tipica delle serie storiche, dove errori vicini nel tempo sono simili fra loro |
| 5 | **Non stocasticità della variabile esplicativa** | La variabile esplicativa è **deterministica**, non soggetta a deviazioni accidentali | Regressori stocastici → serve la **massima verosimiglianza** o le **variabili strumentali** (cap. 11) |
| 6 | **Normalità degli errori** | εᵢ ~ N(0, σ²) per ogni i: l'errore si distribuisce normalmente, con media nulla e varianza costante | Cadono i test *t* e *F* in campioni piccoli; restano validi asintoticamente |

Sull'ipotesi di normalità vale la pena spendere una frase in più, perché ha una rappresentazione grafica che la commissione apprezza: **fissato un valore di x, i valori di Y si distribuiscono normalmente attorno a una media che giace esattamente sulla retta di regressione**. Immagina la retta, e su ciascun punto della retta una campana perpendicolare al piano: quella è l'ipotesi di normalità. La giustificazione teorica dell'ipotesi è il **teorema del limite centrale**: l'errore è la somma di moltissime cause piccole e indipendenti, e una somma di questo tipo tende alla normale.

Da queste ipotesi discendono immediatamente due risultati che il manuale usa in continuazione: essendo E(ε) = 0 e le xᵢ fisse, il **valore medio** di Yᵢ è β₀ + β₁xᵢ (cioè esattamente il punto sulla retta) e la sua **varianza** è σ² (cioè esattamente la varianza dell'errore).

## 35. Il metodo dei minimi quadrati ordinari (OLS)

### 35.1 L'idea geometrica

Dobbiamo trovare la retta che «attraversa» la nuvola di punti del **diagramma a dispersione**. Definiamo **residui** (o scarti) le differenze fra i valori osservati e i valori teorici determinati dalla retta:

> **eᵢ = yᵢ − ŷᵢ**

Il «cappelletto» indica che si tratta di un valore teorico, ottenuto in corrispondenza di un dato valore di X. I residui rappresentano **quella parte di variabilità campionaria di Y che il modello non spiega**.

> **Distinzione da non sbagliare mai.** *Residui* ≠ *disturbi*. I **residui** sono **sempre calcolabili**, una volta ottenute le stime dei coefficienti. I **disturbi** (gli errori ε veri) **non sono mai determinabili**, perché per calcolarli occorrerebbe conoscere i veri parametri del modello. Il residuo è la controparte campionaria e osservabile del disturbo, che resta invece un oggetto teorico. È una domanda-trappola frequente.

### 35.2 Perché i *quadrati* degli scarti

Il metodo dei **minimi quadrati ordinari** — OLS, *Ordinary Least Squares*, proposto da **Carl Friedrich Gauss nel 1795** e da **Adrien-Marie Legendre nel 1805** — sceglie la retta che rende **minima la somma dei quadrati degli scostamenti** fra valori teorici e valori osservati.

Perché non semplicemente la somma degli scarti? Perché **gli scarti possono essere di segno contrario e compensarsi**: una somma degli scarti piccola non garantisce affatto che i singoli scarti siano piccoli. Elevando al quadrato si elimina il problema del segno e si penalizzano più che proporzionalmente gli scarti grandi. Ricorderai che questa è esattamente la **seconda proprietà degli scarti** vista nella statistica descrittiva: *la somma dei quadrati degli scarti da un valore è minima quando quel valore è la media aritmetica*. I minimi quadrati sono l'estensione di quella proprietà dal punto alla retta.

Tecnicamente, la funzione da minimizzare è un **paraboloide convesso**, che ha un unico punto di minimo: per questo la soluzione esiste ed è unica. Uguagliando a zero le derivate parziali rispetto ai due parametri si ottiene il **sistema delle equazioni normali**. Il manuale spiega anche perché si chiamano «normali»: la seconda equazione implica una **condizione di perpendicolarità** (ortogonalità) fra i residui eᵢ e i valori xᵢ.

### 35.3 Come si legge il coefficiente angolare

La formula operativa per β̂₁ ha un'interpretazione che vale la pena dire ad alta voce in commissione, perché lega la regressione a tutta la statistica descrittiva vista nella Parte I:

> **Il coefficiente di regressione β̂₁ è il rapporto fra la covarianza di X e Y e la varianza di X.**

Cioè: quanto le due variabili variano insieme, normalizzato per quanto varia il solo regressore. Il segno di β̂₁ è il segno della covarianza. E una volta ottenuto β̂₁, l'intercetta si ricava immediatamente come **β̂₀ = ȳ − β̂₁x̄**. Conviene sempre calcolare prima il coefficiente angolare e poi l'intercetta.

Attenzione alla simbologia, che il manuale raccomanda di non confondere: **β₀ e β₁ senza cappelletto sono i parametri veri e ignoti** della relazione che si ipotizza esistere nella popolazione; **β̂₀ e β̂₁ con il cappelletto sono le stime OLS** ottenute sul campione.

### 35.4 Le quattro proprietà della retta di regressione

Sono proprietà algebriche, che valgono sempre, indipendentemente dalla bontà del modello. Elencarle ordinatamente è un buon modo di rispondere a «che cosa può dirmi della retta di regressione?».

1. **La retta di regressione è unica**, perché unico è il punto di minimo del paraboloide.
2. **La retta passa per il baricentro della distribuzione**, cioè per il punto di coordinate (x̄, ȳ), la coppia delle medie. Discende direttamente dalla prima equazione normale. È una proprietà elegante e facile da ricordare: *la retta dei minimi quadrati passa sempre per il punto medio della nuvola*.
3. **La somma (e quindi la media) dei valori osservati coincide con la somma (e la media) dei valori stimati**. Conseguenza: **la somma dei residui è nulla**.
4. Passando la retta per il baricentro, si può assumere il punto (x̄, ȳ) come **nuova origine** e riscrivere tutto in termini di **scarti dalle medie**, il che semplifica enormemente i calcoli.

## 36. La scomposizione della devianza e l'R²

Questo è il passaggio che permette di **leggere un output di regressione**, ed è quindi doppiamente utile.

La devianza totale del carattere Y — la somma dei quadrati degli scarti dei valori osservati dalla loro media — si scompone **esattamente** in due parti (il doppio prodotto si annulla):

> **TSS = ESS + RSS**

dove:

- **TSS** (*Total Sum of Squares*) è la **devianza totale**: quanto Y varia complessivamente attorno alla propria media. È la variabilità che vogliamo spiegare;
- **ESS** (*Explained Sum of Squares*) è la **devianza di regressione**: la devianza dei valori teorici ŷᵢ rispetto alla loro media (che coincide con la media dei valori osservati). È la variabilità **spiegata** dal modello;
- **RSS** (*Residual Sum of Squares*) è la **devianza residua**: la devianza dei valori osservati attorno ai valori teorici, cioè la somma dei quadrati dei residui. È la variabilità **non spiegata**. RSS è una misura dell'errore di previsione legato all'uso del modello: **più è elevata, peggiore è la qualità del modello**.

Da qui l'**indice (o coefficiente) di determinazione lineare R²**, definito come rapporto fra devianza di regressione e devianza totale, ossia come complemento a uno del rapporto fra devianza residua e devianza totale:

> **R² = ESS / TSS = 1 − RSS / TSS**

**Come si interpreta.** R² misura **la quota di variabilità della variabile dipendente che il modello riesce a spiegare**. Assume valori compresi fra 0 e 1:

- **R² = 0**: si ha RSS = TSS. La retta di regressione è **perfettamente orizzontale** — è il caso dell'**indipendenza interpolativa**: X non aiuta in alcun modo a spiegare la variabilità di Y;
- **R² = 1**: tutti i punti sperimentali **giacciono esattamente sulla retta** (ŷᵢ = yᵢ per ogni i). Il modello spiega tutta la variabilità di Y.

Un R² di 0,94 si commenta dicendo che «la regressione ha spiegato circa il 94% della variabilità di Y».

## 37. Il coefficiente di correlazione di Bravais-Pearson

È l'indice **del grado di dipendenza lineare fra due variabili**, e nella regressione semplice è strettamente legato a R².

**Il punto di partenza è la covarianza.** La covarianza analizza congiuntamente due variabili fornendo una misura della loro contemporanea variazione: oltre a descrivere la dispersione delle variabili, ne esprime la relazione. A differenza della varianza, che è sempre positiva, **il suo segno può essere positivo o negativo**, a seconda che la relazione sia diretta o inversa. Si parla di **concordanza** quando scarti positivi (o negativi) di X tendono ad associarsi a scarti positivi (o negativi) di Y: i prodotti fra gli scarti sono positivi e la covarianza risulta positiva. Si parla di **discordanza** nel caso opposto.

La covarianza però dipende dall'unità di misura, e quindi non è confrontabile. Il **coefficiente di correlazione lineare r** la normalizza dividendola per il prodotto degli scarti quadratici medi delle due variabili.

**Un po' di storia**, utile perché il manuale la riporta e a volte viene chiesta: la paternità dell'indice è tripla. Nel **1846 August Bravais** pubblicò per primo la formulazione matematica della correlazione statistica. Nel **1885 Francis Galton** — cugino di primo grado di Charles Darwin e come lui interessato all'ereditarietà dei caratteri — fu il primo a usare la lettera **r** (abbreviazione di *regressione*), volendo quantificare la forza della relazione fra le stature di genitori e figli. Nel **1890 Karl Pearson** riprese il lavoro di Galton e Bravais e sviluppò il coefficiente nella forma attuale.

**Le proprietà di r** — da elencare così:

- è un **numero puro**, adimensionale;
- assume valori **compresi fra −1 e +1**;
- **r = 0**: non vi è relazione di tipo lineare fra i due caratteri; si dice che le variabili sono «linearmente incorrelate»;
- **r = ±1**: esiste fra i due caratteri un **legame lineare perfetto**, concorde (+1) o discorde (−1). Tutti i punti giacciono su una retta.

E qui vengono le **due avvertenze che la commissione ama sentire**, perché distinguono chi ha capito da chi ha memorizzato:

**Prima avvertenza — incorrelazione non è indipendenza.** Se due variabili sono indipendenti, allora r = 0. Ma **r può essere nullo anche quando le due variabili sono legate da una relazione diversa da quella lineare** (per esempio una parabola perfetta, simmetrica rispetto all'asse y, ha r = 0 pur essendoci dipendenza totale). Il manuale lo dice esplicitamente: *il coefficiente di correlazione non è, in generale, un indice di dipendenza, ma di concordanza; è un indice di dipendenza solo nel caso in cui quest'ultima sia di tipo lineare.*

**Seconda avvertenza — la correlazione spuria.** Talvolta r assume un valore elevato **pur non sussistendo alcuna relazione fra le variabili**, per l'influenza esercitata su entrambe da uno o più **fattori comuni**. In quel caso si parla di **correlazione spuria**. È la base di tutti gli esempi divertenti sulle correlazioni assurde, ed è il ponte diretto verso il capitolo 16: *correlazione non è causalità*, e tutto il metodo controfattuale nasce esattamente da questo problema.

**Il legame con R².** Nella regressione semplice vale una relazione di grande importanza pratica:

> **r = ± √R²**   ovvero   **R² = r²**

Il coefficiente di correlazione lineare è, in valore assoluto, **la radice quadrata dell'indice di determinazione**. Il segno di r è il segno di β̂₁. Attenzione: questa identità vale **nella regressione semplice**; nella regressione multipla R² conserva il suo significato ma non è più il quadrato di un singolo coefficiente di correlazione.

## 38. Gli stimatori OLS e il teorema di Gauss-Markov

### 38.1 Stimatori, non stime

Le stime β̂₀ e β̂₁ **mutano al variare del campione**: se estraessi un altro campione otterrei altri numeri. Considerate come funzioni del campione, esse generano **due variabili casuali**, che sono gli **stimatori OLS**. In pratica, *lo stimatore è la variabile casuale descritta dai diversi valori che la stima può assumere al variare del campione estratto*. Gli stimatori OLS risultano essere **combinazioni lineari** delle Yᵢ, con coefficienti che sono funzioni delle sole osservazioni xᵢ (e quindi non casuali): è questo che li rende «lineari».

### 38.2 Correttezza

Si dimostra che **E(β̂₀) = β₀** e **E(β̂₁) = β₁**: gli stimatori dei minimi quadrati sono **non distorti** (corretti). In media, colpiscono il bersaglio.

### 38.3 Le varianze e gli errori standard

Le varianze degli stimatori sono **funzione della varianza σ² della variabile casuale errore**, che è incognita e va a sua volta stimata. Lo stimatore della varianza dell'errore è la somma dei quadrati dei residui divisa per **n − 2**:

> **s² = RSS / (n − 2)**

Perché **n − 2** e non n? Perché nelle equazioni normali sono stati imposti **due vincoli** per ottenere le stime di β₀ e β₁: che la somma dei residui sia nulla, e che sia nulla la somma dei prodotti dei residui per le xᵢ. Si perdono due gradi di libertà. È la stessa logica dell'n−1 nella varianza campionaria, applicata due volte.

La radice quadrata di s² si chiama **errore standard della regressione — SER**, *Standard Error of Regression*. Sostituendo s² nelle espressioni delle varianze degli stimatori si ottengono le stime delle varianze di β̂₀ e β̂₁, la cui radice quadrata è l'**errore standard della stima — SEE**, *Standard Error of Estimate*, indicato con es(β̂₀) ed es(β̂₁). **È il numero che nella seconda colonna di qualunque output di regressione sta accanto al coefficiente**, ed è il denominatore di tutti i test che seguono.

Due proprietà ulteriori che il manuale segnala: la varianza di β̂₁ ha al denominatore la **devianza del regressore**, il che significa che *più il regressore varia, più preciso è il coefficiente stimato*; e i due stimatori β̂₀ e β̂₁ sono **correlati negativamente**.

### 38.4 Il teorema di Gauss-Markov

È **il** teorema dell'econometria, da citare a memoria:

> **Teorema di Gauss-Markov.** *Sotto le ipotesi classiche del modello di regressione lineare semplice, gli stimatori OLS dei minimi quadrati sono lineari, non distorti e i più efficienti nella classe degli stimatori lineari e non distorti.*

In sigla: **BLUE — Best Linear Unbiased Estimator**. Scomponendo l'acronimo parola per parola:

- **Linear**: sono combinazioni lineari delle osservazioni della variabile dipendente;
- **Unbiased**: sono corretti, E(β̂) = β;
- **Best**: fra tutti gli stimatori lineari e corretti, sono **quelli a varianza minima**.

Sul significato di «Best» il manuale dà la spiegazione tecnica che conviene saper riportare: poiché gli stimatori sono non distorti, **le loro varianze coincidono con l'errore quadratico medio (MSE, *Mean Squared Error*)**. L'errore quadratico medio è uguale alla somma della varianza e del quadrato della distorsione (*bias*) dello stimatore, e fornisce una misura complessiva della qualità di uno stimatore in termini sia di variabilità sia di distorsione. Quando il bias è nullo, MSE = varianza. Si dimostra allora che qualunque altro stimatore lineare e corretto ha varianza **maggiore o uguale** a quella OLS, con l'uguaglianza solo nel caso in cui coincida con lo stimatore OLS stesso.

> **Il punto che vale un voto in più.** Gauss-Markov vale **sotto le ipotesi classiche**. Sono proprio le ipotesi 3 (omoschedasticità) e 4 (covarianza nulla) a garantire la proprietà «Best». Quando cadono — eteroschedasticità o autocorrelazione — **gli stimatori OLS restano lineari e corretti, ma non sono più efficienti**, e soprattutto gli errori standard calcolati nel modo abituale diventano sbagliati, il che falsa tutti i test. È esattamente questo il tema del capitolo 12. Se in commissione dici *«gli OLS restano corretti ma perdono l'efficienza, e gli errori standard diventano inattendibili»*, hai detto la cosa giusta.

Il manuale aggiunge, per completezza, le **proprietà asintotiche**: sotto condizioni generali gli stimatori OLS sono anche **consistenti in media quadratica** — la precisione delle stime cresce all'aumentare della dimensione del campione — e, sotto l'ulteriore ipotesi che gli errori siano indipendenti, **asintoticamente normali**. E lo stimatore s² della varianza è a sua volta **corretto** e, assumendo l'indipendenza degli errori, **consistente**.

Sotto l'ipotesi di normalità degli errori, infine, gli stimatori OLS sono **completamente specificati**: essendo funzioni lineari di una variabile casuale normale, sono **anch'essi normali**. Ed è questo che apre la porta all'inferenza.

## 39. I test sui coefficienti: come si legge davvero un output di regressione

### 39.1 Da dove viene la *t*

Il ragionamento è quello visto nella Parte IV. Se la varianza σ² fosse nota, standardizzando lo stimatore (normale) si otterrebbe una normale standard. Ma σ² non è nota e va stimata con s². È noto che **il rapporto fra una variabile casuale normale standardizzata e la radice quadrata di una chi-quadrato indipendente, rapportata ai propri gradi di libertà, si distribuisce come una t di Student**. Ed è esattamente ciò che accade qui. Il σ incognito **si semplifica**, comparendo sia al numeratore sia al denominatore: ed è per questo che possiamo fare inferenza senza conoscerlo.

### 39.2 Il test di significatività

La verifica d'ipotesi in un modello di regressione mira a **valutare la significatività dei parametri**, cioè a stabilire se le variabili esplicative siano statisticamente in grado di spiegare la variabile dipendente. La regola di decisione consiste nello stabilire se la differenza fra il valore del parametro specificato dall'ipotesi nulla e quello ottenuto dall'osservazione campionaria sia significativa o meno.

Le due ipotesi nulle tipiche:

- **H₀: β₀ = 0** contro H₁: β₀ ≠ 0. Postula una **relazione di proporzionalità diretta** fra X e Y: graficamente, la retta di regressione **manca dell'intercetta**, passa per l'origine;
- **H₀: β₁ = 0** contro H₁: β₁ ≠ 0. Riguarda il **coefficiente angolare**, e afferma che esso è nullo — o perché la retta è parallela all'asse delle ascisse, o perché **la variabile X non è significativa nello spiegare la variabile Y**. Postula dunque che **non esista alcuna relazione fra i due caratteri**. È **l'ipotesi nulla più frequentemente sottoposta a verifica nella pratica**, e la procedura si chiama per questo **test di significatività di X**: se H₀ fosse vera, X non giocherebbe alcun ruolo nello spiegare Y.

**La statistica-test.** In entrambi i casi è la stessa cosa, e va saputa a memoria perché è concettualmente semplicissima:

> **t = (stima campionaria del coefficiente) / (suo errore standard)**

cioè **il rapporto fra la stima e il suo errore standard**. Sotto l'ipotesi nulla si distribuisce come una **t di Student con n − 2 gradi di libertà**. Le statistiche-test si calcolano in **valore assoluto**, data la simmetria della *t*.

**La regola di decisione** per un'ipotesi alternativa bidirezionale, a un livello di significatività α:

- se **|t| > t₍α/2, n−2₎** → il valore cade **nella regione critica** → **si rifiuta l'ipotesi nulla** → il coefficiente **è significativamente diverso da zero** → la variabile esplicativa X **è decisiva nello spiegare linearmente Y**;
- se **|t| ≤ t₍α/2, n−2₎** → si è nella **regione di accettazione** → **non si rifiuta** l'ipotesi nulla → il coefficiente **non è significativamente diverso da zero**.

Da qui l'importanza centrale della **t di Student nell'analisi econometrica**: consente di verificare la significatività di una variabile in un modello e il suo contributo alla spiegazione del fenomeno.

Il test si generalizza immediatamente al caso in cui l'ipotesi nulla non sia la nullità del coefficiente ma un **valore specificato b**: la statistica diventa (stima − b) / errore standard, e tutto il resto è identico. È il modo in cui si verifica un vincolo teorico: per esempio, si può testare se la propensione marginale al consumo è pari a un valore previsto dalla teoria.

### 39.3 Le regioni critiche

Ripasso rapido, perché il manuale lo ricorda qui: stabilito il livello di significatività α, che rappresenta **l'ampiezza della regione critica**, si fissano i valori critici e si rifiuta l'ipotesi nulla se il valore sperimentale del test vi ricade. Se si tratta della **coda di sinistra**, la regione di rifiuto è l'insieme dei valori inferiori a un certo valore critico molto basso; se della **coda di destra**, l'insieme dei valori superiori a un valore critico elevato; se l'ipotesi alternativa è **bidirezionale**, le due code corrispondono ciascuna a una probabilità α/2 e la regione di rifiuto è l'unione dei due insiemi.

### 39.4 Il test sulla varianza

Si può anche testare **H₀: σ² = σ₀²** contro un'alternativa. La statistica-test è **(n − 2)s² / σ₀²**, che sotto l'ipotesi nulla si distribuisce come una **chi-quadrato con n − 2 gradi di libertà**.

## 40. Gli intervalli di confidenza nella regressione

Alla stima puntuale di un parametro — inadeguata perché non fornisce alcun elemento circa l'errore — si preferisce la **stima intervallare**. L'intervallo di confidenza è lo strumento con cui si attribuisce un **giudizio di validità** alla stima: un intervallo di valori, determinato sulla base del campione, che si ritiene contenere il vero parametro con una prefissata fiducia.

La struttura è quella già vista nella Parte IV, e vale sia per β₀ sia per β₁:

> **stima ± (valore critico della t con n−2 g.d.l.) × (errore standard della stima)**

Per la varianza σ², l'intervallo si costruisce invece a partire dalla distribuzione **chi-quadrato con n − 2 gradi di libertà**, usando i due quantili corrispondenti ad α/2 e 1−α/2. Essendo la chi-quadrato **asimmetrica**, questo intervallo **non è simmetrico attorno alla stima**: è un dettaglio che dimostra attenzione.

**Che cosa fa restringere l'intervallo.** A parità di livello di significatività, **al crescere della dimensione del campione gli estremi dell'intervallo si restringono**. Il meccanismo, spiegato nel manuale passo per passo: all'aumentare della numerosità il campione diventa maggiormente rappresentativo della popolazione → diminuisce l'errore standard della stima → aumenta la precisione delle stime campionarie. È lo stesso ragionamento della Parte IV, qui applicato ai coefficienti di regressione.

> **Il collegamento fra test e intervallo — dirlo all'orale fa sempre effetto.** Verificare al livello α l'ipotesi H₀: β₁ = 0 con il test *t* ed esaminare se lo zero cade dentro l'intervallo di confidenza al livello (1−α) sono **la stessa identica operazione**. Se l'intervallo di confidenza al 95% per β₁ non contiene lo zero, allora il coefficiente è significativo al 5%, e viceversa. Test e intervallo sono due modi di guardare lo stesso oggetto.

## 41. Come si legge un output di regressione — sintesi operativa

Mettendo insieme i paragrafi 36-40, ecco la griglia da seguire davanti a una tabella di risultati, che è poi la sequenza logica con cui rispondere alla domanda «mi commenti questa regressione»:

1. **Il segno dei coefficienti**: è coerente con la teoria economica? (verifica di conformità alle aspettative teoriche)
2. **La grandezza dei coefficienti**: β₁ dice di quanto varia Y quando X aumenta di un'unità. È un ordine di grandezza plausibile? (il coefficiente è il «moltiplicatore»)
3. **Gli errori standard**: quanto sono precise le stime?
4. **Le statistiche t**: coefficiente diviso errore standard. In valore assoluto, come regola pratica, **valori superiori a circa 2 segnalano significatività al 5%** per campioni non piccolissimi.
5. **L'R²**: quale quota della variabilità di Y è spiegata dal modello?
6. **Il SER**: qual è la dispersione tipica dei residui, cioè l'errore di previsione medio?
7. **E infine la domanda che conta più di tutte**: *le ipotesi classiche reggono?* Perché se non reggono, i punti 3, 4 e 5 non valgono nulla. È questo che apre i capitoli successivi.

## 42. L'analisi della varianza (ANOVA) applicata alla regressione

L'ipotesi H₀: β₁ = 0 può essere verificata anche in un secondo modo, attraverso l'**analisi della varianza** (**ANOVA**, da *Analysis of Variance*): la tecnica statistica che cerca di **stabilire quanta parte della variabilità di un insieme di osservazioni può essere attribuita a fattori specificati**. La sua applicazione richiede la normalità della distribuzione osservata.

La logica è quella della scomposizione della devianza già vista: si confronta la variabilità **spiegata** dal modello con quella **residua**, ciascuna divisa per i propri gradi di libertà. Il rapporto fra due chi-quadrato indipendenti divise per i rispettivi gradi di libertà è una **F di Fisher**, e la statistica-test risulta dunque:

> **F = [ESS / 1] / [RSS / (n − 2)]**

che, se H₀: β₁ = 0 è vera, si distribuisce come una **F di Fisher con 1 e n − 2 gradi di libertà**. Il test è **a una sola coda, quella destra**: se il valore empirico supera il valore critico si rifiuta l'ipotesi nulla e si conclude che **X è significativa nello spiegare Y**.

La tabella ANOVA, che è poi la tabella che compare in fondo a ogni output di regressione, ha questa struttura:

| Causa di variabilità | Devianza | Gradi di libertà | Stima della varianza |
|---|---|---|---|
| **Regressione** | ESS | 1 | ESS / 1 |
| **Residuo** | RSS | n − 2 | RSS / (n − 2) |
| **Totale** | TSS | n − 1 | — |

> **Il risultato da sapere a memoria.** Nella regressione **semplice** il test *F* e il test *t* sono **equivalenti**, e vale l'identità **F = t²**. È una conseguenza di un fatto noto dalla statistica: il quadrato di una *t* con *g* gradi di libertà si distribuisce come una *F* con (1, g) gradi di libertà. Attenzione però: questa equivalenza vale **solo nella regressione semplice**. Nella regressione multipla il test *t* verifica la significatività di *un singolo* coefficiente, mentre il test *F* verifica la significatività **congiunta** di tutti i coefficienti: sono due domande diverse, e può benissimo accadere che nessun coefficiente sia significativo individualmente mentre la *F* congiunta lo è (è il sintomo classico della **multicollinearità**, capitolo 10).

Sia la *F* sia la *t* possono essere espresse **in funzione dell'R²**. Per la *F*:

> **F = R² / [(1 − R²) / (n − 2)]**

Una relazione che merita un commento: mostra in modo trasparente che la significatività **non dipende solo dalla bontà dell'adattamento (R²) ma anche dalla numerosità campionaria (n)**. Con un campione abbastanza grande, anche un R² modestissimo produce una F significativa. È l'ennesima declinazione del principio già visto: **significatività statistica ≠ rilevanza sostanziale**.

## 43. La previsione nel modello di regressione semplice

Stimati i parametri, il modello si può usare per prevedere. Il manuale è molto chiaro su un punto preliminare, che vale la pena riportare: il processo di determinazione di valori teorici in corrispondenza di valori di X **esterni all'intervallo di osservazione** presuppone che i valori campionari osservati si siano succeduti in passato **con una certa regolarità**. E aggiunge l'avvertenza: *in quanto basata solo sulla regolarità passata del fenomeno, la previsione può essere poco attendibile, non tenendo conto di cause perturbatrici che potrebbero verificarsi in futuro.*

**Previsione puntuale.** In corrispondenza di un valore x₀ della variabile esplicativa, la previsione è semplicemente **ŷ₀ = β̂₀ + β̂₁x₀**: si legge il valore sulla retta stimata. L'**errore di previsione** — la differenza fra il valore vero e quello previsto — è una variabile casuale con **valore atteso nullo**, perché gli stimatori OLS sono non distorti e l'errore ha media zero. La previsione puntuale dei minimi quadrati è dunque **corretta**.

**Previsione intervallare.** Più utile del previsore puntuale è la varianza dell'errore di previsione, perché consente di costruire un **intervallo di previsione**. Da questa varianza il manuale ricava due conclusioni di grande valore intuitivo, che sono la cosa da dire all'orale:

> **La varianza dell'errore di previsione è funzione inversa del numero delle osservazioni** — al crescere di n si riduce — **ed è funzione positiva dello scarto al quadrato fra x₀ e il valore medio x̄**: quanto più il valore per cui si prevede si allontana dalla media dei dati osservati, tanto più la previsione è imprecisa.

Graficamente questo significa che la **banda di previsione ha la forma di una clessidra**: è strettissima in corrispondenza del baricentro (x̄, ȳ) e si allarga progressivamente allontanandosi da esso. È la giustificazione formale di una regola di prudenza elementare: **estrapolare lontano dai dati osservati è pericoloso**. Se ho stimato una relazione su redditi fra 20.000 e 50.000 euro, prevedere il consumo di chi guadagna 500.000 euro è un esercizio con un intervallo di previsione enorme — e per giunta fondato sull'ipotesi, indimostrabile, che la stessa forma funzionale valga anche là fuori.

**Le due previsioni da non confondere.** Il manuale distingue accuratamente:

- la previsione del **singolo valore Y₀** che si realizzerà;
- la previsione del **valore atteso E(Y₀)**, cioè della media della popolazione in corrispondenza di x₀.

La previsione **puntuale è la stessa** nei due casi (ŷ₀). Ma l'**errore di previsione è diverso**: prevedere un singolo valore comporta un'incertezza aggiuntiva — quella dell'errore ε₀ specifico di quell'osservazione — che invece non c'è quando si prevede la media. Di conseguenza **l'intervallo per il singolo valore è sempre più ampio dell'intervallo per il valore atteso**. È una distinzione fine ma che, se la fai, dimostra di aver capito la differenza fra la variabilità della retta e la variabilità attorno alla retta.

---

# PARTE VIII — LE ESTENSIONI DEL MODELLO DI REGRESSIONE SEMPLICE

Il modello con una sola variabile esplicativa è, come dice il manuale, «un caso estremo di semplificazione della realtà, che è indubbiamente più complicata di qualsiasi modello che tenti di rappresentarla». Il capitolo 8 lo estende in tre direzioni: osservazioni ripetute e test di linearità; forme funzionali non lineari ma **linearizzabili**; e il passaggio a due variabili esplicative, come ponte verso la regressione multipla.

## 44. Osservazioni ripetute e test di linearità

Supponiamo di avere, per ciascun valore della variabile X, **più osservazioni** di Y. È la situazione tipica della ricerca sperimentale: si somministrano dosi progressivamente crescenti di un principio attivo a gruppi di pazienti e si osserva come varia la risposta media; oppure si applica un fertilizzante a terreni di data misura. In economia è la situazione dei dati raggruppati in classi.

In questo caso la stima del coefficiente di regressione si applica **alle medie di classe**, pesate con il numero di osservazioni di ciascuna classe: si parla di **regressione ponderata**.

Il vantaggio di avere osservazioni ripetute è che si può fare qualcosa che con una sola osservazione per valore di X è impossibile: **testare la linearità stessa della relazione**. La logica è questa. La devianza totale si scompone in **devianza entro le classi** (la variabilità delle risposte a parità di dose) e **devianza tra le classi** (la variabilità delle medie di classe). Da queste si costruisce:

- un test *F* per l'ipotesi di **assenza di relazione** fra X e Y, cioè che tutte le medie di classe siano uguali;
- e, dal loro rapporto, il **rapporto di correlazione di Pearson η²** (eta quadro): un indice normalizzato che vale 0 quando la devianza tra le classi è nulla e 1 quando l'intera variabilità di Y è attribuibile alla variabilità fra le classi.

**Il test di linearità vero e proprio** nasce da un confronto illuminante. La devianza totale si scompone ulteriormente in tre pezzi: la devianza **entro le classi** (rispetto alle medie di classe), la devianza **delle medie di classe rispetto ai valori di regressione**, e la devianza **di regressione**. Da qui:

- **R²** (indice di determinazione lineare) misura solo la quota catturata **dalla retta**;
- **η²** (rapporto di correlazione) misura la quota catturata **dalle medie di classe**, qualunque sia la forma della relazione.

Ne segue la relazione fondamentale:

> **η² ≥ R²**, con **η² = R² se e solo se le medie di classe giacciono esattamente sulla retta di regressione.**

Il test di linearità confronta quindi le due quantità: se le medie di classe **divergono significativamente** dai valori di regressione, la differenza fra η² e R² è grande, la statistica *F* supera il valore critico e **si rifiuta l'ipotesi di linearità**. In parole semplici: *η² dice quanto X spiega Y comunque; R² dice quanto lo spiega una retta; la loro distanza dice quanta relazione la retta sta perdendo perché la vera relazione è curva.* È un'idea elegante e vale la pena saperla esporre.

## 45. Le forme funzionali — il paragrafo da studiare per intero

Questo è il paragrafo più «economico» del capitolo, quello dove econometria e microeconomia si toccano. La commissione lo apprezza perché permette di far parlare il candidato di elasticità, funzione Cobb-Douglas e curva di Phillips.

**Il principio generale.** Quando la relazione fra X e Y non è lineare nei parametri, occorre **ridurre la funzione a un'espressione lineare** negli stessi parametri o in altri esprimibili in funzione di quelli originari. L'operazione di trasformazione è di importanza fondamentale: **rende lineari relazioni che non lo sono**, così da poter applicare gli usuali metodi di stima, minimi quadrati in testa. Un modello «non lineare nelle variabili ma linearizzabile» resta trattabile con l'OLS; è solo la non linearità **nei parametri** che richiede metodi diversi.

Il manuale organizza le forme funzionali attraverso la **trasformazione di Box-Cox (1964)**, che applica a ciascuna variabile una trasformazione dipendente da un parametro λ, stimato insieme agli altri: per λ ≠ 0 la trasformazione è di tipo potenza, per λ = 0 è il **logaritmo**. Variando i due parametri λ₁ (per Y) e λ₂ (per X) si ottengono, come casi particolari, tutte le forme funzionali usate in pratica. È un modo elegante di presentarle come una famiglia unica.

### 45.1 Modello lineare (λ₁ = λ₂ = 1)

> **Y = β₀ + β₁X + ε**

**Interpretazione del coefficiente:** β₁ è la **variazione assoluta** di Y per una variazione unitaria di X. Se X aumenta di 1, Y aumenta di β₁ unità. L'effetto è **costante** lungo tutta la curva.

### 45.2 Modello doppio logaritmico (λ₁ = λ₂ = 0)

> **ln Y = β₀ + β₁ ln X + ε**

È lineare nei parametri e lineare nei logaritmi delle variabili, quindi stimabile con OLS. Trascurando il disturbo, la relazione fra le variabili originarie è una **funzione potenza**.

> **La proprietà che rende famoso questo modello: β₁ misura l'ELASTICITÀ COSTANTE di Y rispetto a X.** Cioè: se X aumenta dell'1%, Y varia di β₁ per cento, e questa percentuale **è la stessa in ogni punto della curva**. È questa la ragione del suo larghissimo impiego.

Il comportamento della curva dipende dal segno e dal valore di β₁:

- **β₁ > 0**: pendenza sempre positiva, Y tende a infinito al crescere di X. In particolare, se **0 < β₁ < 1** la pendenza è positiva ma **decrescente** (rendimenti decrescenti); se **β₁ > 1** la pendenza **aumenta continuamente**;
- **β₁ < 0**: pendenza negativa.

**In economia** è la forma d'elezione per specificare **funzioni di produzione** e **funzioni di domanda** — perché in entrambi i casi il concetto economicamente rilevante è proprio l'elasticità.

**La funzione di produzione Cobb-Douglas.** L'esempio che il manuale sviluppa per intero, e che conviene saper raccontare:

> **P = γ₀ L^α K^β**

dove P è la quantità prodotta, L il fattore lavoro, K il fattore capitale, **γ₀ > 0** una costante che rappresenta l'**efficienza nell'uso dei fattori produttivi** (misura la scala della produzione), e **α, β** i parametri esponenti. Fu formulata da **C.W. Cobb e P.H. Douglas nel 1925**.

Le proprietà, tutte da citare:

- la funzione è **omogenea di grado α + β**: moltiplicando ciascun fattore per una costante k, la produzione risulta moltiplicata per k^(α+β). **La somma α + β misura dunque i rendimenti di scala**: costanti se α+β = 1, crescenti se > 1, decrescenti se < 1;
- le **produttività marginali** del lavoro e del capitale si ottengono derivando rispetto a ciascun fattore;
- il **saggio marginale di sostituzione tecnica** fra i fattori è il rapporto fra le produttività marginali;
- e soprattutto: **α e β sono le elasticità dei fattori**, cioè i rapporti fra produttività marginale e produttività media di ciascun fattore. **Rappresentano la variazione percentuale del livello di output conseguente a una variazione percentuale unitaria dell'input** di lavoro e di capitale rispettivamente.

**Il punto econometrico**: la Cobb-Douglas è **non lineare**, ma prendendo il logaritmo di entrambi i membri e aggiungendo il disturbo diventa:

> **ln P = ln γ₀ + α ln L + β ln K + ε**

che è una **regressione multipla in forma doppio-logaritmica**, perfettamente stimabile con i minimi quadrati. I coefficienti stimati **sono direttamente le elasticità**, e la loro somma dice immediatamente se i rendimenti di scala sono costanti, crescenti o decrescenti — ipotesi che si può testare con un test *F* sul vincolo α + β = 1. Questo è un esempio completo e memorabile di come l'econometria metta alla prova una teoria economica.

### 45.3 Modello semilogaritmico (λ₁ = 0, λ₂ = 1)

> **ln Y = β₀ + β₁X + ε**

**Interpretazione:** il **tasso di variazione relativo di Y per un'unità di variazione di X è costante e pari a β₁**. In altre parole: se X aumenta di un'unità, **Y varia di β₁ per cento** (approssimativamente, per valori piccoli di β₁). È il modello delle **crescite percentuali costanti**.

**L'applicazione più interessante** è quella in cui **X è il tempo**: la funzione descrive allora l'andamento temporale di una variabile caratterizzata da un tasso di crescita costante, cioè una **crescita esponenziale** Y = Y₀ e^(β₁t). Prendendo i logaritmi, la relazione diventa lineare nel tempo e stimabile con OLS, e **β₁ è il tasso istantaneo di crescita**.

Il manuale sviluppa poi un raccordo che fa la differenza in sede d'esame, quello fra **capitalizzazione continua e capitalizzazione discreta**. Se la variazione di Y non è continua ma avviene a **intervalli discreti**, si scrive Y_t = Y₀(1 + g)^t, dove g è il tasso di crescita costante applicato a intervalli. Prendendo i logaritmi di entrambe le formulazioni e confrontandole si ottiene:

> **β₁ = ln(1 + g)**

cioè: **β₁ è quel tasso che, applicato istante per istante, è equivalente al tasso g applicato a intervalli discreti**. Da una stima di β₁ si ricava dunque immediatamente una stima di g, e viceversa. È lo stesso rapporto che in matematica finanziaria lega il tasso istantaneo di interesse al tasso annuo effettivo.

### 45.4 Modello iperbolico (λ₁ = 1, λ₂ = −1)

> **Y = β₀ + β₁ (1/X) + ε**

La funzione ha **pendenza positiva se β₁ < 0** e **pendenza negativa se β₁ > 0**. La caratteristica distintiva è che **β₀ indica il livello di saturazione**: per Y = β₀ la curva presenta un **asintoto** orizzontale. È quindi la forma adatta a tutti i fenomeni che tendono a un limite.

Due applicazioni economiche, entrambe da citare:

- con **β₁ < 0**, in contesto microeconomico, la funzione descrive la **spesa Y per un dato bene o servizio in funzione del reddito totale X**, e β₀ rappresenta il **livello di spesa asintotica** — la spesa massima verso cui si tende anche con reddito illimitato. È la forma di una curva di Engel per un bene di prima necessità;
- con **β₁ > 0**, la funzione rappresenta la **curva di Phillips**, che descrive la relazione fra il tasso di variazione dei salari monetari (asse Y) e il tasso di disoccupazione (asse X). Il manuale riporta l'origine storica: nel **1958** l'economista inglese **A.W. Phillips** pubblicò uno studio sul livello dei salari nel Regno Unito lungo quasi un secolo (**1861-1957**), notando **una correlazione negativa fra il tasso di cambiamento dei salari nominali e il tasso di disoccupazione**: i salari aumentavano tanto più rapidamente quanto minore era il saggio di disoccupazione.

> **Collegamento con economia politica.** La curva di Phillips è uno dei rari punti in cui l'econometria del tuo bando tocca direttamente l'economia politica e la politica economica. Se ti capita di poterla citare, aggiungi che la relazione originaria — puramente empirica — fu poi messa in crisi dalla **stagflazione degli anni Settanta** e riformulata da Friedman e Phelps nella versione **aumentata per le aspettative**, con il tasso naturale di disoccupazione: è esattamente l'esempio del manuale sull'**ipotesi di stabilità della struttura**, cioè di un modello che «fallisce» perché la teorizzazione sottostante non regge alla prova dei fatti.

### 45.5 Modello logaritmico-iperbolico (λ₁ = 0, λ₂ = −1)

> **ln Y = β₀ + β₁ (1/X) + ε**

Per β₁ < 0 la curva presenta pendenza positiva. Il **tasso di variazione relativo di Y per unità di variazione di X è inversamente proporzionale al quadrato di X**, e quindi **decresce rapidamente** all'allontanarsi di X dall'origine.

### 45.6 La curva logistica

Con andamento analogo, ma non stimabile con i minimi quadrati, c'è la **curva logistica**. Il manuale ne dà la descrizione geometrica completa, che è facile da ricordare e sempre spendibile:

- ha la **forma di una S allungata**;
- ha per **asintoti** l'asse delle ascisse (y = 0) e la retta y = k, dove k è il livello di saturazione;
- ha un **punto di flesso**, che è il punto in cui il tasso di crescita è massimo;
- è **convessa fino al flesso e concava oltre il flesso**.

È la curva dei fenomeni di diffusione: adozione di una tecnologia, penetrazione di un prodotto, epidemie. I suoi parametri **non possono essere ottenuti con il metodo dei minimi quadrati** e richiedono metodi non lineari.

> **Tabella riassuntiva — come si interpreta il coefficiente. Impara questa, vale da sola l'intero capitolo 8.**
>
> | Modello | Forma | Interpretazione di β₁ |
> |---|---|---|
> | **Lineare** | Y = β₀ + β₁X | variazione **assoluta** di Y per +1 unità di X |
> | **Doppio logaritmico** | ln Y = β₀ + β₁ ln X | **elasticità costante**: +1% di X → +β₁% di Y |
> | **Semilogaritmico** | ln Y = β₀ + β₁X | **tasso di variazione costante**: +1 unità di X → +β₁% di Y |
> | **Iperbolico** | Y = β₀ + β₁(1/X) | effetto decrescente, con **asintoto = β₀** (livello di saturazione) |
> | **Logaritmico-iperbolico** | ln Y = β₀ + β₁(1/X) | tasso relativo inversamente proporzionale a X² |

## 46. Dalla bivariata alla trivariata

L'ultima estensione del capitolo 8 è il passaggio a **due variabili esplicative**, che il manuale tratta come argomento propedeutico alla regressione multipla. Il modello diventa:

> **Y = β₀ + β₁X₁ + β₂X₂ + ε**

Un caso particolare interessante è quello in cui la seconda variabile è il **quadrato della prima** (Y = β₀ + β₁X + β₂X² + ε): formalmente è una regressione a tre variabili, stimabile con OLS, ma economicamente descrive una relazione **parabolica**, adatta a tutti i fenomeni con un massimo o un minimo interno. È l'esempio più semplice di modello **non lineare nelle variabili ma lineare nei parametri**.

Con due regressori compare per la prima volta il concetto che diventerà centrale nel capitolo 9: **l'effetto di ciascuna variabile va inteso "a parità delle altre"** (*ceteris paribus*). β₁ non è più la pendenza di una retta, ma **la variazione di Y per una variazione unitaria di X₁ tenendo costante X₂**. È la differenza fra una correlazione grezza e un effetto netto, ed è il motivo per cui la regressione multipla è lo strumento con cui si «controlla» per i fattori di confondimento.

---

# PARTE IX — IL MODELLO DI REGRESSIONE MULTIPLA

Con più di una variabile esplicativa cambia poco dal punto di vista concettuale e molto dal punto di vista pratico. Il manuale introduce qui la **notazione matriciale**, che serve a scrivere in una riga ciò che altrimenti richiederebbe un sistema di equazioni. Coerentemente con l'impostazione di questa dispensa **non riporto l'algebra matriciale**: ti serve sapere **che cosa** fa ciascun oggetto, non come si moltiplicano le matrici. Se vorrai le formule, le trovi tutte raccolte in fondo.

## 47. Il modello e la notazione compatta

Il modello di regressione multipla si scrive:

> **Y = β₀ + β₁X₁ + β₂X₂ + … + β_k X_k + ε**

e in forma compatta **Y = Xβ + ε**, dove **X** è la **matrice dei dati** (una riga per ogni osservazione, una colonna per ogni variabile esplicativa, più una colonna di uno per l'intercetta), **β** è il **vettore dei coefficienti** da stimare ed **ε** il vettore dei disturbi.

Il principio di stima è identico: **minimizzare la somma dei quadrati dei residui**. L'unica novità tecnica è una condizione di esistenza che vale la pena conoscere perché è il seme del capitolo 10:

> **La stima OLS esiste solo se la matrice X′X è invertibile**, cioè solo se **le colonne di X sono linearmente indipendenti** — le variabili esplicative non devono essere combinazioni lineari le une delle altre. Se lo sono, la matrice è singolare, l'inversa non esiste e **il modello non è stimabile**. Questa è la **collinearità perfetta**; il capitolo 10 tratterà il caso, molto più frequente, della collinearità *quasi* perfetta.

**L'interpretazione geometrica.** Con una variabile esplicativa si cercava la **retta** che minimizza la somma dei quadrati delle distanze dai punti. Con k variabili si cerca l'**iperpiano** (un piano, se le esplicative sono due) che, fra gli infiniti possibili, rende minima la somma dei quadrati delle lunghezze dei segmenti che congiungono i punti osservati al piano stesso. L'idea è la stessa, salita di dimensione.

## 48. Come si interpretano i coefficienti — il punto che conta davvero

Il manuale sviluppa un esempio che conviene memorizzare perché è il modo più chiaro di dire la cosa giusta. Si stima il volume di alberi (Y) in funzione del **diametro** (X₁) e dell'**altezza** (X₂), ottenendo un piano di regressione. I tre coefficienti si leggono così:

- l'**intercetta** è il valore teorico della variabile risposta quando **entrambe** le variabili esplicative assumono valore zero;
- il coefficiente di X₁ è **la variazione della variabile risposta quando il diametro aumenta di 1 centimetro, mentre l'altezza rimane costante**;
- il coefficiente di X₂ è **la variazione della variabile risposta quando l'altezza aumenta di 1 metro, fermo restando il diametro**.

> **Questa è la frase da dire all'orale.** *Nella regressione multipla ciascun coefficiente misura l'effetto della propria variabile sulla variabile dipendente **tenendo costanti tutte le altre variabili incluse nel modello**: è un effetto «netto», ceteris paribus.* È esattamente il motivo per cui la regressione multipla è lo strumento base del **controllo statistico** dei fattori di confondimento — e quindi il ponte diretto verso il capitolo 16 sulla valutazione delle politiche. Aggiungi, se vuoi essere preciso: il controllo vale **solo per le variabili effettivamente incluse**; nulla dice sulle variabili omesse, ed è proprio da lì che nasce il *selection bias*.

## 49. La stima della varianza dell'errore

Come nel modello semplice, la varianza dell'errore σ² si stima dividendo la somma dei quadrati dei residui per i gradi di libertà residui, che ora sono **n − k** (n osservazioni meno i k parametri stimati):

> **s² = RSS / (n − k)**

Lo stimatore è **non distorto**, e la sua radice quadrata è di nuovo l'**errore standard della regressione**. Dalla stessa quantità si ricavano gli **errori standard dei singoli coefficienti**, che dipendono da due cose: dalla varianza dell'errore (il «rumore» complessivo) e dagli elementi sulla diagonale principale di (X′X)⁻¹, che riflettono **quanto ciascuna variabile è correlata con le altre**. Anche questo prepara il capitolo 10: sarà proprio quel secondo fattore a esplodere in presenza di multicollinearità.

## 50. Il teorema di Gauss-Markov in versione multipla

Il teorema si riformula identico, in versione matriciale:

> **Sotto le ipotesi classiche del modello di regressione lineare, gli stimatori OLS sono lineari, non distorti e i più efficienti nella classe degli stimatori lineari e non distorti — BLUE.**

Si dimostra anche che **s² è a sua volta uno stimatore BLUE di σ²**. E, sotto l'ipotesi di normalità dei disturbi, il vettore degli stimatori si distribuisce come una **normale multivariata**, mentre la somma dei quadrati dei residui, rapportata a σ², si distribuisce come una **chi-quadrato con n − k gradi di libertà** — indipendentemente dagli stimatori dei coefficienti. È questa indipendenza che consente di costruire le statistiche *t* e *F*.

## 51. R² e R² corretto — il problema dell'inflazione dell'adattamento

L'**indice di determinazione multipla R²** ha lo stesso significato di prima: la proporzione di variabilità di Y spiegata dall'insieme delle variabili esplicative, compresa fra 0 e 1. Quanto più è prossimo a 1, tanto più il modello sembra adeguato.

**Sembra.** Ed è qui che il manuale pone un avvertimento che è **una domanda d'esame classica**:

> **Al crescere del numero di variabili esplicative la devianza dei residui si riduce sempre, e quindi R² aumenta sempre. L'aggiunta di una qualsiasi variabile esplicativa accresce R² a prescindere dal fatto che la variabile contribuisca o meno al modello.**

Di conseguenza — e questa è la conclusione da citare — **non è affatto vero che un R² vicino all'unità significhi che il modello è adeguato**: è possibilissimo che modelli con R² elevatissimi siano **poco adatti alla previsione o alla stima**. Un R² più alto non è un criterio per identificare il modello migliore. È il fenomeno che in inglese si chiama *overfitting*: il modello impara il rumore del campione, non la struttura del fenomeno.

**Il rimedio: l'R² corretto (*adjusted R²*).** Si costruisce rapportando la devianza residua ai suoi gradi di libertà (n − k) e la devianza totale ai propri (n − 1), invece di usare le devianze grezze. In questo modo **si penalizza l'aggiunta di variabili**: ogni variabile in più fa scendere il denominatore n − k, e se il guadagno in devianza spiegata non compensa la perdita di un grado di libertà, **l'R² corretto diminuisce**.

Da cui la regola operativa, che vale la pena dire esplicitamente:

> **R² non diminuisce mai aggiungendo variabili. R² corretto può diminuire. È perciò l'R² corretto — non l'R² — l'indice da usare quando si confrontano modelli che spiegano la stessa variabile dipendente con un numero diverso di variabili esplicative.**

Altre due proprietà utili dell'R² corretto: è **sempre minore o uguale all'R² semplice**, e a differenza di quest'ultimo **può assumere valori negativi** quando il modello è pessimo.

## 52. I test nella regressione multipla

Il manuale organizza tutti i test come casi particolari di un'unica **ipotesi lineare generale**, scritta in forma matriciale come un insieme di q vincoli sui coefficienti. Non serve sapere l'algebra; serve sapere che **un'unica statistica F copre tutti i casi** e riconoscere i tre casi particolari.

### 52.1 Significatività di un singolo coefficiente

> **H₀: βᵢ = 0** contro H₁: βᵢ ≠ 0

Statistica-test: **t = β̂ᵢ / es(β̂ᵢ)**, distribuita come una **t di Student con n − k gradi di libertà** (equivalentemente, una F con 1 e n−k gradi di libertà: F = t²). Il test verifica **se il modello sia più adeguato con l'inclusione o con l'esclusione di quell'ulteriore variabile esplicativa**: l'accettazione di H₀ implica che la variabile può essere rimossa dal modello perché **non significativa nello spiegare Y**.

> **L'avvertenza cruciale, testuale nel manuale.** *Quello utilizzato è solo un **test parziale**, in quanto il generico coefficiente i-esimo dipende da tutte le altre variabili incluse nel modello.* Detto altrimenti: il test *t* non dice se la variabile conta in assoluto, ma **se aggiunge qualcosa rispetto a quello che già spiegano le altre variabili presenti**. Cambiando le altre variabili, il verdetto può ribaltarsi. È una frase che, detta in commissione, dimostra di aver capito la regressione multipla.

Il test si generalizza a H₀: βᵢ = valore specificato, come nel caso semplice.

### 52.2 Significatività congiunta di tutti i coefficienti

> **H₀: β₁ = β₂ = … = β_k = 0** (tutti i coefficienti delle esplicative sono nulli; l'intercetta resta libera)

È il test che stabilisce **se esista o no una relazione significativa fra la variabile dipendente e l'insieme delle variabili esplicative**. La statistica-test è la **F di Fisher con k−1 e n−k gradi di libertà**, ed è

> **F = (devianza di regressione / k−1) / (devianza dei residui / n−k) = varianza di regressione / varianza dei residui**

esprimibile anche in funzione dell'R²: **F = [R²/(k−1)] / [(1−R²)/(n−k)]**.

**Che cosa significa rifiutare H₀.** Attenzione alla formulazione esatta, perché è un'altra domanda-trappola: il rifiuto dell'ipotesi nulla implica che **almeno una** delle variabili esplicative contribuisce significativamente a spiegare la dipendente. Non che contribuiscano tutte.

> **La configurazione diagnostica da riconoscere a colpo d'occhio: F significativa, nessuna t significativa.** Il modello nel suo insieme funziona, ma nessuna variabile presa singolarmente risulta significativa. È il **sintomo classico della multicollinearità**: le variabili spiegano bene Y insieme, ma sono così correlate fra loro che il modello non riesce ad attribuire il merito a nessuna in particolare. Se in commissione riconosci questa configurazione e la nomini, hai fatto centro.

### 52.3 Ipotesi sulla varianza

> **H₀: σ² = σ₀²**

Statistica-test **(n − k)s²/σ₀²**, distribuita come una **chi-quadrato con n − k gradi di libertà**.

### 52.4 Intervalli di confidenza

Identici nella struttura a quelli della regressione semplice: **stima ± (quantile della t con n−k gradi di libertà) × (errore standard del coefficiente)** per ciascun βᵢ; per σ² si usano i due quantili della chi-quadrato con n−k gradi di libertà, ottenendo un intervallo **asimmetrico**.

## 53. La previsione nella regressione multipla

Del tutto analoga al caso semplice. La **previsione puntuale** si ottiene sostituendo nell'equazione stimata i valori desiderati delle variabili esplicative. La **previsione intervallare** è più complessa, ma conserva le stesse due proprietà qualitative: **l'ampiezza cresce allontanandosi dal baricentro dei dati** e **l'intervallo per il singolo valore è più ampio di quello per il valore atteso**. Con più regressori, però, il «baricentro» è un punto in uno spazio a k dimensioni, e diventa possibile un'estrapolazione insidiosa: **una combinazione di valori che, presa variabile per variabile, è del tutto ordinaria, ma che nel campione non si è mai presentata congiuntamente**. È una versione anticipata del problema del *common support* che ritroverai al capitolo 16.

## 54. Le variabili dummy — argomento ad altissima probabilità d'esame

Fin qui abbiamo supposto variabili esplicative **quantitative**. Ma moltissime informazioni economicamente rilevanti sono **qualitative**.

**Il concetto.** Una **variabile qualitativa** (o **mutabile**) si manifesta nell'unità statistica mediante modalità dette **attributi**, esprimibili solo con espressioni verbali: il sesso di una persona («maschio»/«femmina»), il tipo di lavoro svolto («operaio», «impiegato»), il titolo di studio. Il manuale aggiunge un'osservazione utile: **anche quando le si indica con simboli numerici, restano qualitative**. L'esempio è calzante per il tuo bando: *gli impiegati dello Stato sono classificati secondo categorie (A, B ecc.) previste dalla legge sul pubblico impiego; questi simboli, tuttavia, non sono altro che qualifiche e restano variabili qualitative*. Non ha senso farne la media.

Alcune variabili qualitative presentano **due soli attributi** e sono dette **binarie** (uomo/donna, presente/assente); altre ne presentano più di due (grado di istruzione, professione).

**Le variabili dummy** sono le variabili binarie usate nell'analisi econometrica, particolarmente impiegate per la facilità di trattamento. Servono a due scopi: **inserire variabili qualitative** nel modello e **discriminare gli effetti di due situazioni differenti** sulla variabile dipendente.

**L'esempio del manuale**, che è anche l'esempio storico della tecnica: una **funzione di consumo in tempo di pace e in tempo di guerra**, con **intercette differenti ma la medesima pendenza**. Generalizzando, si tratta di osservazioni rilevate in presenza o in assenza di un fenomeno (una guerra, un cambiamento climatico, una riforma).

**Come si costruiscono.** Una dummy vale **1 in presenza del fenomeno e 0 in assenza**. Inserita nel modello accanto alle variabili quantitative, il suo coefficiente misura **di quanto si sposta l'intercetta** passando da una situazione all'altra: cioè la differenza sistematica fra i due gruppi, a parità di tutto il resto.

**La trappola della collinearità perfetta.** Il manuale mostra che si può scrivere il modello in due modi equivalenti: o con **una dummy per ciascuna delle due situazioni e nessuna intercetta**, oppure con **l'intercetta e una sola dummy**. Non si possono avere entrambe le dummy *e* l'intercetta, perché la loro somma è esattamente uguale alla colonna di uno dell'intercetta: si avrebbe **collinearità perfetta**, X′X non sarebbe invertibile e il modello non sarebbe stimabile. È la celebre **«trappola delle variabili dummy»** (*dummy variable trap*), e la regola operativa che ne discende è memorabile:

> **Con g modalità qualitative si inseriscono g−1 dummy, più l'intercetta. La modalità lasciata fuori diventa la «categoria di riferimento» (o «base»), e ogni coefficiente si legge come differenza rispetto ad essa.**

Nella seconda formulazione — quella con intercetta, che è quella usata da tutti i pacchetti statistici — i coefficienti si reinterpretano immediatamente: **l'intercetta diventa il livello del gruppo di riferimento, e il coefficiente della dummy diventa la differenza fra i due gruppi**.

**Le dummy di interazione.** Il passaggio più importante del paragrafo. Se la dummy fa spostare solo l'intercetta, i due gruppi hanno **rette parallele**: stesso effetto della variabile X, livello diverso. Ma se si vuole che anche **la pendenza** cambi fra i due gruppi, occorre **inserire una nuova variabile data dal prodotto fra la variabile X e la variabile dummy D**. Il modello diventa allora, nella versione con intercetta:

> **Y = α₁ + (α₂ − α₁)D + β₁X + (β₂ − β₁)(D·X) + ε**

e implica **due rette distinte**, una per ciascuno stato del fenomeno, con **intercette diverse e pendenze diverse**. Il vantaggio di scriverlo così, sottolinea il manuale, è che **i coefficienti sono direttamente le differenze**, e quindi se ne può testare la significatività con gli ordinari test *t* e *F* già visti: si può cioè **verificare statisticamente se il fenomeno cambia il livello, la pendenza, o entrambi**.

> **Perché questo paragrafo vale doppio per il tuo bando.** Il modello con una dummy di gruppo, una dummy di periodo e la loro **interazione** è, letteralmente, il modello **differenza-nelle-differenze** del capitolo 16 — lo strumento principe della valutazione d'impatto delle politiche pubbliche. Quando in commissione arriverai al DiD, potrai dire che **non è una tecnica nuova: è una regressione multipla con variabili dummy e un termine di interazione**, e il coefficiente dell'interazione è l'effetto della politica. È esattamente il tipo di collegamento che distingue una buona risposta da un'ottima risposta.

---

# PARTE X — LA MULTICOLLINEARITÀ

Il capitolo 10 è il primo dei «capitoli delle patologie»: che cosa succede quando un'ipotesi del modello classico non regge. Qui l'ipotesi in questione è quella di **non collinearità** delle variabili esplicative — il requisito, visto al paragrafo 47, che le colonne della matrice dei dati siano linearmente indipendenti.

## 55. Che cos'è la multicollinearità

Se fra le variabili esplicative **non esiste alcuna dipendenza lineare**, si dice che esse sono **ortogonali**: è la situazione ideale, in cui ciascuna porta informazione propria.

Si ha **multicollinearità perfetta** quando una variabile esplicativa è **esattamente** una combinazione lineare delle altre. In quel caso la matrice X′X è singolare, non è invertibile, e **il modello semplicemente non è stimabile**. È una situazione rara e quasi sempre dovuta a un errore di specificazione — l'esempio tipico è la *dummy variable trap* vista al paragrafo 54, o l'inserimento di una variabile e della stessa variabile espressa in un'altra unità di misura.

Molto più frequente, e molto più insidiosa, è la **quasi-multicollinearità**: **una dipendenza quasi lineare** fra le variabili. La definizione operativa che dà il manuale è la più chiara:

> **La multicollinearità è un problema dovuto all'eccessiva correlazione fra due o più variabili esplicative all'interno di un modello predittivo.**

E l'esempio è perfetto per la memoria: «Peso» e «Percentuale di massa grassa» sono spesso fortemente correlate; usarle insieme come predittori della colesterolemia **risulterebbe ridondante**, dal momento che vanno a spiegare **la stessa fetta di variabilità** della variabile dipendente.

Attenzione: il modello è stimabile, i coefficienti escono, il computer non protesta. È proprio questo che rende il problema pericoloso.

## 56. Gli effetti: perché la ridondanza è un danno

Il manuale elenca le conseguenze. Vale la pena impararle come un elenco, perché è la risposta diretta a «quali sono gli effetti della multicollinearità?».

1. **Gli errori standard dei coefficienti delle variabili correlate diventano più ampi**: le stime risultano **meno precise**. Questa è la conseguenza centrale, e ha una spiegazione formale elegante: la varianza di ciascun coefficiente contiene al denominatore il termine **(1 − R²ᵢ)**, dove R²ᵢ è l'indice di determinazione della regressione **di quella variabile esplicativa su tutte le altre**. Se la variabile è quasi perfettamente spiegata dalle altre, R²ᵢ tende a 1, il denominatore tende a zero e **la varianza esplode**.
2. **Gli intervalli di confidenza per i parametri diventano molto ampi**, di conseguenza.
3. **I coefficienti sono instabili**: possono cambiare — **anche di segno** — a seguito di lievi modifiche della struttura del modello. Il manuale indica esplicitamente questo come sintomo diagnostico: *grossi cambiamenti nelle stime dei coefficienti a seguito dell'aggiunta o dell'eliminazione di una variabile esplicativa sono un indizio della presenza di multicollinearità*. E lo stesso vale quando **segno e grandezza dei coefficienti sono contrari alle aspettative teoriche** — un coefficiente con il segno «sbagliato» è spesso un coefficiente multicollineare.
4. **Anche la covarianza fra due stime è alta** se le corrispondenti variabili sono fortemente collineari.
5. Le stime risultano **troppo grandi in valore assoluto**: formalmente, l'errore quadratico medio dipende dalla somma dei reciproci degli **autovalori** della matrice X′X, e in presenza di multicollinearità almeno un autovalore è molto piccolo, sicché il reciproco — e quindi l'MSE — diventa grande.

> **Il punto concettuale, da dire così.** *La multicollinearità non rende gli stimatori OLS distorti: restano corretti e restano BLUE. Il problema è che «Best» significa «a varianza minima fra gli stimatori lineari e corretti», e — come osserva il manuale a proposito della ridge — **il teorema di Gauss-Markov non garantisce affatto che questa varianza sia piccola**. In presenza di multicollinearità il modello nel suo insieme continua a prevedere bene, ma non riesce più a separare il contributo delle singole variabili: l'informazione per farlo, semplicemente, non c'è nei dati.*

## 57. Le cause

Quattro, secondo il manuale:

- **le tecniche di rilevazione dei dati** — per esempio un intervallo di variazione troppo limitato di alcuni regressori, o la presenza di errori di misurazione simili su regressori diversi;
- una **correlazione spuria o latente**: i regressori, pur non essendo in linea di principio legati, **risentono di fenomeni esterni che agiscono su entrambi**;
- una **non coerenza dei dati con la specificazione del modello** — per esempio quando si usa una polinomiale di grado più elevato del necessario (X e X² sono inevitabilmente correlate);
- l'**applicazione del modello a un numero ridotto di casi**.

## 58. Come si diagnostica — le cinque tecniche

### 58.1 Analisi della matrice di correlazione

Si esaminano i coefficienti di correlazione **fuori dalla diagonale**: se due variabili esplicative sono quasi linearmente dipendenti, il loro coefficiente assume un valore prossimo all'unità. **Il limite**, che il manuale segnala espressamente: questa tecnica è utile solo quando la correlazione riguarda **coppie** di variabili, **non quando si verifica fra più di due**. Tre variabili possono essere due a due debolmente correlate e tuttavia legate da una relazione lineare quasi esatta.

### 58.2 Il VIF — coefficiente di inflazione della varianza

È **lo strumento diagnostico standard**, quello da citare per primo. Definito da **Marquardt (1970)** come *Variance Inflation Factor*, misura, per ciascun termine del modello, **l'effetto della dipendenza fra variabili sulla varianza di quel termine**:

> **VIFᵢ = 1 / (1 − R²ᵢ)**

dove **R²ᵢ è l'indice di determinazione della regressione della variabile Xᵢ su tutte le altre variabili esplicative**.

Come si legge:

- se Xᵢ è **ortogonale** alle rimanenti, R²ᵢ ≈ 0 e **VIFᵢ ≈ 1**: nessun problema;
- se Xᵢ è legata da dipendenza quasi lineare a qualcuna delle altre, R²ᵢ tende a 1 e **VIFᵢ diventa grande**;
- al limite, se Xᵢ dipende linearmente dalle rimanenti, R²ᵢ = 1 e **VIFᵢ è infinito**.

**Le soglie**, entrambe riportate dal manuale: **Marquardt sostiene che un VIF maggiore di 10** segnala un'elevata correlazione fra Xᵢ e le altre esplicative; **altri studiosi suggeriscono di ricorrere a metodi di stima diversi dai minimi quadrati già quando il VIF supera 3**. Nella pratica corrente si usa spesso come regola pratica VIF > 5 come «attenzione» e VIF > 10 come «problema serio».

Una nota utile: **con due sole variabili esplicative, VIF₁ = VIF₂**, perché l'R² della regressione di X₁ su X₂ coincide con quello della regressione di X₂ su X₁ (entrambi sono il quadrato del coefficiente di correlazione fra le due).

### 58.3 Gli autovalori e il numero di condizionamento

Si esaminano gli **autovalori** della matrice X′X. **La presenza di multicollinearità è evidenziata dal fatto che uno o più autovalori è piccolo** (al limite nullo, che è il caso della collinearità perfetta). Si definisce allora il **numero di condizionamento** (*condition number*):

> **κ(X) = autovalore massimo / autovalore minimo**

Se la matrice è standardizzata e κ = 1, **le colonne sono ortogonali e non esiste problema di multicollinearità**; valori maggiori di 1 evidenziano una relazione fra le variabili, crescente al crescere di κ. **La soglia empirica riportata è 30: numeri di condizionamento maggiori di 30 indicano la presenza di multicollinearità.**

Il manuale riporta anche la **procedura a due stadi di Belsley, Kuh e Welsch (1990)**: nel primo stadio si selezionano gli autovalori con indice di condizionamento **≥ 30**; nel secondo si identificano le variabili potenzialmente affette da collinearità come **quelle in cui le proporzioni di varianza sono maggiori di 0,50**. È il metodo più raffinato perché non si limita a segnalare il problema, ma dice **quali variabili** vi sono coinvolte.

### 58.4 Il determinante della matrice X′X

Essendo X′X una matrice di correlazione, il suo determinante è compreso fra 0 e 1:

- **determinante = 1** → variabili esplicative **ortogonali**;
- **determinante = 0** → matrice **singolare**, esatta dipendenza lineare, multicollinearità perfetta.

Il manuale sviluppa un esempio numerico molto efficace: partendo da una matrice identità (determinante 1, regressori ortogonali) e portando le correlazioni fuori diagonale a 0,9, poi 0,99, poi 0,999, il determinante crolla a **0,628 → 0,0012 → 0,0001**, e contemporaneamente **gli elementi diagonali della matrice inversa — cioè le varianze dei coefficienti stimati — crescono in modo drammatico**. È la dimostrazione numerica del punto teorico.

### 58.5 I test d'ipotesi

Come già anticipato al paragrafo 52.2: **un test F globale significativo accompagnato da singoli test t tutti non significativi implica l'esistenza di multicollinearità**. Il manuale però avverte che **l'utilità di questa tecnica è discutibile**, perché non tutte le configurazioni di dati assumono questo comportamento in presenza di multicollinearità: è un indizio forte quando c'è, ma la sua assenza non esclude il problema.

## 59. I rimedi

### 59.1 Raccogliere ulteriori dati

La soluzione concettualmente più corretta: più informazione può separare ciò che nel campione attuale è confuso. Il manuale però segnala due limiti pratici: i dati aggiuntivi possono non essere disponibili o non riguardare la regione d'interesse dell'analista, e **spesso i dati aggiunti ripropongono lo stesso problema di multicollinearità** (se peso e massa grassa sono correlati nella popolazione, lo saranno in qualunque campione).

### 59.2 Rispecificare il modello

Poiché fra le cause c'è l'errata specificazione, si può intervenire sull'equazione:

- **ridefinire le variabili**, cercando funzioni che mantengano l'informazione originaria ma riducano l'impatto della multicollinearità (tipicamente: sostituire due variabili correlate con la loro somma e la loro differenza, o con un rapporto);
- **eliminare una o più variabili** fra quelle legate da dipendenza. Il manuale accompagna questo rimedio con un avvertimento netto: *la tecnica può essere di notevole aiuto, ma anche **pericolosa**, perché la variabile o le variabili eliminate potrebbero avere una capacità esplicativa significativa nei confronti della variabile dipendente*. Eliminare una variabile rilevante introduce una **distorsione da omissione**: si scambia varianza con distorsione.

### 59.3 La regressione ridge

È il rimedio «tecnico», e il ragionamento che lo giustifica merita di essere esposto per intero perché è concettualmente bellissimo.

Il teorema di Gauss-Markov assicura che lo stimatore OLS ha varianza minima **nella classe degli stimatori non distorti**; ma **non garantisce che questa varianza sia piccola**. Se la varianza è elevata, gli intervalli di confidenza diventano così ampi che lo stimatore risulta **instabile**. A quel punto conviene **accettare un compromesso**: uno stimatore **distorto**, che però ha **una varianza molto più piccola**.

La **ridge regression**, proposta da **Hoerl e Kennard (1970)**, fa esattamente questo. Tecnicamente consiste nel **trasformare la matrice X′X nella matrice X′X + cI**, dove c ≥ 0 è una costante arbitraria e I la matrice identità: in pratica si aggiunge una piccola quantità alla diagonale principale, rendendo la matrice «meglio condizionata» e invertibile in modo stabile.

I punti da sapere:

- **c è il «fattore di distorsione», detto anche *shrinkage parameter*** (parametro di contrazione);
- **se c = 0, lo stimatore ridge coincide con lo stimatore OLS**: l'OLS è il caso particolare senza contrazione;
- **lo stimatore ridge è distorto**, ma il suo **errore quadratico medio è minore** di quello dello stimatore OLS. Cioè: si perde in correttezza, si guadagna molto di più in precisione, e il bilancio complessivo è favorevole;
- **la ridge non elimina il problema della collinearità: ne riduce gli effetti**;
- per scegliere c, gli autori propongono un metodo esplorativo: si costruisce un grafico che rappresenta i coefficienti stimati in funzione di c, detto **«traccia della regressione ridge»** (*ridge trace*), e si sceglie il valore di c in corrispondenza del quale le curve **tendono a stabilizzarsi**. Il metodo consiste essenzialmente nello scegliere la costante in modo da realizzare **un equilibrio soddisfacente fra distorsione e varianza**.

> **La frase da portare all'orale.** *La regressione ridge è il primo esempio, nel manuale, del **trade-off fra distorsione e varianza**: si rinuncia deliberatamente alla correttezza dello stimatore per ottenere una riduzione della varianza tale da migliorare l'errore quadratico medio complessivo. È l'idea alla base di tutta la moderna statistica della regolarizzazione — LASSO, elastic net — e il ponte naturale con la parte di data science.*

## 60. I criteri di selezione delle variabili: i metodi stepwise

Il capitolo si chiude con il problema pratico: **quali regressori includere**? È il *trade-off* già incontrato al paragrafo 30, riformulato qui in termini di costo: da un lato **va considerato il maggior numero di variabili affinché il modello sia attendibile**, dall'altro **all'aumentare del numero di variabili indipendenti aumentano i costi delle osservazioni** (e la varianza delle stime).

I **metodi stepwise** sono procedure **sequenziali automatiche** in cui le singole variabili sono progressivamente aggiunte o eliminate dal modello, sulla base di test statistici. L'attenzione si sposta dalla «selezione delle variabili» al quesito **«sono significative o meno nello spiegare la variabile dipendente?»**. Sono tre:

**1. Forward selection (selezione in avanti).** Si parte da un modello **senza variabili esplicative**, con la sola intercetta. Si inserisce per prima la variabile che presenta **la più alta correlazione semplice con la variabile dipendente** (equivalentemente: quella che dà il più alto valore del test F), **purché il suo F osservato ecceda un valore prefissato F_in**. La seconda variabile scelta è quella che presenta la più alta **correlazione parziale** con Y — cioè considerando l'effetto della variabile già inserita — e viene aggiunta se il suo F parziale eccede F_in. E così via. La procedura termina quando il test F parziale non eccede più F_in, oppure quando è stata inserita l'ultima variabile candidata.

**2. Backward elimination (eliminazione all'indietro).** Direzione opposta. Si parte dal modello **completo**, con tutte le variabili candidate. Si calcola un F parziale per ciascun regressore, **come se esso fosse l'ultima variabile a entrare nel modello**; il più piccolo di questi F viene confrontato con un valore prefissato F_out: **se è più piccolo, la variabile viene rimossa**. Si ripete la procedura sul modello ridotto, finché il minimo F osservato non è più piccolo di F_out.

**3. Stepwise regression (regressione a passi).** Proposta da **Efroymson (1960)**, è **una combinazione delle due**: a ogni passo si può sia aggiungere sia eliminare una variabile, perché una variabile inserita in una fase precedente può diventare ridondante dopo l'ingresso di altre. Il manuale segnala la convenzione operativa: **in genere si scelgono i due valori soglia in modo che F_in > F_out**, così che **sia più difficile aggiungere una variabile esplicativa al modello piuttosto che eliminarne una**.

> **L'avvertenza critica, testuale nel manuale, da non dimenticare.** *Queste tecniche automatiche di selezione delle variabili consentono di specificare modelli econometrici **validi dal punto di vista statistico, ma la cui interpretazione è discutibile**.* È il punto da aggiungere sempre quando si parla di stepwise: sono procedure che **massimizzano l'adattamento ai dati, non la coerenza teorica**; ripetono decine di test d'ipotesi sugli stessi dati (con conseguente inflazione dell'errore di primo tipo); e producono modelli che spesso non si replicano su un campione diverso. In econometria la selezione delle variabili dovrebbe essere guidata **dalla teoria economica**, non da un algoritmo — coerentemente con quanto il manuale afferma già al capitolo 6: *nessuna procedura di selezione garantisce equazioni «migliori in assoluto»*.

---

# PARTE XI — METODI ASINTOTICI, MASSIMA VEROSIMIGLIANZA E VARIABILI STRUMENTALI

Il capitolo 11 è, insieme al 12, il più teorico del manuale. Ma contiene due argomenti che vale davvero la pena padroneggiare — **la massima verosimiglianza** e **le variabili strumentali** — perché sono nomi che qualunque commissione riconosce e perché il secondo è un pezzo essenziale del metodo controfattuale.

## 61. Perché servono i metodi asintotici

Le condizioni che giustificano l'applicazione dei minimi quadrati e delle procedure inferenziali associate sono, dice il manuale, **relativamente limitate**. In particolare l'ipotesi di **normalità dei disturbi** è forte e spesso indimostrabile. La buona notizia è che **le stesse procedure possono essere adoperate anche senza invocarla, purché il numero di osservazioni campionarie sia rilevante**: sotto certe condizioni, infatti, **lo stimatore converge in distribuzione alla legge normale al divergere della numerosità campionaria**.

I due concetti chiave sono due modi diversi di dire «che cosa succede quando n cresce».

**La convergenza in probabilità (consistenza).** Si dice che uno stimatore **converge in probabilità** al parametro vero se, al crescere di n, la probabilità che se ne discosti più di una quantità piccola a piacere **tende a zero**: l'evento «lo scarto è minore di ε» diventa **certo**. Si scrive con il simbolo **plim** (*limite in probabilità*). Il manuale dimostra che:

- **la media campionaria è uno stimatore consistente della media della popolazione**;
- **lo stimatore OLS è consistente**: plim β̂ = β.

**La convergenza in distribuzione (normalità asintotica).** Applicando il **teorema del limite centrale** allo stimatore OLS si stabilisce che, **asintoticamente, la legge dello stimatore OLS si approssima alla distribuzione normale centrata sul parametro vero**.

> **La conclusione pratica, ed è quella da dire all'orale.** *La proprietà di normalità asintotica degli stimatori OLS consente di ritenere approssimativamente validi i risultati sugli stimatori e sulle statistiche t ed F **anche quando gli errori non hanno distribuzione normale**, purché il campione sia sufficientemente ampio.* In altre parole: **l'ipotesi 6 del modello classico si può lasciar cadere se n è grande**. È questo che rende l'econometria applicabile al mondo reale, dove nessuno ha mai visto un errore veramente normale.

Il manuale coglie l'occasione per un richiamo utile sul **campionamento**: la teoria è molto più semplice assumendo che le osservazioni siano **indipendenti**, cosa che accade con il **campionamento bernoulliano** (con ripetizione) o da popolazione infinita. Con campionamento **senza ripetizione** da popolazione finita le osservazioni non sono indipendenti; ma **se n è molto più piccolo di N, come avviene quasi sempre in pratica, la differenza è minima**.

## 62. Il metodo della massima verosimiglianza (ML)

### 62.1 L'idea

La **massima verosimiglianza** (*Maximum Likelihood*, ML) è un procedimento generale per costruire stimatori, sviluppato originariamente dal genetista e statistico inglese **Ronald Fisher fra il 1912 e il 1922**. Il manuale la definisce così: consiste nel **massimizzare la funzione di verosimiglianza**, cioè una funzione di probabilità condizionata considerata come funzione del *secondo* argomento (i parametri), tenendo fisso il primo (i dati). In termini intuitivi:

> **La verosimiglianza è la probabilità di osservare esattamente i dati che ho osservato, calcolata in funzione dei parametri. Lo stimatore di massima verosimiglianza è quel valore dei parametri che rende i dati osservati "i più probabili possibile".**

È un rovesciamento di prospettiva rispetto ai minimi quadrati: l'OLS chiede *«quale retta passa più vicino ai punti?»*, la ML chiede *«quale popolazione avrebbe più plausibilmente generato questo campione?»*.

Nella pratica si lavora sempre con la **log-verosimiglianza**, ottenuta applicando il logaritmo naturale: poiché il logaritmo è una trasformazione **monotona crescente**, il punto di massimo non cambia, ma **la forma analitica diventa molto più semplice da trattare** — soprattutto perché la densità congiunta di osservazioni indipendenti è un **prodotto**, che il logaritmo trasforma in una **somma**.

### 62.2 Il risultato che conta per la regressione

Applicando la ML al modello di regressione lineare **sotto l'ipotesi di normalità degli errori**, il manuale ottiene un risultato che è **la cosa da sapere**:

> **Lo stimatore ML dei coefficienti β coincide esattamente con lo stimatore OLS.** Lo stimatore ML della varianza σ², invece, **è distorto**: differisce da quello OLS perché divide la somma dei quadrati dei residui per **n** anziché per **n − k**.

La ragione è intuitiva: per ogni dato valore di σ², la verosimiglianza è massima quando è minima la somma dei quadrati dei residui — cioè esattamente quando è soddisfatto il criterio dei minimi quadrati. **Sotto normalità, OLS e ML sono la stessa cosa per i coefficienti.**

### 62.3 Le proprietà e il teorema di Cramér-Rao

Gli stimatori ML godono di proprietà sia **finite** (per campioni di ampiezza limitata) sia **asintotiche**.

**La proprietà finita più importante**, nella formulazione del manuale: *se esiste uno stimatore a minima varianza, il metodo della massima verosimiglianza lo identifica*. È una garanzia di ottimalità molto forte.

Il risultato teorico che la sostiene è il **teorema di Cramér-Rao**, dai nomi del matematico e statistico svedese **Harald Cramér** e dello statistico indiano **Calyampudi Radhakrishnan Rao**:

> **Teorema di Cramér-Rao.** *La varianza di qualsiasi stimatore **corretto** non può scendere al di sotto di un limite inferiore determinato — il «lower bound», spesso indicato con MVB (Minimum Variance Bound), pari all'inversa della cosiddetta **matrice d'informazione di Fisher**.*

Due precisazioni che il manuale segnala e che fanno la differenza se le riporti:

- la disuguaglianza **è riferita esclusivamente a stimatori corretti**: uno stimatore **distorto può benissimo avere varianza inferiore** al limite di Cramér-Rao. È di nuovo il *trade-off* distorsione/varianza visto con la ridge;
- **non esiste alcuno stimatore corretto di σ² che raggiunga questo estremo inferiore**: per campioni di ampiezza limitata la varianza dello stimatore OLS della varianza è sicuramente maggiore del limite minimo.

**Le tre proprietà asintotiche degli stimatori ML** — questo è un elenco da memorizzare, è una domanda perfetta:

1. **consistente**: plim θ̂ = θ;
2. **asintoticamente normale**, con matrice di varianze e covarianze pari all'inversa della matrice d'informazione;
3. **asintoticamente efficiente**, in quanto la sua matrice di varianze e covarianze **raggiunge il limite inferiore di Cramér-Rao** — cioè, asintoticamente, **è lo stimatore migliore possibile fra quelli corretti**.

> **Quando si usa la ML e non l'OLS.** Sotto le ipotesi classiche con errori normali le due coincidono e tanto vale usare l'OLS, che è più semplice. La ML diventa indispensabile quando **il modello non è lineare nei parametri** o quando **la variabile dipendente non è continua**: è il metodo con cui si stimano i **modelli a variabile dipendente qualitativa — logit e probit**, quelli in cui la Y è una dummy (occupato/disoccupato, ha ottenuto il contributo/non l'ha ottenuto). È un collegamento che vale la pena avere pronto, perché quei modelli sono usatissimi nella valutazione delle politiche, e sono anche il punto di contatto con la classificazione nel data mining.

## 63. Le variabili strumentali — il tema più importante del capitolo

### 63.1 Il problema: l'endogeneità dei regressori

Un'ipotesi fondamentale del modello classico è che **le variabili esplicative siano ortogonali al termine di disturbo** — che esplicative e componente d'errore siano indipendenti. In questo caso si dice che le variabili esplicative sono **esogene**.

Quando invece esiste un legame fra regressori ed errore, sorge il problema dell'**endogeneità dei regressori**, che **rende impossibile la stima corretta dei parametri**: lo stimatore OLS diventa **distorto e inconsistente**, e la distorsione non si attenua all'aumentare del campione.

**Le tre fonti di endogeneità**, da elencare così perché sono esattamente le tre situazioni in cui salta la valutazione di una politica:

**1. Omissione di una variabile esplicativa rilevante.** L'esempio del manuale è il più celebre dell'econometria applicata: *la stima dell'effetto dell'istruzione sul reddito*. Chi ha studiato di più guadagna di più — ma se non si considera l'**abilità**, che **non è misurabile**, il coefficiente dell'istruzione cattura anche l'effetto dell'abilità, perché le persone più abili tendono a studiare di più *e* a guadagnare di più indipendentemente dallo studio. La variabile omessa finisce nell'errore, e l'errore risulta correlato con il regressore. Il rimedio suggerito dal manuale: **utilizzare una variabile correlata con quella omessa** — per esempio il quoziente d'intelligenza.

**2. Errori di misurazione delle variabili indipendenti.** Se gli errori di misura riguardassero **soltanto la variabile dipendente** non ci sarebbero problemi, perché verrebbero semplicemente incorporati nel termine di errore. Ma se riguardano le **esplicative**, la variabile osservata è la somma di quella vera e di un errore, e quell'errore è per costruzione correlato con il disturbo.

**3. Simultaneità e autocorrelazione nei modelli dinamici.** La simultaneità si verifica **quando le variabili sono determinate congiuntamente in equilibrio**: l'esempio canonico è **il prezzo e la quantità di un bene scambiato sul mercato**. La quantità è data dall'uguaglianza fra domanda e offerta, per cui **non è possibile distinguere l'effetto dei due fattori** — non si sa se si sta stimando la curva di domanda o quella di offerta. Nell'analisi delle serie storiche, invece, le variabili economiche sono spesso **autocorrelate**: il valore attuale è connesso con quelli passati, e occorre costruire un modello dinamico che tenga esplicitamente conto degli shock già avvenuti.

### 63.2 La soluzione: le variabili strumentali (IV)

Il metodo consiste nel trovare un numero di variabili — **almeno pari a quello dei regressori endogeni** — che soddisfino **tre condizioni**. Questa è la parte da sapere a memoria, parola per parola, perché è la domanda tipica:

> **Le tre condizioni di una variabile strumentale valida:**
>
> 1. **Condizione di rilevanza** — lo strumento deve essere **correlato con i regressori endogeni**. Se non lo fosse, non porterebbe alcuna informazione utile a identificare l'effetto.
> 2. **Condizione di esogeneità** — lo strumento deve risultare **incorrelato con i disturbi**. È questa che «ripulisce» la stima.
> 3. **Condizione di esclusione** — lo strumento **non deve influenzare direttamente la variabile dipendente**, ma solo attraverso il regressore endogeno.

**L'intuizione.** Lo strumento agisce come una **leva esterna**: è una fonte di variazione del regressore sospetto che **non ha niente a che fare con l'errore**. Usando solo quella parte di variazione — la parte «pulita» — si riesce a identificare l'effetto causale.

**L'esempio del manuale**, quello del mercato: per stimare la curva di domanda separandola dall'offerta serve *una variabile strumentale correlata con una delle due curve ma non con l'altra*; per esempio **i fattori meteorologici, che influenzano l'offerta di un certo bene alimentare ma non la domanda**. Un'ondata di gelo sposta la curva di offerta lungo la curva di domanda, e questo permette di tracciare quest'ultima.

### 63.3 Le condizioni di identificazione

Il manuale formalizza due condizioni che tornano identiche nel capitolo 13 sulle equazioni simultanee:

- **condizione d'ordine**: occorre **disporre di almeno tante variabili strumentali quante sono le variabili endogene**. Se la condizione è soddisfatta come **uguaglianza**, si ha un numero «appena sufficiente» di strumenti e il modello si dice **just identified** (esattamente identificato); se gli strumenti sono di più, il modello è **sovraidentificato**;
- **condizione di rango**: una condizione tecnica sulla matrice degli strumenti, che garantisce che essi siano effettivamente informativi e non ridondanti.

La condizione d'ordine è **necessaria ma non sufficiente**; quella di rango è **necessaria e sufficiente**. È una distinzione che vale la pena riportare.

### 63.4 La proprietà dello stimatore IV

Lo stimatore a variabili strumentali è **consistente**: plim β̂_IV = β, a condizione che valgano esattamente le due proprietà sopra — **esogeneità** (la correlazione fra strumento ed errore tende a zero) e **rilevanza** (la correlazione fra strumento e regressore endogeno non è nulla).

> **La precisazione da fare per non sbagliare.** *Lo stimatore IV è **consistente ma non corretto**: in campioni finiti resta distorto, e la sua varianza è **maggiore** di quella dell'OLS. Si accetta questo costo perché l'OLS, in presenza di endogeneità, non è né corretto né consistente: è **sistematicamente sbagliato**, e resta sbagliato per quanti dati si aggiungano. Meglio uno stimatore un po' impreciso ma che converge al valore vero, che uno stimatore preciso attorno a un valore sbagliato.* E aggiungi, se puoi: **strumenti "deboli"** — cioè poco correlati con il regressore endogeno — producono stime molto instabili e possono essere peggiori dell'OLS. La condizione di rilevanza non è una formalità.

> **Perché questo paragrafo conta doppio per il tuo bando.** Le variabili strumentali sono **uno dei metodi quantitativi di valutazione delle politiche pubbliche** che ritroverai al capitolo 16 e nella scheda sulla valutazione d'impatto. L'idea è sempre la stessa: quando l'assegnazione al trattamento non è casuale, si cerca una fonte di variazione «quasi casuale» — una lotteria, una soglia amministrativa, la distanza geografica da un servizio — che influenzi la probabilità di ricevere il trattamento ma non l'esito, e la si usa come strumento. Il **regression discontinuity design** è, da questo punto di vista, un caso particolare di variabile strumentale.

---

# PARTE XII — LA VIOLAZIONE DELL'IPOTESI DI SFERICITÀ: ETEROSCHEDASTICITÀ E AUTOCORRELAZIONE

Questo è il capitolo più lungo del manuale e, dopo il capitolo 7, il più importante. Contiene due patologie distinte che condividono la stessa diagnosi formale e lo stesso rimedio generale.

## 64. L'ipotesi di sfericità degli errori

La matrice di varianze e covarianze dei termini d'errore, sotto le ipotesi classiche, ha una struttura molto particolare: **tutti gli elementi sulla diagonale principale sono uguali a σ²** e **tutti gli elementi fuori dalla diagonale sono nulli**. Questa condizione doppia — **varianza costante** e **assenza di correlazione fra coppie di errori** — si chiama **ipotesi di sfericità degli errori**.

Le due violazioni possibili sono:

- **eteroschedasticità**: gli elementi **sulla diagonale non sono tutti uguali**, cioè Var(ε₁) ≠ Var(ε₂) ≠ … Gli errori hanno varianza diversa da osservazione a osservazione;
- **autocorrelazione**: alcuni o tutti gli elementi **fuori dalla diagonale sono diversi da zero**, cioè Cov(εᵢ, εⱼ) ≠ 0 per i ≠ j. Gli errori sono correlati fra loro.

**Dove si trovano.** Il manuale fa una mappatura che vale la pena ricordare perché è la risposta perfetta a «dove si incontrano questi problemi?»:

- **l'eteroschedasticità è tipica dei dati cross section**. L'esempio canonico: **l'analisi sui profitti di imprese di diversa dimensione**. La varianza del profitto non è costante da osservazione a osservazione — le grandi imprese hanno profitti più elevati e una variabilità, in valore assoluto, molto maggiore di quella delle piccole. In generale: quando le unità osservate hanno scale molto diverse, gli errori hanno dispersioni molto diverse;
- **l'autocorrelazione è tipica delle serie storiche**, dove **una non corretta specificazione dinamica si tramuta in autocorrelazione dei residui**: gli errori possono **cumularsi nel tempo** oppure **ripetersi secondo le stesse modalità**.

## 65. Che cosa succede agli stimatori OLS

È **la domanda d'esame** su questo capitolo, e la risposta è secca:

> **In presenza di errori non sferici, lo stimatore OLS resta CORRETTO ma NON è più EFFICIENTE**: non soddisfa più la proprietà di minima varianza, perché non sfrutta tutta l'informazione teoricamente disponibile. **Di conseguenza le procedure di stima intervallare e i test d'ipotesi basati su tale stimatore non risultano più adeguati.**

Scomponiamo, perché ogni pezzo conta:

1. **La correttezza si conserva**: E(β̂) = β. Il valore atteso dello stimatore è ancora il parametro vero. **Non c'è distorsione.** Questa è la buona notizia, ed è il motivo per cui l'eteroschedasticità è un problema meno grave dell'endogeneità.
2. **L'efficienza si perde**: esiste un altro stimatore, lineare e corretto, con varianza minore. **Gauss-Markov non vale più**, perché la dimostrazione del teorema usa proprio le ipotesi 3 e 4.
3. **Il danno pratico vero**: le formule con cui si calcolano gli **errori standard** sono derivate *assumendo* la sfericità. Se questa non vale, **gli errori standard stampati nell'output sono sbagliati** — tipicamente sottostimati. Di conseguenza **le statistiche t sono gonfiate** e si finisce per **dichiarare significative variabili che non lo sono**. Tutta l'inferenza — test t, test F, intervalli di confidenza — diventa inaffidabile.

> **La formula da ripetere.** *L'eteroschedasticità e l'autocorrelazione non distorcono le stime: distorcono la nostra misura della loro precisione. Il coefficiente è giusto in media, ma non sappiamo più quanto fidarci.*

## 66. Il rimedio generale: i minimi quadrati generalizzati (GLS)

L'idea è semplice ed elegante: **se il modello non soddisfa le ipotesi classiche, lo si trasforma in un modello equivalente che le soddisfa**, e poi vi si applicano i normali minimi quadrati.

Tecnicamente si moltiplica l'intero modello per un'opportuna **matrice di trasformazione**, costruita in modo che gli errori del modello trasformato abbiano **varianza costante e siano incorrelati**. A quel punto le ipotesi classiche valgono di nuovo e l'OLS è applicabile.

Lo stimatore che ne risulta si chiama **stimatore dei minimi quadrati generalizzati (GLS, *Generalized Least Squares*)**, detto anche **stimatore di Aitken**. Le sue proprietà:

- **è non distorto**;
- **è BLUE**, perché è ottenuto applicando il criterio dei minimi quadrati a un modello che rispetta le ipotesi classiche;
- **se si aggiunge l'ipotesi di normalità dei termini di errore, è anche stimatore di massima verosimiglianza**;
- **coincide con lo stimatore OLS quando gli errori sono sferici**: l'OLS è il caso particolare del GLS in assenza di patologie.

> **Il limite pratico, che il manuale sottolinea espressamente.** *Nella pratica non è nota la matrice di varianze e covarianze degli errori, per cui **l'utilità dello stimatore GLS è notevolmente limitata dalla necessità di conoscere gli elementi di tale matrice**.* È esattamente qui che nasce tutto il resto del capitolo: poiché la struttura degli errori non è nota, occorre prima **diagnosticarla** (i test) e poi **stimarla** (le procedure iterative). Quando la matrice è stimata anziché nota si parla di **GLS ammissibili** o *feasible GLS*.

---

## 67. L'ETEROSCHEDASTICITÀ

### 67.1 La struttura e i minimi quadrati ponderati

In presenza di eteroschedasticità gli errori **restano incorrelati** — gli elementi fuori dalla diagonale sono nulli — ma **hanno varianza disuguale**: Var(εᵢ) = σᵢ², diversa per ciascuna osservazione.

Poiché la matrice è **diagonale**, il GLS assume una forma particolarmente semplice e intuitiva: le componenti che compongono la funzione obiettivo dei minimi quadrati vengono **pesate** da fattori che tengono conto della diversa varianza. La procedura si chiama **metodo dei minimi quadrati ponderati (WLS, *Weighted Least Squares*)**.

**Il principio dei pesi**, che è la cosa da capire e da saper dire:

> **Si dà più peso alle osservazioni con varianza piccola — quelle più affidabili, che portano informazione precisa — e meno peso alle osservazioni con varianza grande, quelle più rumorose. Il peso è inversamente proporzionale alla varianza dell'errore.**

Il manuale sviluppa un caso concreto illuminante: quello dei **dati raggruppati**. Se si dispone solo delle **medie** di m gruppi di numerosità diversa, la varianza della media del gruppo i-esimo è σ²/nᵢ — cioè **inversamente proporzionale alla numerosità del gruppo**. Le medie dei gruppi grandi sono più precise di quelle dei gruppi piccoli, e i pesi corretti risultano essere **le numerosità dei gruppi stessi**. È un risultato di grande buon senso statistico: la media di 1.000 osservazioni deve contare di più della media di 10.

L'eteroschedasticità, segnala il manuale, oltre che nelle analisi cross section **è tipicamente presente proprio nelle analisi con dati raggruppati**.

### 67.2 I test di eteroschedasticità

Tre, da conoscere per nome, ambito di applicazione e logica.

**a) Test di uguaglianza delle varianze (test di Bartlett).** Si usa quando i dati sono **raggruppati in classi**. Si calcolano le varianze campionarie **entro ciascun gruppo**, poi la varianza totale, e si costruisce una statistica basata sui **logaritmi** delle varianze, che sotto l'ipotesi di omoschedasticità si distribuisce come una **chi-quadrato con m − 1 gradi di libertà** (m = numero di gruppi). L'approssimazione migliora dividendo per un opportuno fattore di correzione. Si rifiuta l'ipotesi nulla se il valore empirico supera il valore critico.

**b) Test di Breusch-Pagan.** È il test **asintotico**, quindi **per grandi campioni**, ed è il **caso più frequente, quello di osservazioni puntuali**. È il test da citare per primo.

La procedura, in quattro passi:

1. si stima il modello con OLS e si ricavano i **residui**;
2. si calcola una serie normalizzata basata sui **quadrati dei residui** divisi per la loro varianza media;
3. **si regredisce questa serie sulle variabili z che si sospetta possano spiegare l'eteroschedasticità** e si calcola la devianza spiegata ESS;
4. la statistica-test — proporzionale alla devianza spiegata — si distribuisce asintoticamente come una **chi-quadrato con p−1 gradi di libertà** (p−1 = numero di variabili z). Se supera il valore critico, **si rigetta l'ipotesi nulla di omoschedasticità**.

Il manuale dà anche il **significato intuitivo**, che è il modo migliore di esporlo: *se sussiste eteroschedasticità, e se questa è effettivamente spiegata dalle variabili z prescelte, allora queste stesse variabili forniranno una buona spiegazione dell'andamento della regressione dei quadrati dei residui; per questo la devianza spiegata sarà elevata e la statistica cadrà nella zona di rifiuto.* In una frase: **si prova a spiegare la dispersione dei residui; se ci si riesce, la dispersione non è costante**.

Nota importante: il test **è indipendente dalla forma funzionale** ipotizzata per la relazione fra varianza e variabili z. Non occorre sapere *come* la varianza dipende dalle z, basta sapere *da quali* z.

**c) Test di Goldfeld-Quandt.** Si usa **per piccoli campioni**, **quando si sospetta che una specifica variabile esplicativa sia la causa dell'eteroschedasticità**. La procedura, che è visivamente intuitiva:

1. **si dispongono i dati in ordine crescente rispetto alla variabile X sospettata**;
2. **si omettono le c osservazioni centrali** (in pratica, circa **un quarto** del totale: nell'esempio del manuale, con 30 osservazioni, se ne omettono 8). Il motivo dell'omissione è accentuare il contrasto fra i due estremi;
3. **si stima separatamente il modello sulle prime osservazioni e sulle ultime**, e si calcolano le due somme dei quadrati dei residui;
4. la statistica-test è il **rapporto fra la somma dei quadrati dei residui più grande e quella più piccola**, distribuito come una **F di Fisher**. Se eccede il valore critico si **rifiuta l'ipotesi di omoschedasticità**.

L'idea: se la varianza cresce con X, allora i residui del sottocampione con X alto saranno molto più dispersi di quelli del sottocampione con X basso, e il loro rapporto sarà grande.

> **Il test che il manuale nomina ma non sviluppa, e che conviene comunque citare: il test di White**, che è il più generale di tutti, perché non richiede di specificare quali variabili causino l'eteroschedasticità: regredisce i quadrati dei residui su tutte le esplicative, sui loro quadrati e sui loro prodotti incrociati. È il test di routine dei pacchetti statistici. Utile da menzionare insieme a una nota finale: nella pratica corrente, prima ancora di correggere il modello, si usano gli **errori standard robusti all'eteroschedasticità** (detti *robusti* o *di White*), che lasciano intatte le stime OLS ma ne ricalcolano gli errori standard in modo valido anche in presenza di eteroschedasticità. È la soluzione più diffusa oggi.

---

## 68. L'AUTOCORRELAZIONE (e gli elementi di analisi delle serie storiche)

L'ipotesi di covarianza nulla fra errori è, dice il manuale, **la più esposta a essere violata, soprattutto in presenza di serie storiche**. Per trattarla il capitolo introduce contestualmente tutta la strumentazione di base dell'analisi delle serie temporali — che è poi la stessa che tornerà, applicata, nel capitolo 14.

### 68.1 Serie storiche e processi stocastici

**Definizione di serie storica** (da sapere testualmente): *una successione di osservazioni ordinate logicamente secondo una variabile t, la quale nella maggior parte dei casi rappresenta il tempo.* Lo studio riguarda sia la **dinamica temporale** della serie (analisi univariata) sia le **connessioni con altre serie storiche collegate** (analisi multivariata).

La caratteristica che distingue le serie storiche da tutti gli altri dati, e che il manuale spiega molto bene in nota, è che **la serie storica «ha memoria di sé»**: il dato rilevato in un istante t è più simile a quello rilevato in t−1 che a quelli di epoche lontane. **Nelle serie storiche l'ordinamento delle osservazioni ha importanza fondamentale**, mentre nei dati cross section è irrilevante.

**Definizione di processo stocastico** (altra definizione da sapere a memoria): *una famiglia di variabili casuali dipendenti dal parametro tempo t, che varia in un insieme T di numeri reali*. Si distingue fra processi **continui e discreti** (secondo la natura delle variabili casuali) e fra processi **a tempo continuo e a tempo discreto** (secondo il supporto del parametro t).

**Il legame fra i due concetti** è il passaggio concettuale più importante del paragrafo, ed è bellissimo:

> **Una serie storica osservata è una parte finita di UNA realizzazione di un processo stocastico.** È solo una parte, perché è un campione finito e unico della famiglia di variabili casuali che caratterizzano il processo. **Si stabilisce così un'analogia fra serie storica osservata e campione casuale**: come a una popolazione statistica corrisponde un universo dei campioni che consente di inferire sui parametri incogniti, così **a un processo stocastico corrisponde un insieme di serie storiche, di cui quella osservata costituisce una realizzazione finita** e rappresenta la base per costruire un modello statistico del meccanismo generatore.

Detto in modo più diretto: della storia economica abbiamo **una sola realizzazione**. Non possiamo rifare il Novecento. Ed è precisamente questa la difficoltà fondativa dell'econometria delle serie storiche.

**I momenti di un processo stocastico** sono tre e li useremo tutti:

- il **valore medio** al tempo t;
- l'**autocovarianza** fra Xₜ e Xₜ₊ₛ, che misura, **per ogni lag (ritardo temporale) s, la covarianza fra il processo e se stesso ritardato**. Per s = 0 coincide con la varianza;
- il **coefficiente di autocorrelazione al ritardo s**, che esprime **la correlazione interna alle osservazioni di un processo**, detta per questo **correlazione seriale**.

### 68.2 La classificazione dei processi stocastici

Per poter fare inferenza su una serie storica occorre imporre delle restrizioni ai processi. Cinque definizioni, tutte brevi e tutte potenzialmente oggetto di domanda.

**a) Processo stazionario (in senso debole, o in covarianza).** Tre condizioni:

1. **valore medio costante** al variare del tempo (invarianza in media);
2. **varianza finita e costante** al variare del tempo (omoschedasticità);
3. **autocovarianza dipendente solo dal lag s**, non dall'istante t.

> **Perché la stazionarietà è la condizione fondamentale.** Se le proprietà statistiche del processo cambiano nel tempo, non ha senso stimarle su un campione passato per applicarle al futuro. **La stazionarietà è ciò che rende possibile l'inferenza su una serie storica.** Quasi tutte le serie economiche grezze — il PIL, i prezzi, la popolazione — **non sono stazionarie**, perché crescono: per questo il primo passo dell'analisi è quasi sempre **renderle stazionarie**, tipicamente prendendo le **differenze prime** o i **logaritmi**.

**b) Processo White Noise (rumore bianco).** Un processo stazionario particolare, il più semplice di tutti, con: **valore medio nullo**, **varianza finita e costante**, **variabili incorrelate in tempi successivi**. È il «processo senza struttura»: il presente non contiene alcuna informazione sul futuro. **È l'obiettivo della modellazione**: un modello è adeguato quando i suoi residui sono un white noise, cioè quando ha estratto dai dati tutta l'informazione disponibile.

**c) Processo gaussiano.** Un processo le cui variabili casuali hanno distribuzioni **normali**. Se è anche white noise, si parla di **white noise gaussiano**.

**d) Processo ergodico.** Un processo in cui **l'autocovarianza tende a zero al crescere del lag**: la memoria si esaurisce. Serve perché, avendo una sola realizzazione, si possa comunque stimare i momenti del processo usando le medie temporali.

**e) Processo invertibile.** Un processo che si può **esprimere tramite le variabili casuali precedenti**, cioè regredire sui propri valori passati. Il manuale segnala perché conta: **l'invertibilità è importante in un'ottica di previsione**.

### 68.3 ACF e PACF: gli strumenti diagnostici

**La funzione di autocorrelazione globale (ACF, *Autocorrelation Function*).** L'autocovarianza è fondamentale ma ha il difetto di **non essere compresa fra limiti fissi**, il che rende difficile giudicare il significato di un dato valore. Dividendola per il prodotto degli scarti quadratici medi si ottiene l'**autocorrelazione**, che ha il vantaggio di essere **compresa fra −1 e +1** e gode delle stesse proprietà del coefficiente di correlazione di Pearson. Esprime **la dipendenza lineare fra il processo al tempo t e se stesso al tempo t+s**.

**Il correlogramma** è la sua rappresentazione grafica: un grafico in cui ogni barretta verticale riporta il valore dell'autocorrelazione in funzione del ritardo. Il manuale insegna a leggerlo distinguendo **tre situazioni tipiche** — ed è una griglia di lettura molto efficace, da riportare tale e quale:

| Andamento del correlogramma | Interpretazione | Componente dominante |
|---|---|---|
| Autocorrelazione **sempre positiva, che decresce lentamente** al crescere del ritardo | I valori sono fortemente correlati con quelli del periodo precedente, un po' meno con quelli di due periodi prima, ecc.: **il presente è influenzato dal passato recente**, e la serie ha una tendenza di fondo | **TREND** (componente tendenziale) |
| Autocorrelazione **positiva e massima in corrispondenza di ritardi che configurano una periodicità annuale** (s = 4 e multipli, per dati trimestrali), minore o negativa altrove | I valori di un dato periodo dell'anno sono fortemente correlati con quelli degli stessi periodi degli anni precedenti: **il fenomeno varia nel corso dell'anno e in modo simile da un anno all'altro** | **STAGIONALITÀ** |
| Autocorrelazioni che per s > 0 **oscillano sempre entro una banda ristretta** | La serie non è significativamente correlata con le serie ritardate: **il passato non spiega il presente**, le variazioni sono sostanzialmente casuali | **COMPONENTE ACCIDENTALE** (parte stocastica) |

Il correlogramma è quindi utile **sia prima dell'analisi**, per individuare subito un'eventuale componente dominante, **sia dopo**, per verificarne i risultati.

**La funzione di autocorrelazione parziale (PACF, *Partial Autocorrelation Function*).** Parte della correlazione fra Xₜ e Xₜ₊ₛ può essere dovuta **alla correlazione che entrambe hanno con i ritardi intermedi**. La PACF misura **l'autocorrelazione al netto della dipendenza lineare dalle variabili intermedie**. Il manuale precisa che **l'informazione contenuta nella PACF è esattamente la stessa contenuta nell'ACF** — è una sua trasformazione — ma **è utile perché mette in evidenza caratteristiche diverse**. È l'analogo, in versione temporale, della differenza fra correlazione semplice e correlazione parziale.

### 68.4 I processi AR, MA e ARMA

I tre modelli fondamentali. Questa sezione è la base del capitolo 14.

**Processo autoregressivo AR(p)** — da *Auto-Regressive*. L'osservazione al tempo t è **una combinazione lineare di p termini immediatamente precedenti più una componente casuale** (un white noise). Si chiama così **perché è assimilabile a una regressione della variabile su se stessa**.

Un **AR(1)** è il caso più semplice: Xₜ = φXₜ₋₁ + Wₜ, con **|φ| < 1** — condizione necessaria perché il processo abbia varianza finita, ed è la **condizione di stazionarietà**.

La sua funzione di autocorrelazione è **ρₛ = φˢ**: decresce **geometricamente**. L'interpretazione che dà il manuale è molto efficace:

> *Le autocorrelazioni, che sono **un indice della memoria del processo**, sono tanto più grandi quanto più grande è φ, il quale rappresenta una sorta di **«parametro di persistenza»**.*

**La firma diagnostica di un AR** — questo è il punto operativo:

- **ACF**: **decresce progressivamente e lentamente verso zero**, in modo esponenziale o con oscillazioni smorzate (l'alternanza dei segni dipende dal segno di φ). **Non si annulla mai bruscamente**;
- **PACF**: presenta **un solo valore significativo, il primo** (per un AR(1)); due per un AR(2); p per un AR(p). Poi **si annulla di colpo**.

Per l'**AR(2)** valgono tre condizioni di stazionarietà sui parametri, e il correlogramma può decrescere esponenzialmente oppure con oscillazioni.

**Processo a media mobile MA(q)** — da *Moving Average*. L'osservazione al tempo t è **una combinazione lineare di processi white noise**: del rumore corrente e di q rumori passati. Il termine «media mobile» deriva dal fatto che Xₜ è costruito come **somma pesata, simile a una media, dei valori più recenti del rumore**.

**La firma diagnostica di un MA** è l'**esatto speculare** di quella di un AR:

- **ACF**: presenta **esattamente q termini non nulli e poi si annulla di colpo**. Il correlogramma di un MA(1) è costituito **da un solo termine**, positivo o negativo a seconda del segno del parametro; quello di un MA(q) da q termini;
- **PACF**: **decresce gradualmente** verso zero.

Il manuale segnala una curiosità tecnica che vale la pena conoscere: **esistono sempre due valori distinti del parametro θ che restituiscono la medesima funzione di autocorrelazione** (uno è il reciproco dell'altro). Per esempio i processi con θ = 0,5 e θ = 2 hanno la stessa ACF. È per questo che si impone la **condizione di invertibilità**, che seleziona l'unica rappresentazione sensata. Nota anche che quando θ = 0 il processo **è un white noise**, e che al crescere di θ **la serie si "smussa" e la sua varianza aumenta**.

**Processo misto ARMA(p, q).** Costituito congiuntamente da **una parte autoregressiva di ordine p e una parte a media mobile di ordine q**. Ovviamente ARMA(1,0) = AR(1) e ARMA(0,1) = MA(1). Il vantaggio: **consente di rappresentare processi complessi con pochi parametri** — il manuale osserva che un ARMA(1,1) produce «un modello potente e con capacità di rappresentare serie storiche reali molto superiore a quanto ci si potrebbe aspettare dalla sua semplicità».

Le sue ACF e PACF sono **una mistura** di quelle dei due processi costituenti: in generale il correlogramma di un ARMA(p,q) conserva le caratteristiche di quello di un AR(p) **a eccezione dei primi valori**.

> **La tabella che vale un esame — l'identificazione dei processi.**
>
> | Processo | ACF (autocorrelazione globale) | PACF (autocorrelazione parziale) |
> |---|---|---|
> | **AR(p)** | decresce gradualmente (esponenziale o sinusoidale smorzata), **non si annulla mai** | **si annulla dopo p ritardi** (taglio netto) |
> | **MA(q)** | **si annulla dopo q ritardi** (taglio netto) | decresce gradualmente |
> | **ARMA(p,q)** | mistura: decresce gradualmente dopo i primi ritardi | mistura: decresce gradualmente dopo i primi ritardi |
>
> **La regola mnemonica: AR taglia la PACF, MA taglia l'ACF.** Questa tabella è letteralmente **la fase di identificazione della procedura Box-Jenkins** che incontrerai al capitolo 14.

### 68.5 Gli effetti dell'autocorrelazione

Il manuale considera il caso in cui **i termini di errore seguono un processo AR(1)**: εₜ = ρεₜ₋₁ + uₜ, con |ρ| < 1 e uₜ white noise. In questo caso si dice che **fra i residui vi è autocorrelazione del primo ordine**, e **ρ** — chiamato spesso semplicemente **«rho»** — è il coefficiente di autocorrelazione.

Le conseguenze sono quelle generali già viste al paragrafo 65: **stimatori corretti ma non efficienti, errori standard sbagliati, inferenza inaffidabile**. Nel caso specifico dell'autocorrelazione positiva — di gran lunga la più frequente in economia — l'effetto tipico è che **gli errori standard vengono sottostimati**, e quindi si tende sistematicamente a **sopravvalutare la significatività** dei coefficienti e la bontà del modello.

### 68.6 I test di autocorrelazione

**La fase diagnostica.** Il manuale premette un discorso di metodo che vale la pena riportare perché è la miglior giustificazione dell'intero paragrafo:

> *I residui di un modello econometrico di serie storiche **devono essere «puliti»**, cioè non affetti da autocorrelazione: il passato non deve in alcun modo poter essere utilizzato per prevedere il presente. **Se i residui mostrano un qualche grado di autocorrelazione, il modello è «mispecificato»**, ossia non è stato in grado di catturare tutte le relazioni dinamiche contenute nella variabile dipendente. Ciò accade soprattutto quando **ci sono variabili esplicative omesse** oppure quando quelle disponibili hanno **limitata capacità di spiegazione**: qualsiasi dinamica non catturata dal modello **si scarica automaticamente all'interno dei residui, "sporcandoli"**.*

Questa è la chiave: **l'autocorrelazione dei residui non è un difetto statistico da correggere con un artificio, è un sintomo che il modello è incompleto**.

**a) Il test di Durbin-Watson (1950).** Il «classico» della diagnostica. Il manuale è onesto sulla sua natura: *non è un vero e proprio test, ma piuttosto una statistica i cui valori dovrebbero indicare se i residui mostrano una qualche autocorrelazione rilevante del primo ordine*. Il suo merito è **fornire in maniera rapida un'indicazione della presenza o assenza di autocorrelazione**.

**La relazione da sapere a memoria**, e la sua lettura:

> **d ≈ 2(1 − r)**, dove r è il coefficiente di autocorrelazione campionario di primo ordine dei residui.
>
> Per costruzione **d varia fra 0 e 4**, e:
> - **d < 2 → autocorrelazione POSITIVA** (perché r > 0);
> - **d ≈ 2 → NESSUNA autocorrelazione** (r ≈ 0);
> - **d > 2 → autocorrelazione NEGATIVA** (r < 0).

**Il problema delle zone d'ombra.** A differenza degli altri test, **non è possibile definire la legge di distribuzione di d sotto l'ipotesi nulla**, perché essa dipende dalle osservazioni della matrice delle esplicative. Durbin e Watson hanno però dimostrato che d può essere racchiuso fra **un limite inferiore d_L e un limite superiore d_U**, tabulati in funzione della numerosità n e del numero di variabili esplicative k. Poiché la maggior parte dei modelli su serie storiche presenta autocorrelazione positiva, le tavole si basano sull'ipotesi alternativa ρ > 0. La regola di decisione è:

| Valore di d | Decisione |
|---|---|
| **0 < d < d_L** | **si rifiuta H₀**: c'è autocorrelazione positiva |
| **d_L < d < d_U** | **zona d'incertezza**: il test è inconcludente |
| **d_U < d < 4 − d_U** | **non si rifiuta H₀**: nessuna autocorrelazione |
| **4 − d_U < d < 4 − d_L** | **zona d'incertezza** |
| **4 − d_L < d < 4** | **si rifiuta H₀**: c'è autocorrelazione negativa |

**I tre limiti del test DW**, che il manuale elenca esplicitamente e che conviene saper ripetere:

1. **non rileva autocorrelazioni di ordine superiore al primo**. È la ragione principale per cui non può essere considerato un test di autocorrelazione a tutti gli effetti;
2. **non può essere applicato quando fra i regressori compare la variabile dipendente ritardata** — cioè proprio nei modelli dinamici. Nel caso dei modelli ARMA **sottostima l'autocorrelazione** e si configura come uno stimatore distorto di ρ;
3. **soffre del problema delle «zone d'ombra»** (regioni di indeterminazione), in cui è impossibile stabilire se l'ipotesi nulla vada accettata o rifiutata, perché la regione di non rifiuto e quelle di rifiuto non sono separate da un valore critico ma **da un intervallo di valori critici**.

**b) Il test di Breusch-Godfrey (1978).** È **il test generale**, quello da preferire. I suoi vantaggi, esattamente complementari ai limiti del DW:

- **è in grado di testare diversi ordini di autocorrelazione seriale**, non solo il primo;
- **può essere adoperato anche quando i ritardi della variabile dipendente sono utilizzati come regressori**;
- funziona sia che gli errori seguano un processo AR(p) sia che seguano un MA(q).

**L'idea generale**, nelle parole del manuale: *la ricerca di una relazione significativa fra i residui e i residui di periodi immediatamente precedenti*. Operativamente: si stima il modello con OLS, si regrediscono i residui sulle variabili esplicative **e sui propri ritardi**, e si verifica la significatività congiunta dei coefficienti dei ritardi con una statistica che si distribuisce come una chi-quadrato.

### 68.7 I rimedi all'autocorrelazione

Il problema pratico è che il GLS richiederebbe di conoscere **ρ**, che non è noto. Occorre dunque stimarlo. Quattro metodi.

**a) Stima diretta di ρ dai residui.** Due modalità:
- **per regressione diretta dei residui sui residui ritardati di un periodo**;
- **dalla statistica di Durbin-Watson**, invertendo la relazione d ≈ 2(1−ρ), cioè **ρ̂ ≈ 1 − d/2**.

**b) Il processo iterativo delle «quasi differenze prime».** È il meccanismo comune a tutti i metodi iterativi, e conviene capirlo perché rende trasparente l'idea. Si prende il modello, lo si ritarda di un periodo, lo si moltiplica per ρ e lo si **sottrae** dal modello originario. Nel modello così trasformato **il termine di errore diventa uₜ, che è un white noise**: l'autocorrelazione è sparita. Le variabili trasformate (Yₜ − ρYₜ₋₁) e (Xₜ − ρXₜ₋₁) si chiamano **«quasi differenze prime»** — «quasi», perché se ρ fosse esattamente 1 sarebbero le differenze prime vere e proprie. Si attribuisce a ρ un valore iniziale, si stima con OLS, si ricalcola ρ dai nuovi residui, si sostituisce, si itera. **Il procedimento termina quando la differenza fra due successive stime di ρ è minore di un valore piccolissimo prefissato.**

**c) Il metodo di Cochrane-Orcutt.** È il procedimento iterativo classico, ideato dagli statistici **D. Cochrane e G.H. Orcutt**. A ogni iterazione si ottiene una stima di ρ migliore della precedente. I passaggi:

1. si stimano i parametri del modello lineare **come se fossero soddisfatte le assunzioni di Gauss-Markov** e si determinano i residui, da cui si ricava una **prima stima di ρ**;
2. si ritarda il modello di un periodo, lo si moltiplica per ρ̂ e lo si sottrae dall'originario, ottenendo il modello detto **«rho-differenced»**;
3. si stimano con OLS i parametri del modello trasformato (i cui errori non sono più serialmente correlati) e si ricomincia, calcolando una nuova stima di ρ;
4. **l'iterazione si interrompe quando fra due stime successive di ρ non esiste una differenza significativa**.

**d) Il metodo di Hildreth-Lu.** È un metodo **per approssimazioni successive**, concettualmente diverso: invece di iterare, **esplora sistematicamente**. Individuato il tipo di autocorrelazione (positiva o negativa), **si stima il modello per una griglia di valori di ρ** — per esempio tutti i valori da 0 a 1 con passo 0,1 — e **fra i modelli ottenuti si sceglie quello che presenta la somma dei quadrati dei residui minima**. Si può poi **affinare** ripetendo la procedura su un intervallo ristretto attorno al valore trovato, con passo più fine (per esempio da 0,45 a 0,55 con passo 0,01).

Il manuale esprime una preferenza esplicita: **questo metodo è il migliore secondo il criterio OLS, in quanto comporta la scelta del ρ che minimizza la somma dei quadrati dei residui** — cioè è l'unico che ottimizza davvero il criterio, invece di approssimarlo iterativamente.

**e) La massima verosimiglianza.** Consiste nello **stimare congiuntamente** il vettore dei coefficienti e il valore di ρ massimizzando la funzione di verosimiglianza. Esiste una procedura iterativa, dovuta a **Beach e MacKinnon**, ed **è stato dimostrato che le stime così ottenute sono migliori rispetto alla procedura di Cochrane-Orcutt**.

### 68.8 La previsione in presenza di autocorrelazione

Una nota finale con un'implicazione interessante. Quando gli errori seguono un AR(1), la previsione **non è semplicemente il valore sulla retta**: poiché **il valore atteso dell'errore futuro, condizionato all'errore corrente, non è nullo ma pari a ρ volte l'errore corrente**, alla previsione ordinaria si **aggiunge un termine correttivo** pari a ρ̂ moltiplicato per l'ultimo residuo osservato.

> **L'intuizione è molto economica.** *Se il modello ha sottostimato la variabile nell'ultimo periodo, e gli errori sono positivamente autocorrelati, allora è ragionevole aspettarsi che la sottostimerà anche nel prossimo: l'autocorrelazione, che nell'inferenza è un problema, **nella previsione è un'informazione da sfruttare**.* Se ρ fosse noto, lo stimatore così ottenuto sarebbe il **migliore stimatore lineare non distorto**.

---

# PARTE XIII — I MODELLI A EQUAZIONI SIMULTANEE

## 69. Perché servono e perché l'OLS non basta

Fino a qui tutti i modelli erano costituiti da **una sola equazione**: anche la regressione multipla, per quanti regressori abbia, ipotizza **un'unica relazione** fra le variabili. Ma l'economia è fatta di **sistemi**: il consumo dipende dal reddito, e il reddito dipende dal consumo. Un **modello a equazioni simultanee** è un sistema di equazioni legate fra loro da variabili che compaiono in due o più di esse.

**L'osservazione di partenza, che è anche la ragione dell'intero capitolo:**

> **Non è possibile applicare i minimi quadrati ordinari a ciascuna di queste equazioni come se fossero indipendenti l'una dall'altra.**

Il manuale lo dimostra sull'esempio più semplice possibile — una versione elementare della teoria del reddito nazionale:

> **Cₜ = α + βYₜ + εₜ**  (funzione del consumo)
> **Yₜ = Cₜ + Zₜ**  (identità del reddito nazionale)

dove C è la spesa aggregata per consumi, Z la spesa per investimenti (più la spesa pubblica), Y il reddito nazionale, ε la componente stocastica. **C e Y sono variabili endogene**, **Z è la variabile esogena**.

**Il problema salta agli occhi.** Nella prima equazione il regressore è Y. Ma dalla seconda equazione **Y contiene C**, e C contiene ε. Quindi **Y è correlato con ε**: siamo esattamente nel caso di **endogeneità del regressore** studiato al capitolo 11, nella sua forma da **simultaneità**. Il manuale trae la conseguenza in modo netto:

> **Le stime OLS della funzione di consumo risultano INCONSISTENTI**: i valori dei coefficienti stimati **non tenderanno verso i coefficienti teorici neanche quando si abbia a disposizione un numero di informazioni infinitamente grande.**

Non è un problema di campione piccolo. È un **errore sistematico che nessuna quantità di dati può correggere**. Questa è la frase da dire in commissione.

**Le ipotesi del modello** sono due: **normalità dei termini di errore** e **indipendenza fra la variabile esogena e il termine di errore** — cioè fra Z ed ε non deve esistere alcuna relazione. Ciò avviene se Z è una quantità deterministica oppure una variabile casuale distribuita indipendentemente da ε.

## 70. Forma strutturale e forma ridotta (di nuovo)

La distinzione vista al paragrafo 29 diventa qui operativa. Il **modello in forma ridotta** si ottiene **sostituendo l'identità nella funzione di comportamento** ed esprimendo ciascuna endogena **in funzione della sola variabile esogena e del termine d'errore**.

Due osservazioni sulla forma ridotta che vale la pena fare:

- **le equazioni della forma ridotta soddisfano le ipotesi che rendono gli OLS consistenti**, perché a destra compare solo la variabile esogena, che per ipotesi è incorrelata con l'errore. **La forma ridotta è stimabile, la forma strutturale no**;
- i coefficienti della forma ridotta sono **combinazioni** dei parametri strutturali. Nell'esempio, il coefficiente di Z nell'equazione del reddito è 1/(1−β): **è il moltiplicatore keynesiano**, che compare naturalmente come coefficiente della forma ridotta. È un bell'esempio di come la forma ridotta sia il «modello di strategia»: dice direttamente di quanto aumenta il reddito se aumenta la spesa pubblica.

## 71. I tre metodi di stima

### 71.1 Il metodo delle variabili strumentali

Si applica quanto visto al capitolo 11. Nell'esempio, **la variabile Z è uno strumento perfetto**: è **correlata con Y** (come si vede dalla forma ridotta) ma è **incorrelata con il termine d'errore** (per ipotesi del modello). Applicando il metodo IV, con Y come esplicativa, C come dipendente e Z come strumento, si ottengono stimatori **consistenti**.

Il manuale aggiunge in nota una precisazione importante: **questi stimatori sono corretti solo asintoticamente**, il che significa che **per produrre stime attendibili occorre lavorare con un campione sufficientemente ampio**.

### 71.2 Il metodo dei minimi quadrati indiretti (ILS)

*Indirect Least Squares*. Consiste in tre fasi:

1. **ridurre il modello strutturale in forma ridotta**;
2. **stimare con gli OLS i coefficienti della forma ridotta** (cosa che è lecita, come si è visto);
3. **calcolare i coefficienti della forma strutturale attraverso un'opportuna trasformazione dei coefficienti stimati della forma ridotta** — cioè risolvendo all'indietro le relazioni che legano i due insiemi di parametri.

Il nome dice tutto: **non si stimano direttamente i parametri che interessano, ma li si ricava indirettamente da parametri che si possono stimare**. Nell'esempio del reddito nazionale, lo stimatore ILS della propensione marginale al consumo risulta essere il **rapporto fra due coefficienti stimati nella forma ridotta**.

**Il limite del metodo**, che introduce il paragrafo successivo: la trasformazione all'indietro **funziona solo se il sistema di relazioni fra parametri ridotti e strutturali ha soluzione unica**. È esattamente il problema dell'identificazione.

### 71.3 Il metodo dei minimi quadrati a due stadi (2SLS)

*Two Stage Least Squares*. Il manuale è esplicito: **è il metodo più utilizzato nella pratica**. Si fonda sull'applicazione, in due stadi, degli OLS:

> **Primo stadio.** Si regredisce la **variabile endogena che compare come regressore** sulla (o sulle) **variabili strumentali**, ottenendo il **valore predetto** Ŷ. Si dimostra che questo valore predetto è **asintoticamente incorrelato con il termine d'errore**: è la parte «pulita» di Y, quella spiegata dallo strumento.
>
> **Secondo stadio.** Si stima l'equazione strutturale **sostituendo alla variabile endogena il suo valore predetto di primo stadio**. Poiché Ŷ è incorrelato con l'errore, **i parametri possono ora essere stimati con gli OLS** e lo stimatore è consistente.

L'intuizione, che conviene saper esprimere: **si "purifica" il regressore endogeno, trattenendone solo la parte di variazione attribuibile allo strumento — cioè quella che sicuramente non è contaminata dall'errore — e si usa solo quella per stimare l'effetto.**

Il manuale segnala un risultato di coerenza che vale la pena citare: **nel caso esattamente identificato, la stima 2SLS coincide con quella del metodo delle variabili strumentali e con quella dei minimi quadrati indiretti**. I tre metodi danno lo stesso risultato. La differenza emerge nel caso **sovraidentificato**, dove solo il 2SLS è applicabile perché sa combinare in modo efficiente più strumenti.

**La scelta degli strumenti.** Il manuale offre indicazioni operative molto concrete, e sono le stesse che ritroverai nella valutazione delle politiche: al di là dei requisiti formali, gli strumenti possono essere individuati mediante considerazioni legate al problema concreto — **modifiche esogene di una data politica** (per esempio la cancellazione di un programma di borse di studio), **differenze geografiche nell'applicazione di standard** (per esempio i risultati richiesti per il superamento di un dato esame in Stati diversi), o **la mera casualità**. Sono esattamente le «fonti di variazione quasi sperimentale» dell'econometria della valutazione.

## 72. Il problema dell'identificazione

### 72.1 Che cos'è

È **la questione centrale** dei modelli a equazioni simultanee, e una delle poche idee dell'econometria che sono davvero eleganti.

La conoscenza dei parametri strutturali dipende esclusivamente dalla conoscenza dei parametri della forma ridotta. Ma **non tutti i parametri strutturali possono essere recuperati**: si riscontra un **problema di identificazione**, ossia **l'impossibilità di risalire dai parametri stimati della forma ridotta alla struttura del modello iniziale**.

**Un modello è identificato se i suoi parametri sono univocamente determinati.** Se non lo è, avverte il manuale con una formulazione che rimane impressa:

> **Se il modello non è identificato, non è che non esistono soluzioni: ne esistono TROPPE.** Il modello è compatibile con differenti insiemi di parametri strutturali, e occorre procedere **introducendo vincoli** finché non risulti identificato.

L'esempio del manuale è didatticamente perfetto: se so soltanto che a + b = 10, le soluzioni sono infinite (4 e 6, 1 e 9, −9.990 e 10.000…). Se aggiungo il vincolo ab = 24, restano due coppie: (4,6) e (6,4). Se aggiungo a > b, resta **un'unica soluzione**: a = 6, b = 4. **Ora il modello è identificato.**

**Una condizione semplice e necessaria** per l'identificazione: **nel sistema vi devono essere più equazioni che parametri da stimare**.

### 72.2 I vincoli sui coefficienti strutturali

C'è un vincolo ogni volta che **un parametro è posto uguale a un valore determinato**. Due tipologie:

- **vincoli strutturali** (o **di esclusione**): ogni volta che **una variabile non compare in un'equazione**, essa è caratterizzata da un coefficiente nullo. Sono di gran lunga i più importanti, e nascono direttamente dalla teoria economica: dire che «il tasso d'interesse non entra nella funzione di consumo» *è* un vincolo di esclusione;
- **vincoli lineari**, che possono essere **omogenei** (si impone valore nullo a determinati coefficienti o a loro combinazioni lineari) oppure **non omogenei** (si attribuisce loro un valore diverso da zero).

### 72.3 Le tre condizioni — e la condizione d'ordine

**Le condizioni per l'identificazione si determinano equazione per equazione**, non per il sistema nel suo complesso. Tre casi:

| Caso | Definizione | Metodi di stima applicabili |
|---|---|---|
| **Sottoidentificata** | il numero di equazioni è **minore** di quello dei parametri da identificare: **il sistema è impossibile** | **nessuno**: occorre rimediare riducendo il numero di parametri o introducendo restrizioni |
| **Esattamente identificata** | il numero di equazioni è **pari** a quello dei parametri da identificare | **ILS** (minimi quadrati indiretti) **e 2SLS** |
| **Sovraidentificata** | il numero di equazioni è **maggiore** di quello dei parametri da identificare | **solo 2SLS** (minimi quadrati a due stadi) |

**La condizione d'ordine per l'identificabilità.** È la regola pratica, e va saputa in almeno una delle sue formulazioni. Il manuale la enuncia così:

> **Affinché un'equazione non sia sottoidentificata, il numero di variabili escluse dall'equazione deve essere almeno uguale al numero di equazioni del modello meno una.**

Formulazione equivalente, forse più maneggevole:

> **Per ogni equazione, il numero di variabili ESOGENE ESCLUSE deve essere maggiore o uguale al numero di variabili ENDOGENE INCLUSE meno una.**

Con la notazione del manuale — G = numero di equazioni (= variabili endogene del modello), K = variabili esogene del modello, g = endogene correnti che figurano nell'equazione, k = esogene che figurano nell'equazione — le tre situazioni si scrivono confrontando **(G − g) + (K − k)** con **G − 1**:

- **sottoidentificata** se le variabili escluse sono **meno** di G − 1;
- **esattamente identificata** se sono **esattamente** G − 1;
- **sovraidentificata** se sono **più** di G − 1.

**Due precisazioni conclusive** che il manuale fa e che è bene riportare:

1. la condizione d'ordine è **solo necessaria, non sufficiente**: occorre anche una **condizione di rango**, più complessa, che è quella necessaria e sufficiente;
2. nella realtà applicativa, **ogni equazione di un modello simultaneo presenta di regola un numero di endogene incluse molto inferiore al numero di esogene escluse**, e pertanto **il problema della sottoidentificazione è, in genere, più teorico che reale**. È una nota di realismo utile: nella pratica il problema opposto — la **sovraidentificazione**, cioè avere troppi strumenti, magari deboli — è molto più frequente.

> **Come si racconta l'identificazione all'orale, in trenta secondi.** *Nei sistemi simultanei l'OLS è inconsistente perché i regressori endogeni sono correlati con l'errore. Si passa allora alla forma ridotta, che è stimabile, e da lì si prova a tornare indietro ai parametri strutturali. Il problema dell'identificazione è se questo passaggio all'indietro dia una soluzione unica: se le informazioni sono troppo poche il sistema ha infinite soluzioni ed è sottoidentificato; se sono esattamente sufficienti è esattamente identificato e si usano i minimi quadrati indiretti o i due stadi; se sono più che sufficienti è sovraidentificato e si usano i doppi minimi quadrati, che è il metodo standard nella pratica. L'esempio classico è il mercato: osservando solo prezzi e quantità non si può distinguere la domanda dall'offerta, perché ogni punto osservato è un'intersezione; per identificare la domanda serve una variabile che sposti l'offerta e non la domanda, per esempio il clima.*

---

# PARTE XIV — L'ANALISI DELLE SERIE STORICHE

Il capitolo 14 riprende e sistematizza quanto già introdotto al capitolo 12, aggiungendo la parte più «applicata» dell'intero manuale — e quella con più probabilità di essere chiesta a un funzionario pubblico, perché riguarda **direttamente il lavoro dell'ISTAT**.

## 73. Definizioni e obiettivi

**Che cos'è.** Una **serie storica** è una successione di osservazioni ordinate logicamente secondo un indice temporale t, che ne definisce l'ordinamento. L'analisi delle serie storiche è **la metodologia statistica che si occupa di esaminare le serie, determinare il processo che sta alla loro base e stabilire previsioni**.

**Un requisito preliminare che vale la pena citare**, perché è quello che in pratica fa fallire più analisi: *fondamentale è la scelta dei periodi di osservazione: tutti devono essere contraddistinti da **omogeneità di caratteristiche**.* Se a metà serie cambia la definizione statistica del fenomeno, la serie non è più confrontabile con se stessa. Generalmente le serie storiche sono **mensili, trimestrali o annuali**.

**Le tipologie**, con gli esempi del manuale:

- **serie storiche economiche**, fornite dagli uffici di statistica: i **numeri indici dei prezzi** all'ingrosso e al consumo, i **dati della contabilità nazionale**;
- **serie storiche demografiche**: numero di nascite e tassi di natalità, di matrimoni e tassi di nuzialità, di morti e tassi di mortalità;
- **serie storiche fisiche**: precipitazioni nevose mensili, temperature settimanali;
- **serie storiche binarie**, in cui le osservazioni assumono due soli valori: variazioni positive/negative del mercato azionario, astensione/partecipazione alle elezioni politiche.

Le serie si dicono **univariate o multivariate** (se riguardano uno o più fenomeni) e **a parametro discreto o continuo**.

**I quattro obiettivi dell'analisi** — è un elenco perfetto per aprire una risposta:

1. **descrivere** sinteticamente l'andamento nel tempo di un fenomeno. Il grafico mette facilmente in evidenza sia le regolarità sia i **valori anomali**;
2. **spiegare** il fenomeno, individuandone il meccanismo generatore ed eventuali relazioni con altri eventi;
3. **filtrare** la serie, cioè **scomporla nelle sue componenti non osservabili**;
4. **prevedere** l'andamento futuro.

**I due approcci.** Distinzione fondamentale, da esporre sempre:

- l'**analisi classica (o tradizionale)** assume che il processo abbia **una parte deterministica**, che consente di scomporlo in componenti tendenziali, cicliche e stagionali, e che la differenza fra i dati teorici e i dati osservati sia attribuibile a **una componente casuale residuale**;
- l'**analisi moderna (o stocastica)** assume che il processo sia stato generato da **un procedimento stocastico descrivibile mediante un modello probabilistico di tipo parametrico**. È l'approccio di Box-Jenkins.

## 74. L'analisi classica: le quattro componenti

L'analisi classica — che, avverte il manuale, **si adatta bene alle serie solo se sono «regolari»** — concepisce la serie come **la somma di varie componenti**. La componente sistematica, di tipo deterministico, individua la legge di evoluzione temporale del fenomeno; accanto ad essa c'è una componente stocastica con funzione compensativa, che include l'effetto indistinto dei **fattori omessi o imprevedibili**.

Le componenti sono quattro, e vanno sapute con precisione:

| Componente | Simbolo | Che cos'è |
|---|---|---|
| **Trend** (componente di fondo) | **T** | La **tendenza di fondo** che contraddistingue l'andamento del fenomeno in un certo periodo. Il concomitante effetto di molteplici fattori fa sì che il fenomeno assuma un andamento regolare, spesso crescente o decrescente, **nel lungo periodo** |
| **Ciclo** (componente congiunturale) | **C** | Il **susseguirsi di fasi ascendenti e discendenti attorno al trend**, in un periodo **necessariamente maggiore di un anno**. Sono le successioni delle fasi del ciclo economico: **prosperità, crescita, depressione, ripresa** |
| **Stagionalità** | **S** | **Solo eventuale**, e **solo se le osservazioni sono relative a periodi inferiori all'anno**. Esprime l'alternanza legata al **ciclo solare annuale**: deriva dal movimento della Terra attorno al Sole, che genera la ripetizione annuale del clima, delle usanze, dei consumi, **degli adempimenti legali e amministrativi** |
| **Componente accidentale (o erratica, o residuale)** | **ε** | Ciò che resta: le oscillazioni **irregolari e non prevedibili**. Idealmente una sequenza i.i.d., cioè un **rumore bianco**, «completamente priva d'informazione», perché essendo i valori indipendenti non è possibile prevederne alcuno anche conoscendo tutti gli altri |

> **La frase da ricordare**, testuale nel manuale: *le componenti T, S e C **comprendono tutta l'informazione presente nei dati***. Tutto il resto è rumore. Ed è questo che giustifica lo sforzo di separarle.

**Ciclo e stagionalità non sono la stessa cosa** — è un errore frequente. La **stagionalità** ha periodo **fisso e infrannuale** (si ripete ogni anno nello stesso modo); il **ciclo** ha durata **variabile e pluriennale** (i cicli economici non hanno lunghezza fissa). Per questa ragione, e poiché sono difficili da separare, nella pratica **si stimano insieme** come **«trend-ciclo»** (TC), che rappresenta la tendenza di fondo della serie.

## 75. I tre modelli decompositivi

Individuate le componenti, occorre stabilire il modello che le mette in relazione. Tre tipologie:

**a) Modello additivo: x = T + C + S + ε.** Assume che **le componenti siano espresse tutte nella medesima unità di misura della serie e siano indipendenti fra loro**, per cui non possono influenzarsi vicendevolmente.

**b) Modello moltiplicativo: x = T · C · S · ε.** Assume che **solo il trend sia espresso nella stessa unità di misura**, mentre le altre componenti si configurano come **numeri puri, sotto forma di indici**, legate al trend **da una relazione di proporzionalità**. Esiste quindi **dipendenza fra le componenti** — ipotesi che, osserva il manuale, **si verifica di frequente nei casi reali**. Il modello si può **linearizzare** passando ai **logaritmi**, che lo riconducono esattamente al modello additivo.

**c) Modello misto**, configurabile in due modi a seconda che l'effetto stagionale si supponga additivo o moltiplicativo: **x = (T · C) + S + ε** oppure **x = (T · C · S) + ε**.

> **Come si sceglie — la regola operativa, che è visiva e facile da ricordare.**
> **Un modello additivo è appropriato quando l'ampiezza dell'oscillazione stagionale NON muta al variare del livello della serie.** Se invece **la fluttuazione stagionale aumenta (o diminuisce) proporzionalmente all'aumento (o diminuzione) del livello della serie, è più adeguato un modello moltiplicativo.**
> E la conclusione che conta: **molte serie economiche esibiscono fluttuazioni stagionali che crescono all'aumentare del livello della serie; per questo motivo, in ambito economico, il modello moltiplicativo trova più larga applicazione.**

Il manuale avverte comunque che **non c'è una maniera sistematica per scegliere**: alcune serie potrebbero richiedere contemporaneamente i due tipi di analisi. I due modelli, però, «sono soddisfacenti nella stragrande maggioranza dei casi».

## 76. La stima del trend-ciclo: le medie mobili

Il metodo classico per stimare il trend-ciclo è la **media mobile**.

**Che cos'è.** Consiste nel **sostituire ai dati osservati la media aritmetica di valori contigui**. Si chiama «mobile» perché **ogni successiva media viene calcolata eliminando il valore più vecchio e inserendone uno nuovo**. È un **metodo di adattamento locale**: crea una serie di valori **smussati** di lunghezza pari alla serie originaria, ciascuno in corrispondenza del punto di osservazione.

**L'intervallo di perequazione (lo *span*).** La prima decisione è la **lunghezza** della media, che determina **la maggiore o minore reattività della media alle variazioni proprie della serie**. Media corta = molto reattiva ma poco lisciante; media lunga = molto lisciante ma poco reattiva.

**La regola di scelta dell'ordine**, che è la cosa più operativa del paragrafo: **l'ordine della media mobile deve essere pari al numero di osservazioni contenute in un anno**, così da eliminare esattamente la stagionalità. Dunque:

| Cadenza delle osservazioni | Ordine della media mobile |
|---|---|
| **Mensili** | 12 |
| **Bimestrali** | 6 |
| **Trimestrali** | 4 |
| **Giornaliere** | 7 |
| **Orarie** | 24 |

**La centratura.** Occorre distinguere:

- se l'ordine è **dispari**, la media mobile **è centrata automaticamente** (c'è un termine centrale);
- se l'ordine è **pari** — che è il caso più frequente, dati mensili e trimestrali — **non c'è un termine centrale**, e si ricorre alla **media mobile centrata**: si applica la formula su **k+1 dati**, con **pesi 1, 2, 2, …, 2, 2, 1** e somma dei pesi pari a 2k. È cioè una **media ponderata in cui i termini centrali hanno peso 2 e quelli estremi peso 1**.

## 77. L'approccio moderno: dai processi stocastici agli ARIMA

### 77.1 La difficoltà di fondo

Il manuale spiega con chiarezza perché le serie storiche richiedano una teoria propria. Con dati indipendenti e identicamente distribuiti si stimano media e varianza con le formule consuete, sfruttando indipendenza e identica distribuzione. **Con le serie storiche la situazione è molto diversa:**

- **i dati si rilevano una sola volta** e **non si hanno repliche della stessa quantità**;
- **le osservazioni sono in generale correlate fra loro**;
- **solo quando il processo è strettamente stazionario** esse presentano la medesima distribuzione di probabilità.

La soluzione è la **stazionarietà debole**: se il processo è debolmente stazionario, tutte le variabili hanno **lo stesso valore atteso**, e la media campionaria — calcolata come **media storica dei dati** — resta uno stimatore **non distorto e consistente**. Analogamente si stimano **l'autocovarianza** e **l'autocorrelazione** facendo la **media temporale fra tutte le coppie di osservazioni che si trovano alla stessa distanza**. Questi stimatori sono **distorti ma asintoticamente corretti**.

Un risultato pratico utile: **se il processo è un white noise, i coefficienti di autocorrelazione campionari si distribuiscono approssimativamente come una normale con media nulla e varianza 1/n**. È da qui che si ricavano **le bande di confidenza del correlogramma** (approssimativamente ±2/√n): i valori che restano dentro la banda non sono significativamente diversi da zero.

### 77.2 Il teorema di Wold

Il principio che sta alla base della costruzione dei processi misti, dovuto allo statistico svedese **Herman Wold**:

> **Teorema di Wold.** *Ogni processo stocastico stazionario può essere scomposto in due processi stocastici, stazionari e fra loro mutuamente incorrelati: una **componente deterministica**, che può essere prevista senza errore a partire dai valori passati, e una **componente non deterministica**, che è un processo lineare costituito da una combinazione lineare di infiniti processi white noise.*

È un risultato di grande portata concettuale: **giustifica l'intera impostazione ARMA**, mostrando che ogni processo stazionario ammette una rappresentazione come media mobile infinita di rumori bianchi. Tutto il lavoro di modellazione consiste nell'approssimare quella rappresentazione infinita con **pochi parametri**.

### 77.3 I processi ARIMA

Qui sta il punto di svolta. Il manuale lo pone con realismo:

> **La condizione di stazionarietà di una serie storica è raramente riscontrabile empiricamente: in linea di massima, le serie storiche sono di tipo «evolutivo».**

Quasi nessuna serie economica reale è stazionaria: il PIL cresce, i prezzi crescono, la popolazione cambia. Come si applicano allora gli ARMA?

**La soluzione di Box e Jenkins**: invece di riferire il processo ARMA ai dati, **lo si riferisce alle differenze d-esime della serie**. Cioè: si trasforma la serie non stazionaria in una stazionaria **differenziandola** — prendendo le differenze prime (xₜ − xₜ₋₁), e se non basta le differenze seconde — e si applica l'ARMA al risultato.

Si ottiene così il **processo ARIMA(p, d, q)**, acronimo di ***AutoRegressive Integrated Moving Average***, dove:

- **p** = ordine della parte **autoregressiva**;
- **d** = ordine di **integrazione**, cioè il **numero di differenziazioni** necessarie a rendere stazionaria la serie;
- **q** = ordine della parte a **media mobile**.

I casi particolari:

- se **d = 0**, la serie non necessita di differenziazione e il processo appartiene alla classe **ARMA(p, q)**;
- se **p = 0** si ha un processo a **media mobile**; se **q = 0** un processo **autoregressivo**.

> **Come lo spieghi in due frasi.** *«Integrated» vuol dire che la serie osservata non è stazionaria, ma lo diventa dopo averla differenziata d volte; «integrata» perché la serie originaria si ottiene dalla serie differenziata sommando, cioè integrando. Il parametro d è, in pratica, il numero di volte che devo togliere il trend. Un ARIMA(0,1,0) è il **random walk**: la differenza prima è un rumore bianco, cioè la migliore previsione di domani è il valore di oggi — che è esattamente l'ipotesi di efficienza dei mercati finanziari.*

## 78. La procedura di Box e Jenkins — i cinque passi

È **il cuore operativo del capitolo** e la cosa più probabile che venga chiesta. La procedura si occupa di **costruire un modello ARIMA tale da approssimare il processo generatore di una serie storica osservata**, ed è **iterativa**.

**I cinque passi, da sapere in ordine:**

**a) Analisi preliminare.** Si stabilisce **se la serie è stazionaria** e, qualora non lo sia, la si trasforma perché lo diventi. **In questa fase si individua il valore dell'ordine d.** Gli strumenti sono due: **il grafico della serie storica** e **il grafico della sua funzione di autocorrelazione**. La non stazionarietà può essere dovuta a:
- la presenza del **trend** → rimedio: **differenze successive**;
- la presenza della **stagionalità** → rimedio: **differenze stagionali**;
- un **comportamento irregolare nell'ampiezza delle oscillazioni** (cioè eteroschedasticità) → rimedio: **trasformazione logaritmica** o **trasformazione di Box-Cox (1964)**, in cui il parametro λ viene stimato insieme agli altri parametri del modello.

**b) Identificazione del modello ARIMA.** Consiste **nell'individuazione degli ordini p e q**, in modo da trovare il modello che meglio si adatta alla serie resa stazionaria. **I principali strumenti sono le funzioni di autocorrelazione stimate**: si confrontano l'ACF e la PACF calcolate sulla serie con le rappresentazioni grafiche delle funzioni teoriche dei vari modelli, e si sceglie fra i due o tre modelli plausibili. **È qui che serve la tabella del paragrafo 68.4: AR taglia la PACF, MA taglia l'ACF.**

**c) Stima del modello.** I parametri sono stimati **ricorrendo al metodo della massima verosimiglianza**, che opera sulla serie resa stazionaria; **meno frequente è l'utilizzo dei minimi quadrati**. È un **metodo iterativo**, per cui è importante partire da buoni valori iniziali. Il manuale annota con onestà che «tale fase risulta parecchio macchinosa e pertanto ci si avvale di software specifici».

**d) Verifica del modello.** Si tratta di provare che il modello possa essere considerato **il generatore della serie analizzata**. Due criteri:

1. **le stime dei parametri devono essere significativamente diverse da zero**: nello specifico, **ogni parametro deve risultare, in valore assoluto, almeno due volte superiore alla propria deviazione standard** (è la solita regola del t ≈ 2). Inoltre **la correlazione fra le stime dei parametri deve risultare bassa**, per evitare problemi di instabilità;
2. **il modello deve risultare parsimonioso**, ossia **il numero di parametri adoperati deve essere il minore possibile**. Il **principio di parsimonia** è uno dei pilastri di Box-Jenkins e vale la pena nominarlo esplicitamente;
3. **i residui devono poter essere considerati la realizzazione di un processo di rumore bianco**, e quindi devono: avere **media e funzione di autocorrelazione non significativamente diverse da zero**; avere **varianza costante nel tempo**; essere **normalmente distribuiti**.

Per verificare congiuntamente che tutte le autocorrelazioni dei residui siano nulle si usa **il test di Ljung-Box**. Se i residui **non** sono un rumore bianco gaussiano, allora **il modello stimato è incapace di cogliere e spiegare la dipendenza temporale presente nei dati**, e occorre tornare indietro: riesaminare ACF e PACF, oppure trattare i residui stimati come **una nuova serie storica** su cui ripetere il ciclo identificazione-stima-verifica.

**e) Utilizzo del modello.** L'ultimo passo prevede la valutazione della **capacità di previsione**. Si riprende il criterio già visto al capitolo 6: un modello è attendibile non solo se riproduce adeguatamente i dati storici e genera parametri coerenti con le aspettative teoriche, **ma anche se si dimostra capace di dar luogo a buone previsioni**. La capacità previsionale si valuta con **tecniche di previsione ex post**: si stima il modello usando **solo le prime n−l osservazioni** e si confrontano le previsioni con i valori effettivi delle ultime l, che sono conosciuti.

**La misura adottata è il MAPE** (*Mean Absolute Percent Error*), cioè **la media dei valori assoluti degli errori relativi espressi in percentuale**. E il manuale dà anche **la soglia pratica**:

> **Il modello ha una buona capacità di previsione se il MAPE risulta inferiore al 12-15%.**

## 79. La procedura TRAMO-SEATS dell'ISTAT — il paragrafo più «da concorso» del capitolo

Questo è il paragrafo che conviene studiare con più attenzione, perché è **il punto in cui l'econometria diventa attività istituzionale della pubblica amministrazione italiana**. Una commissione RIPAM lo apprezza moltissimo.

### 79.1 Il problema: perché destagionalizzare

L'analisi della congiuntura economica si svolge sulla base di numerosi **indicatori prodotti dall'ISTAT**. L'avvio dell'**Unione Monetaria Europea**, allargando la platea dei fruitori delle informazioni statistiche prodotte in ciascun Paese, **ha richiesto che esse fossero sempre più agevolmente interpretabili e comparabili**. È cresciuta in particolare la richiesta di dati congiunturali presentati **in forma destagionalizzata**, cioè **depurati dalle fluttuazioni di carattere stagionale che, per molti fenomeni, impediscono una valutazione delle tendenze di breve periodo**.

Il punto è intuitivo e vale la pena dirlo: **se la produzione industriale cala sempre ad agosto, il fatto che sia calata ad agosto non è una notizia**. Per capire se l'economia sta rallentando davvero occorre prima togliere ciò che è sistematicamente attribuibile al calendario.

### 79.2 La storia istituzionale

I passaggi, da citare perché sono precisi e fanno impressione:

- **agli inizi del 1997 l'ISTAT nomina una commissione scientifica** con il compito di formulare proposte relative alle strategie di destagionalizzazione delle serie storiche prodotte dall'Istituto;
- nasce il **progetto di ricerca SARA** (*Seasonal Adjustment Research Appraisal*), al quale partecipano esperti **del mondo accademico, dell'ISTAT, della Banca d'Italia** e di altre istituzioni pubbliche e private. Il progetto esamina e confronta le principali procedure disponibili, soffermandosi soprattutto su **TRAMO-SEATS** e su **X-11-ARIMA**;
- **l'Istituto decide di adottare la procedura TRAMO-SEATS**, abbandonando **X-11-ARIMA**, che era impiegata a partire **dalla metà degli anni Ottanta**;
- **la scelta è pienamente coerente con quella effettuata dagli Istituti Nazionali di Statistica degli altri Stati membri dell'UE e da Eurostat** (l'Ufficio Statistico dell'Unione Europea);
- **a partire dal comunicato stampa sulla produzione industriale del febbraio 1999**, l'ISTAT implementa la nuova metodologia per molte serie storiche pubblicate correntemente.

### 79.3 Come funziona: le due parti

La procedura si compone di **due parti**, ciascuna con un acronimo che conviene saper sciogliere.

**TRAMO** — *Time series Regression with Arima noise, Missing observations and Outliers*. È la fase di **pretrattamento** («linearizzazione») della serie, in quattro momenti:

a) **individuazione e rimozione degli «effetti deterministici»**, ossia delle conseguenze dovute:
 - al **diverso numero di giorni lavorativi** nei diversi periodi,
 - alle **festività che non cadono sempre lo stesso giorno** (le cosiddette **festività mobili**, come la Pasqua),
 - ai **valori anomali (*outliers*)** causati da eventi straordinari.
 In questa fase si valuta anche il ricorso a opportune **trasformazioni logaritmiche** dei valori originari, per ottenere una **serie linearizzata**;
b) **identificazione del modello ARIMA** che meglio si adatta alla serie;
c) **stima del modello ARIMA con il metodo della massima verosimiglianza**;
d) **verifica della validità del modello** mediante test statistici.

Si riconosce, come si vede, **esattamente la procedura di Box-Jenkins** applicata in modo automatizzato e su scala industriale.

**SEATS** — *Signal Extraction in Arima Time Series*. Effettua **la vera e propria destagionalizzazione**, adoperando la struttura dei modelli individuati da TRAMO. In tre momenti:

a) **suddivisione della serie nelle sue componenti** — **ciclo-trend, stagionale e stocastica** — ipotizzando che **ciascuna segua un modello ARIMA conforme a quello identificato per la serie d'origine**;
b) **stima delle componenti e analisi degli errori**;
c) **assegnazione alle varie componenti degli effetti deterministici accertati da TRAMO**.

### 79.4 Perché è considerata migliore

> **TRAMO-SEATS è una procedura di tipo «model-based», fondata sulla costruzione di un particolare modello statistico per ogni serie storica analizzata.**

È questa la differenza fondamentale rispetto a X-11-ARIMA, che applicava invece **filtri predefiniti uguali per tutte le serie**. La procedura model-based:

- **incorpora i progressi compiuti nel campo dell'analisi moderna delle serie storiche**;
- **offre un ampio spettro di strumenti statistici per valutare la qualità della destagionalizzazione effettuata**;
- produce **serie destagionalizzate contraddistinte da minore irregolarità**, il che favorisce un esame più agevole delle tendenze in atto. Il manuale documenta il punto confrontando le variazioni congiunturali percentuali dell'indice della produzione industriale ottenute con i due metodi: **la sequenza ottenuta con TRAMO-SEATS presenta un'irregolarità meno pronunciata**, facilitando l'interpretazione della dinamica di breve termine.

### 79.5 L'esempio: l'indice della produzione industriale

Fra gli indicatori fondamentali per valutare l'andamento congiunturale, **l'indice della produzione industriale è uno di quelli che presenta le maggiori fluttuazioni stagionali**, e viene perciò destagionalizzato. La versione destagionalizzata è prodotta e pubblicata per le principali **destinazioni economiche della produzione**: **beni di consumo, beni di investimento, beni intermedi**.

**Il cambiamento nel trattamento preliminare**, che è un dettaglio tecnico ma molto istruttivo su come lavora un istituto di statistica. Prima, le serie grezze venivano **prima corrette** per il diverso numero di giorni lavorativi (con il «metodo proporzionale»), ottenendo dati di **produzione media giornaliera**, e **solo dopo** destagionalizzate. Con TRAMO-SEATS, invece, **la correzione per i giorni lavorativi e la destagionalizzazione si effettuano congiuntamente**, valutando simultaneamente:

- l'influenza che il numero di giorni lavorativi ha avuto sulla produzione;
- l'andamento tendenziale e stagionale;
- la distribuzione nei diversi mesi dei giorni lavorativi.

Il vantaggio è che si separano in maniera più corretta effetti che altrimenti si confondono fra loro.

> **Come chiudere una risposta su questo argomento, collegandola al tuo bando.** *La destagionalizzazione non è un esercizio tecnico: è **la condizione perché i dati congiunturali siano leggibili e comparabili fra Stati membri**. Serve alla Commissione europea per la sorveglianza macroeconomica, al Governo per il DPFP, alla Banca centrale per la politica monetaria. È un esempio perfetto di come una tecnica econometrica — l'ARIMA, nato come strumento di previsione — diventi **infrastruttura informativa pubblica**, con una governance istituzionale (la commissione ISTAT, il progetto SARA, l'allineamento a Eurostat) e un impatto diretto sulle decisioni di politica economica.*

---

# PARTE XV — L'ANALISI DEI DATI PANEL

Il capitolo 15 è breve ma denso, e ha un valore particolare per il tuo bando: **i dati panel sono lo strumento con cui la pubblica amministrazione valuta gli effetti delle proprie politiche**. Regioni osservate nel tempo, imprese beneficiarie di un incentivo osservate prima e dopo, comuni, scuole, ASL. Il capitolo 16 non sarà che l'applicazione di questa logica.

## 80. Che cosa sono e perché convengono

**La definizione.** I dati in formato panel **combinano le informazioni relative alle caratteristiche di N individui rilevate nel medesimo istante temporale con quelle rilevate per gli stessi individui in T diversi periodi di tempo**. Hanno dunque entrambe le caratteristiche:

- dei **dati cross section**, che consentono di osservare, per un dato istante, le caratteristiche di più individui;
- dei **dati time series**, che per un dato collettivo permettono di rilevare le diverse caratteristiche in istanti differenti.

**Esempi**: i dati sulle scelte di consumo di N famiglie per T anni — il manuale cita il **PSID, Panel Study of Income Dynamics**, l'indagine panel longitudinale sulle famiglie americane più longeva al mondo, condotta dal Survey Research Center dell'Università del Michigan, che raccoglie dati **dalle stesse famiglie e dai loro discendenti fin dal 1968** —; oppure i dati su N Paesi per T anni: PIL, occupazione, export.

**Perché sono migliori — i due esempi del manuale**, da riportare tali e quali perché sono efficacissimi.

> **Cross section vs. panel.** *In un dato anno osserviamo che il 30% di un campione di imprese realizza una o più innovazioni.* Due interpretazioni sono possibili: **ogni anno, in media, un 30% (diverso) di imprese innova**; oppure **sono sempre le stesse imprese, quel 30% del campione, a innovare ogni anno**. Sono due mondi economici completamente diversi — nel primo l'innovazione è un evento episodico e diffuso, nel secondo è una caratteristica persistente di poche imprese — e **con un solo dato trasversale non si può distinguerli**.

> **Serie storica vs. panel.** *Dall'analisi della serie storica degli investimenti in R&S delle imprese risulta che il tasso di crescita annuo è pari al 2%.* Questo potrebbe risultare da **una crescita del 2% in tutte le imprese**, oppure da **una crescita del 4% in alcune e nulla nelle altre**. Il dato aggregato non lo dice.

**La conclusione**, che è la risposta alla domanda «a che servono i dati panel?»: *i dati panel consentono di evidenziare **un effetto del tempo, ma anche una differenziazione fra individui**.* E il vantaggio statistico, che il manuale enuncia esplicitamente:

> **La convenienza dell'utilizzo dei modelli panel risiede soprattutto nel guadagno di efficienza della stima**, perché il maggior numero di osservazioni che si ha rispetto alla sola dimensione cross section o time series **genera uno stimatore con varianza più piccola**.

## 81. La struttura del modello

Nel modello panel ciascuna osservazione porta **due indici**: il primo identifica **il soggetto** (i = 1, …, N), il secondo **il tempo** (t = 1, …, T). Il modello si scrive:

> **Yᵢₜ = αᵢ + Xᵢₜβ + εᵢₜ**

dove la novità rispetto a tutto quanto visto finora è che **la costante porta l'indice i**: **c'è una costante diversa per ciascun individuo**.

**Che cosa rappresenta αᵢ** — questo è il punto concettuale centrale dell'intero capitolo:

> **Se αᵢ ≠ αⱼ, la costante misura l'EFFETTO INDIVIDUALE, cioè quell'insieme di caratteristiche specifiche proprie di ciascun individuo che però restano immutate nel tempo.**

Sono le caratteristiche **non osservate ma costanti**: la cultura organizzativa di un'impresa, la qualità dell'amministrazione di una Regione, l'abilità innata di una persona. Il manuale le chiama **l'eterogeneità presente fra gli individui, connotazione specifica dei dati panel**. Sono esattamente il tipo di variabili che, **omesse in una regressione cross section, generano distorsione da variabile omessa** — e il panel offre il modo di neutralizzarle senza doverle misurare.

Il modello ha in tutto **k + N parametri**: i k coefficienti di interesse più le N costanti individuali. E **secondo come si considera αᵢ** si aprono le due grandi famiglie:

- **modelli a effetti fissi** (*fixed effects*);
- **modelli a effetti casuali** (*random effects*).

## 82. Il modello a effetti fissi

### 82.1 Lo stimatore a variabili dummy (LSDV)

Il modo più diretto di stimare il modello è **trattare gli effetti individuali come parametri da stimare**, cioè **inserire nella matrice dei regressori tante variabili dummy quanti sono gli individui**. Il modello prende per questo il nome di **modello a variabili dummy** (in letteratura: *Least Squares Dummy Variable*, LSDV). È la diretta applicazione di quanto visto al paragrafo 54: **ogni dummy sposta l'intercetta del proprio individuo**.

Funziona, ma è **costoso**: con N grande occorrono moltissime dummy, con conseguente **perdita di gradi di libertà**.

### 82.2 Lo stimatore within

L'alternativa, algebricamente equivalente ma molto più economica, è **eliminare** gli effetti individuali invece di stimarli. Si applica il **modello lineare classico** dopo aver espresso **sia la variabile dipendente sia i regressori in deviazione dalle corrispondenti medie individuali calcolate rispetto al tempo** — operazione che in letteratura si chiama ***time-demeaning***.

L'intuizione è bellissima e va detta così: **poiché αᵢ è costante nel tempo per ciascun individuo, sottraendo a ogni osservazione la media temporale dell'individuo, l'effetto individuale si cancella da solo.** Sparisce senza bisogno di stimarlo, e senza bisogno di sapere che cos'era.

Lo stimatore che ne risulta si chiama **stimatore within** perché **tiene conto degli effetti individuali ma li elimina dal modello, utilizzando per ciascun individuo l'informazione derivante dalle sole variazioni temporali** — le **variazioni «nei gruppi»**.

Due proprietà da sapere:

- **lo stimatore within e lo stimatore a variabili dummy producono sempre gli stessi valori numerici**. Sono due strade per lo stesso risultato;
- una volta ottenuto lo stimatore within, **gli effetti individuali possono essere recuperati** per differenza, come scarto fra la media individuale della dipendente e la media individuale delle esplicative moltiplicata per i coefficienti stimati.

Lo stimatore within è **BLUE**, **consistente** al crescere di NT e **asintoticamente normale**.

### 82.3 Il limite dello stimatore within

Il manuale lo segnala con chiarezza, ed è **una domanda d'esame quasi garantita**:

> **Il limite più evidente di quest'approccio consiste nell'impossibilità di includere nel modello regressori che assumano un valore costante all'interno delle osservazioni relative al singolo individuo.**

Due spiegazioni, una statistica e una algebrica:

- **statisticamente**, una variabile esplicativa costante nel tempo risulterebbe **collineare con le dummy individuali**;
- **algebricamente**, calcolare lo scostamento di tali variabili dal loro valore medio individuale **produrrebbe colonne di zeri** nella matrice dei regressori, che non avrebbe più rango pieno. **Il metodo OLS non sarebbe applicabile.**

In pratica: **con gli effetti fissi non si può stimare l'effetto del sesso, della regione di nascita, del titolo di studio già conseguito** — di tutto ciò che nel periodo osservato non cambia. Sono proprio le variabili che vengono eliminate insieme all'effetto individuale.

### 82.4 Il test di significatività degli effetti individuali

Per verificare se l'eterogeneità fra individui esiste davvero, **il test t sull'azzeramento delle singole costanti non è di alcuna utilità pratica**. Si costruisce invece un **test F congiunto**, con ipotesi nulla:

> **H₀: α₁ = α₂ = … = α_N** (N−1 vincoli in tutto)

cioè **tutti gli individui hanno la stessa costante**. La statistica confronta i residui del **modello vincolato** (senza effetti individuali, cioè un OLS su tutti i dati impilati, il cosiddetto *pooled OLS*) con quelli del **modello libero**. Se si rifiuta H₀, **gli effetti individuali esistono** e il pooled OLS è inadeguato.

## 83. Il modello a effetti casuali

### 83.1 L'idea e le ipotesi aggiuntive

Il modello a effetti casuali fa una scelta diversa: **tratta gli effetti individuali come parte del termine di errore**, considerandoli **componenti stocastiche incorrelate con i regressori**. La costante si scompone in una parte comune a tutti e in una parte che varia da individuo a individuo, quest'ultima trattata come **variabile casuale**.

**Il vantaggio immediato**: poiché gli effetti individuali non vengono eliminati per differenziazione, **è possibile includere nella matrice X variabili che cambiano fra soggetto e soggetto pur rimanendo costanti nel tempo** — proprio quelle precluse agli effetti fissi.

**Il prezzo**: servono ipotesi aggiuntive sulla componente individuale, e in particolare — questa è **la condizione decisiva** —:

> **Affinché si ottengano stime consistenti, la condizione necessaria è l'INCORRELAZIONE fra gli effetti individuali e la matrice dei regressori.**

Il termine di errore del modello a effetti casuali risulta composto da **due componenti**: una che **varia fra gli individui ma resta costante nel tempo**, e una che **varia stocasticamente sia fra gli individui sia nel tempo**. Proprio per questa struttura, il modello a effetti casuali **deve essere stimato con il metodo GLS** — i minimi quadrati generalizzati del capitolo 12 — perché gli errori non sono sferici.

### 83.2 Lo stimatore between

Una terza trasformazione possibile: la **trasformazione between** consiste nell'esprimere le variabili **attraverso le medie temporali di ciascun individuo**. Cioè si riduce ogni individuo a **un solo dato**, la sua media, e si fa una regressione su questi N punti.

Lo stimatore between **sfrutta la variabilità delle osservazioni fra diversi individui** (variazioni «fra i gruppi»), mentre **lo stimatore within sfrutta la variazione che avviene all'interno delle osservazioni di ciascun individuo**. Entrambi, presi singolarmente, **determinano una perdita d'informazione**, perché ciascuno usa solo metà della variabilità disponibile.

### 83.3 La relazione fra i tre stimatori

Ed ecco il risultato che unifica tutto il capitolo, **da citare perché è elegante e memorabile**:

> **Lo stimatore GLS (a effetti casuali) è una MEDIA PONDERATA dello stimatore within e dello stimatore between.**

I due casi limite chiariscono tutto:

- se **la varianza degli effetti individuali è nulla**, il peso del between è massimo e **lo stimatore GLS coincide con lo stimatore OLS** applicato ai dati impilati: non c'è eterogeneità individuale da trattare;
- se **la varianza degli effetti individuali tende all'infinito** (o se T tende all'infinito), **lo stimatore GLS coincide con lo stimatore within**: tutto il peso va agli effetti fissi.

Altre proprietà: **per T assegnato, lo stimatore GLS è più efficiente dello stimatore within**. È il vantaggio degli effetti casuali — a patto che le loro ipotesi siano vere.

## 84. Effetti fissi o effetti casuali? Il *trade-off*

Il manuale pone la scelta in termini molto netti, ed è **la domanda d'orale su questo capitolo**:

> **La scelta fra effetti fissi ed effetti casuali si può attuare a seconda della preferenza fra EFFICIENZA e CONSISTENZA. Dal punto di vista statistico, esiste un trade-off fra *robustness* ed *efficiency*.**

Il confronto, punto per punto:

| | **Effetti fissi (within)** | **Effetti casuali (GLS)** |
|---|---|---|
| **Come tratta αᵢ** | parametro da stimare (o da eliminare con il time-demeaning) | **estrazione da una data distribuzione di probabilità**, parte del termine d'errore |
| **Ipotesi richieste** | **poche**: solo che gli effetti esistano e siano testabili | **molte**: gli effetti devono essere **incorrelati con ogni variabile esplicativa** |
| **Validità** | **sempre valido** — ha un set di ipotesi meno restrittivo | **valido solo se le ipotesi aggiuntive reggono** |
| **Efficienza** | minore (costa gradi di libertà) | **maggiore** |
| **Variabili costanti nel tempo** | **non stimabili** | **stimabili** |

La conclusione del manuale è netta e va riportata così:

> **Lo stimatore a effetti fissi è SEMPRE VALIDO**, perché ha un set di ipotesi meno restrittivo, **ma non riesce a stimare i parametri relativi alle variabili che non dipendono dal tempo**. Il modello a effetti casuali, oltre a stimare quei parametri, **permette una stima più efficiente**. Tuttavia **le ipotesi aggiuntive devono essere valide**: se c'è motivo di pensare che gli effetti individuali siano correlati con alcune delle variabili esplicative, **il modello random effects sarebbe incoerente (inconsistente), mentre quello fixed effects resterebbe comunque valido**.

Il manuale segnala anche una restrizione tecnica: se il numero di variabili indipendenti k è maggiore del numero di unità N, **lo stimatore between — e quindi anche quello a effetti casuali — sarebbe indefinito**.

## 85. Il test di Hausman (1978)

È **il test che risolve la scelta**, ed è quasi certamente il nome che una commissione si aspetta di sentire.

**Che cosa verifica.** L'ipotesi nulla è **l'incorrelazione fra gli effetti individuali e i regressori** — cioè esattamente **l'ipotesi che il modello a effetti casuali richiede per essere consistente**:

> **H₀: gli effetti individuali sono incorrelati con i regressori** → il modello a effetti casuali è valido
> **H₁: sono correlati** → il modello a effetti casuali è inconsistente

**La logica del test — ed è la logica di un'intera famiglia di test, vale la pena capirla.** Si confrontano i due stimatori sotto i due scenari:

| | **Se H₀ è vera** | **Se H₀ è falsa** |
|---|---|---|
| **Stimatore within (effetti fissi)** | consistente, ma **inefficiente** | **consistente** |
| **Stimatore GLS (effetti casuali)** | **consistente ed efficiente** | **inconsistente** |

**Il within è consistente in entrambi i casi; il GLS è consistente solo sotto H₀.** Quindi:

> **Il test si basa sulla DIFFERENZA fra i due stimatori.**
> - **Se la differenza è statisticamente irrilevante** → i due stimatori stanno convergendo allo stesso valore → H₀ è plausibile → **è preferibile l'utilizzo degli effetti casuali** (perché sono più efficienti);
> - **Se la differenza è significativamente diversa da zero** → il GLS sta andando da un'altra parte, cioè è inconsistente → **lo stimatore within è preferibile**.

**La statistica-test** è costruita sulla differenza fra i due vettori di stime, pesata per l'inverso della varianza della differenza. Il manuale dimostra un risultato tecnico elegante: **sotto H₀ la covarianza fra i due stimatori è nulla** — perché altrimenti il GLS non sarebbe efficiente — e quindi **la varianza della differenza si riduce alla semplice differenza delle varianze**. La statistica si distribuisce come una **chi-quadrato con k gradi di libertà** (k = numero di regressori).

**Una nota di correttezza storica**, che il manuale riporta in nota e che fa una bella impressione se la citi: *lo stesso test era stato proposto, prima di Hausman, da **Durbin** e da **Wu** indipendentemente, tanto che in alcuni volumi viene chiamato **test di Wu-Hausman** o **test di Durbin-Wu-Hausman***.

> **Come si racconta tutto il capitolo 15 in un minuto.** *I dati panel seguono gli stessi soggetti nel tempo, e questo permette di controllare tutte le caratteristiche individuali non osservate che restano costanti — la cosa che una cross section non può fare. Gli effetti fissi le eliminano sottraendo a ciascuna osservazione la media temporale del proprio soggetto: sono sempre validi, ma non possono stimare l'effetto di ciò che non varia nel tempo. Gli effetti casuali le trattano come parte dell'errore: sono più efficienti e permettono di includere variabili costanti, ma richiedono che gli effetti individuali siano incorrelati con i regressori — un'ipotesi forte. Il test di Hausman decide: confronta i due stimatori e, se differiscono significativamente, impone gli effetti fissi.*

> **E il collegamento con il capitolo successivo, da tenere pronto.** Il modello a effetti fissi su dati panel **è la base formale del metodo differenza-nelle-differenze**: si confrontano le variazioni nel tempo di un gruppo trattato con quelle di un gruppo di controllo, e gli effetti fissi individuali eliminano tutte le differenze preesistenti fra i due gruppi che restano costanti nel tempo. La valutazione controfattuale delle politiche pubbliche, per la parte quantitativa, **è econometria dei dati panel**.

---

# PARTE XVI — LA VALUTAZIONE DELLE POLITICHE E DEI PROGRAMMI PUBBLICI: L'ANALISI CONTROFATTUALE

**Questo è il capitolo che devi conoscere meglio di tutti.** È il punto in cui l'econometria smette di essere una materia tecnica e diventa **il mestiere di un funzionario pubblico che valuta l'efficacia della spesa**. È anche l'argomento che compare **in due materie del tuo bando contemporaneamente** — econometria e valutazione delle politiche pubbliche — ed è quindi statisticamente il più probabile di tutti. Vale la pena saperlo raccontare in modo fluido, con gli esempi.

## 86. Tipi di politiche e tipi di valutazione

**Politiche attive e passive.** Una prima distinzione:

- **politiche attive**: intervengono **direttamente sulle cause del problema**, utilizzando risorse pubbliche e interventi mirati di tipo regolativo, e/o indirettamente, **incentivando e finanziando comportamenti positivi** nei soggetti interessati;
- **politiche passive**: **non agiscono direttamente sui comportamenti** dei soggetti, ma mirano piuttosto a **modificarne le condizioni di vita o di esercizio**.

L'esempio classico è il mercato del lavoro: la formazione professionale e gli incentivi all'assunzione sono politiche attive; l'indennità di disoccupazione è una politica passiva.

**I tre tipi di valutazione** — elenco da sapere a memoria, perché è la premessa di qualunque risposta su questo tema:

| Tipo di valutazione | A quali domande risponde |
|---|---|
| **Valutazione dello stato di avanzamento** (finanziaria/procedurale) | «I soldi assegnati sono stati spesi tutti?», «Qual è il livello di avanzamento dell'intervento?» |
| **Valutazione dei meccanismi** (di implementazione) | «La politica è stata attuata come progettata?», «Ha funzionato tutto?» |
| **Valutazione d'impatto** | Attuata **attraverso strumenti di analisi statistica**, consente di comprendere **se la politica ha contribuito al conseguimento dell'effetto desiderato** |

**Le tre domande della valutazione d'impatto**, testuali nel manuale:

1. **«È stato raggiunto lo scopo?»**
2. **«In quale misura la politica ha contribuito all'ottenimento del risultato?»**
3. **«I cambiamenti osservati sarebbero stati maggiori o minori senza la politica in questione?»**

**Il concetto chiave: l'impatto netto.**

> **La valutazione d'impatto fa riferimento all'IMPATTO NETTO, cioè depurato degli effetti dovuti ad altri fattori esterni alla politica** — evoluzioni del contesto socio-economico, dinamiche sociali ed economiche. Consente cioè di **isolare i mutamenti determinati dalla politica rispetto ai cambiamenti complessivamente osservati**.

**I due obiettivi ulteriori**, che vale la pena citare perché mostrano il valore istituzionale della materia:

- **indicare se gli effetti ottenuti sono quelli desiderati**, questione non scontata perché **una politica, se non progettata in modo adeguato, potrebbe anche produrre effetti di tipo opposto a quelli per cui è stata concepita**;
- **fornire strumenti utili, in termini di conoscenza e di controllo, a coloro che propongono e approvano le politiche**.

## 87. Il metodo controfattuale: fattuale e controfattuale

Ecco il cuore concettuale. Il manuale lo introduce con precisione, e queste due definizioni vanno sapute **alla lettera**:

> **FATTUALE** è **quanto si osserva in presenza di trattamento**.
> **CONTROFATTUALE** è **quanto si sarebbe osservato per gli stessi soggetti se la politica non fosse stata attuata**.

**Perché serve.** Una politica produce effetti che **vanno a sommarsi a quelli che si sarebbero prodotti anche se la politica non fosse intervenuta**. I risultati devono quindi essere **«depurati» da quella quota parte che si sarebbe riscontrata comunque**.

**L'esempio del manuale**, semplice e perfetto da riportare: *per valutare se una politica di incentivo all'acquisizione di certificazioni da parte delle imprese ha effetto, non è sufficiente calcolare la differenza fra il numero di certificazioni prima e dopo la politica, ma è necessario capire **se e quante imprese si sarebbero comunque certificate anche in mancanza degli incentivi**.*

**Il paradosso fondamentale.** Ed è la frase che fa la differenza in commissione:

> **La condizione controfattuale NON È OSSERVABILE**, poiché si fonda sul «cosa sarebbe accaduto se…». Su questo presupposto si comprende che, **in linea di principio, la valutazione di una politica non sarà mai possibile**, in quanto definita come **differenza fra ciò che è successo e ciò che sarebbe accaduto**.
>
> **Il metodo controfattuale è allora un insieme di tecniche statistiche che, sotto determinate ipotesi, permettono di STIMARE il valore controfattuale.** A seconda delle caratteristiche della politica si definisce l'opportuna strategia valutativa.

Questa è la formulazione esatta del cosiddetto **«problema fondamentale dell'inferenza causale»**: non è un problema di dati mancanti che si possa risolvere raccogliendo più dati. **Il dato controfattuale non esiste in nessun archivio, perché riguarda un mondo che non si è verificato.** Tutta la disciplina consiste nel costruirne una stima credibile.

## 88. Il modello causale di Rubin (1974)

Il sistema di identificazione si basa **sull'approccio dei risultati potenziali**, noto come **modello di Rubin** o **modello degli esiti (*outcomes*) potenziali**.

**Le due variabili:**

- la **variabile risultato Y** (per convenzione **continua**: si pensi al reddito);
- la **variabile trattamento D** (per convenzione **binaria**), dove **D = 1** identifica i soggetti **esposti al trattamento** e **D = 0** i soggetti **non trattati**.

**I due risultati potenziali.** Per ogni singola unità si considerano **due risultati potenziali**:

- **Yᴺᵀ** = il valore assunto dalla variabile risultato per l'unità i **in assenza di trattamento**;
- **Yᵀ** = il valore assunto dalla variabile risultato **per la stessa unità i** **in presenza di trattamento**.

> **Per definizione, su ciascun soggetto UNO DEI DUE VALORI NON È MAI OSSERVABILE**, in quanto si tratta di **due risultati potenziali incompatibili**, che non possono mai realizzarsi contemporaneamente sul medesimo soggetto.

La tabella che ne deriva, e che conviene disegnare mentalmente:

| | **D = 1 (trattati)** | **D = 0 (non trattati)** |
|---|---|---|
| **Yᵀ** (esito con trattamento) | **fattuale** — osservabile | **controfattuale** — non osservabile |
| **Yᴺᵀ** (esito senza trattamento) | **controfattuale** — non osservabile | **fattuale** — osservabile |

**L'effetto del trattamento** è definito come **differenza fra i risultati potenziali**: δ = Yᵀ − Yᴺᵀ. Il risultato osservato è la somma del risultato «non trattato» più l'eventuale effetto del trattamento.

**I tre effetti sulla popolazione** — un altro elenco da memorizzare:

| Sigla | Nome | Che cosa misura |
|---|---|---|
| **ATE** | *Average Treatment Effect* | l'**effetto medio nell'intera popolazione**: quale sarebbe l'effetto se si trattassero tutti |
| — | effetto medio fra i **non trattati** (ATU/ATNT) | quale sarebbe stato l'effetto **sui non trattati**, se fossero stati trattati |
| **ATT** | *Average Treatment effect on Treated* | l'**effetto medio fra i soggetti effettivamente trattati** |

> **Tutte queste espressioni contengono componenti controfattuali non osservabili, ma in genere l'effetto che si desidera calcolare con le strategie di valutazione è l'ATT.** È la grandezza che risponde alla domanda operativa del decisore pubblico: *«per chi ha effettivamente ricevuto il contributo, quanto è servito?»*.

Nel caso dell'ATT, la componente **osservabile** è l'esito medio dei trattati; quella **non osservabile** è **l'esito che i trattati avrebbero avuto senza trattamento**. **Tutto il problema è stimare quella singola quantità.**

## 89. I due metodi «ingenui» e le loro distorsioni

Prima delle strategie vere, il manuale esamina **i due metodi più intuitivi**, per far capire i problemi di base. Vale la pena impararli, perché **le due distorsioni che li affliggono danno il nome ai due problemi centrali della materia**.

### 89.1 Il confronto pre-post

Il metodo più intuitivo: **confrontare la variabile risultato prima e dopo il trattamento, per i soli trattati**. Presupposto fondamentale: **avere osservazioni anche pre-trattamento**.

Scomponendo l'ATT si vede che la differenza osservata pre-post è pari all'effetto vero **più** un termine di errore che il manuale chiama:

> **DISTORSIONE DA DINAMICA SPONTANEA.**

**Che cos'è.** *Rappresenta la naturale evoluzione degli eventi.* L'esempio del manuale: *se consideriamo una politica a favore dei disoccupati che favorisca il rientro nel mondo del lavoro, **anche in assenza di incentivi si osserverà comunque una variazione nel tempo del numero di persone occupate***.

**La conclusione**: il confronto pre-post identifica correttamente l'ATT **solo se la dinamica spontanea è nulla** — cioè solo se, senza politica, nulla sarebbe cambiato. **Un'assunzione, dice il manuale, che in genere non è sostenibile.**

### 89.2 Il confronto trattati / non trattati

La seconda strategia: **confrontare la variabile risultato fra trattati e non trattati**. Presupposto fondamentale: **che la politica non sia universale**, cioè che esistano soggetti non trattati per i quali siano stati raccolti dati.

Anche qui la scomposizione rivela un termine di errore:

> **DISTORSIONE DA SELEZIONE (*selection bias*)**, detta anche **da autoselezione**.

**Che cos'è.** *Rappresenta una **differenza iniziale** fra i soggetti che hanno beneficiato della politica e quelli che non ne hanno beneficiato.* Il manuale precisa che **si riscontra per tutte le politiche non universali**, indipendentemente dal fatto che l'assegnazione sia su base volontaria o determinata secondo specifici criteri.

**I tre esempi del manuale**, tutti ottimi da citare:

- **una politica assegnata a chi raggiunge una soglia minima a un test** può selezionare soggetti che **sono di fatto «più dotati»** e che, in ogni caso, avrebbero avuto risultati migliori degli esclusi;
- **una politica in cui i beneficiari sono scelti su base volontaria** può selezionare soggetti che **sono di fatto «più motivati»**;
- **una politica del lavoro che utilizza trattamenti diversi in base all'età** può essere influenzata **dalla diversa probabilità di reimpiego** che soggetti di età differenti hanno a parità di altre caratteristiche.

**La conclusione**: il confronto trattati/non trattati identifica l'ATT **solo se il selection bias è nullo**, cioè solo se i due gruppi erano identici in partenza.

> **La sintesi da tenere a mente, perché organizza tutto il capitolo.**
> **Pre-post** soffre della **dinamica spontanea** (il mondo cambia comunque). **Trattati/non trattati** soffre del **selection bias** (i due gruppi erano già diversi). **Il DiD combina i due metodi per eliminare entrambe le distorsioni**, e gli altri metodi (RCT, matching, RDD) attaccano il selection bias in modi diversi.

## 90. Le ipotesi fondamentali del metodo controfattuale

Quattro condizioni, tutte da conoscere **con il nome inglese**, perché è così che le chiede una commissione.

**a) SUTVA — *Stable Unit Treatment Value Assumption*.** Ha **due conseguenze**:

1. **esiste un gruppo dei trattati e un gruppo di controllo, e i soggetti non possono cambiare l'assegnazione** all'uno o all'altro;
2. **non c'è interferenza fra le unità**: il singolo soggetto **non è influenzato dall'effetto che la stessa politica ha avuto sugli altri**.

Il secondo punto è il più interessante e vale la pena commentarlo: se un incentivo all'assunzione fa sì che un'impresa beneficiaria assuma il lavoratore che sarebbe stato assunto da un'impresa non beneficiaria, **la SUTVA cade** — l'effetto misurato non è un effetto netto ma una redistribuzione fra imprese. Sono i cosiddetti **effetti di spiazzamento (*displacement*)**, molto frequenti nelle politiche del lavoro.

**b) *Common Support Assumption*.** Implica **l'esistenza di almeno un soggetto che non riceve il trattamento**. Per l'ATT è sufficiente la **forma debole** dell'assunto: **a parità di caratteristiche, nei trattati, ci deve essere almeno un soggetto non trattato**. Detto altrimenti: **per ogni tipo di trattato deve esistere un possibile gemello non trattato**. Se una politica ha coinvolto *tutte* le imprese di un certo settore, per quel settore non c'è common support e **l'effetto non è stimabile**.

**c) CIA — *Conditional Independence Assumption*, detta anche *unconfoundedness*.** È l'ipotesi che rende possibili tutte le tecniche di matching:

> **Controllare le variabili rispetto alle quali i due gruppi presentano una composizione differente rende gli *outcomes* potenziali INDIPENDENTI DAL PROCESSO DI SELEZIONE.**

In parole semplici: **a parità delle caratteristiche osservate X, essere trattati o no è come se fosse casuale**. Tutto ciò che distingue i due gruppi è misurato e può essere controllato.

**d) *Strong ignorability*.** Quando sono rispettati **contemporaneamente** gli assunti di **Common Support** e di **CIA**, si verificano le condizioni per applicare la *strong ignorability*: **è possibile ignorare il meccanismo di assegnazione del trattamento**, cioè trattarlo come se fosse casuale.

**Validità interna e validità esterna.** La validità di queste ipotesi porta a:

- **individuare correttamente l'effetto sulla popolazione considerata** → **validità interna**;
- **ottenere risultati generalizzabili all'intera popolazione** → **validità esterna**.

È una distinzione che vale la pena avere pronta, perché torna alla fine del capitolo a proposito dell'RDD.

> **E il problema pratico**, come lo formula il manuale: *uno dei problemi più comuni che si riscontrano nella valutazione di una politica è **la presenza di selection bias**: in questi casi viene a mancare la condizione di strong ignorability.* Tutte le strategie che seguono sono modi diversi di aggirare quel problema.

## 91. Le strategie di valutazione

### 91.1 Statistical Matching (abbinamento statistico) e propensity score

**L'idea.** La tecnica sfrutta le proprietà della CIA per **ricostruire, a posteriori, un gruppo di controllo che abbia la stessa distribuzione delle caratteristiche X** che influenzano sia il processo di selezione sia la variabile risultato, in modo tale che, **a parità di X, l'assegnazione del trattamento sia casuale**. Si ricostruisce così un gruppo di controllo confrontabile con il gruppo trattamento ed è possibile **considerare nullo il selection bias**.

**Il problema della dimensionalità.** Ed è qui che entra in scena l'idea più famosa della materia:

> Il processo di abbinamento **risulta spesso difficoltoso nel caso di elevata dimensione del vettore X**: il numero dei gruppi omogenei cresce **esponenzialmente**. Due individui possono essere identici in una dimensione e differire lungo un'altra, e quindi **un abbinamento esatto che consenta di trovare un «non trattato» identico a un «trattato» è praticamente impossibile**.

**La soluzione: Rosenbaum e Rubin (1983)** suggeriscono l'utilizzo di un ***balancing score***, ossia di una funzione dell'insieme X che riassuma tutte le caratteristiche in **un unico numero**. Fra i possibili balancing score, i due studiosi propongono il **PROPENSITY SCORE**:

> **Il propensity score e(X) è LA PROBABILITÀ DI ESSERE TRATTATO DATO IL VETTORE X delle caratteristiche osservate.**

Il risultato teorico che lo giustifica: **se la CIA è rispettata per il vettore X, allora lo è anche per qualsiasi funzione di X** — e quindi anche per il propensity score. **Si passa così da un problema multidimensionale a un problema unidimensionale.** È un'idea semplice e potentissima, e va detta con questa enfasi.

**L'implementazione in due stadi**, da esporre così:

> **Primo stadio**: si **stima per ogni soggetto il valore del propensity score**, utilizzando **un modello standard di probabilità, come un *probit* o un *logit***.
> **Secondo stadio**: si effettua il vero e proprio **abbinamento statistico**, associando **a ogni soggetto trattato uno o più controlli sulla base del valore assunto dal propensity score**, e si calcola l'**ATT**.

**Gli algoritmi di matching** — il manuale ne elenca quattro, e **possono condurre a risultati anche molto diversi**:

1. **Nearest Neighbour Matching** — *abbinamento al vicino più prossimo*: **accoppia a ciascun trattato il controllo che ha il propensity score più vicino**. Può accadere che esistano **molteplici nearest neighbour per lo stesso trattato** (o lo stesso controllo per più trattati); il fenomeno **è tanto più raro quanto più continua è la distribuzione del propensity score**, cioè quanto più numerose sono le variabili continue usate per stimarlo. Può essere **«con replacement»** — un non trattato può essere usato **più di una volta** come match di più trattati — **o «senza replacement»**;
2. **Radius Matching** — *abbinamento per raggio*: **evoluzione del nearest neighbour**, in cui ogni trattato è accoppiato **con tutti i controlli che cadono in un intorno predefinito** del suo propensity score. **Quanto più piccolo è l'intorno, tanto migliore sarà la qualità dell'accoppiamento** (ma tanti meno abbinamenti si troveranno);
3. **Stratification Matching** — si suddivide il campo di variazione del propensity score in **strati** e si confrontano trattati e controlli all'interno di ciascuno strato;
4. **Kernel Matching** — a ciascun trattato si associa **una media ponderata di tutti i controlli**, con pesi decrescenti al crescere della distanza nel propensity score.

**Il vantaggio**: consente la costruzione di **un gruppo di controllo bilanciato rispetto alle caratteristiche X**.

**Le due assunzioni necessarie**: che il vettore X **influenzi l'assegnazione al trattamento**; e che **la distribuzione della variabile risultato, condizionata a X, sia indipendente dal trattamento** (la CIA).

**IL LIMITE FONDAMENTALE** — questo è il punto da non mancare mai:

> **Lo Statistical Matching garantisce un common support solo per le VARIABILI OSSERVABILI sulle quali viene stimato il propensity score. In presenza di variabili NON OSSERVABILI che influenzano la selezione o il risultato, tale strategia non è da sola sufficiente a garantire la validità delle conclusioni.**

E il manuale specifica **quali** sono tipicamente queste variabili non osservabili, nelle politiche non obbligatorie: **l'abilità, la propensione, le preferenze, la motivazione**. Sono esattamente le determinanti dell'**autoselezione**, e **non possono essere controllate attraverso il matching**, perché con esse **salta l'assunto CIA**. Per questo il matching **può essere utilizzato in abbinamento ad altre tecniche valutative**, per alleggerire le assunzioni necessarie.

**L'esempio del manuale — la riforma del *workfare* in Argentina.** *Gli economisti **Jalan e Ravallion (2003)** hanno usato questo metodo per testare l'impatto sul reddito di una riforma del sistema di welfare in Argentina. In mancanza di dati di **baseline**, ed essendo la valutazione stata progettata **dopo** l'attuazione del programma, i ricercatori hanno optato per l'abbinamento statistico: mediante un sondaggio hanno raccolto informazioni su **circa 200 caratteristiche individuali**, così da abbinare a ogni partecipante il non partecipante più simile; hanno poi calcolato la differenza media di reddito fra i gruppi abbinati e verificato la **robustezza** dei risultati applicando le diverse tecniche disponibili. **Tuttavia, i ricercatori non hanno potuto escludere le distorsioni provocate dalle variabili non osservabili.***

> **Nota di lessico utile.** La ***baseline*** è, come spiega il manuale in nota, **il punto di riferimento rispetto al quale calcolare gli scostamenti delle principali variabili implicate nella gestione di un intervento**. In assenza di una baseline **è impossibile svolgere l'attività di monitoraggio e controllo, nonché una validazione dei risultati rispetto agli obiettivi pianificati**. È una parola che in commissione conviene usare: *«la valutazione va progettata prima dell'intervento, perché senza baseline si è costretti a ripiegare su tecniche più deboli»*.

### 91.2 Difference-in-Differences (differenza nelle differenze)

**L'idea.** La tecnica **permette di ovviare al problema dell'autoselezione combinando le metodologie del confronto pre-post e del confronto trattati/non trattati in un'unica strategia**.

I due metodi ingenui richiedevano, rispettivamente, **assenza di dinamica spontanea** e **assenza di selection bias**. Il DiD sostituisce entrambe con **una sola ipotesi, più debole**:

> **L'ASSUNTO DI PARALLELISMO DEL TREND: la dinamica spontanea è uguale per trattati e non trattati.**

Non si assume che i due gruppi siano uguali — possono essere diversissimi — **si assume solo che, in assenza della politica, sarebbero cambiati nello stesso modo**.

**Il requisito dei dati**: occorre essere **in possesso dei dati pre- e post-trattamento sia dei trattati sia dei non trattati**. Quattro medie in tutto.

**Come funziona**, e qui vale la pena scriverlo in modo trasparente:

> **DiD = (esito dei trattati DOPO − esito dei trattati PRIMA) − (esito dei non trattati DOPO − esito dei non trattati PRIMA)**
>
> La prima differenza contiene **l'effetto della politica + la dinamica spontanea**. La seconda differenza contiene **solo la dinamica spontanea**. Sottraendo, **resta l'effetto della politica**.
>
> Equivalentemente, riordinando: la differenza fra i due gruppi **dopo** meno la differenza fra i due gruppi **prima** — cioè **l'effetto più il selection bias, meno il selection bias**.

**Tutte le componenti sono osservabili.** È questo che rende il metodo così usato.

**Graficamente**: due rette, una per il gruppo trattato e una per il controllo. Prima del trattamento sono **parallele** (magari a livelli diversi). Dopo il trattamento, **la retta dei trattati devia dalla traiettoria parallela**: quella deviazione è l'effetto. La **retta tratteggiata** che prolunga il parallelismo è **il controfattuale stimato**.

**Il rischio da segnalare**, che il manuale sottolinea: **eventi locali indipendenti dal programma potrebbero influenzare le tendenze mentre l'intervento viene attuato** — per esempio **l'applicazione di un altro programma nella regione d'intervento o di controllo**, oppure **uno shock esogeno relativo a uno solo dei due gruppi** — e questo distorcerebbe la misura dell'impatto stimato.

> **Il collegamento con il capitolo 9, da fare in commissione.** *Il DiD si stima in pratica come una **regressione multipla con due variabili dummy e il loro termine di interazione**: una dummy che identifica il gruppo trattato, una dummy che identifica il periodo post-intervento, e il loro prodotto. **Il coefficiente del termine di interazione è esattamente la stima DiD dell'effetto della politica**, e il suo errore standard fornisce immediatamente il test di significatività. Su dati panel, il modello a effetti fissi generalizza la stessa idea a più periodi e più gruppi.*

### 91.3 Randomized Controlled Trial (RCT)

**Il principio.** *La credibilità di una valutazione d'impatto dipende dal grado di somiglianza fra gruppo di controllo e gruppo d'intervento, in termini di caratteristiche **sia osservabili sia non osservabili**.* E qui sta la superiorità del metodo:

> **L'assegnazione casuale al gruppo d'intervento e al gruppo di controllo costituisce, probabilmente, il metodo più affidabile: se il campione è sufficientemente grande, si ha la garanzia che i due gruppi abbiano le stesse peculiarità** — **sia sulle caratteristiche osservabili sia su quelle non osservabili**. In tal modo **l'unica differenza fra i due gruppi è la partecipazione o meno all'intervento**, ed è più facile stabilire relazioni causali.

**Questo è il punto decisivo**: la randomizzazione bilancia anche **ciò che non si sa di dover misurare**. È l'unico metodo che lo fa, ed è per questo che **gli studi randomizzati controllati sono considerati un metodo rigoroso per la costruzione di un controfattuale valido**.

**I due esempi speculari del manuale**, che mostrano che il selection bias può andare **in entrambe le direzioni** — vale molto la pena saperli raccontare:

- *è molto probabile che saranno proprio le persone **più motivate** quelle che maggiormente tenderanno a iscriversi a un programma di consulenza per la ricerca di un'occupazione; la motivazione a sua volta è correlata con la probabilità di trovare lavoro. Confrontando semplicemente partecipanti e non partecipanti **si otterrà una misura SOVRASTIMATA** dell'impatto*;
- *ma è possibile anche il contrario: se un programma di consulenza fosse disponibile **solo per i disoccupati non qualificati di lungo periodo**, il confronto fornirebbe una misura **SOTTOSTIMATA**, perché i partecipanti se la sarebbero cavata peggio dei non partecipanti anche in assenza del programma.*

**La prova di bilanciamento (*balance test*).** Quando si randomizza c'è **alta probabilità che i due gruppi siano identici**, e l'ipotesi **può essere testata empiricamente**: si misura **la distribuzione delle caratteristiche nei gruppi** per verificare che non ci siano differenze significative nelle variabili chiave. Il manuale avverte che una mancanza di bilanciamento può verificarsi anche con un'assegnazione casuale corretta, ma **il rischio si minimizza al crescere delle dimensioni del campione**. E pone due ***caveat***:

- **non c'è mai garanzia che il test includa tutte le variabili rilevanti**;
- **la composizione dei due gruppi può quindi essere distorta per effetto di una variabile non osservabile** — anche se è comunque «rassicurante» che non vi siano differenze significative nelle variabili osservabili.

**Le due condizioni di validità del disegno randomizzato:**

1. **gli aspetti etici** collegati alla ricerca su soggetti umani devono essere stati ben considerati e non impedire l'applicazione di interventi diversi a persone diverse. *Per esempio, in presenza di vincoli di risorse, **non sarebbe etico negare a qualcuno un intervento i cui benefici siano già stati documentati**, al solo fine di realizzare un esperimento*;
2. **la dimensione del campione deve essere abbastanza grande**: con pochi partecipanti al progetto pilota potrebbero non esserci **sufficienti osservazioni per stimare statisticamente l'impatto** anche in caso di successo.

**I limiti pratici.** L'applicazione richiede **tempo, risorse** e, soprattutto, **la necessità che il disegno di valutazione sia progettato PRIMA dell'implementazione dell'intervento**. E non sempre è applicabile: **gli interventi sociali sono spesso vincolati da leggi e procedure amministrative**. Il manuale fa due esempi molto pertinenti per un funzionario pubblico:

- **la Costituzione di un Paese potrebbe vietare di rivolgere esclusivamente a un sottoinsieme della popolazione un intervento che comporta la riduzione o l'aumento dei benefici** (è il problema di uguaglianza dell'art. 3 Cost.);
- **alcuni interventi potrebbero applicarsi a intere comunità**, come quelli che promuovono economie parallele di mutuo aiuto.

La conclusione realistica: *in generale, **un piano di riforma prevede solitamente alcune misure che possono essere testate con studi randomizzati e altre che richiedono metodi differenti**.*

**La distinzione metodologica generale**, che il manuale pone in nota ed è ottima da citare:

> **Metodi PROSPETTIVI (sperimentali)** vs **metodi RETROSPETTIVI (quasi-sperimentali)**. In questi ultimi **non c'è un'assegnazione casuale ma una «manipolazione» della documentazione disponibile**, in maniera da **creare un gruppo di confronto statistico e/o intertemporale**. Quando non è pratico o etico assegnare casualmente i partecipanti a un programma si utilizzano dei **quasi-esperimenti**, progettati per massimizzare la validità dei risultati, **la quale tenderà comunque a rimanere inferiore a quella di uno studio randomizzato**.

**L'esempio del manuale — la «sanità integrata» negli Stati Uniti.** *Uno studio americano pubblicato nel **2002** ha riguardato un gruppo di anziani beneficiari di servizi di assistenza domiciliare, esposti al rischio di un uso elevato di servizi. **Metà dei pazienti sono stati assegnati in modo casuale** a un'infermiera (*Nurse Care Manager*), con il compito di migliorare il collegamento fra i servizi per le forme acute e quelli di assistenza a lungo termine. Lo scopo era ridurre i ricoveri ospedalieri. **Gli autori hanno concluso che non vi erano differenze fra i due gruppi in nessuna delle variabili risultato** esaminate durante i 18 mesi di sperimentazione: l'intervento, che ha tentato di raggiungere l'obiettivo ricorrendo a un *case manager* **senza incentivi finanziari o regolamentari**, non si è rivelato in grado di produrre un mutamento significativo.*

È un esempio prezioso proprio perché **ha dato esito nullo**, e il manuale lo usa apposta.

### 91.4 Regression Discontinuity Design (RDD)

**Il principio.** L'RDD **consente di simulare la valutazione su dati sperimentali**, cioè con processo di selezione randomizzato, **senza aver randomizzato**. Il concetto su cui si basa è **la discontinuità del trattamento**:

> **Se i soggetti vengono assegnati al trattamento sulla base di una variabile criterio OSSERVABILE, e la discriminante è una SOGLIA di ammissibilità su questa variabile, allora coloro che si trovano APPENA SOPRA e APPENA SOTTO la soglia sono fra loro del tutto SIMILI: di fatto, dunque, non vi è selection bias. In queste condizioni l'assegnazione al trattamento può essere considerata come frutto di un esperimento randomizzato.**

L'intuizione da esprimere all'orale: **chi ha un punto in più e chi ha un punto in meno di una soglia burocratica non sono persone diverse; la soglia è arbitraria, e quindi nell'immediato intorno della soglia l'assegnazione è, nella sostanza, casuale.**

**L'esempio del manuale**: *si supponga che, a seguito di una nuova disposizione sugli assegni d'invalidità, alle persone al di sotto di una certa soglia d'invalidità siano ridotti i vantaggi e offerte misure attive per l'ingresso nel mercato del lavoro. Il metodo confronterebbe **i disabili appena sopra la soglia** (che godrebbero dei vecchi benefici) **con quelli appena sotto** (ai quali si applicherebbe la nuova disposizione).*

**I due presupposti:**

1. **i soggetti sono ammessi all'intervento con un criterio di selezione quantificato chiaramente**;
2. **i partecipanti non sono in grado di prevedere e manipolare i punteggi vicini al punto di *cut-off*** (nell'esempio: modificare il loro livello di disabilità). È la condizione di **non manipolazione**, ed è cruciale: se i soggetti possono scegliersi da che parte della soglia stare, la casualità sparisce.

Si assume inoltre che gli individui appena sotto e appena sopra la soglia **non siano significativamente diversi**, il che comporta di solito che **il punteggio intorno alla soglia sia un continuum**.

**I tre criteri che la variabile di selezione deve soddisfare:**

1. **deve essere continua oppure ordinale**, con un numero sufficiente di valori univoci. **Non deve mai essere basata su categorie non ordinali** (come il genere);
2. **non deve generare confusione**: **lo stesso valore di soglia non deve essere utilizzato per assegnare ai soggetti interventi diversi da quello in fase di test**. L'esempio che il manuale fa è **estremamente rilevante per il tuo bando**: *l'**ISEE** (Indicatore della Situazione Economica Equivalente) **non può essere la base di un confronto attorno al punto di discontinuità**, perché il medesimo criterio è utilizzato per l'ammissibilità a **una più vasta gamma di servizi**.* Questa limitazione è fondamentale per garantire che lo studio possa **isolare** gli effetti causali dell'intervento testato dagli effetti di altri interventi;
3. **non deve essere riportata in maniera non fedele** per rendere i cittadini ammissibili a un programma o a un'agevolazione (di nuovo: non manipolabilità).

**Le due criticità.**

**a) La validità esterna limitata** — questa è **la critica principale**, da dire sempre:

> **L'RDD misura l'effetto dell'intervento SOLO sulle persone che si trovano VICINO alla soglia di ammissibilità.** Se i decisori politici sono interessati a valutare l'impatto su tutta la popolazione (**validità esterna**), **questo metodo non è appropriato**: i risultati, per esempio, **non possono essere adoperati per analizzare l'impatto di un'eventuale variazione, verso l'alto o verso il basso, del valore di soglia**.

È un caso da manuale di **fortissima validità interna e debole validità esterna**: si sa con grande precisione una cosa che vale per pochi.

**b) L'ampiezza dell'intervallo** — è un *trade-off* che vale la pena esporre così:

- se l'intervallo è **piccolo**, i due gruppi sono molto **simili** (stima poco distorta), **ma l'effetto è misurato su poche persone, con maggiore incertezza**;
- se l'intervallo è **ampio**, si ottiene una stima **più precisa** ma **confrontando gruppi con maggiori differenze fra loro** (stima più distorta).

È, ancora una volta, il *trade-off* fra **distorsione e varianza** che attraversa tutta l'econometria — lo stesso della ridge regression.

**L'esempio del manuale — la riforma dell'assicurazione sull'invalidità in Norvegia.** *Gli studiosi **Kostøl e Mogstad (2014)** hanno usato questo metodo per valutare l'impatto di un cambiamento nella politica di erogazione degli incentivi a favore dei beneficiari di indennità per inabilità. Gli individui divenuti **beneficiari prima del 1° gennaio 2004** erano stati esposti a norme più generose sulla possibilità di **cumulare sussidi e salari** (nuovi incentivi al lavoro) rispetto ai beneficiari del periodo successivo. Gli autori hanno ipotizzato che i richiedenti **subito prima e subito dopo tale data fossero molto simili fra loro**, per cui le differenze nei risultati (tasso di occupazione mentre si gode del sussidio, tasso di uscita dal mercato del lavoro) potessero essere attribuite alla variazione delle norme. **Questo non è un confronto prima-dopo**, precisa il manuale, **in quanto tutti gli individui sono osservati simultaneamente nella medesima situazione di contesto.** Il risultato: gli incentivi economici inducono una parte sostanziale dei beneficiari a tornare al lavoro, **ma solo la componente più giovane** — il che conferma sia che alcuni beneficiari possono lavorare, sia che gli incentivi sono efficaci nell'incoraggiarli.*

Nota la finezza metodologica: **la soglia qui è una data**, non un punteggio. È un ottimo esempio di come si trovi una discontinuità nella normativa.

**L'RDD con più soglie.** Un caso particolare è quello in cui **più variabili criterio determinano l'ammissibilità**. Quella che sembrerebbe una complicazione **può essere sfruttata applicando la strategia separatamente su ciascuna soglia di discontinuità**: e **trovare effetti analoghi su entrambe (o più) soglie rafforza la validità dei risultati, confermando la corretta identificazione del controfattuale**. È una forma di **verifica di robustezza**, ed è un bel punto da citare.

## 92. L'interpretazione dei risultati: i quattro aspetti chiave

Il manuale chiude con una sezione di metodo **valida per tutti i metodi di valutazione**. È la parte che, in commissione, distingue chi ha capito che la valutazione è un mestiere e non un calcolo.

Premessa: *l'effetto netto di un intervento corrisponde generalmente alla differenza nel livello della variabile d'interesse fra i due gruppi.* Ma su quella differenza pesano quattro insidie.

### 92.1 La scelta del momento di misurazione — l'effetto *lock-in*

> **Alcuni risultati possono richiedere del tempo prima di manifestarsi e diventare pienamente osservabili.**

L'esempio, tipico delle politiche attive del lavoro: nelle **misure di attivazione** le persone in cerca di lavoro sono **incoraggiate a fermare temporaneamente la loro ricerca** per seguire la formazione offerta dall'intervento — è il periodo di ***lock-in***. La ricerca di lavoro **riprende solo dopo il completamento del ciclo formativo**, e occorre ancora tempo prima che si producano esiti misurabili. **Se i tassi di occupazione fossero stimati durante il periodo di lock-in, l'impatto sarebbe ovviamente SOTTOVALUTATO** — anzi, potrebbe apparire addirittura negativo.

**La lezione**: misurare troppo presto significa sbagliare; l'effetto **diventa più evidente con il trascorrere del tempo**.

### 92.2 Il monitoraggio della *compliance* (conformità)

> **I risultati possono essere fuorvianti se alcune delle unità assegnate al gruppo di controllo dovessero comunque ricevere il servizio previsto dal programma, e/o alcuni beneficiari rimanere esclusi.**

Una **conformità parziale** riduce potenzialmente **la differenza fra i gruppi in termini di esposizione all'intervento**. Il caso estremo: **se lo stesso numero di soggetti nei due gruppi ricevesse il programma, non sarebbe possibile misurare alcun impatto**, perché entrambi avrebbero avuto la stessa esposizione.

**Il rimedio**: **solo con il monitoraggio continuo della conformità, mentre l'intervento è in corso**, i ricercatori possono agire tempestivamente. E **i tassi di conformità devono essere rigorosamente registrati**, così da poter essere presi in considerazione nell'analisi.

### 92.3 La limitazione dell'«attrito»

> **L'attrito è ciò che si verifica quando i ricercatori non sono in grado di misurare i risultati per alcuni dei soggetti inclusi nella valutazione.**

Il problema non è l'attrito in sé, ma **l'attrito differenziale**: **se tipo e dimensione dell'attrito sono diversi nel gruppo dei beneficiari e in quello di controllo, i risultati potrebbero essere distorti**.

**L'esempio del manuale**, molto raffinato: *in una politica di attivazione, i **disoccupati meno impiegabili nel gruppo d'intervento** potrebbero essere più propensi a migliorare le proprie prospettive e **a non abbandonare il programma**, mentre **i meno impiegabili nel gruppo di controllo potrebbero scoraggiarsi e abbandonare**. La conseguenza sarebbe una **sovrarappresentazione delle persone meno occupabili nel gruppo d'intervento**, che renderebbe i due gruppi **non più confrontabili**. In questo caso **l'impatto del programma risulterebbe sottovalutato**.*

**Il requisito di indipendenza**: *è della massima importanza che la valutazione sia condotta da **una parte terza obiettiva e indipendente**. Il disegno valutativo e i suoi metodi devono essere accuratamente **registrati** e, quando possibile, **i dati devono essere resi pubblici per semplificare la replicabilità della valutazione**.*

### 92.4 La comunicazione dei risultati — il valore dell'effetto nullo

È la chiusura del manuale, ed è **la frase più bella del capitolo**. Vale la pena impararla quasi a memoria:

> **Valutazioni indipendenti e imparziali, con sufficiente potenza statistica e progettazione adeguata, possono anche registrare EFFETTI NULLI. UN IMPATTO NULLO PUÒ ESSERE UTILE QUANTO UN AMPIO IMPATTO POSITIVO O NEGATIVO.**
>
> Per questo motivo, **ricercatori e *policy makers* dovrebbero avere ben chiaro che l'obiettivo di una valutazione d'impatto è misurare se un intervento sia efficace nel raggiungere gli obiettivi previsti, e che è comunque possibile che l'intervento non mostri alcun effetto o, addirittura, ne esibisca di negativi.** Al fine di migliorare l'apprendimento reciproco, **il gruppo di valutazione deve riportare e diffondere i risultati in modo trasparente e completo.**

> **Perché questa è la conclusione giusta per l'orale.** *La valutazione d'impatto non serve a giustificare una politica: serve a sapere se funziona. Una valutazione che non può dare esito negativo non è una valutazione. Per un funzionario pubblico questo significa che la valutazione va progettata **prima** dell'intervento, affidata a **soggetti terzi**, basata su **dati resi disponibili**, e comunicata **anche quando dice che la politica non ha funzionato** — perché anche quello è un risultato che migliora la spesa pubblica futura.*

---

# PARTE XVII — LE VENTI FORMULE FONDAMENTALI

Queste sono **le uniche formule** che ho estratto da tutto il manuale. Le ho raccolte qui, come promesso all'inizio, perché tu possa **valutarle in blocco e decidere quali memorizzare**. Per ciascuna indico **che cosa dice a parole** e **quanto conta davvero** con un giudizio esplicito.

La mia raccomandazione, sulla base di quanto raccontano i candidati sulle prove orali RIPAM: **impara le prime sette, che servono a capire e a rispondere; leggi le altre una volta, per riconoscerle se la commissione le nomina, ma non memorizzarle.** Nessuna commissione ti chiederà di derivare uno stimatore; molte ti chiederanno di spiegare che cosa significa un R² di 0,85.

## Le sette da sapere davvero

**1. Il modello di regressione lineare**
> **Y = β₀ + β₁X + ε**  (semplice)
> **Y = β₀ + β₁X₁ + … + β_k X_k + ε**  (multipla)

*Che cosa dice:* la variabile dipendente è la somma di una **parte sistematica** e di una **componente stocastica**. β₁ è la variazione di Y per una variazione unitaria di X, **a parità delle altre variabili**.
**★★★ Indispensabile.** È la materia.

**2. Il criterio dei minimi quadrati**
> **min Σ(yᵢ − ŷᵢ)² = min Σeᵢ²**

*Che cosa dice:* si sceglie la retta che **rende minima la somma dei quadrati degli scarti** fra valori osservati e valori teorici. I quadrati servono perché scarti di segno opposto non si compensino.
**★★★ Indispensabile**, ma **da sapere a parole, non da scrivere**.

**3. Il coefficiente di regressione come rapporto**
> **β̂₁ = Cov(X, Y) / Var(X)**   e   **β̂₀ = ȳ − β̂₁x̄**

*Che cosa dice:* la pendenza è **quanto le due variabili variano insieme, diviso quanto varia il regressore**. L'intercetta si ricava imponendo che la retta passi per il **baricentro** (x̄, ȳ).
**★★★ Da sapere**: è il ponte fra regressione e statistica descrittiva, ed è facilissima da ricordare.

**4. La scomposizione della devianza e l'R²**
> **TSS = ESS + RSS**
> **R² = ESS/TSS = 1 − RSS/TSS**

*Che cosa dice:* la variabilità totale di Y si divide in **spiegata** e **residua**; R² è la **quota spiegata dal modello**, compresa fra 0 e 1.
**★★★ Indispensabile.** È il numero che ti verrà chiesto di commentare.

**5. La statistica t di significatività**
> **t = β̂ᵢ / es(β̂ᵢ)**    (con n−k gradi di libertà)

*Che cosa dice:* **coefficiente diviso il suo errore standard**. Se in valore assoluto supera circa 2, il coefficiente **è significativamente diverso da zero** al 5%.
**★★★ Indispensabile.** È come si legge un output.

**6. Il coefficiente di correlazione e il suo legame con R²**
> **r = Cov(X,Y) / (σ_X · σ_Y)**,  con **−1 ≤ r ≤ 1**
> **Nella regressione semplice: R² = r²**

*Che cosa dice:* r misura **la dipendenza lineare** fra due variabili. È un **numero puro**. Attenzione: **r = 0 non significa indipendenza**, significa assenza di relazione *lineare*.
**★★★ Da sapere**, insieme alle due avvertenze (incorrelazione ≠ indipendenza; correlazione spuria).

**7. Il differenza-nelle-differenze**
> **DiD = (Ȳ_trattati,dopo − Ȳ_trattati,prima) − (Ȳ_controllo,dopo − Ȳ_controllo,prima)**

*Che cosa dice:* **la variazione dei trattati meno la variazione dei non trattati**. La seconda differenza stima la **dinamica spontanea**; ciò che resta è **l'effetto della politica**. Vale sotto l'**assunto di parallelismo dei trend**.
**★★★ Indispensabile per il tuo bando.** È l'unica formula del capitolo 16 e va saputa **a parole**, non in simboli.

## Le sette da riconoscere

**8. Lo stimatore della varianza dell'errore**
> **s² = RSS / (n − k)**,  con **SER = √s²**

*Perché n−k:* si perdono tanti gradi di libertà quanti sono i parametri stimati. La radice è l'**errore standard della regressione**.
**★★ Utile**: giustifica i gradi di libertà di tutti i test.

**9. La statistica F di significatività congiunta**
> **F = [ESS/(k−1)] / [RSS/(n−k)] = [R²/(k−1)] / [(1−R²)/(n−k)]**

*Che cosa dice:* rapporto fra **varianza spiegata e varianza residua**. Verifica se **almeno una** variabile è significativa. Nella regressione semplice **F = t²**.
**★★ Utile**, soprattutto per la diagnosi «F significativa, nessuna t significativa» = multicollinearità.

**10. L'R² corretto**
> **R̄² = 1 − [RSS/(n−k)] / [TSS/(n−1)]**

*Che cosa dice:* penalizza l'aggiunta di variabili. **Serve a confrontare modelli con un diverso numero di regressori**, cosa che l'R² semplice non può fare perché **non diminuisce mai**.
**★★ Utile**, il concetto più della formula.

**11. Il VIF — fattore di inflazione della varianza**
> **VIFᵢ = 1 / (1 − R²ᵢ)**

dove R²ᵢ è l'R² della regressione **di Xᵢ sulle altre esplicative**. Soglia di allarme: **VIF > 10** (Marquardt); alcuni già a **VIF > 3**.
**★★ Utile**: è il numero che si guarda per diagnosticare la multicollinearità.

**12. L'intervallo di confidenza**
> **stima ± (valore critico) × (errore standard)**

*Che cosa dice:* vale per **qualunque** parametro. Si restringe **al crescere di n** e **al diminuire del livello di confidenza**. Per dimezzarne l'ampiezza serve **quadruplicare il campione**.
**★★ Utile**: è uno schema, non una formula.

**13. La statistica di Durbin-Watson**
> **d ≈ 2(1 − r)**,  con **0 ≤ d ≤ 4**

*Come si legge:* **d ≈ 2** → nessuna autocorrelazione; **d < 2** → positiva; **d > 2** → negativa. Rileva **solo il primo ordine** e ha **zone d'ombra**.
**★★ Utile**: il numero e la sua lettura, niente di più.

**14. Il propensity score**
> **e(X) = P(D = 1 | X = x)**

*Che cosa dice:* **la probabilità di essere trattato date le caratteristiche osservate**. Riduce un problema multidimensionale a **un solo numero**. Si stima con un **logit** o un **probit**, poi si abbinano trattati e controlli con punteggio simile.
**★★★ per il tuo bando**, anche se non è propriamente una formula: è **una definizione**, e come tale va saputa.

## Le sei da lasciar perdere (ma di cui conoscere il nome)

**15. Lo stimatore OLS in forma matriciale** — **β̂ = (X′X)⁻¹X′y**. Da sapere solo che **esiste se e solo se X′X è invertibile**, cioè in assenza di collinearità perfetta. ★ Non memorizzare.

**16. Lo stimatore GLS (di Aitken)** — l'OLS applicato al modello trasformato in modo da ripristinare la sfericità degli errori. **BLUE**; coincide con l'OLS quando gli errori sono sferici. ★ Solo il concetto.

**17. Lo stimatore ridge** — **β̂_R = (X′X + cI)⁻¹X′y**. Da sapere che **c è lo *shrinkage parameter***, che **per c = 0 si torna all'OLS**, e che è **distorto ma con MSE minore**. ★ Solo il concetto.

**18. Il processo AR(1)** — **Xₜ = φXₜ₋₁ + Wₜ**, con **|φ| < 1** (condizione di stazionarietà) e **ρₛ = φˢ**. Da sapere che **φ è il parametro di persistenza**. ★ Solo il concetto e la firma ACF/PACF.

**19. La statistica del test di Hausman** — basata sulla **differenza fra lo stimatore within e quello GLS**, distribuita come **chi-quadrato con k gradi di libertà**. Da sapere **che cosa confronta e come si decide**, non come si calcola. ★★ Il concetto è importante.

**20. Il MAPE** — **media dei valori assoluti degli errori relativi percentuali**. Soglia di buona previsione: **inferiore al 12-15%**. ★ Facile e ricordabile, tanto vale saperla.

> **Un consiglio sul metodo.** Se in commissione ti chiedono una formula che non ricordi, **non improvvisare simboli**: di' che cosa fa quella formula e perché è costruita così. *«Il VIF è il reciproco di uno meno l'R² della regressione di quella variabile su tutte le altre: se quella variabile è perfettamente spiegata dalle altre, il denominatore va a zero e la varianza del coefficiente esplode»* è una risposta migliore di qualunque formula scritta correttamente ma non capita.

---

# PARTE XVIII — SESSANTA DOMANDE D'ORALE CON TRACCIA DI RISPOSTA

Le ho organizzate per parte, in ordine crescente di difficoltà all'interno di ciascuna. Le **dodici contrassegnate con ►** sono quelle che, per struttura del bando e per frequenza nelle testimonianze, hanno la probabilità più alta.

## Statistica di base (Parti I-V)

1. **Quali sono le medie analitiche e che relazione c'è fra loro?** — Armonica, geometrica, aritmetica, quadratica; vale sempre **M_a ≤ M_g ≤ M_A ≤ M_Q**. Ciascuna risponde a un tipo di problema diverso: l'armonica per le velocità e i rapporti, la geometrica per i tassi di variazione.
2. **Quali sono le due proprietà degli scarti dalla media?** — La **somma degli scarti è nulla**; la **somma dei quadrati degli scarti è minima**. La seconda è **la radice del metodo dei minimi quadrati**.
3. **Che differenza c'è fra varianza, scarto quadratico medio e coefficiente di variazione?** — La varianza è in unità al quadrato; lo s.q.m. è nella stessa unità del carattere; il **coefficiente di variazione è un numero puro**, e serve a confrontare la variabilità di fenomeni misurati in unità diverse.
4. **Che cos'è il teorema di Bayes e a che serve?** — Permette di **invertire il condizionamento**: dalla probabilità dell'effetto data la causa, alla probabilità della causa dato l'effetto. L'esempio classico del test diagnostico su malattia rara mostra che **anche un test accurato dà molti falsi positivi se la malattia è rara**.
5. **A che cosa servono la chi-quadrato, la t di Student e la F di Fisher?** — La **chi-quadrato** per l'inferenza sulla varianza e i test di adattamento; la **t** per l'inferenza sulla media e sui coefficienti quando σ è ignota; la **F** per confrontare varianze e per i test congiunti.
6. **Che cos'è il teorema del limite centrale e perché conta in econometria?** — La somma di molte variabili indipendenti tende alla normale, indipendentemente dalle loro distribuzioni. **Giustifica l'ipotesi di normalità degli errori** e la validità asintotica dei test anche senza normalità.
7. ► **Quali sono le proprietà desiderabili di uno stimatore?** — **Correttezza** (in media colpisce il bersaglio), **consistenza** (converge al vero al crescere di n), **efficienza** (varianza minima), **sufficienza**, **normalità asintotica**. Precisare che **correttezza e consistenza sono indipendenti**: uno stimatore può essere corretto ma non consistente e viceversa.
8. **Come si interpreta correttamente un intervallo di confidenza al 95%?** — **Non** «il parametro cade in questo intervallo con probabilità 0,95»: il parametro è fisso. È una **proprietà della procedura**: ripetendo l'estrazione molte volte, il 95% degli intervalli così costruiti conterrebbe il vero valore.
9. **Quali sono i due tipi di errore nella verifica d'ipotesi?** — **Prima specie**: rifiutare H₀ quando è vera (probabilità α); **seconda specie**: non rifiutare H₀ quando è falsa (probabilità β). **1−β è la potenza.** C'è un *trade-off*: ridurre α aumenta β, a parità di n.
10. **Significatività statistica e rilevanza sostanziale sono la stessa cosa?** — **No.** Con un campione abbastanza grande qualunque differenza, anche irrilevante, diventa significativa. La significatività dice **che l'effetto non è zero**, non **che è importante**.

## Il modello di regressione (Parti VI-IX)

11. ► **Che cos'è l'econometria?** — La disciplina che misura le relazioni economiche combinando **teoria economica** (quali variabili, quale direzione causale), **matematica** (forma funzionale) e **statistica inferenziale** (stima e verifica). La sua difficoltà specifica è che **lavora su dati non sperimentali e non ripetibili**.
12. ► **Quali sono i quattro stadi della costruzione di un modello econometrico?** — **Specificazione, stima, verifica, utilizzo.** Nella verifica distinguere i tre piani: **significatività statistica**, **capacità descrittiva**, **conformità alle aspettative teoriche** (tramite i moltiplicatori).
13. **Quali sono i tre tipi di dati?** — **Serie storiche** (una unità nel tempo; problema tipico: autocorrelazione), **cross section** (più unità in un istante; problema tipico: eteroschedasticità), **panel** (entrambe le dimensioni; permettono di controllare l'eterogeneità individuale non osservata).
14. **Che differenza c'è fra forma strutturale e forma ridotta?** — La **strutturale** esprime le endogene in funzione delle esogene **e delle altre endogene**: è **un modello di analisi**, la fotografia della teoria. La **ridotta** esprime ciascuna endogena in funzione delle sole esogene: è **un modello di strategia**, quello che si usa per simulare e prevedere.
15. **Perché un modello econometrico può fallire?** — Tre cause: la **teorizzazione non regge**; la teoria è giusta ma la **formulazione è errata** (per esempio si usa una forma lineare per una relazione non lineare); i **dati o il metodo di stima non sono idonei**.
16. ► **Quali sono le ipotesi classiche del modello di regressione lineare?** — **Linearità**, **non sistematicità degli errori** (media nulla), **omoschedasticità**, **covarianza nulla fra errori**, **non stocasticità delle esplicative**, **normalità degli errori**. Saperle elencare **con la patologia corrispondente** a ciascuna.
17. ► **Che cos'è il metodo dei minimi quadrati e perché i quadrati?** — Sceglie la retta che minimizza la somma dei **quadrati** degli scarti; i quadrati perché gli scarti di segno opposto si compenserebbero, e perché così si penalizzano di più gli scarti grandi. Proposto da **Gauss (1795)** e **Legendre (1805)**.
18. **Che differenza c'è fra residui e disturbi?** — I **residui** sono **sempre calcolabili** una volta stimati i coefficienti; i **disturbi** (gli errori veri) **non sono mai osservabili**, perché richiederebbero di conoscere i veri parametri. Il residuo è la controparte campionaria del disturbo.
19. **Quali sono le proprietà algebriche della retta di regressione?** — È **unica**; passa per il **baricentro** (x̄, ȳ); **la media dei valori stimati coincide con la media degli osservati** (e quindi la somma dei residui è nulla).
20. ► **Che cos'è l'R² e quali sono i suoi limiti?** — La **quota di variabilità di Y spiegata dal modello**, fra 0 e 1. Limite fondamentale: **non diminuisce mai aggiungendo variabili**, quindi un R² alto non significa che il modello sia buono. Per confrontare modelli con un diverso numero di regressori serve l'**R² corretto**.
21. ► **Che cos'è il teorema di Gauss-Markov?** — Sotto le ipotesi classiche, gli stimatori OLS sono **BLUE**: **lineari, non distorti e i più efficienti** fra gli stimatori lineari e non distorti. Aggiungere che **«Best» non garantisce che la varianza sia piccola** — da lì nasce la ridge.
22. **Correlazione significa causalità?** — **No.** Il coefficiente r misura **concordanza**, non dipendenza; può essere nullo pur in presenza di relazione non lineare; e può essere alto per **correlazione spuria**, quando un fattore comune agisce su entrambe le variabili. È il problema da cui nasce tutta l'analisi controfattuale.
23. **Che cos'è l'elasticità e come si stima?** — La **variazione percentuale di Y per una variazione percentuale di X**. Si stima con il **modello doppio logaritmico**, in cui **il coefficiente È l'elasticità, costante lungo tutta la curva**.
24. **Mi parli della funzione di produzione Cobb-Douglas.** — P = γ₀L^αK^β; **omogenea di grado α+β**, che misura i **rendimenti di scala**; **α e β sono le elasticità** dei fattori. **Non è lineare ma si linearizza prendendo i logaritmi**, diventando una regressione multipla doppio-logaritmica stimabile con OLS.
25. **Che cos'è la curva di Phillips?** — La relazione **inversa fra tasso di variazione dei salari monetari e tasso di disoccupazione**, osservata da **A.W. Phillips (1958)** sui dati britannici **1861-1957**. Nel manuale è l'esempio del **modello iperbolico**.
26. ► **Come si interpreta un coefficiente nella regressione multipla?** — Come **l'effetto della propria variabile tenendo costanti tutte le altre incluse nel modello** (*ceteris paribus*). È un effetto **netto**, ma solo rispetto alle variabili **effettivamente incluse**: nulla dice su quelle omesse.
27. **Che differenza c'è fra il test t e il test F nella regressione multipla?** — Il **t** verifica la significatività **di un singolo coefficiente**, ed è un **test parziale**, perché dipende dalle altre variabili incluse. L'**F** verifica la significatività **congiunta**; il suo rifiuto significa che **almeno una** variabile conta.
28. ► **Che cosa sono le variabili dummy e a che servono?** — Variabili binarie (0/1) che permettono di **inserire informazione qualitativa** nel modello e di **discriminare fra due situazioni**. Con g modalità si inseriscono **g−1 dummy più l'intercetta**, altrimenti si cade nella **trappola della collinearità perfetta**. Con un **termine di interazione** cambiano anche la pendenza, non solo l'intercetta: è la base del **DiD**.

## Le patologie (Parti X-XIII)

29. ► **Che cos'è la multicollinearità e che effetti ha?** — Eccessiva correlazione fra variabili esplicative. Gli stimatori **restano corretti**, ma **le varianze esplodono**, gli intervalli di confidenza si allargano, e **i coefficienti diventano instabili, cambiando anche di segno** a fronte di piccole modifiche del modello.
30. **Come si diagnostica la multicollinearità?** — **Matrice di correlazione** (limite: coglie solo le coppie); **VIF** (soglia 10, o 3 per i più prudenti); **autovalori e numero di condizionamento** (soglia 30; procedura di **Belsley, Kuh e Welsch**); **determinante di X′X**; **configurazione F significativa / t non significative**.
31. **Come si rimedia?** — **Raccogliere più dati** (ma spesso ripropongono il problema); **rispecificare il modello**, ridefinendo o eliminando variabili (pericoloso: si introduce distorsione da omissione); **regressione ridge**, che accetta uno stimatore distorto in cambio di varianza molto minore.
32. **Che cosa sono i metodi stepwise e quali limiti hanno?** — **Forward selection**, **backward elimination**, **stepwise** (Efroymson, 1960). Producono modelli **validi statisticamente ma di interpretazione discutibile**, perché massimizzano l'adattamento ai dati e non la coerenza teorica.
33. **Che cos'è la massima verosimiglianza?** — Il metodo che sceglie i parametri **che rendono più probabili i dati osservati** (Fisher, 1912-1922). **Sotto normalità coincide con l'OLS per i coefficienti**; è **consistente, asintoticamente normale e asintoticamente efficiente** (raggiunge il limite di Cramér-Rao). Indispensabile per i modelli **logit e probit**.
34. ► **Che cos'è l'endogeneità e quali sono le sue fonti?** — La **correlazione fra un regressore e il termine d'errore**. Tre fonti: **omissione di variabili rilevanti** (l'esempio istruzione/reddito senza controllare l'abilità), **errori di misura nelle esplicative**, **simultaneità** (prezzo e quantità di equilibrio). Conseguenza: **l'OLS è distorto E INCONSISTENTE**.
35. ► **Che cos'è una variabile strumentale e quali condizioni deve soddisfare?** — Tre condizioni: **rilevanza** (correlata con il regressore endogeno), **esogeneità** (incorrelata con l'errore), **esclusione** (non influenza direttamente la dipendente). Lo stimatore IV è **consistente ma non corretto**, con varianza maggiore dell'OLS: un costo accettabile perché **l'OLS, in presenza di endogeneità, è sbagliato e resta sbagliato**.
36. ► **Che cosa succede agli stimatori OLS in presenza di eteroschedasticità o autocorrelazione?** — **Restano corretti ma perdono l'efficienza**; soprattutto **gli errori standard calcolati nel modo abituale sono sbagliati**, il che **falsa tutti i test**. Il rimedio generale sono i **minimi quadrati generalizzati (GLS)**.
37. **Che cos'è l'eteroschedasticità e con quali test si rileva?** — Varianza dell'errore non costante fra le osservazioni; tipica dei **dati cross section** (esempio: profitti di imprese di dimensione diversa). Test: **Bartlett** (dati raggruppati), **Breusch-Pagan** (grandi campioni), **Goldfeld-Quandt** (piccoli campioni, quando si sospetta una specifica variabile), **White** (generale).
38. **Che cosa sono i minimi quadrati ponderati?** — La forma che assume il GLS in presenza di eteroschedasticità: si **pesano le osservazioni inversamente alla loro varianza**, dando più peso a quelle più affidabili.
39. **Che cos'è un processo stocastico e che cos'è la stazionarietà?** — Un processo stocastico è una **famiglia di variabili casuali dipendenti dal tempo**; una serie storica ne è **una realizzazione finita**. È **stazionario in senso debole** se ha **media costante, varianza finita e costante, e autocovarianza dipendente solo dal lag**.
40. **Che cos'è un white noise?** — Un processo stazionario con **media nulla, varianza costante e osservazioni incorrelate**. **È l'obiettivo della modellazione**: i residui di un buon modello devono essere un white noise.
41. ► **Come si riconosce un AR da un MA?** — **AR(p)**: l'ACF decresce gradualmente, **la PACF si annulla dopo p ritardi**. **MA(q)**: **l'ACF si annulla dopo q ritardi**, la PACF decresce gradualmente. *Mnemonica: **AR taglia la PACF, MA taglia l'ACF**.*
42. **Che cos'è il test di Durbin-Watson e quali limiti ha?** — Statistica **d ≈ 2(1−r)**, con d ≈ 2 = assenza di autocorrelazione. Tre limiti: **rileva solo il primo ordine**; **non è applicabile con la dipendente ritardata fra i regressori**; ha **zone d'ombra** in cui è inconcludente. Il test generale è **Breusch-Godfrey**.
43. **Quali sono i rimedi all'autocorrelazione?** — Stima diretta di ρ dai residui o da DW; processo iterativo delle **quasi differenze prime**; **Cochrane-Orcutt** (iterativo); **Hildreth-Lu** (a griglia — il manuale lo considera il migliore secondo il criterio OLS); **massima verosimiglianza** (Beach-MacKinnon, ancora migliore).
44. **L'autocorrelazione dei residui è solo un problema tecnico?** — **No: è un sintomo di mispecificazione.** Il manuale è esplicito: se i residui sono autocorrelati, il modello **non ha catturato tutte le relazioni dinamiche** presenti nei dati, tipicamente perché **mancano variabili esplicative**.
45. ► **Perché nei modelli a equazioni simultanee non si può usare l'OLS?** — Perché i regressori endogeni **sono correlati con l'errore per costruzione**, e gli stimatori risultano **inconsistenti**: non convergono al valore vero **neanche con infinite osservazioni**. Si usano **variabili strumentali, minimi quadrati indiretti o doppi minimi quadrati**.
46. **Che cos'è il problema dell'identificazione?** — La possibilità di **risalire univocamente dai parametri della forma ridotta a quelli della forma strutturale**. Se il modello non è identificato **non è che non esistono soluzioni: ne esistono troppe**, e occorre introdurre vincoli. **Sottoidentificata** (nessun metodo applicabile), **esattamente identificata** (ILS e 2SLS), **sovraidentificata** (solo 2SLS).
47. **Come funziona il 2SLS?** — **Primo stadio**: si regredisce il regressore endogeno sugli strumenti, ottenendo il valore predetto, che è **incorrelato con l'errore**. **Secondo stadio**: si stima l'equazione strutturale **usando il valore predetto al posto del regressore endogeno**. È il metodo **più utilizzato nella pratica**.

## Serie storiche e panel (Parti XIV-XV)

48. ► **Quali sono le componenti di una serie storica?** — **Trend** (tendenza di lungo periodo), **ciclo** (fasi ascendenti e discendenti, durata pluriennale variabile), **stagionalità** (periodicità infrannuale fissa, legata al ciclo solare), **componente accidentale**. Le prime tre **contengono tutta l'informazione**; la quarta è rumore.
49. **Quando si usa il modello additivo e quando il moltiplicativo?** — **Additivo** se l'ampiezza dell'oscillazione stagionale **non cambia** al variare del livello della serie; **moltiplicativo** se **cresce proporzionalmente** al livello. In economia **prevale il moltiplicativo**. Il moltiplicativo si linearizza con i **logaritmi**.
50. **Come si stima il trend-ciclo?** — Con le **medie mobili**, di ordine pari al numero di osservazioni in un anno (12 per dati mensili, 4 per trimestrali). Con ordine **pari** si usa la **media mobile centrata**, con pesi 1, 2, 2, …, 2, 1.
51. ► **Che cos'è un modello ARIMA?** — *AutoRegressive Integrated Moving Average*(p, d, q): un ARMA applicato **alle differenze d-esime** della serie. **d è il numero di differenziazioni necessarie a rendere stazionaria la serie.** Serve perché **le serie economiche reali sono quasi sempre evolutive, non stazionarie**.
52. ► **Mi descriva la procedura di Box-Jenkins.** — Cinque passi **iterativi**: **analisi preliminare** (stazionarietà, si trova d), **identificazione** (si trovano p e q da ACF e PACF), **stima** (massima verosimiglianza), **verifica** (parametri significativi, modello **parsimonioso**, **residui = white noise**, test di **Ljung-Box**), **utilizzo** (previsione, valutata con il **MAPE**, buono sotto il 12-15%).
53. ► **Che cos'è TRAMO-SEATS e perché l'ISTAT l'ha adottata?** — La procedura di **destagionalizzazione** adottata dall'ISTAT **nel 1997** (progetto **SARA**, con Banca d'Italia e mondo accademico) al posto di **X-11-ARIMA**, in linea con gli altri istituti europei ed **Eurostat**; applicata dal **comunicato sulla produzione industriale del febbraio 1999**. **TRAMO** pretratta la serie (giorni lavorativi, festività mobili, *outlier*) e identifica un ARIMA; **SEATS** estrae le componenti. È **model-based**: costruisce **un modello specifico per ogni serie**, e produce serie destagionalizzate **meno irregolari**.
54. ► **Perché si usano i dati panel?** — Perché **combinano la dimensione trasversale e quella temporale**, consentendo di distinguere **effetti del tempo da differenze fra individui** e, soprattutto, di **controllare l'eterogeneità individuale non osservata ma costante nel tempo**. Guadagno anche in **efficienza**, grazie al maggior numero di osservazioni.
55. ► **Effetti fissi o effetti casuali?** — **Effetti fissi**: gli effetti individuali si **eliminano** sottraendo la media temporale di ciascun soggetto (*within*); **sempre validi**, ma **non permettono di stimare variabili costanti nel tempo**. **Effetti casuali**: gli effetti individuali sono trattati come **parte dell'errore**; **più efficienti** e permettono le variabili costanti, ma richiedono che siano **incorrelati con i regressori**. È un *trade-off* fra **robustezza ed efficienza**.
56. **Che cos'è il test di Hausman?** — Verifica **l'incorrelazione fra effetti individuali e regressori**, confrontando lo stimatore **within** (sempre consistente) con quello **GLS** (consistente solo sotto H₀). **Se la differenza è significativa si scelgono gli effetti fissi**; altrimenti gli effetti casuali, più efficienti. Detto anche **Durbin-Wu-Hausman**.

## Valutazione delle politiche (Parte XVI)

57. ► **Che cos'è il metodo controfattuale?** — L'insieme delle tecniche statistiche che, sotto determinate ipotesi, **stimano ciò che sarebbe accaduto ai soggetti trattati se la politica non fosse stata attuata**. **Fattuale** = ciò che si osserva con il trattamento; **controfattuale** = ciò che si sarebbe osservato senza. **Il controfattuale non è mai osservabile**: da qui il problema fondamentale dell'inferenza causale.
58. ► **Che cos'è il modello di Rubin e che cos'è l'ATT?** — Il modello degli **esiti potenziali** (1974): per ogni unità esistono **due risultati potenziali**, uno con e uno senza trattamento, **e uno solo è osservabile**. L'**ATT** (*Average Treatment effect on Treated*) è l'effetto medio **sui soggetti effettivamente trattati** ed è **la grandezza che di norma si vuole stimare**.
59. ► **Quali sono le ipotesi del metodo controfattuale?** — **SUTVA** (assegnazione stabile e **assenza di interferenza fra unità**), **Common Support** (per ogni tipo di trattato deve esistere un non trattato confrontabile), **CIA/unconfoundedness** (a parità delle X osservate, l'assegnazione è come casuale). CIA + Common Support danno la ***strong ignorability***.
60. ► **Quali sono le principali strategie di valutazione e i loro limiti?** —
 - **RCT**: assegnazione casuale; **bilancia anche le variabili non osservabili**; è il metodo più affidabile, ma richiede tempo, risorse, **progettazione ex ante** e può scontrarsi con **vincoli etici e giuridici**;
 - **Statistical matching / propensity score** (Rosenbaum-Rubin 1983): ricostruisce a posteriori un gruppo di controllo; **bilancia solo le variabili osservabili**, e **non regge in presenza di autoselezione** su motivazione e abilità;
 - **DiD**: combina pre-post e trattati/non trattati; elimina sia dinamica spontanea sia selection bias **sotto l'assunto di parallelismo dei trend**; vulnerabile a **shock che colpiscano un solo gruppo**;
 - **RDD**: sfrutta una **soglia amministrativa**; ottima **validità interna**, ma **misura l'effetto solo vicino alla soglia** — debole **validità esterna** — e richiede che la variabile criterio **non sia manipolabile né usata per altri interventi** (esempio: **l'ISEE non va bene**).

---

# PARTE XIX — COLLEGAMENTI CON LE ALTRE MATERIE DEL BANDO

Una commissione apprezza molto quando il candidato **collega** invece di recitare. Ecco i ponti più solidi, pronti da usare.

**Con la valutazione delle politiche pubbliche.** È il collegamento più diretto: **il capitolo 16 è letteralmente la stessa materia**. Ma puoi arricchirlo mostrando che gli strumenti vengono da prima: **le variabili strumentali** (cap. 11) sono la base dell'RDD e di molti disegni quasi-sperimentali; **i dati panel a effetti fissi** (cap. 15) sono la forma generale del DiD; **la regressione multipla con dummy e interazioni** (cap. 9) è il modo in cui il DiD si stima in pratica; **logit e probit**, stimati per massima verosimiglianza (cap. 11), sono il modo in cui si stima il **propensity score**.

**Con la contabilità pubblica e la finanza pubblica.** La **previsione macroeconomica** che sta dietro al **DPFP** e alla manovra è econometria applicata: modelli a equazioni simultanee, serie storiche, moltiplicatori. Il **moltiplicatore** del capitolo 6 è esattamente la grandezza che si discute quando si valuta l'effetto di una manovra sul PIL. La **regola di spesa** del nuovo Patto di stabilità (Reg. UE 1263 e 1264/2024) si fonda su stime di **PIL potenziale** e di *output gap*, che sono stime econometriche con margini di incertezza rilevanti: è un punto critico che vale la pena saper nominare.

**Con la statistica economica e il diritto amministrativo — il SISTAN.** TRAMO-SEATS è un pezzo di **attività istituzionale dell'ISTAT**, disciplinata dal **D.Lgs. 322/1989** che istituisce il **Sistema statistico nazionale**. Qui econometria, statistica e diritto amministrativo si toccano: la produzione statistica ufficiale è **funzione pubblica**, soggetta al **segreto statistico (art. 9 D.Lgs. 322/1989)** e a obblighi europei di comparabilità.

**Con il data science e il data mining.** La **regressione lineare** è il primo algoritmo supervisionato; la **ridge regression** è il capostipite delle tecniche di **regolarizzazione** (LASSO, elastic net); il problema dell'**overfitting** è esattamente quello dell'R² che cresce sempre; la **previsione ex post** con separazione del campione è la **validazione *train/test***. La differenza di fondo da saper esprimere: **il data mining cerca la previsione migliore, l'econometria cerca il parametro causale** — per questo l'econometria si preoccupa tanto delle ipotesi e dell'endogeneità, mentre il machine learning si preoccupa dell'accuratezza fuori campione.

**Con l'economia politica.** La **funzione del consumo keynesiana** (cap. 6), la **Cobb-Douglas** e i rendimenti di scala (cap. 8), la **curva di Phillips** (cap. 8), l'**identificazione della domanda e dell'offerta** (cap. 13): sono tutti punti in cui la teoria economica fornisce le ipotesi che l'econometria mette alla prova. Il messaggio da trasmettere è che **l'econometria non sostituisce la teoria: la sottopone a verifica**.

**Con il diritto amministrativo — la motivazione del provvedimento.** Una valutazione d'impatto ben condotta è **istruttoria**: è il modo in cui un'amministrazione accerta i fatti su cui fonda una scelta. Il collegamento con l'**AIR** (analisi di impatto della regolamentazione) e la **VIR** (verifica di impatto della regolamentazione) è immediato, e mostra che il capitolo 16 non è un esercizio accademico ma **uno strumento previsto dall'ordinamento**.

---

# PARTE XX — COME PORTARE QUESTA MATERIA ALL'ORALE

**Tre cose da sapere prima di tutto il resto.** Se il tempo di studio è poco, concentralo su: **(1)** le sei ipotesi classiche e che cosa succede quando cadono; **(2)** come si legge un output di regressione (coefficienti, errori standard, t, R²); **(3)** l'intero capitolo 16, che per il tuo bando vale doppio.

**La struttura di risposta che funziona sempre.** Per qualunque tecnica: *«Serve a risolvere questo problema → funziona così → richiede queste ipotesi → ha questo limite»*. Quattro passaggi, trenta secondi ciascuno. Chiudere sul limite è ciò che distingue il candidato che ha capito.

**Non dire mai «non ricordo la formula».** Di' che cosa fa. Nessuna commissione RIPAM chiede derivazioni; tutte apprezzano chi sa spiegare perché un indice è costruito in quel modo.

**Le tre frasi che fanno sempre buona impressione**, e che puoi inserire quasi ovunque:

1. *«Gli stimatori OLS restano corretti, ma perdono efficienza e soprattutto gli errori standard diventano inattendibili: è per questo che il problema non si vede guardando i coefficienti, si vede guardando i test.»*
2. *«Significatività statistica e rilevanza sostanziale sono due cose diverse: con un campione grande qualunque differenza diventa significativa.»*
3. *«Il controfattuale non è osservabile per definizione: tutta la valutazione d'impatto consiste nel costruirne una stima credibile, e ogni metodo lo fa a prezzo di un'ipotesi diversa.»*

**Se ti chiedono qualcosa che non sai.** Riconducilo a quello che sai. Quasi tutto in econometria è una variazione su tre temi: *che cosa stiamo stimando*, *sotto quali ipotesi la stima è valida*, *che cosa succede se l'ipotesi cade*. Dirlo esplicitamente — *«non conosco quella tecnica nello specifico, ma il problema che affronta è verosimilmente questo…»* — è una risposta onesta e intelligente, molto meglio di un silenzio o di un'invenzione.

**Infine, il tono.** L'econometria in un concorso per funzionari non è una materia da matematici: è **il linguaggio con cui un'amministrazione dimostra che una politica funziona**. Se la racconti così — con esempi di politiche, soglie, incentivi, valutazioni — passerà il messaggio che sai a che cosa serve, che è esattamente quello che una commissione RIPAM vuole sapere.

---

*Dispensa elaborata sul manuale Simone — Parte III «Econometria e metodi qualitativi e quantitativi», capitoli 1-16 (pp. 261-571), letto integralmente. Le formule sono state deliberatamente raccolte nella Parte XVII invece di essere disseminate nel testo, secondo l'impostazione concordata. Aggiornata al 14 settembre 2026.*
