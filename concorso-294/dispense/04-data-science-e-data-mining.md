# Data science e data mining

## Sintesi ragionata per la prova orale

*Concorso RIPAM 294 unità — Codice 02, Area dei funzionari — prova orale del 27 novembre 2026*

Questa dispensa nasce dalla scheda **«Elementi di data science e data mining»** (Simone, edizione RIPAM 294) caricata su Drive, letta integralmente. La scheda è però **breve — sei pagine** — e copre soltanto l'impianto metodologico: definizioni, processo KDD, modello CRISP-DM. Per una prova orale su una materia del bando questo non basta: la commissione, davanti a un candidato dell'area dei funzionari, chiede quasi sempre **che cosa fa concretamente un algoritmo, come si valuta se funziona, e che cosa cambia quando i dati sono quelli di una pubblica amministrazione**.

Ho quindi costruito la dispensa su **due livelli, e li tengo visivamente distinti**:

- le **Parti I-III** sono la scheda, riportata integralmente e resa discorsiva: è il nucleo che devi conoscere alla lettera perché è il materiale ufficiale del concorso;
- le **Parti IV-X** sono **integrazione mia**, necessaria e segnalata come tale: i dati e la loro qualità, il pre-processing in dettaglio, la tassonomia del machine learning, gli algoritmi fondamentali, le metriche di valutazione, e soprattutto il **capitolo su dati e algoritmi nella P.A. italiana**, che è quello in cui un funzionario RIPAM deve saper parlare meglio di un informatico.

> **Sul livello di formalizzazione.** Ho applicato qui la stessa regola che mi hai dato per econometria e statistica: **niente derivazioni, niente dimostrazioni**. Le poche formule presenti sono raccolte in un riquadro alla fine (**«Le dieci formule che vale la pena sapere»**) e sono tutte del tipo che si scrive in tre secondi alla lavagna: le metriche di classificazione, l'errore quadratico medio, la distanza euclidea. Valuta tu quali memorizzare: nessuna di esse è indispensabile per rispondere bene, tutte e dieci insieme fanno una risposta eccellente.

---

# Parte I — Che cos'è la data science

## 1. La definizione

La **data science** è una **disciplina trasversale a molteplici settori**, che integra **statistica, programmazione, machine learning e conoscenze di dominio** per trasformare **dati grezzi in informazioni utili**. Supporta i processi decisionali, anche **predittivi**, attraverso l'analisi di dataset complessi — tabelle SQL strutturate, ma anche testi e immagini non strutturati. Identificando **pattern nascosti**, automatizza e ottimizza l'intero processo di analisi per estrarre informazioni immediatamente utilizzabili.

Conviene fermarsi sui **quattro ingredienti**, perché la definizione regge o cade su di essi:

| Ingrediente | Che cosa porta |
|---|---|
| **Statistica** | il rigore inferenziale: sapere quando un pattern è reale e quando è rumore |
| **Programmazione** | la capacità operativa: manipolare volumi che nessun foglio di calcolo regge |
| **Machine learning** | la capacità predittiva: imparare dai dati una regola non scritta a priori |
| **Conoscenza di dominio** | il senso: sapere quali domande valga la pena porre e quali risposte siano plausibili |

> **La frase da dire all'orale.** «La data science non è statistica con il computer, né informatica applicata ai numeri: è la disciplina che **tiene insieme il rigore statistico, la potenza computazionale e la conoscenza del dominio** per trasformare dati grezzi in decisioni. Il quarto ingrediente — la conoscenza di dominio — è quello che più spesso viene dimenticato ed è quello che distingue un'analisi utile da un'analisi formalmente corretta ma priva di senso.»

## 2. Un po' di storia

La scheda ricostruisce una cronologia precisa, e vale la pena saperla raccontare perché mostra che la materia ha una genealogia e non è nata con ChatGPT.

- **Anni '60 — John Tukey** descrive l'**analisi dei dati come campo autonomo**, distinto dalla statistica tradizionale, enfatizzando l'**esplorazione empirica** su grandi dataset;
- **1974 — Peter Naur** propone formalmente il termine *data science*, come evoluzione della **«datalogy»**, per integrare informatica e analisi dei dati;
- **anni '80** — l'esplosione dei **database relazionali** e i primi sistemi computazionali potenti introducono il **Knowledge Discovery in Databases (KDD)** e il **data mining**, **formalizzati nel 1996 da Fayyad**: sono le basi pratiche della data science moderna;
- **1990-2000** — il termine si consolida in ambito informatico; nel **2001 William S. Cleveland** pubblica ***«Data Science: An Action Plan»***, proponendola come **espansione della statistica** verso machine learning e deep learning;
- **dopo il 2010** — il vero *boom*, con **big data, cloud computing e social media** che generano volumi esponenziali di dati. Oggi la disciplina integra statistica, intelligenza artificiale, machine learning e deep learning.

> **Il punto che rende interessante la cronologia.** Tukey nel 1960 e Cleveland nel 2001 dicono, a quarant'anni di distanza, la stessa cosa: **la statistica accademica è troppo stretta per i dati che abbiamo**. La data science non nasce dall'informatica che invade la statistica, nasce **dalla statistica che chiede di allargarsi**. Dirlo all'orale è un modo elegante di mostrare che hai capito la materia e non solo la scheda.

## 3. Data science, data mining e KDD a confronto

Sono concetti **correlati ma distinti**, e confonderli è l'errore più frequente.

- la **data science** è un **campo ampio e moderno**: copre l'**intero ciclo di vita dei dati**, dalla definizione degli obiettivi aziendali allo sviluppo e monitoraggio continuo delle soluzioni. Si concentra su **previsioni precise, automazioni intelligenti e comunicazione efficace dei risultati**, per generare valore concreto;
- il **KDD** è un **processo specifico e tecnico**, iterativo, finalizzato all'**estrazione di conoscenza da database strutturati** attraverso fasi precise;
- il **data mining** è la **fase centrale del KDD**: attraverso l'applicazione di algoritmi specifici consente di individuare **pattern o relazioni nascoste** nei dati.

La data science **integra il KDD come struttura metodologica** nel proprio flusso di lavoro, con il data mining come elemento chiave — **circa il 20% del tempo totale** — contestualizzandolo in soluzioni complete che includono obiettivi aziendali, implementazione pratica e iterazioni continue.

> **Il dato del 20% è una gemma da usare all'orale.** Significa che **quattro quinti del lavoro di un data scientist non sono l'algoritmo**: sono capire il problema, procurarsi i dati, pulirli, e poi validare e comunicare i risultati. È esattamente il contrario dell'immagine popolare della disciplina, ed è la cosa che un'amministrazione deve sapere prima di avviare un progetto: **se il budget prevede solo il modello, il progetto fallirà**.

**Lo schema delle inclusioni**, che conviene saper disegnare:

> **Intelligenza artificiale** ⊃ **Machine learning** ⊃ **Deep learning**
> **Data science** ⊃ **KDD** ⊃ **Data mining** (→ che *usa* algoritmi di machine learning)

Non sono due gerarchie separate: si intersecano. Il **data mining** è il punto in cui il processo KDD **attinge** alla cassetta degli attrezzi del machine learning; la **data science** è il contenitore più ampio, perché aggiunge ciò che né il KDD né il ML contengono — **gli obiettivi, il valore, la messa in produzione e la comunicazione**.

---

# Parte II — Il processo KDD

## 4. La struttura

Il processo KDD si articola in **cinque fasi interconnesse e iterabili**, progettate per convertire dati grezzi in **conoscenza concreta e immediatamente applicabile**. Attraverso un approccio **sistematico ma non lineare**, integra **feedback continui** che permettono raffinamenti progressivi, garantendo una **pulizia graduale dei dati** e la scoperta di risultati affidabili, pronti per l'uso diretto in contesti operativi reali.

> **Sottolinea sempre l'iteratività.** Il KDD non è una catena di montaggio: è un ciclo in cui ogni fase può rimandare alle precedenti. Chi lo descrive come una sequenza lineare mostra di averlo letto ma non praticato.

## 5. Le cinque fasi

### 5.1 Selezione dei dati

Prevede l'**identificazione e l'estrazione selettiva** dei dati da fonti diversificate. Si selezionano **attributi rilevanti** e **campioni rappresentativi** mediante **query strutturate** o **campionamento probabilistico**, in coerenza con gli obiettivi prefissati, **minimizzando bias** e ottimizzando le analisi successive.

> **Il rischio nascosto.** È qui che si annidano i *selection bias*: se il campione non è rappresentativo, nessun algoritmo successivo potrà rimediare. È il motivo per cui la scheda insiste sul **campionamento probabilistico** — l'unico che consente di quantificare l'errore.

### 5.2 Pulizia e integrazione (*preprocessing*)

Si agisce sulla **qualità dei dati grezzi**, che spesso risultano imperfetti, per renderli uniformi e adatti alle fasi successive. Quattro operazioni:

- **rimozione degli outlier**: identificare e rimuovere **valori anomali estremi** che distorcono l'analisi;
- **riempimento dei dati mancanti**: sostituire i valori mancanti per completare il dataset, usando **media o mediana** per i casi semplici, oppure **algoritmi di machine learning come il k-nearest neighbors** per preservare relazioni complesse che le medie globali cancellerebbero;
- **eliminazione dei duplicati**: trovare e cancellare righe identiche, evitando **ridondanze che gonfiano i dati** e causano risultati sbilanciati;
- **integrazione da fonti diverse**: combinare informazioni da origini multiple (database aziendali, registri operativi, file esterni) in un **unico dataset uniforme**.

