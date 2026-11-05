# EC-15 — Data science e data mining

**Copre tutte e 9 le domande della sezione**: 131 bootstrap · 132 tecniche di
data science · 133 anomalie e outlier · 134 sensibilita' e specificita' · 135
cross-validation e train/test · 136 classificazione supervisionata · 137
sovra-adattamento · 248 falsi positivi e falsi negativi · 266 analisi delle
componenti principali.

**Quattro erano gia' coperte dal blocco D**: bootstrap, outlier,
train/test e sovra-adattamento. Qui si richiamano e si completano.

Solo definizioni. Ogni termine attaccato al suo pezzo di definizione.

---

# 0. La differenza di fondo, e va detta per prima

**L'econometria vuole spiegare; la data science vuole prevedere.**

All'econometria interessa **il coefficiente**: quanto vale, se e' significativo,
se e' interpretabile come effetto causale. Alla data science interessa
**l'accuratezza della previsione su dati nuovi**, e il singolo parametro puo'
anche restare inintelligibile.

Da questa differenza seguono due conseguenze che tornano in tutte le risposte
della materia: la data science **non si giudica sull'adattamento ma sulla
validazione fuori campione**, e accetta modelli **non interpretabili** purche'
funzionino.

Dirlo in apertura colloca subito la risposta, e mostra che si padroneggiano
entrambe le materie del bando.

---

# 1. La domanda che organizza tutta la materia

**Nei dati ho gia' la risposta giusta, oppure no?** Due famiglie, e non ce n'e'
una terza.

**L'apprendimento supervisionato, cioe' quello in cui i dati contengono anche la
variabile da prevedere**, detta etichetta: il modello impara dagli esempi di cui
si conosce la risposta. Due compiti: **la classificazione**, quando la variabile
da prevedere e' una categoria, e **la regressione**, quando e' un numero.

**L'apprendimento non supervisionato, cioe' quello in cui l'etichetta non c'e'**
e si cerca una struttura nascosta nei dati. Due compiti tipici: il **clustering**,
cioe' raggruppare osservazioni simili, e la **riduzione della dimensionalita'**,
cioe' sintetizzare molte variabili in poche.

Questa sola domanda ordina tre delle nove domande della sezione: le tecniche, la
classificazione e la PCA.

---

# 2. La classificazione supervisionata *(domanda 136)*

**La classificazione supervisionata, cioe' la tecnica con cui, partendo da un
insieme di osservazioni di cui si conosce la classe di appartenenza, si
costruisce un modello capace di assegnare la classe a osservazioni nuove.**

**Le tre fasi**: **addestramento** sui dati etichettati, **validazione** su dati
tenuti da parte per misurare l'accuratezza, **applicazione** ai casi nuovi.

**Gli algoritmi da saper nominare**: regressione logistica, alberi decisionali,
foreste casuali, k-nearest neighbours, support vector machine, reti neurali.

**Gli impieghi nella PA**: individuazione del rischio di evasione o di frode,
selezione dei controlli, classificazione automatica di pratiche e documenti,
previsione della morosita' o dell'abbandono di un servizio.

---

# 3. Le principali tecniche di data science *(domanda 132)*

La domanda e' plurale: si risponde **per famiglie**, usando la domanda del punto
1, non con un elenco disordinato.

**Supervisionate**: la **regressione lineare** per prevedere grandezze continue,
la **regressione logistica** per esiti binari, gli **alberi decisionali** e le
**foreste casuali**, le tecniche di **boosting**, le **reti neurali**.

**Non supervisionate**: il **clustering**, con k-means e metodi gerarchici, e
l'**analisi delle componenti principali**.

**Per le previsioni economiche in senso proprio**, che e' quello a cui la domanda
allude: i **modelli di previsione su serie storiche**; le **regressioni
penalizzate** — ridge e lasso — che servono quando i predittori sono molti e
correlati, perche' selezionano e restringono i coefficienti; e il **nowcasting,
cioe' la stima del valore corrente di una grandezza non ancora pubblicata**,
ottenuta da dati ad alta frequenza come transazioni con carta, ricerche sul web,
dati satellitari.

