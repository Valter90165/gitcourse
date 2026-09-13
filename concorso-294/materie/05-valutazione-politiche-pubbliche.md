# 5. Metodi qualitativi e quantitativi per l'analisi e la valutazione delle politiche pubbliche

> **Materia nucleo — la più importante del concorso.** È letteralmente il mestiere
> descritto nel bando. Se hai tempo limitato, questo file viene prima di tutti.

## Programma di riferimento

### Impianto concettuale
- Il ciclo di vita di una politica pubblica: agenda setting, formulazione,
  decisione, attuazione, valutazione
- **Teoria del programma** e *logic model*: input → attività → output → risultati
  → impatti
- Distinzione fondamentale: **monitoraggio ≠ valutazione**
- Tipi di valutazione: *ex ante*, *in itinere*, *ex post*; di processo, di
  implementazione, di impatto
- Domande valutative: rilevanza, efficacia, efficienza, sostenibilità, coerenza,
  valore aggiunto (criteri OCSE-DAC)

### Valutazione d'impatto controfattuale
- Il **problema fondamentale dell'inferenza causale**; potential outcomes
- Gruppo dei trattati e gruppo di controllo; distorsione da selezione
- **Randomized Controlled Trial (RCT)**: logica, punti di forza, limiti etici e
  pratici nella PA
- **Differenze-nelle-differenze (DID)**: assunzione dei trend paralleli
- **Regression Discontinuity Design (RDD)**: soglie amministrative, validità locale
- **Propensity Score Matching (PSM)**: selezione su osservabili, supporto comune
- **Variabili strumentali** in contesto valutativo; effetto locale (LATE)
- **Controllo sintetico** per politiche che riguardano una singola unità (una
  regione, un comune)
- Validità interna e validità esterna; trasferibilità dei risultati