> **La distinzione che fa la differenza sull'imputazione.** Riempire un valore mancante con la **media** è semplice ma **distrugge la struttura di correlazione**: tutti i valori mancanti diventano identici, e la varianza si riduce artificialmente. Il **k-NN** guarda invece i «vicini» di quel record e imputa un valore coerente con essi, **preservando le relazioni fra variabili**. È esattamente la ragione che la scheda dà, ed è una risposta che colpisce perché mostra che hai capito *perché* la tecnica sofisticata esiste.

### 5.3 Trasformazione dei dati

Si adatta il dataset alle **specifiche degli algoritmi**, attraverso:

- **normalizzazione** (scale **Min-Max** o **Z-score**);
- **creazione di variabili derivate** (***feature engineering***);
- **discretizzazione** (suddivisione dei dati in intervalli);
- **riduzione dimensionale** (metodi come la **PCA**).

Tali interventi **semplificano i dati e li rendono più veloci da elaborare**, preparandoli per le fasi successive.

### 5.4 Data mining

È la **fase centrale**: applicazione di algoritmi avanzati — **supervisionati e non supervisionati** — per identificare pattern nascosti. Le tecniche principali indicate dalla scheda:

| Tecnica | Che cosa fa |
|---|---|
| **Clustering** | raggruppa dati simili, rappresentandoli in gruppi, attraverso algoritmi come il **K-Means** |
| **Classificazione** | assegna automaticamente i dati a **categorie predefinite**, sulla base delle loro caratteristiche |
| **Regressione** | stima **valori numerici** futuri o mancanti, attraverso relazioni matematiche fra variabili |
| **Sintesi** | crea **descrizioni compatte** dei dati, attraverso regole riassuntive o viste multidimensionali |
| **Modellazione delle dipendenze** | scopre **relazioni significative fra variabili** (es. reti bayesiane per probabilità condizionali) |
| **Rilevamento anomalie** | identifica **cambiamenti significativi o deviazioni** rispetto a valori storici o standard |

> **La linea di faglia da tenere a mente:** *clustering* e *rilevamento anomalie* sono **non supervisionati** (nessuna etichetta nota in partenza); *classificazione* e *regressione* sono **supervisionati** (si impara da esempi già etichettati). È la distinzione più probabile in assoluto in una domanda d'orale su questa materia.

### 5.5 Valutazione e presentazione dei pattern

Fase conclusiva: si **valida l'affidabilità dei risultati** emersi, impiegando **metriche quantitative** — accuratezza, precisione/richiamo e **F1-score** per dataset sbilanciati, **coefficiente di silhouette** per i raggruppamenti — integrate da **test statistici (p-value)**. I risultati vengono poi **confrontati con la conoscenza di un esperto del dominio** per verificarne l'utilità pratica.

> **Non saltare l'ultimo passaggio.** La validazione **non è solo statistica**: la scheda è esplicita nel richiedere il confronto con l'**esperto di dominio**. Un pattern statisticamente significativo ma privo di senso sostantivo è un artefatto, non una scoperta. In una pubblica amministrazione questo si traduce in una regola operativa: **nessun modello va in produzione senza la validazione dell'ufficio che conosce il fenomeno**.

## 6. I sei passi operativi del data mining

Il data mining è la **quarta fase** del KDD: i dati, già puliti e trasformati, vengono analizzati per far emergere relazioni e schemi nascosti che l'occhio umano non coglierebbe. È il **momento operativo vero e proprio**, in cui gli algoritmi «scavano» (*mining*) nel dataset per estrarre **conoscenza grezza**: i risultati **non sono ancora pronti per l'uso pratico** — richiedono la fase finale di valutazione — ma costituiscono il cuore dell'intero flusso.

**1. Preparazione del dataset.** Si scinde il dataset in due insiemi complementari: il ***training set***, di norma **circa l'80%** dei dati, dedicato all'apprendimento dei modelli; il ***test set***, circa il **20%**, utilizzato per **valutazioni indipendenti**. Per la suddivisione si adottano tecniche come lo ***stratified sampling***, che **preserva le proporzioni delle classi** nei due insiemi, oppure lo ***split temporale*** per dati cronologici. Questo approccio **previene l'overfitting** e garantisce una rappresentazione fedele della popolazione.

> **Perché lo split temporale per i dati cronologici.** Se i dati hanno un ordine nel tempo, mescolarli a caso significa **addestrare il modello sul futuro per prevedere il passato**: una perdita di informazione dal futuro (*data leakage*) che gonfia artificialmente le prestazioni e crolla in produzione. È un errore comunissimo e citarlo fa un'ottima impressione.

**2. Selezione degli algoritmi.** Si valutano e scelgono categorie appropriate al contesto: **clustering** per raggruppamenti naturali, **classificazione** per analisi categorica, **regressione** per stime quantitative, **algoritmi di associazione** per estrarre regole di co-occorrenza. **Si confrontano più algoritmi** per selezionare quello più adatto all'obiettivo specifico.

**3. Addestramento dei modelli.** Gli algoritmi elaborano ripetutamente i dati del training set attraverso tecniche di **ottimizzazione progressive**, combinando diversi approcci (**metodi *ensemble***) per aumentare affidabilità e precisione.

**4. Validazione incrociata.** I modelli vengono testati sistematicamente su **diverse porzioni del dataset**, suddividendo i dati in **sottogruppi multipli** per valutare ripetutamente la capacità di **generalizzare su dati non visti**. Il processo identifica vulnerabilità come l'**overfitting**.

**5. Ottimizzazione dei parametri.** Si regolano finemente le **configurazioni chiave** degli algoritmi tramite ricerche sistematiche o esplorative, confrontando varianti multiple per identificare la configurazione ottimale (*hyperparameter tuning*).

**6. Generazione dei pattern.** I risultati preliminari vengono trasformati in **strutture interpretabili**, attraverso analisi di qualità e **prioritizzazione delle variabili più influenti**, preparando *output* pronti per la validazione finale del KDD.

---

# Parte III — Il modello CRISP-DM

## 7. Origine e attualità

Il **CRISP-DM (1996)** — *CRoss-Industry Standard Process for Data Mining* — è nato per **standardizzare il data mining**, ma si è evoluto in un **framework fondamentale per la data science, il machine learning e l'analisi avanzata dei dati**. Le sue **sei fasi cicliche** offrono una struttura robusta adattabile a qualsiasi progetto orientato all'analisi dei dati.

La data science moderna **integra il CRISP-DM originale** — pensato per l'informatica degli anni '90 — con soluzioni e tecnologie contemporanee:

- **cloud computing**: piattaforme come **AWS, Azure o GCP** per gestire big data e *training* distribuiti, impossibili con l'hardware dell'epoca;
- **machine learning**: automatizza **implementazione, monitoraggio e riaddestramento** dei modelli, rendendo i progetti pronti per la produzione (è ciò che oggi si chiama **MLOps**);
- **metodologie agili**: sostituiscono il ciclo rigido con **sprint iterativi e feedback continui**, tipici dell'approccio **DevOps**.

## 8. Il flusso e la decisione chiave

Il diagramma ufficiale mostra un flusso con **frecce bidirezionali fra tutte le fasi consecutive**, che riflettono l'**iteratività non lineare** del processo:

1. si parte dalla **Comprensione del Business** per definire obiettivi e requisiti;
2. si passa alla **Comprensione dei Dati** per esplorare il dataset iniziale;
3. poi alla **Preparazione dei Dati** per pulire e trasformare i dati grezzi;
4. si procede con la **Modellazione** per sviluppare gli algoritmi;
5. e con la **Valutazione** per confrontare i risultati **contro i KPI aziendali**.

**In questa fase va presa una decisione chiave**: se il modello raggiunge gli obiettivi prefissati si procede con l'**Implementazione**; in caso contrario **si torna principalmente alla Comprensione del Business**, per rivedere i requisiti iniziali. Dopo un'implementazione riuscita, **nuovi insight dal modello in produzione riavviano il ciclo** dalla Comprensione del Business.

> **La freccia che sorprende, e che vale la pena commentare.** Quando un modello non funziona, l'istinto è tornare alla *modellazione* — cambiare algoritmo. Il CRISP-DM dice l'opposto: si torna alla **comprensione del business**. Perché il fallimento di un modello, nove volte su dieci, non è un problema tecnico: è il segno che **si è risposto alla domanda sbagliata**. Questa struttura adattiva gestisce incertezze e feedback continui, riducendo i rischi e rendendo il CRISP-DM ideale per progetti scalabili.

## 9. Le sei fasi in dettaglio

**1. Comprensione del Business.** Definisce gli **obiettivi strategici**, traducendoli in **problemi di analisi dati specifici e misurabili**. Si identificano le **risorse disponibili** (dati, competenze, budget), i **vincoli legali e organizzativi** e i **criteri di successo** (miglioramenti misurabili nei processi). Risultato concreto: il **piano di progetto**, che **delimita il perimetro** per evitare che il progetto si espanda troppo, con richieste extra che farebbero lievitare costi e tempi (*scope creep*).

**2. Comprensione dei Dati.** Partendo dagli obiettivi definiti, si raccolgono i **dati iniziali** e si procede con un'**analisi esplorativa (EDA — *Exploratory Data Analysis*)** per studiarne qualità e caratteristiche. Si identificano problemi comuni — **valori incompleti, outlier, squilibri nelle classi, dati ridondanti** — producendo un **report con le osservazioni chiave** e un **tracciato del flusso dati**.