**E le tecniche di validazione**, che non sono un accessorio ma parte del
metodo: separazione fra dati di addestramento e di verifica, e
**cross-validation**.

---

# 4. La valutazione di un classificatore *(domande 248 e 134)*

## La matrice di confusione

Domanda generatrice: **il modello ha detto si' o no — e aveva ragione o torto?**
Quattro caselle, non ce n'e' una quinta.

**Vero positivo**: il modello dice si' ed e' si'. **Vero negativo**: dice no ed e'
no. **Falso positivo**: dice si' ed e' no — e' il **falso allarme**. **Falso
negativo**: dice no ed e' si' — e' il **mancato rilevamento**.

## Sensibilita' e specificita' *(134)*

**La sensibilita', cioe' la quota dei positivi reali che il modello riesce a
individuare.** Risponde alla domanda: *quanti dei casi veri riesco a trovare?*
Sensibilita' alta significa **pochi falsi negativi**.

**La specificita', cioe' la quota dei negativi reali che il modello classifica
correttamente.** Risponde a: *quanti dei casi non veri lascio correttamente
fuori?* Specificita' alta significa **pochi falsi positivi**.

## Il trade-off, ed e' il punto che vale il voto

**Le due non si massimizzano insieme.** Abbassando la soglia di decisione il
modello dichiara positivi piu' casi: **la sensibilita' sale e la specificita'
scende**, perche' aumentano i falsi allarmi. Alzandola accade l'opposto.

**Quale privilegiare dipende dal costo relativo dei due errori**, e questa e' la
frase da dire: in uno **screening sanitario** il falso negativo e' il piu' grave,
perche' significa non trovare un malato; in un **controllo antifrode che blocca
pagamenti** il falso positivo ha un costo altissimo, perche' blocca cittadini in
regola.

## E l'avvertenza sull'accuratezza

**L'accuratezza da sola inganna quando le classi sono sbilanciate.** Se i casi
positivi sono l'uno per cento, un modello che risponde sempre «no» ha il
novantanove per cento di accuratezza **ed e' completamente inutile**. Per questo
si guardano sensibilita' e specificita', e non la sola percentuale di risposte
corrette.

---

# 5. Il sovra-adattamento e la validazione *(domande 137 e 135)*

**Il sovra-adattamento, in inglese overfitting, cioe' quando il modello impara
anche il rumore specifico dei dati di addestramento**, e percio' funziona
benissimo su quelli e male sui dati nuovi.

**I rischi**: un'**illusione di accuratezza** che porta a decisioni sbagliate;
**risultati non replicabili** su altri dati; e modelli inutilmente complessi che
non generalizzano. **E' lo stesso punto dell'R quadro: adattarsi bene non e'
prevedere bene.**

**Come si rileva e si previene.** **La separazione fra dati di addestramento e
dati di verifica**, cioe' si stima su una parte e si misura l'errore sulla parte
tenuta da parte, che il modello non ha mai visto.

**La cross-validation, cioe' la divisione del campione in k parti: si addestra su
k meno una e si valida sulla rimanente, ruotando finche' ogni parte ha fatto da
verifica una volta**, e si media l'errore. Serve perche' con una sola divisione
il risultato dipende da quali osservazioni sono finite nel test: la rotazione
rende la misura stabile, e sfrutta tutti i dati.

**Gli altri rimedi**: la **regolarizzazione** — ridge e lasso —, la **potatura**
degli alberi, la limitazione della complessita' del modello, e piu' dati.

---

# 6. Anomalie e outlier nel data mining *(domanda 133)*

**L'outlier, cioe' un'osservazione molto distante dal resto della
distribuzione.**

**La risposta alla domanda «perche' interessano» ha due facce opposte, e dirle
entrambe e' ciò che la rende completa.**