### Metodi qualitativi
- Studio di caso; interviste in profondità; focus group; osservazione
- Analisi documentale e analisi del contenuto
- *Theory-based evaluation*, *realist evaluation* ("cosa funziona, per chi, in
  quali circostanze"), *contribution analysis*
- Process tracing; analisi degli stakeholder
- **Metodi misti** (*mixed methods*): triangolazione, sequenzialità, complementarità

### Analisi economica
- Analisi **costi-benefici**: attualizzazione, tasso di sconto sociale, VAN
- Analisi **costo-efficacia** e costo-utilità
- **Spending review / revisione della spesa**: logica, metodologia, esperienza
  italiana
- Valutazione d'impatto della regolamentazione (**AIR**) e verifica d'impatto
  (**VIR**)

## Domande d'orale probabili

1. **Cosa distingue il monitoraggio dalla valutazione di una politica pubblica?**
2. Illustri il problema fondamentale dell'inferenza causale. Perché non basta
   confrontare i partecipanti a un programma prima e dopo?
3. Perché il confronto tra chi ha aderito a una misura e chi non ha aderito è
   tipicamente distorto? Faccia un esempio.
4. Descriva il metodo delle differenze-nelle-differenze. **Qual è l'assunzione
   cruciale e come si può corroborarla empiricamente?** (test sui trend pre-trattamento)
5. Quando è applicabile un disegno di regressione discontinua? Che tipo di effetto
   identifica e con quale limite di generalizzabilità?
6. Cos'è il propensity score matching? Su quale assunzione forte si regge e perché
   è più fragile di un RDD?
7. Un RCT è sempre la soluzione migliore? Quali ostacoli incontra nella valutazione
   di politiche pubbliche reali?
8. Cosa aggiunge un metodo qualitativo a una valutazione d'impatto quantitativa?
   Faccia un esempio in cui la sola stima dell'effetto sarebbe insufficiente.
9. Differenza tra analisi costi-benefici e analisi costo-efficacia: quando si usa
   l'una e quando l'altra?
10. Cosa si intende per revisione della spesa? In che modo la valutazione delle
    politiche può alimentarla?
11. Differenza tra AIR e VIR.
12. Validità interna e validità esterna: una valutazione può essere solida e
    comunque inutile per il decisore? Argomenti.

## La domanda di sintesi — allenala espressamente

Prepara una risposta strutturata di 4-5 minuti a una domanda di questo tipo:

> *"Il Governo introduce un credito d'imposta per le assunzioni nel Mezzogiorno.
> Come imposterebbe la valutazione della misura?"*

Traccia per rispondere bene:

1. **Domanda valutativa e teoria del cambiamento** — cosa dovrebbe succedere e
   attraverso quale meccanismo; distinguere output (imprese che usano il credito)
   da risultato (assunzioni aggiuntive) da impatto (occupazione netta).
2. **Il rischio principale**: l'effetto di sostituzione e il *deadweight* —
   assunzioni che ci sarebbero state comunque. È il punto che dimostra maturità.
3. **Disegno identificativo**: esiste una soglia (dimensionale, territoriale,
   temporale)? Allora RDD o DID su imprese ammissibili vs non ammissibili.
   Dichiarare l'assunzione e come la si verifica.
4. **Dati**: archivi amministrativi (comunicazioni obbligatorie, dichiarazioni
   fiscali, registro imprese), linkage, periodo pre e post.
5. **Integrazione qualitativa**: interviste a imprese per capire *perché* il
   meccanismo ha o non ha funzionato.
6. **Ritorno alla decisione**: costo per occupato aggiuntivo, confronto con misure
   alternative, implicazioni per la revisione della spesa.

Chi risponde solo con il punto 3 prende un voto medio. Chi apre col punto 1 e
chiude col punto 6 dimostra di saper fare il lavoro.

## Sintesi — dispensa "Valutazione d'impatto (o degli effetti) e paradigma controfattuale"

> Fonte: Simone, collana `349/3 — Concorso RIPAM 294 posti`. Materiale scritto per
> questo concorso: il taglio è quello che ti aspetta all'orale. **Copre i metodi
> quantitativi; i metodi qualitativi non ci sono** (vedi `materiali/INVENTARIO.md`).

### L'impianto in quattro passi

**1. La domanda.** Pensare la politica come una *terapia* per un problema
collettivo: la cura ha sortito effetto? Ha modificato le condizioni su cui
intendeva incidere, e ha prodotto altri cambiamenti? La valutazione d'impatto
produce un'evidenza — in linea di massima quantitativa — su *se* e *in che misura*
la politica ha prodotto mutamenti.

**2. La variabile risultato (Y).** L'obiettivo di una politica è formulato in
termini generali; per stimarne l'impatto va *circoscritto* in una o più grandezze
osservabili e misurabili che lo rappresentino.

| Intervento | Obiettivo | Variabili risultato Y |
|---|---|---|
| Corsi di formazione professionale | Favorire l'occupazione giovanile | % avviati al lavoro, % occupati, tempo di attesa, reddito medio |
| Norme sulla sicurezza sul lavoro | Ridurre i rischi | Tasso d'infortuni, totale giorni di prognosi |
| Assistenza domiciliare agli anziani | Supportare i dimessi dall'ospedale | Tasso di riospedalizzazione, tasso di mortalità |

**3. La variabile trattamento (T).** Risponde a "di cosa si vuole stimare
l'effetto?": è la regola che distingue esposizione e non esposizione. Di norma
dicotomica (0/1), ma può essere continua (es. *ammontare* del credito ricevuto,
non solo accesso al credito). Attenzione: la scelta non è scontata — una politica
può constare di più trattamenti in tempi diversi, e la stessa politica può essere
letta da punti di vista diversi identificando i trattati in modo dissimile.

**4. Il paradigma controfattuale.** L'effetto è l'influenza di T su Y, definita
come confronto tra:
- **situazione fattuale** — Y osservato dopo l'esposizione (T = 1);
- **situazione controfattuale** — Y che si sarebbe osservato senza esposizione (T = 0).

L'effetto medio è la differenza tra il valore medio di Y osservato dopo il
trattamento e il valore medio di Y che si sarebbe osservato in assenza di esso.

### Il punto cruciale — da dire esattamente così

Un soggetto **può essere esposto o non esposto, non entrambi contemporaneamente**.
Da qui l'impossibilità di osservare direttamente una delle due condizioni: poiché
l'effetto d'interesse è quello sui trattati, la condizione non osservabile è quella
che i trattati avrebbero mostrato in assenza di trattamento.

> Valutare gli effetti significa quindi **osservare la condizione dei trattati e
> confrontarla con una stima credibile di quella in cui sarebbero stati senza
> trattamento.** Tutto il resto della materia è: come si costruisce quella stima.

### I due approcci di base

La scelta dipende dal tipo di politica, dalle condizioni di lavoro e dai dati
disponibili.

**Control group design** — il controfattuale è stimato dal valore medio di Y in un
gruppo di soggetti non trattati.
*Limite della versione ingenua*: una semplice differenza tra trattati e non trattati
raramente è credibile, perché i due gruppi possono differire già prima del
trattamento. L'errore che ne deriva è la **distorsione da selezione** (*selection bias*).

**Pre-post design** — il controfattuale è stimato dal valore di Y osservato sugli
stessi trattati prima della politica.
*Limite della versione ingenua*: Y può variare nel tempo spontaneamente, in modo
indipendente dalla politica; il valore precedente non è quindi necessariamente una
buona stima del controfattuale.

Entrambe le intuizioni, però, fondano metodi più raffinati:

| Metodo | Approccio | Come stima il controfattuale | Assunzione / limite |
|---|---|---|---|
| **Valutazione sperimentale (RCT)** | Control group | Gruppo di controllo per **sorteggio** → caratteristiche iniziali equivalenti | Il più solido in assoluto. Costoso, gestionalmente impegnativo, osteggiato per ragioni etiche, politiche e legali. Usato soprattutto negli **interventi pilota**. Con *partial compliance* la stima va corretta: consistente ma meno interpretabile |
| **Cross-section con regressione multivariata** | Control group | Modello di regressione con T più **variabili di controllo** per le differenze iniziali | Corretta **solo** se i controlli spiegano *tutte* le differenze iniziali → ipotesi di **selezione sulle osservabili**. La qualità dipende dalla ricchezza dei controlli |
| **Matching statistico** | Control group | Abbina ogni trattato a uno o più controlli con caratteristiche iniziali simili, tramite una misura di distanza; ricostruisce un gruppo di controllo di pari composizione | Stessa ipotesi di **selezione sulle osservabili** |
| **Synthetic control** | Control group | Il controfattuale di **una** unità trattata è una **media pesata** dei controlli; i pesi si derivano in fase preliminare su caratteristiche iniziali *e* osservazioni passate di Y | Per politiche su singola unità (una regione, un comune) |
| **Regression discontinuity design** | Control group | Si applica quando la regola di selezione è **nota** e assimilabile a una **graduatoria**: confronta chi gravita attorno alla soglia | Vicino alla soglia l'assegnazione è quasi casuale. Effetto valido per soggetti simili a quelli intorno alla soglia: **generalizzabile solo sotto condizioni**. Con assegnazione imperfetta si corregge via variabili strumentali |
| **Variabili strumentali** | Trasversale | Non è una strategia a sé: sfrutta un meccanismo di assegnazione anche solo parzialmente assimilabile al caso | Z deve incidere sulla probabilità di esposizione **ma non gravare direttamente su Y**. Stime consistenti, interpretabilità spesso limitata |
| **Serie storiche interrotte** | Pre-post | Analizza l'andamento passato di Y per **prevedere** quale sarebbe stato senza intervento | Richiede una serie storica adeguata |
| **Difference in differences** | **Combina i due** | Confronta l'**evoluzione nel tempo** di un gruppo esposto e uno non esposto, prima e dopo | Assume che in assenza d'intervento **le differenze tra i gruppi sarebbero rimaste costanti**. Adottabile a integrazione degli altri metodi |

### Esempi di variabile strumentale (dalla dispensa)

- l'assegnazione casuale all'intervento, anche con *partial compliance*;
- il punteggio delle unità intorno alla soglia di una graduatoria, anche con
  assegnazione imperfetta;
- qualsiasi variabile che incida sulla probabilità di esposizione ma non su Y.

### Come ricordarla all'orale

Tre famiglie, non otto metodi sparsi:

1. **Confronto con altri** (control group) — e il problema è il *selection bias*;
2. **Confronto con il proprio passato** (pre-post) — e il problema è la *dinamica
   spontanea di Y*;
3. **DID**, che combina le due e proprio per questo neutralizza entrambi i problemi
   — a prezzo dell'assunzione sui trend.

Dentro la famiglia 1, i metodi si ordinano per **quanto poco chiedono di credere**:
RCT (nulla, l'equivalenza è costruita) → RDD (quasi-casualità locale alla soglia) →
matching e regressione (selezione sulle osservabili, l'assunzione più forte e la
più contestabile). Saper dire *questa gerarchia* vale più che elencare i metodi.

## Da integrare — non c'è nella dispensa

Vedi `materiali/INVENTARIO.md`: metodi qualitativi, teoria del programma, ciclo di
policy, monitoraggio vs valutazione, ex ante/in itinere/ex post, criteri OCSE-DAC,
costi-benefici e costo-efficacia, AIR/VIR, revisione della spesa, validità interna
ed esterna.

## Punti su cui ho esitato