**3. Preparazione dei dati.** È la **fase più impegnativa** del CRISP-DM: trasforma dati grezzi e imperfetti in **dataset affidabili e pronti per la modellazione**, attraverso tre macro-attività interconnesse:

- **pulizia**: rimozione dei duplicati, trattamento dei valori mancanti, gestione degli outlier;
- **integrazione**: unione di dati da fonti diverse per creare una **visione completa**, utile ad analisi *cross*-dominio che nessun singolo dataset potrebbe fornire;
- **trasformazione**: **standardizzazione** tramite normalizzazione, **feature engineering**, **selezione degli attributi rilevanti** eliminando ridondanze, **bilanciamento delle classi** e ottimizzazione per gli algoritmi.

**4. Modellazione.** I dati preparati vengono analizzati con **algoritmi specifici** per identificare pattern nascosti e relazioni significative nei dati storici, producendo un **modello ottimizzato**, completo di **analisi delle variabili principali** e **metriche di performance**.

**5. Valutazione.** Prima della produzione è fondamentale **verificare che il modello raggiunga davvero gli obiettivi aziendali** definiti all'inizio. **Non basta controllare i numeri tecnici**: serve capire se risolve i problemi di business individuati nella prima fase e se **tutte le fasi precedenti sono state eseguite correttamente**, individuando eventuali aspetti trascurati. Se i risultati non convincono, si torna indietro per miglioramenti mirati.

**6. Implementazione (*deployment*).** Si integra il modello nei **processi operativi**, con **monitoraggio continuo** per rilevare cambiamenti nei dati e pianificare aggiornamenti. Include **documentazione, formazione del team e gestione del cambiamento organizzativo**.

> **L'ultima fase è quella che le amministrazioni sottovalutano di più.** «Implementazione» non significa consegnare un file: significa **inserire il modello in un processo, formare chi lo userà, e monitorarlo**. I dati cambiano (è il fenomeno del ***data drift***), e un modello non monitorato si degrada silenziosamente. Se la commissione ti chiede quale sia il rischio principale di un progetto di data science nella P.A., questa è la risposta migliore: **non che il modello sbagli, ma che nessuno se ne accorga**.

## 10. Data science, CRISP-DM e KDD: il confronto finale

La data science **integra sia il KDD sia il CRISP-DM**, estendendo entrambi verso applicazioni che generano **valore concreto** attraverso analisi predittive e automazioni.

| | **KDD** | **CRISP-DM** |
|---|---|---|
| **Natura** | framework **accademico** generale per la scoperta della conoscenza nei dati | **standard industriale pratico** orientato al business |
| **Fasi** | **5**, con enfasi tecnica sul ciclo di estrazione della conoscenza | **6**, strategiche |
| **Punto di forza** | **granularità tecnica** | **completezza pratica**: gestione manageriale, iteratività strutturata, implementazione produttiva, stakeholder eterogenei |

La data science utilizza il **KDD per i fondamenti teorici** e il **CRISP-DM come metodologia operativa preferita** in contesti industriali, **mappando la fase «Data Mining» del KDD sulla fase «Modellazione» del CRISP-DM**.

> **La risposta completa, in una frase:** «KDD e CRISP-DM non sono alternativi: sono lo **stesso processo visto da due punti di vista**. Il KDD lo guarda dal dato — e infatti la sua fase centrale si chiama *data mining*; il CRISP-DM lo guarda dall'organizzazione — e infatti comincia e ricomincia dalla *comprensione del business*. La corrispondenza puntuale è fra il *data mining* del KDD e la *modellazione* del CRISP-DM.»

---

> **Da qui in avanti: integrazione.** Le Parti IV-X non sono nella scheda. Le ho scritte perché senza di esse la materia del bando resterebbe coperta solo per metà: la scheda spiega **come si organizza** un progetto di analisi dei dati, ma non **che cosa si fa dentro la scatola**. Sono le parti su cui una commissione approfondisce quando il candidato ha risposto bene sull'impianto metodologico.

# Parte IV — I dati: tipi, qualità, dimensioni

## 11. La tassonomia dei dati

**Per struttura:**

| Tipo | Che cos'è | Esempi nella P.A. |
|---|---|---|
| **Strutturati** | organizzati in righe e colonne, con schema predefinito; risiedono in database relazionali e si interrogano in **SQL** | anagrafiche, contabilità, tributi, protocollo |
| **Semi-strutturati** | hanno una struttura, ma flessibile e auto-descrittiva (**XML, JSON**) | fatturazione elettronica (XML), API dei servizi digitali |
| **Non strutturati** | privi di schema: testo libero, immagini, audio, video | atti amministrativi, PEC, segnalazioni dei cittadini, immagini da telecamere o droni |

Si stima che la **grande maggioranza dei dati di un'amministrazione sia non strutturata** — atti, verbali, corrispondenza — ed è esattamente la parte che la contabilità e la statistica tradizionali non toccano. È lì che il *text mining* (§ 28) diventa interessante.

**Per scala di misura** — è la tassonomia statistica classica, e serve perché **determina quali operazioni sono lecite** e quali algoritmi si possono usare:

| Scala | Proprietà | Esempio | Statistica di sintesi |
|---|---|---|---|
| **Nominale** | solo classificazione | comune di residenza, tipo di atto | **moda** |
| **Ordinale** | classificazione + ordine | livello di istruzione, giudizio di soddisfazione | **mediana**, quantili |
| **A intervalli** | + distanze costanti, zero convenzionale | temperatura in °C, anno di calendario | **media**, deviazione standard |
| **A rapporti** | + zero assoluto | reddito, spesa, popolazione, tempi di attesa | tutte, incluse le **medie geometriche** e i rapporti |

> **L'errore che un funzionario non deve fare.** Calcolare la **media di una variabile ordinale** (la «media» dei giudizi da 1 a 5 in un questionario di *customer satisfaction*) è tecnicamente improprio: fra «poco soddisfatto» e «abbastanza soddisfatto» non c'è la stessa distanza che fra «abbastanza» e «molto». Si fa continuamente, anche nelle relazioni ufficiali, e va almeno saputo.

## 12. La qualità dei dati: le sei dimensioni

La qualità non è un concetto unico. Le dimensioni comunemente riconosciute — e che ritrovi anche nelle linee guida AgID sui dati della P.A. — sono:

| Dimensione | Domanda a cui risponde |
|---|---|
| **Accuratezza** | il dato corrisponde alla realtà? |
| **Completezza** | mancano valori o record? |
| **Consistenza** | il dato è coerente fra le diverse fonti che lo contengono? |
| **Tempestività** | il dato è aggiornato al momento in cui serve? |
| **Unicità** | esistono duplicati dello stesso soggetto o evento? |
| **Validità** | il dato rispetta il formato e il dominio ammesso (un codice fiscale ben formato, una data esistente)? |

> **Il principio da citare: *garbage in, garbage out*.** Nessun algoritmo, per quanto sofisticato, corregge un dato sbagliato in partenza. E nella P.A. il problema tipico non è l'accuratezza del singolo dato, ma la **consistenza fra banche dati diverse**: lo stesso cittadino con indirizzi diversi in anagrafe, nei tributi e nei servizi sociali. È esattamente il problema che l'**interoperabilità** (§ 26) cerca di risolvere.

## 13. I big data e le cinque V

Il termine **big data** non indica semplicemente «molti dati»: indica dati che, per una o più delle loro caratteristiche, **non sono trattabili con gli strumenti tradizionali**. Le dimensioni classiche sono tre, poi diventate cinque:

| V | Significato |
|---|---|
| **Volume** | la quantità: ordini di grandezza che eccedono la capacità di un singolo server |
| **Velocità** | la rapidità di generazione e la necessità di elaborazione in tempo reale (*streaming*) |
| **Varietà** | l'eterogeneità dei formati: strutturati, semi-strutturati, non strutturati |
| **Veridicità** | l'incertezza sulla qualità e l'affidabilità della fonte |
| **Valore** | la capacità effettiva di generare un beneficio: senza di essa, gli altri quattro sono solo un costo |

> **La V che conta nella P.A. è la quinta.** Un'amministrazione non ha un problema di volume: ha un problema di **valore**, cioè di trasformare dati che già possiede in decisioni migliori. Dirlo previene l'idea, molto diffusa e molto costosa, che la soluzione sia comprare una piattaforma.

---

# Parte V — Il pre-processing in dettaglio

La scheda elenca le operazioni; qui c'è **come si fanno e perché**, perché è la parte su cui una commissione tecnica approfondisce volentieri.

## 14. I valori mancanti

Prima di scegliere la tecnica, bisogna capire **perché** il dato manca — la classificazione di Rubin:

- **MCAR** (*missing completely at random*): la mancanza è indipendente da tutto. Rara, ma innocua: eliminare i record non introduce distorsione;
- **MAR** (*missing at random*): la mancanza dipende da **variabili osservate** (il reddito manca più spesso fra i giovani). È il caso più comune: l'imputazione condizionata funziona;
- **MNAR** (*missing not at random*): la mancanza dipende dal **valore stesso non osservato** (chi ha redditi molto alti non li dichiara). È il caso pericoloso: **nessuna imputazione risolve**, e la mancanza va modellata esplicitamente.

**Le strategie**, in ordine crescente di sofisticazione: **eliminazione** del record o della variabile; **imputazione con media/mediana/moda** (semplice, ma comprime la varianza); **imputazione con k-NN** (preserva le relazioni, come nota la scheda); **imputazione multipla**, che genera più dataset completi e combina i risultati, tenendo conto dell'incertezza dell'imputazione stessa.

## 15. Gli outlier