**Come disturbo**: poiche' molte tecniche minimizzano errori al quadrato, un dato
anomalo pesa in modo sproporzionato e puo' distorcere il modello. Qui l'outlier
e' un problema da individuare e trattare.

**Come segnale**: nel data mining **l'anomalia e' molto spesso l'oggetto stesso
dell'analisi**, non un fastidio. Si chiama **anomaly detection**, e serve a
individuare frodi, intrusioni informatiche, guasti, comportamenti evasivi,
transazioni sospette. **Il caso raro e' esattamente quello che si vuole trovare.**

**La frase: in econometria l'outlier e' un problema da correggere, nel data
mining e' spesso il risultato da cercare.**

---

# 7. L'analisi delle componenti principali *(domanda 266)*

**L'analisi delle componenti principali, o PCA, cioe' una tecnica non
supervisionata di riduzione della dimensionalita': sostituisce molte variabili
correlate fra loro con un numero minore di nuove variabili, dette componenti
principali, costruite come combinazioni delle originarie e fra loro
incorrelate.**

**L'obiettivo**: ridurre il numero di variabili **perdendo il meno possibile
dell'informazione**, cioe' della variabilita' complessiva. **La prima componente
e' quella che spiega la quota maggiore di variabilita', la seconda la quota
maggiore fra quelle restanti**, e cosi' via.

**L'interpretazione**: ogni componente si legge guardando **quali variabili
originarie pesano di piu'** su di essa — e' da quei pesi che si capisce che cosa
quella componente rappresenta. **Quante componenti tenere** si decide guardando
**la quota cumulata di variabilita' spiegata**.

**A cosa serve**: a **risolvere la multicollinearita'**, perche' le componenti
sono per costruzione incorrelate; a **visualizzare** dati a molte dimensioni; e a
**costruire indicatori sintetici** — nella PA, gli indici compositi di benessere,
di deprivazione o di rischio.

**Il limite, da dire sempre**: le componenti sono combinazioni matematiche e
**possono non avere un significato economico immediato**. Si guadagna in sintesi
e **si perde in interpretabilita'**.

---

# 8. Il bootstrap *(domanda 131)*

**Il bootstrap, cioe' una tecnica di ricampionamento: dal campione osservato si
estraggono molti campioni con reinserimento, si ristima la grandezza di interesse
su ciascuno, e dalla distribuzione delle stime ottenute si ricavano errore
standard e intervalli di confidenza.**

**Come si usa per stimare l'incertezza**, che e' il taglio della domanda: invece
di ricavare la precisione da una formula teorica, la si **osserva direttamente**
dalla variabilita' delle stime ottenute sui ricampionamenti. Serve **quando la
formula teorica non esiste o quando le ipotesi che la giustificano non valgono**.

---

# La frase d'attacco

*«La data science si distingue dall'econometria per l'obiettivo: l'econometria
vuole spiegare e guarda al coefficiente, la data science vuole prevedere e guarda
all'accuratezza fuori campione. Per questo le sue tecniche si dividono secondo
che l'etichetta sia presente o no — supervisionate e non supervisionate — e il
suo problema centrale e' il sovra-adattamento, che si contrasta validando il
modello su dati che non ha mai visto.»*

# Le nove domande

1. Che cos'e' la classificazione supervisionata? *(136)*
2. Quali sono le principali tecniche di data science per stimare congetture
   economiche? *(132)*
3. Che cosa sono i falsi positivi e i falsi negativi in un modello di
   classificazione? *(248)*
4. Che cosa significano sensibilita' e specificita' nella valutazione dei
   modelli? *(134)*
5. Che cos'e' il sovra-adattamento e quali rischi comporta? *(137)*
6. Che cos'e' la cross-validation e a cosa servono i dati di addestramento e di
   verifica? *(135)*
7. Che cosa sono anomalie e outlier, e perche' interessano il data mining? *(133)*
8. Illustri l'analisi delle componenti principali: obiettivo e interpretazione.
   *(266)*
9. Che cos'e' il bootstrap e come si utilizza per stimare l'incertezza? *(131)*