Un **outlier** è un'osservazione molto distante dalle altre. Tre metodi di individuazione che vale la pena saper nominare:

- **regola dello scarto interquartile (IQR)**: sono outlier i valori esterni all'intervallo *[Q1 − 1,5·IQR ; Q3 + 1,5·IQR]*. È la regola che disegna i «baffi» del ***box plot***;
- **regola dello Z-score**: sono sospetti i valori che distano dalla media più di **3 deviazioni standard**;
- **metodi multivariati** (distanza di Mahalanobis, *isolation forest*, *local outlier factor*), necessari quando l'anomalia non è in una singola variabile ma nella **combinazione** di più variabili.

> **Il punto di metodo, che è anche un punto di sostanza amministrativa:** un outlier **non va rimosso per riflesso**. Può essere un errore di misura — e allora si elimina o si corregge — oppure può essere **esattamente il fenomeno che stiamo cercando**: nella lotta all'evasione, nel controllo delle frodi, nella verifica degli appalti anomali, **l'outlier è il risultato, non il disturbo**. La scheda parla di rimozione perché descrive il caso generale; in un contesto di controllo la logica si rovescia.

## 16. La normalizzazione

Serve perché molti algoritmi **basati sulle distanze** (k-NN, K-Means, SVM, reti neurali) sono sensibili alla scala: una variabile espressa in euro dominerebbe una variabile espressa in anni semplicemente perché ha numeri più grandi.

- **Min-Max**: riporta i valori nell'intervallo [0,1]. Conserva la forma della distribuzione ma è **sensibile agli outlier**;
- **Z-score (standardizzazione)**: porta la variabile a media 0 e deviazione standard 1. È **più robusta** ed è la scelta di default;
- **scalatura robusta**: usa mediana e IQR invece di media e deviazione standard, quindi resiste agli outlier.

> **Non tutti gli algoritmi la richiedono.** Gli **alberi decisionali** e gli algoritmi da essi derivati (random forest, gradient boosting) sono **invarianti a trasformazioni monotone**: normalizzare non serve. Saperlo distingue chi ha capito da chi applica ricette.

## 17. Le variabili categoriali

Gli algoritmi lavorano con numeri: le categorie vanno codificate.

- ***one-hot encoding***: crea una variabile binaria per ciascuna categoria. Corretto ma **esplode la dimensionalità** se le categorie sono molte (si pensi agli 8.000 comuni italiani);
- ***label encoding***: assegna un intero a ciascuna categoria. Compatto, ma **introduce un ordine inesistente** — è lecito solo per variabili ordinali o per algoritmi ad albero;
- ***target encoding***: sostituisce la categoria con la media della variabile risposta in quella categoria. Efficace ma a forte rischio di *leakage*: va calcolato **solo sul training set**.

## 18. La riduzione dimensionale e la «maledizione della dimensionalità»

All'aumentare del numero di variabili, lo spazio si «svuota»: i punti diventano tutti **equidistanti fra loro**, le distanze perdono significato e i modelli richiedono quantità di dati che crescono esponenzialmente. È la ***curse of dimensionality***.

Due famiglie di rimedi:

- **selezione delle variabili (*feature selection*)**: si scelgono le variabili più informative e si scartano le altre. Metodi *filter* (basati su correlazione o test statistici), *wrapper* (che provano sottoinsiemi valutando il modello), *embedded* (in cui la selezione è interna all'algoritmo, come nella regressione **LASSO**);
- **estrazione di variabili (*feature extraction*)**: si costruiscono **nuove variabili** combinazione delle originali. La tecnica canonica è la **PCA (analisi delle componenti principali)**, che individua le direzioni di massima varianza e proietta i dati su un numero ridotto di **componenti** fra loro ortogonali.

> **Il prezzo della PCA, che va sempre dichiarato.** Le componenti principali sono **combinazioni lineari** delle variabili originali: si guadagna in compattezza e si **perde in interpretabilità**. In un contesto amministrativo, dove la decisione va motivata, questo prezzo può essere inaccettabile — ed è la ragione per cui, nella P.A., spesso si preferisce la *selezione* all'*estrazione*.

## 19. Il bilanciamento delle classi

Molti problemi reali sono **fortemente sbilanciati**: le frodi sono l'1% delle pratiche, gli eventi avversi una minoranza dei casi. Un modello che predicesse sempre «nessuna frode» avrebbe **99% di accuratezza ed è inutile**: è il cosiddetto **paradosso dell'accuratezza**.

Rimedi: ***oversampling*** della classe minoritaria (nella variante **SMOTE**, che genera esempi sintetici invece di duplicare); ***undersampling*** della classe maggioritaria; **pesi di classe** nell'algoritmo; e soprattutto **cambiare metrica** — usare **precisione, richiamo e F1** invece dell'accuratezza (§ 24).

---

# Parte VI — Il machine learning: la mappa

## 20. Le tre famiglie

| Famiglia | Che cosa riceve | Che cosa impara | Compiti tipici |
|---|---|---|---|
| **Apprendimento supervisionato** | dati **etichettati** (coppie input-output) | una funzione che mappa input in output | **classificazione**, **regressione** |
| **Apprendimento non supervisionato** | dati **non etichettati** | una struttura latente nei dati | **clustering**, **riduzione dimensionale**, **regole associative**, **anomaly detection** |
| **Apprendimento per rinforzo** | un ambiente e un segnale di **ricompensa** | una **politica** di azione che massimizza la ricompensa cumulata | controllo, ottimizzazione sequenziale, gestione dinamica di risorse |

Esiste anche il **semi-supervisionato** (poche etichette, molti dati non etichettati), rilevante nella P.A. perché **etichettare costa**: classificare a mano diecimila atti richiede persone e tempo.

## 21. Il compromesso distorsione-varianza

È il concetto teorico più importante di tutto il machine learning, e si spiega in tre righe:

- un modello **troppo semplice** non coglie la struttura reale: ha **distorsione (*bias*) alta** — è il ***underfitting***. Sbaglia sia sui dati di addestramento sia su quelli nuovi;
- un modello **troppo complesso** impara anche il **rumore** dei dati di addestramento: ha **varianza alta** — è l'***overfitting***. È quasi perfetto sui dati visti e **crolla su quelli nuovi**;
- l'errore atteso si scompone in **distorsione² + varianza + errore irriducibile**, e il modello migliore è quello che **minimizza la somma**, non uno dei due addendi.

> **Il sintomo da riconoscere:** performance **ottime in addestramento e scarse in test** = overfitting. Performance **scarse in entrambi** = underfitting. È una domanda d'orale frequentissima ed è a risposta secca.

**I rimedi all'overfitting**: più dati; **regolarizzazione** (penalizzare la complessità: *ridge*, *lasso*); **potatura** degli alberi; ***early stopping***; ***dropout*** nelle reti neurali; e i **metodi ensemble**.

## 22. La validazione: come si misura davvero un modello

- ***holdout***: la divisione train/test descritta dalla scheda (≈80/20). Semplice, ma il risultato dipende da **quale** divisione è capitata;
- ***k-fold cross validation***: si divide il dataset in **k parti**; a turno ciascuna fa da test e le altre k−1 da addestramento; si media il risultato sui k giri. Con **k = 5 o 10** è lo standard. È esattamente la «validazione incrociata» del quarto passo del data mining;
- ***stratified k-fold***: come sopra, ma **preservando le proporzioni delle classi** in ogni *fold* — obbligatoria con classi sbilanciate;
- ***leave-one-out***: caso estremo con k = numero di osservazioni. Usata quando i dati sono pochissimi;
- ***nested cross validation***: due cicli annidati, uno per l'ottimizzazione degli iperparametri e uno per la stima delle prestazioni. È l'unico modo **corretto** di fare *tuning* e valutazione insieme, perché evita che il test set «contamini» la scelta dei parametri.

> **La regola d'oro, e vale la pena enunciarla così:** il **test set si guarda una volta sola, alla fine**. Ogni volta che si usa il test set per decidere qualcosa — quale algoritmo, quali parametri — quel test set **smette di essere una stima onesta** delle prestazioni future. Per decidere serve un terzo insieme, il ***validation set***, o la validazione incrociata interna.

---

# Parte VII — Gli algoritmi fondamentali

Qui, come concordato, **nessuna derivazione**: che cosa fa l'algoritmo, quando si usa, qual è il suo punto debole. È il livello a cui una commissione non tecnica si aspetta che tu sappia parlarne.

## 23. Supervisionati

### 23.1 Regressione lineare

Stima una variabile numerica come **combinazione lineare** dei predittori. È il modello più semplice, il più interpretabile (ogni coefficiente è l'effetto marginale di una variabile) e il punto di partenza di qualunque analisi. Limite: assume **linearità** e soffre la **multicollinearità** fra predittori.

### 23.2 Regressione logistica

Nonostante il nome, è un modello di **classificazione**: stima la **probabilità** che un'osservazione appartenga a una classe, vincolandola fra 0 e 1. È lo standard quando serve una **probabilità interpretabile** e una **motivazione** della decisione — e quindi è spesso la scelta giusta nella P.A. anche quando esistono modelli più accurati.

### 23.3 k-Nearest Neighbors (k-NN)

Classifica un'osservazione guardando le **k osservazioni più vicine** e assegnando la classe prevalente. Non «addestra» nulla: memorizza i dati (*lazy learning*). Semplice e sorprendentemente efficace; richiede **normalizzazione obbligatoria** ed è lento su grandi dataset.

### 23.4 Alberi decisionali

Costruiscono una sequenza di **domande binarie** sulle variabili, fino ad arrivare a una previsione. La scelta di ogni divisione massimizza la «purezza» dei rami (misurata con **indice di Gini** o **entropia**). Il grande pregio è la **piena interpretabilità**: l'albero si legge come un regolamento. Il difetto è l'**instabilità** — piccole variazioni nei dati producono alberi molto diversi — e la tendenza all'overfitting, che si contrasta con la **potatura**.

### 23.5 I metodi ensemble

Sono i «metodi ensemble» citati dalla scheda al terzo passo del data mining, e sono oggi lo stato dell'arte sui dati tabellari:

- ***bagging*** e **Random Forest**: si addestrano molti alberi su campioni diversi (con reinserimento) e su sottoinsiemi casuali di variabili, poi si **media** il risultato. Riduce drasticamente la **varianza**;
- ***boosting*** (AdaBoost, **Gradient Boosting**, XGBoost, LightGBM): gli alberi si costruiscono **in sequenza**, ciascuno correggendo gli errori del precedente. Riduce la **distorsione** e dà tipicamente le prestazioni migliori, al prezzo di una maggiore sensibilità al rumore e di una minore interpretabilità.

### 23.6 Support Vector Machine e Naive Bayes

La **SVM** cerca l'iperpiano che separa le classi con il **margine più ampio**, e grazie al *kernel trick* gestisce anche confini non lineari: potente su dataset piccoli e ad alta dimensionalità, poco scalabile. Il **Naive Bayes** applica il teorema di Bayes assumendo l'indipendenza fra le variabili: un'assunzione quasi sempre falsa, eppure l'algoritmo funziona molto bene sulla **classificazione di testi** (è il classico filtro anti-spam), è velocissimo e richiede pochi dati.

### 23.7 Reti neurali e deep learning

Strati di unità elementari che compongono trasformazioni non lineari. Con molti strati si parla di ***deep learning***: è la tecnologia che domina su **immagini, audio, testo e serie complesse**, cioè sui dati **non strutturati**. Richiede **molti dati e molta potenza di calcolo**, ed è il caso tipico di modello ***black box***. Sui **dati tabellari**, che sono la stragrande maggioranza dei dati amministrativi, **i metodi ensemble restano competitivi o superiori**: è un'osservazione che vale la pena fare, perché smonta l'idea che il deep learning sia sempre la scelta migliore.

## 24. Non supervisionati

### 24.1 K-Means

L'algoritmo di clustering citato dalla scheda. Si fissa a priori il numero **k** di gruppi; l'algoritmo assegna ciascun punto al **centroide più vicino** e ricalcola i centroidi, iterando fino alla stabilità. Veloce e diffusissimo; i limiti: **k va scelto a priori** (con il **metodo del gomito** o il **coefficiente di silhouette**), tende a produrre **cluster sferici e di dimensioni simili**, ed è **sensibile all'inizializzazione** e agli outlier.

### 24.2 Clustering gerarchico e DBSCAN

Il **clustering gerarchico** costruisce un **dendrogramma** — un albero di aggregazioni successive — e **non richiede di fissare k in anticipo**: lo si sceglie «tagliando» l'albero all'altezza desiderata. **DBSCAN** individua i cluster come **regioni dense** separate da regioni rade: trova cluster di **forma arbitraria** e classifica automaticamente i punti isolati come **rumore**, il che lo rende naturalmente adatto anche all'*anomaly detection*.

### 24.3 Regole associative

Cercano co-occorrenze del tipo «chi fa A tende a fare anche B». L'algoritmo classico è ***Apriori***. Si valutano con tre indicatori: il ***supporto*** (quanto è frequente la combinazione), la ***confidenza*** (con che probabilità B segue A) e il ***lift*** (quanto la regola è migliore del caso). È la tecnica nata per il *market basket analysis* e trasferibile all'analisi di **percorsi dei cittadini fra i servizi** o di **combinazioni ricorrenti di irregolarità**.

## 25. Le metriche di valutazione

### 25.1 Classificazione: la matrice di confusione

Tutto parte da una tabella 2×2 che incrocia **classe reale** e **classe predetta**:

|  | **Predetto positivo** | **Predetto negativo** |
|---|---|---|
| **Reale positivo** | **VP** (veri positivi) | **FN** (falsi negativi) |
| **Reale negativo** | **FP** (falsi positivi) | **VN** (veri negativi) |

Da essa discendono le metriche:

| Metrica | Che cosa misura | Quando è quella giusta |
|---|---|---|
| **Accuratezza** | quota di previsioni corrette sul totale | solo con **classi bilanciate** |
| **Precisione** | fra i casi segnalati come positivi, quanti lo erano davvero | quando **un falso allarme costa** (un controllo fiscale a un contribuente in regola) |
| **Richiamo (*recall*, sensibilità)** | fra i casi realmente positivi, quanti ne abbiamo trovati | quando **mancare un caso costa** (una frode non rilevata, una patologia non diagnosticata) |
| **F1-score** | media armonica di precisione e richiamo | con **classi sbilanciate**, quando servono entrambe — ed è esattamente ciò che dice la scheda |
| **ROC-AUC** | capacità di separare le classi **a ogni soglia** | per confrontare modelli indipendentemente dalla soglia scelta |

> **Precisione e richiamo sono in trade-off**, e la scelta **non è tecnica: è politica**. Abbassare la soglia aumenta il richiamo (trovo più casi) e abbassa la precisione (do più falsi allarmi). Decidere dove mettersi lungo questa curva significa decidere **quale errore l'amministrazione preferisce commettere** — e questa è una decisione che non può essere delegata al data scientist. Se porti questa riflessione all'orale, hai detto la cosa più importante dell'intera materia.

### 25.2 Regressione e clustering

Per la **regressione**: **MAE** (errore assoluto medio, nell'unità di misura della variabile, robusto agli outlier); **MSE/RMSE** (errore quadratico, penalizza fortemente gli errori grandi); **R²**, la quota di varianza spiegata dal modello.

Per il **clustering**, dove non esiste una «risposta giusta»: il **coefficiente di silhouette** (citato dalla scheda) confronta, per ogni punto, la distanza media dai punti del proprio cluster con quella dai punti del cluster più vicino; varia fra **−1 e +1**, e valori prossimi a 1 indicano gruppi ben separati. Si usano anche l'**indice di Davies-Bouldin** e il **metodo del gomito** sulla varianza interna.

---

# Parte VIII — Dati e algoritmi nella pubblica amministrazione italiana

> **Questa è la parte decisiva per il tuo concorso.** Un candidato che sa spiegare il K-Means fa la figura di uno che ha studiato; un candidato che sa spiegare **che cosa cambia quando l'algoritmo entra in un procedimento amministrativo** fa la figura di un funzionario. La commissione del RIPAM valuta la seconda cosa.

## 26. Il dato come infrastruttura: il CAD e l'interoperabilità

Il **Codice dell'amministrazione digitale (D.Lgs. 82/2005)** contiene i capisaldi:

- **art. 50 — disponibilità dei dati**: i dati delle pubbliche amministrazioni sono **formati, raccolti, conservati, resi disponibili e accessibili** con l'uso delle tecnologie dell'informazione, e **qualunque dato trattato da una P.A. è reso accessibile e fruibile alle altre amministrazioni** quando l'utilizzazione sia necessaria per lo svolgimento dei loro compiti;
- **art. 50-*ter* — Piattaforma Digitale Nazionale Dati (PDND)**: l'infrastruttura tecnologica che rende possibile l'**interoperabilità dei sistemi informativi** e delle basi di dati delle amministrazioni, mediante l'**accreditamento, l'identificazione e la gestione dei livelli di autorizzazione** dei soggetti abilitati ad operarvi, e la **raccolta e conservazione delle informazioni relative agli accessi e alle transazioni**;
- **art. 60 — basi di dati di interesse nazionale**: gli insiemi di informazioni omogenee, rilevanti per lo svolgimento delle funzioni istituzionali, la cui disponibilità è essenziale (si pensi all'**ANPR**, l'Anagrafe nazionale della popolazione residente);
- **art. 68, comma 3 — la definizione di dato aperto**: è aperto il dato **disponibile secondo i termini di una licenza che ne permetta l'utilizzo da parte di chiunque, anche per finalità commerciali**, in formato **disaggregato**; accessibile **attraverso le tecnologie dell'informazione e della comunicazione**, in formati **aperti**, adatti all'utilizzo automatico da parte di programmi e **provvisto dei relativi metadati**; reso disponibile **gratuitamente** o ai soli costi marginali sostenuti per la riproduzione e divulgazione.

> **Il principio *once only*.** Il cittadino non deve fornire più volte alla P.A. un dato che la P.A. già possiede: l'amministrazione lo recupera dalla banca dati che lo detiene. È il senso pratico dell'interoperabilità, ed è il motivo per cui la PDND non è una questione informatica ma **una riforma amministrativa**.

## 27. Il riutilizzo e gli open data

Il riutilizzo dell'informazione del settore pubblico è disciplinato dal **D.Lgs. 36/2006**, profondamente modificato dal **D.Lgs. 200/2021**, che ha recepito la **Direttiva (UE) 2019/1024 («Open Data»)**. I punti da conoscere:

- il principio è **open data by default**: i documenti detenuti dalle amministrazioni sono **riutilizzabili** a fini commerciali o non commerciali, salvo eccezioni;
- sono individuate categorie di **dati di elevato valore (*high-value datasets*)**, da rendere disponibili **gratuitamente, in formato leggibile meccanicamente e tramite API**: geospaziali, osservazione della terra e ambiente, meteorologici, statistici, sulle imprese, sulla mobilità (l'elenco specifico è nel **Regolamento di esecuzione (UE) 2023/138**);
- si affiancano il **Data Governance Act — Reg. (UE) 2022/868**, che disciplina il riutilizzo di **dati protetti** detenuti dal settore pubblico, gli **intermediari di dati** e l'**altruismo dei dati**, e il **Data Act — Reg. (UE) 2023/2854** sull'accesso ai dati generati da prodotti connessi.

> **Da non confondere — e la commissione lo chiede.** **Trasparenza** (D.Lgs. 33/2013) e **open data** (D.Lgs. 36/2006) hanno finalità diverse: la prima serve al **controllo diffuso** sull'operato dell'amministrazione ed è un obbligo di pubblicazione; il secondo serve alla **creazione di valore** — economico, sociale, conoscitivo — da parte di chiunque, e riguarda il **formato e la licenza**. Un dato può essere pubblicato per trasparenza in un PDF scansionato: è trasparente, **non è un open data**.

## 28. Il text mining sugli atti amministrativi

Poiché la maggior parte del patrimonio informativo di un'amministrazione è **testo**, vale la pena conoscere il vocabolario minimo del *text mining*, anche solo per governare un affidamento esterno:

- la **pipeline** classica: *tokenizzazione* (spezzare il testo in unità), rimozione delle ***stopword***, ***stemming*** o ***lemmatizzazione*** (ricondurre le parole alla radice o al lemma);
- la **rappresentazione**: ***bag of words***, **TF-IDF** (che pesa una parola tanto più quanto è frequente nel documento e rara nel corpus), ***word embedding*** e oggi i **modelli linguistici di grandi dimensioni**;
- i **compiti tipici applicabili alla P.A.**: **classificazione automatica** di istanze e segnalazioni verso l'ufficio competente; ***topic modeling*** per capire di che cosa parlano migliaia di segnalazioni; **estrazione di entità** (nomi, date, importi, riferimenti normativi) dagli atti; **ricerca semantica** negli archivi documentali; **sentiment analysis** sulle comunicazioni dei cittadini.

## 29. Gli usi concreti nel settore pubblico

Vale la pena avere pronti **tre o quattro esempi**, perché la domanda «a che cosa serve, in concreto, in un'amministrazione?» arriva quasi sempre.

| Ambito | Tecnica | Uso |
|---|---|---|
| **Contrasto all'evasione e alle frodi** | anomaly detection, classificazione, regole associative | selezione delle posizioni da controllare sulla base del **rischio stimato**, invece che a campione |
| **Sanità** | modelli predittivi, clustering | previsione della domanda di prestazioni, stratificazione della popolazione per rischio, gestione delle liste d'attesa |
| **Manutenzione delle infrastrutture** | manutenzione predittiva su dati sensoristici | intervenire **prima** del guasto su ponti, reti idriche, edifici pubblici |
| **Gestione del personale e dei procedimenti** | *process mining*, analisi dei tempi | individuare i colli di bottiglia nei procedimenti e i motivi reali degli scostamenti dai termini |
| **Politiche pubbliche** | metodi controfattuali, matching | **valutazione d'impatto** degli interventi — il ponte diretto con l'altra materia del tuo bando |
| **Servizi al cittadino** | classificazione testi, NLP | instradamento automatico di istanze e segnalazioni, *chatbot* di primo livello |

## 30. I limiti giuridici: algoritmo e provvedimento amministrativo

È il cuore giuridico della materia, ed è la parte in cui puoi far convergere data science e diritto amministrativo.

### 30.1 I tre principi del Consiglio di Stato

Con le sentenze della **sez. VI, n. 2270 dell'8 aprile 2019** e **n. 8472 del 13 dicembre 2019** (la vicenda degli algoritmi per la mobilità del personale scolastico), il Consiglio di Stato ha ammesso l'uso dell'algoritmo nel procedimento amministrativo — riconoscendone anzi i vantaggi in termini di **efficienza, imparzialità e velocità** — ma lo ha subordinato a **tre principi**:

| Principio | Contenuto |
|---|---|
| **Conoscibilità (e comprensibilità)** | l'interessato ha diritto di conoscere **l'esistenza** di un processo decisionale automatizzato e la **logica** utilizzata; l'algoritmo, in quanto atto amministrativo informatico, deve essere **conoscibile in tutti i suoi aspetti** ed è pienamente **sindacabile dal giudice** |
| **Non esclusività** | la decisione non può essere **interamente** rimessa alla macchina: deve esistere un **contributo umano** capace di controllare, validare o smentire l'esito automatico (*human in the loop*) |
| **Non discriminazione algoritmica** | il titolare deve **utilizzare procedure matematiche o statistiche appropriate**, mettere in atto misure per **rettificare i fattori che comportano inesattezze** e **minimizzare il rischio di errori**, evitando effetti discriminatori |

> **La formula del Consiglio di Stato che conviene citare quasi alla lettera:** l'algoritmo, quando è utilizzato nel procedimento, **non è uno strumento meramente tecnico ma diventa la regola del procedimento stesso**, e come tale deve rispettare tutti i principi che governano l'azione amministrativa — **motivazione, trasparenza, partecipazione, sindacabilità**. Il segreto industriale del fornitore **non può prevalere** sul diritto di difesa dell'interessato.

### 30.2 Il quadro europeo

- **GDPR, art. 22**: l'interessato ha il **diritto di non essere sottoposto a una decisione basata unicamente sul trattamento automatizzato** — compresa la profilazione — che produca effetti giuridici o incida in modo analogamente significativo sulla sua persona, salvo eccezioni (necessità contrattuale, autorizzazione normativa, consenso esplicito) e comunque con **garanzie minime**: diritto di **ottenere l'intervento umano**, di **esprimere la propria opinione** e di **contestare la decisione**. Vi si affiancano i principi dell'**art. 5** (**minimizzazione**, **limitazione della finalità**, esattezza), la ***privacy by design and by default*** dell'**art. 25** e la **valutazione d'impatto sulla protezione dei dati (DPIA)** dell'**art. 35**, obbligatoria proprio nei casi di valutazione sistematica e automatizzata su larga scala;
- **AI Act — Reg. (UE) 2024/1689**: impianto **basato sul rischio**, con quattro livelli — **rischio inaccettabile** (pratiche vietate: *social scoring*, manipolazione, in larga parte l'identificazione biometrica remota in tempo reale in spazi accessibili al pubblico), **alto rischio** (obblighi stringenti di gestione del rischio, qualità dei dati, documentazione, tracciabilità, **sorveglianza umana**, accuratezza e cybersicurezza), **rischio limitato** (obblighi di **trasparenza**: dire all'utente che sta interagendo con un sistema di IA) e **rischio minimo**. **Molti usi tipici del settore pubblico ricadono nell'alto rischio** — accesso a servizi essenziali, valutazione dell'affidabilità creditizia, occupazione e selezione del personale, istruzione, giustizia, migrazione;
- in Italia, la **L. 23 settembre 2025, n. 132** ha dettato disposizioni in materia di intelligenza artificiale e deleghe al Governo, muovendosi nel solco dell'AI Act e ribadendo, per il settore pubblico, il principio della **centralità della decisione umana** e della **tracciabilità** dei sistemi utilizzati. *(È normativa recentissima: verifica lo stato dei decreti attuativi prima dell'orale.)*

### 30.3 Il *bias* algoritmico: da dove viene davvero

Un punto che vale la pena chiarire perché è quasi sempre frainteso: **l'algoritmo non è «prevenuto»; lo sono i dati**. Le fonti principali:

- ***bias* storico**: i dati riflettono **discriminazioni già avvenute**. Un modello addestrato sui controlli fiscali del passato imparerà a controllare le stesse categorie di prima, a prescindere dal rischio reale;
- ***bias* di campionamento**: alcuni gruppi sono **sotto-rappresentati** nei dati, e il modello funziona peggio su di loro;
- ***bias* di misura**: la variabile osservata è un **proxy imperfetto** di ciò che interessa davvero (si usa «numero di controlli con esito positivo» come proxy di «evasione», ma si misurano i controlli, non l'evasione);
- ***feedback loop***: il modello indirizza i controlli su un gruppo, i controlli generano nuovi dati su quel gruppo, i nuovi dati confermano il modello. **La profezia si autoavvera.**

> **La conclusione da portare all'orale:** la correttezza di un sistema algoritmico **non è una proprietà del codice, è una proprietà del processo**. Si garantisce con la **qualità e la rappresentatività dei dati**, con la **valutazione d'impatto preventiva**, con il **monitoraggio delle prestazioni disaggregate per gruppo** e con la **sorveglianza umana effettiva** — non formale. È esattamente l'architettura che l'AI Act impone ai sistemi ad alto rischio, e coincide con i tre principi del Consiglio di Stato.

## 31. Il sistema statistico nazionale

Chiude il quadro istituzionale, ed è il collegamento con la **statistica economica per le PA**, altra materia del bando: il **SISTAN** — Sistema statistico nazionale, istituito dal **D.Lgs. 322/1989** — è la rete che collega **ISTAT**, uffici di statistica di amministrazioni centrali e locali, enti e organismi pubblici di informazione statistica. Produce la **statistica ufficiale** secondo il **Programma statistico nazionale**, nel rispetto dei principi del **Codice italiano delle statistiche ufficiali** e del **Codice delle statistiche europee**: **indipendenza professionale, imparzialità, obiettività, affidabilità, segreto statistico**.

> **La distinzione fondamentale, che vale un punto:** il **segreto statistico** (art. 9, D.Lgs. 322/1989) impone che i dati raccolti a fini statistici **possano essere usati solo per fini statistici** e diffusi **esclusivamente in forma aggregata**, in modo che non se ne possa trarre alcun riferimento individuale. È un vincolo **ulteriore e diverso** rispetto alla protezione dei dati personali: vale anche quando il trattamento sarebbe lecito ai sensi del GDPR. Ed è la ragione per cui un dato può essere legittimamente raccolto per una finalità amministrativa e **non** essere riutilizzabile per un'altra.

---

# Parte IX — Le dieci formule che vale la pena sapere

Come concordato: **niente derivazioni**. Queste dieci si scrivono in pochi secondi e coprono tutto ciò che può essere chiesto a un funzionario. Valuta tu quali memorizzare; le prime quattro sono quelle che consiglierei a chiunque.

**1. Accuratezza** — quota di previsioni corrette
> Accuratezza = (VP + VN) / (VP + VN + FP + FN)

**2. Precisione** — fra i segnalati, quanti erano davvero positivi
> Precisione = VP / (VP + FP)

**3. Richiamo (sensibilità)** — fra i positivi reali, quanti ne ho trovati
> Richiamo = VP / (VP + FN)

**4. F1-score** — media armonica di precisione e richiamo
> F1 = 2 × (Precisione × Richiamo) / (Precisione + Richiamo)

**5. Specificità** — fra i negativi reali, quanti ne ho riconosciuti
> Specificità = VN / (VN + FP)

**6. Errore quadratico medio e sua radice** — per la regressione
> MSE = media degli (valore osservato − valore previsto)²  ·  RMSE = √MSE

**7. Coefficiente di determinazione** — quota di varianza spiegata
> R² = 1 − (devianza residua / devianza totale)

**8. Standardizzazione Z-score**
> z = (x − media) / deviazione standard

**9. Normalizzazione Min-Max**
> x' = (x − minimo) / (massimo − minimo)

**10. Distanza euclidea** — il fondamento di k-NN e K-Means
> d(a, b) = √[ Σ (aᵢ − bᵢ)² ]

> **Bonus, se vuoi una carta in più:** le tre misure delle **regole associative**. *Supporto* = frequenza della combinazione sul totale; *Confidenza* = P(B|A); *Lift* = Confidenza / P(B). Un lift maggiore di 1 indica associazione positiva, pari a 1 indipendenza, minore di 1 associazione negativa.

---

# Domande d'orale — 60 domande con la traccia della risposta

## Impianto (dalla scheda: qui devi essere impeccabile)

1. **Che cos'è la data science?** — *Disciplina trasversale che integra statistica, programmazione, machine learning e conoscenza di dominio per trasformare dati grezzi in informazioni utili, anche a fini predittivi.*
2. **Chi ha usato per primo il termine e quando?** — *Peter Naur, 1974, come evoluzione della «datalogy»; ma l'idea di analisi dei dati come campo autonomo è di John Tukey, anni '60. Cleveland nel 2001 con «Data Science: An Action Plan».*
3. **Quando è stato formalizzato il KDD?** — *Nel 1996 da Fayyad, sulle basi poste negli anni '80 dai database relazionali.*
4. **Che rapporto c'è fra data science, KDD e data mining?** — *La data science è il campo ampio che copre l'intero ciclo di vita del dato; il KDD è il processo tecnico di estrazione della conoscenza; il data mining è la fase centrale del KDD. Aggancio: il data mining occupa circa il 20% del tempo totale.*
5. **Quali sono le cinque fasi del KDD?** — *Selezione; pulizia e integrazione; trasformazione; data mining; valutazione e presentazione dei pattern.*
6. **Che cosa si fa nella fase di pulizia?** — *Rimozione outlier; riempimento dei mancanti (media/mediana o k-NN); eliminazione duplicati; integrazione da fonti diverse.*
7. **Perché imputare con il k-NN e non con la media?** — *La media cancella le relazioni complesse fra variabili e comprime la varianza; il k-NN imputa un valore coerente con i record simili.*
8. **Quali tecniche di trasformazione?** — *Normalizzazione Min-Max o Z-score; feature engineering; discretizzazione; riduzione dimensionale con PCA.*
9. **Quali sono le tecniche di data mining?** — *Clustering, classificazione, regressione, sintesi, modellazione delle dipendenze, rilevamento anomalie.*
10. **Come si valutano i pattern trovati?** — *Metriche quantitative (accuratezza, precisione/richiamo, F1 per dataset sbilanciati, silhouette per i cluster), test statistici, e confronto con l'esperto di dominio.*
11. **Quali sono i sei passi operativi del data mining?** — *Preparazione del dataset; selezione algoritmi; addestramento; validazione incrociata; ottimizzazione parametri; generazione pattern.*
12. **Come si divide il dataset?** — *Circa 80% training e 20% test; stratified sampling per preservare le proporzioni delle classi, split temporale per dati cronologici.*
13. **Perché lo split temporale per i dati cronologici?** — *Per evitare di addestrare sul futuro e prevedere il passato: è data leakage, gonfia le prestazioni e crolla in produzione.*
14. **Che cos'è il CRISP-DM e quando nasce?** — *Standard industriale del 1996 per il data mining, evoluto in framework generale; sei fasi cicliche con frecce bidirezionali.*
15. **Elenchi le sei fasi del CRISP-DM.** — *Comprensione del business; comprensione dei dati; preparazione dei dati; modellazione; valutazione; implementazione.*
16. **Qual è la fase più impegnativa?** — *La preparazione dei dati: pulizia, integrazione, trasformazione.*
17. **Qual è la decisione chiave del CRISP-DM?** — *In valutazione: se il modello raggiunge gli obiettivi si implementa, altrimenti si torna alla comprensione del business, non alla modellazione.*
18. **Che cos'è l'EDA?** — *Exploratory Data Analysis, l'analisi esplorativa della fase di comprensione dei dati: qualità, valori incompleti, outlier, squilibri, ridondanze.*
19. **Come la data science moderna aggiorna il CRISP-DM?** — *Cloud computing per big data e training distribuiti; automazione di deployment, monitoraggio e riaddestramento (MLOps); metodologie agili al posto del ciclo rigido.*
20. **Differenze fra KDD e CRISP-DM?** — *KDD: accademico, 5 fasi, granularità tecnica. CRISP-DM: industriale, 6 fasi, completezza pratica e orientamento al business. Il data mining del KDD corrisponde alla modellazione del CRISP-DM.*

## Dati e pre-processing

21. **Dati strutturati, semi-strutturati e non strutturati?** — *Schema fisso in database relazionali; struttura flessibile e auto-descrittiva (XML, JSON); testo, immagini, audio senza schema.*
22. **Quali sono le scale di misura?** — *Nominale, ordinale, a intervalli, a rapporti; determinano quali operazioni e quali statistiche di sintesi siano lecite.*
23. **Quali sono le dimensioni della qualità del dato?** — *Accuratezza, completezza, consistenza, tempestività, unicità, validità.*
24. **Che cosa sono i big data?** — *Le cinque V: volume, velocità, varietà, veridicità, valore. Aggancio: nella P.A. il problema non è il volume, è il valore.*
25. **Perché un dato può mancare?** — *MCAR, MAR, MNAR. Solo nel terzo caso l'imputazione non risolve e la mancanza va modellata.*
26. **Come si individuano gli outlier?** — *Regola dell'IQR (1,5 volte lo scarto interquartile, i baffi del box plot); Z-score oltre 3 deviazioni standard; metodi multivariati.*
27. **Un outlier va sempre rimosso?** — *No: può essere un errore di misura oppure il fenomeno cercato. Nel controllo delle frodi l'outlier è il risultato, non il disturbo.*
28. **Quando serve normalizzare?** — *Per algoritmi basati sulle distanze (k-NN, K-Means, SVM, reti neurali). Gli alberi e i metodi ensemble non lo richiedono.*
29. **Come si codificano le variabili categoriali?** — *One-hot (corretto, ma esplode la dimensionalità); label encoding (compatto, introduce un ordine falso); target encoding (efficace, a rischio di leakage).*
30. **Che cos'è la maledizione della dimensionalità?** — *All'aumentare delle variabili i punti diventano equidistanti, le distanze perdono significato e servono dati esponenzialmente maggiori.*
31. **Selezione o estrazione di variabili?** — *La selezione conserva l'interpretabilità; l'estrazione (PCA) comprime meglio ma produce combinazioni lineari non interpretabili. Nella P.A., dove la decisione va motivata, spesso si preferisce la selezione.*
32. **Che cos'è il paradosso dell'accuratezza?** — *Con classi molto sbilanciate un modello banale ha accuratezza altissima ed è inutile: servono precisione, richiamo e F1, oppure SMOTE e pesi di classe.*

## Machine learning e algoritmi

33. **Quali sono le famiglie di apprendimento?** — *Supervisionato, non supervisionato, per rinforzo; più il semi-supervisionato, rilevante nella P.A. perché etichettare costa.*
34. **Classificazione o regressione?** — *Entrambe supervisionate: la prima prevede una categoria, la seconda un valore numerico.*
35. **Che cos'è il trade-off bias-varianza?** — *Modello troppo semplice: distorsione alta, underfitting. Troppo complesso: varianza alta, overfitting. L'errore atteso è distorsione² + varianza + errore irriducibile.*
36. **Come si riconosce l'overfitting?** — *Ottime prestazioni in addestramento, scarse in test. Rimedi: più dati, regolarizzazione, potatura, early stopping, dropout, metodi ensemble.*
37. **Che cos'è la k-fold cross validation?** — *Si divide il dataset in k parti, a turno una fa da test e le altre da addestramento, si media sui k giri. Standard: k = 5 o 10; stratificata con classi sbilanciate.*
38. **Qual è la regola d'oro sul test set?** — *Si guarda una volta sola, alla fine. Per decidere serve un validation set o una validazione incrociata interna, altrimenti la stima non è più onesta.*
39. **Come funziona il K-Means?** — *Si fissa k, si assegna ogni punto al centroide più vicino, si ricalcolano i centroidi, si itera. Limiti: k a priori, cluster sferici, sensibilità a inizializzazione e outlier.*
40. **Come si sceglie k?** — *Metodo del gomito sulla varianza interna e coefficiente di silhouette.*
41. **Che cos'è il coefficiente di silhouette?** — *Confronta per ogni punto la distanza media interna al cluster con quella dal cluster più vicino; varia fra −1 e +1, valori alti indicano gruppi ben separati.*
42. **Clustering gerarchico e DBSCAN: che vantaggi hanno?** — *Il gerarchico non richiede k a priori e produce un dendrogramma; DBSCAN trova cluster di forma arbitraria e isola il rumore, quindi serve anche all'anomaly detection.*
43. **Che cos'è un albero decisionale?** — *Sequenza di domande binarie che massimizzano la purezza (Gini o entropia). Pregio: piena interpretabilità. Difetti: instabilità e overfitting, mitigati dalla potatura.*
44. **Bagging o boosting?** — *Il bagging (Random Forest) addestra alberi in parallelo su campioni diversi e media: riduce la varianza. Il boosting li costruisce in sequenza correggendo gli errori: riduce la distorsione, dà prestazioni migliori ma è più sensibile al rumore.*
45. **Perché la regressione logistica resta importante?** — *Restituisce una probabilità interpretabile e una motivazione della decisione: spesso è la scelta giusta nella P.A. anche quando esistono modelli più accurati.*
46. **Quando serve il deep learning?** — *Su dati non strutturati — immagini, audio, testo — con molti dati e molta potenza. Sui dati tabellari, che sono la maggioranza dei dati amministrativi, i metodi ensemble restano competitivi.*
47. **Che cosa sono le regole associative?** — *Co-occorrenze del tipo «chi fa A tende a fare B», estratte con Apriori e valutate con supporto, confidenza e lift.*
48. **Precisione o richiamo?** — *Dipende da quale errore costa di più: la precisione quando pesa il falso allarme, il richiamo quando pesa il caso mancato. La scelta della soglia non è tecnica, è una decisione di policy.*
49. **Che cos'è la curva ROC e l'AUC?** — *Rappresentano la capacità di separare le classi a ogni soglia; l'area sotto la curva consente di confrontare modelli indipendentemente dalla soglia scelta.*
50. **Quali metriche per la regressione?** — *MAE (robusto, nell'unità della variabile), MSE/RMSE (penalizza gli errori grandi), R² (varianza spiegata).*

## Dati e algoritmi nella P.A.

51. **Che cos'è la PDND?** — *Piattaforma Digitale Nazionale Dati, art. 50-ter CAD: infrastruttura per l'interoperabilità delle basi di dati delle amministrazioni, con accreditamento, livelli di autorizzazione e tracciamento degli accessi. Attua il principio once only.*
52. **Che cos'è un dato aperto?** — *Art. 68, comma 3, CAD: licenza che ne consenta l'uso da parte di chiunque anche per fini commerciali; formato disaggregato, aperto, leggibile meccanicamente, con metadati; gratuito o ai soli costi marginali.*
53. **Trasparenza e open data sono la stessa cosa?** — *No: la trasparenza (D.Lgs. 33/2013) serve al controllo diffuso ed è obbligo di pubblicazione; gli open data (D.Lgs. 36/2006, come modificato dal D.Lgs. 200/2021) servono alla creazione di valore e riguardano formato e licenza. Un PDF scansionato è trasparente ma non è open data.*
54. **Che cosa sono gli high-value datasets?** — *Categorie di dati a elevato valore da rendere disponibili gratuitamente, in formato leggibile meccanicamente e via API (Dir. UE 2019/1024; Reg. di esecuzione UE 2023/138): geospaziali, ambiente, meteo, statistica, imprese, mobilità.*
55. **Quali principi ha posto il Consiglio di Stato sull'algoritmo nel procedimento?** — *Sentenze sez. VI 2270/2019 e 8472/2019: conoscibilità e comprensibilità, non esclusività (contributo umano), non discriminazione algoritmica. L'algoritmo diventa la regola del procedimento e come tale è sindacabile; il segreto industriale non prevale sul diritto di difesa.*
56. **Che cosa prevede l'art. 22 del GDPR?** — *Diritto di non essere sottoposti a decisioni basate unicamente sul trattamento automatizzato con effetti giuridici significativi, salvo eccezioni e con garanzie minime: intervento umano, espressione della propria opinione, contestazione della decisione.*
57. **Come è strutturato l'AI Act?** — *Reg. UE 2024/1689, approccio basato sul rischio: inaccettabile (pratiche vietate), alto (obblighi stringenti, inclusa la sorveglianza umana), limitato (trasparenza), minimo. Molti usi del settore pubblico ricadono nell'alto rischio.*
58. **Da dove viene il bias algoritmico?** — *Dai dati, non dal codice: bias storico, di campionamento, di misura, e feedback loop. Si contrasta con qualità dei dati, valutazione d'impatto preventiva, monitoraggio disaggregato per gruppo e sorveglianza umana effettiva.*
59. **Che cos'è il segreto statistico?** — *Art. 9 D.Lgs. 322/1989: i dati raccolti a fini statistici sono utilizzabili solo per fini statistici e diffusi solo in forma aggregata. È un vincolo ulteriore e diverso rispetto al GDPR.*
60. **A che cosa serve, in concreto, il data mining in un'amministrazione?** — *Selezione dei controlli per rischio nel contrasto a evasione e frodi; previsione della domanda in sanità; manutenzione predittiva delle infrastrutture; process mining sui procedimenti; valutazione controfattuale d'impatto delle politiche; instradamento automatico di istanze e segnalazioni.*

---

# Come collegare questa materia alle altre del bando

È il vero valore di questa dispensa per il tuo orale: la data science è la materia che **tocca tutte le altre**, e una commissione lo apprezza moltissimo.

- **con la valutazione delle politiche pubbliche** — è il collegamento più forte: gli **indicatori di *output* e *outcome*** del D.P.C.M. 18-9-2012 sono lo stesso problema di misurazione che il data mining affronta; e i **metodi controfattuali** (differenze nelle differenze, *matching*, discontinuità nella regressione) sono machine learning applicato alla causalità. La frase da avere pronta: *«un modello predittivo dice che cosa accadrà, un disegno controfattuale dice che cosa sarebbe accaduto senza l'intervento: la valutazione ha bisogno del secondo, e confonderli è l'errore più costoso»*;
- **con l'econometria e la statistica** — regressione, inferenza, test: stessa cassetta degli attrezzi, finalità diverse. **L'econometria cerca il coefficiente** (l'effetto causale, con la sua significatività); **il machine learning cerca la previsione** (e accetta modelli non interpretabili pur di sbagliare meno);
- **con la contabilità pubblica** — i **piani dei conti integrati**, il **SIOPE** e la **BDAP** sono, in senso proprio, **infrastrutture di dati**: codifiche uniformi che rendono i dati confrontabili e consolidabili. È esattamente il problema dell'integrazione da fonti diverse della seconda fase del KDD, risolto per via normativa;
- **con il diritto amministrativo** — **motivazione del provvedimento**, **accesso agli atti**, **responsabilità**: i tre principi del Consiglio di Stato sono la traduzione dell'algoritmo nel linguaggio della L. 241/1990;
- **con le tecnologie informatiche** (l'altra prova del tuo orale) — il vocabolario di questa dispensa è già metà del programma: basi di dati e SQL, formati aperti, API, interoperabilità, CAD.

---

## Metodo per gli ultimi giorni

**Tre cose da saper fare alla lavagna**, perché sono quelle che una commissione chiede di disegnare: il **ciclo CRISP-DM** con le sei fasi e la freccia di ritorno dalla valutazione alla comprensione del business; la **matrice di confusione** 2×2 con le quattro celle; lo **schema delle inclusioni** fra data science, KDD, data mining e machine learning.

**Tre numeri da ricordare**: 1996 (Fayyad formalizza il KDD; nasce il CRISP-DM), 80/20 (training/test), 20% (quota del data mining sul tempo totale di un progetto di data science).

**Una convinzione da trasmettere.** In tutta la materia c'è un'unica idea che conta davvero, ed è che **il modello è la parte facile**. La parte difficile — e la parte che riguarda un funzionario pubblico — è **decidere quale domanda porre, procurarsi dati di qualità, capire quale errore l'amministrazione può permettersi di commettere, e garantire che una persona resti responsabile della decisione**. Se questa idea attraversa le tue risposte, l'orale su questa materia è chiuso bene.

---

*Dispensa redatta sulla scheda «Elementi di data science e data mining» (Simone, edizione per il Concorso RIPAM 294 posti), riportata integralmente nelle Parti I-III, e integrata nelle Parti IV-X con il contenuto tecnico e giuridico necessario alla prova orale. Normativa citata aggiornata al quadro vigente; la L. 132/2025 sull'intelligenza artificiale è di adozione recentissima e va verificata quanto ai decreti attuativi.*
