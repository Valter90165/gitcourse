# EC-15 — Data science e data mining

**Copre le 9 domande della sezione omonima del repertorio**: 131 bootstrap · 132
tecniche per stimare congetture economiche · 133 anomalie e outlier · 134
sensibilita' e specificita' · 135 cross-validation e train/test · 136
classificazione supervisionata · 137 overfitting · 248 falsi positivi e negativi
· 266 analisi delle componenti principali.

**Quattro sono gia' coperte dal blocco D** (bootstrap, outlier, train/test,
sovra-adattamento): qui vengono richiamate e completate. Le nuove sono cinque.

Solo definizioni. Ogni termine attaccato al suo pezzo di definizione.

---

# Movimento 1 — Che cos'e', e la divisione fondamentale

**La data science, cioe' la disciplina che estrae conoscenza utile dai dati**,
combinando statistica, informatica e conoscenza del dominio.

**Il data mining, cioe' l'insieme delle tecniche che scoprono schemi, relazioni e
regolarita' non note dentro grandi quantita' di dati.**

**La differenza, se la chiedono**: la data science e' **il processo complessivo**,
dalla domanda iniziale al risultato utilizzabile; il data mining e' **la fase di
estrazione degli schemi** dentro quel processo.

## La domanda che genera tutto il campo

**Ho una risposta nota da cui imparare, oppure no?** Da qui la divisione
fondamentale, e da qui si ricavano quasi tutte le tecniche.

**L'apprendimento supervisionato, cioe' quello in cui si dispone di dati gia'
etichettati con la risposta corretta**: il modello impara la relazione fra le
caratteristiche e la risposta, e la applica a casi nuovi. Due famiglie: **la
classificazione**, quando la risposta e' una **categoria**; **la regressione**,
quando la risposta e' un **valore numerico**.

**L'apprendimento non supervisionato, cioe' quello in cui non esiste una risposta
nota**: il modello cerca struttura nei dati. Le tecniche principali: **il
clustering**, che raggruppa osservazioni simili; **la riduzione della
dimensionalita'**, di cui la PCA e' il caso principale; **il rilevamento delle
anomalie**; **le regole associative**.

## Le principali tecniche *(domanda 132)*

La domanda del repertorio chiede le tecniche **per stimare congetture
economiche**, quindi la risposta va orientata li'.

**Le tecniche**: la **regressione**, lineare e logistica; gli **alberi
decisionali** e le loro combinazioni, **random forest** e **gradient boosting**;
le **reti neurali**; il **clustering**; la **PCA** e l'analisi fattoriale; i
**modelli per serie storiche**; il **text mining** e l'analisi del sentiment su
fonti testuali.

**E il pezzo specifico che risponde davvero alla domanda: il nowcasting, cioe'
la stima dell'andamento corrente di una variabile economica prima che le
statistiche ufficiali siano disponibili**, usando dati non tradizionali e ad alta
frequenza — ricerche sul web, transazioni con carte di pagamento, consumi
elettrici, immagini satellitari, annunci di lavoro. E' il punto in cui la data
science entra davvero nella politica economica, e citarlo distingue la risposta.

## La classificazione supervisionata *(domanda 136)*

**La classificazione supervisionata, cioe' la tecnica in cui un modello,
addestrato su osservazioni di cui si conosce la categoria di appartenenza, impara
ad assegnare a nuove osservazioni una fra categorie predefinite.**

**Il processo**: si parte da **dati etichettati**, si addestra il modello sul
**train set**, si valuta sul **test set** mai visto, e solo allora si applica ai
casi nuovi.

**Gli algoritmi**: regressione logistica, alberi decisionali, random forest,
k-nearest neighbours, support vector machine, reti neurali, naive Bayes.

**Le due differenze da citare.** Nella classificazione la risposta e' una
**categoria**: se fosse un numero, sarebbe una **regressione**. E nel
**clustering** i gruppi **non sono noti in anticipo**, li trova l'algoritmo:
quella e' la differenza fra supervisionato e non supervisionato vista in
concreto.

---

# Movimento 2 — Il problema centrale: generalizzare

## Il sovra-adattamento *(domanda 137)*

**L'overfitting, o sovra-adattamento, cioe' quando il modello si adatta troppo ai
dati di addestramento, cogliendo anche il rumore e le irregolarita' casuali, e
per questo perde capacita' di generalizzare a dati nuovi.**

**Il sintomo**: prestazioni ottime sui dati di addestramento e cattive sui dati
nuovi.

**Le cause**: modello troppo complesso rispetto alla quantita' di dati, troppe
variabili, pochi casi.

**I rimedi**: semplificare il modello, **regolarizzazione**, piu' dati,
**validazione incrociata**, potatura degli alberi, arresto precoce
dell'addestramento.

**E il difetto opposto, da nominare perche' completa la risposta:
l'underfitting, cioe' il modello troppo semplice che non cattura la struttura
presente nei dati.** Il bilanciamento fra i due e' esattamente il **trade-off
distorsione-varianza**: un modello troppo semplice e' distorto, uno troppo
complesso ha varianza elevata.

## Train set, test set e validazione incrociata *(domanda 135)*

**Il train set e il test set, cioe' la divisione del campione in una parte su cui
il modello viene addestrato e una parte, mai vista dal modello, su cui viene
valutato.** **Perche' serve**: la prestazione misurata sui dati di addestramento
e' **ottimisticamente distorta per costruzione**, perche' il modello quei dati li
ha gia' visti.

**La cross-validation, o validazione incrociata, cioe' la procedura che divide il
campione in k parti e ripete l'addestramento k volte, usando ogni volta k meno
una parti per addestrare e la parte esclusa per valutare, mediando poi i
risultati.**

**I vantaggi**: **usa tutti i dati sia per addestrare sia per valutare**, e
fornisce una stima della prestazione **piu' stabile** di quella ottenuta da
un'unica divisione — cosa decisiva quando i dati sono pochi, perche' li' il
risultato di una singola divisione dipende troppo da quali casi sono finiti dove.

## Il bootstrap *(domanda 131)*

**Il bootstrap, cioe' la tecnica di ricampionamento che estrae dal campione
osservato molti campioni con reinserimento, ristima il modello su ciascuno, e
dalla distribuzione delle stime ottenute ricava errore standard e intervalli di
confidenza.**

**Come stima l'incertezza, ed e' la parte che la domanda chiede: la variabilita'
delle stime ottenute sui campioni bootstrap e' essa stessa una stima diretta
della variabilita' dello stimatore.** In pratica **sostituisce il calcolo teorico
con una simulazione fatta sui dati stessi**, e per questo serve quando la formula
teorica non e' disponibile o le ipotesi che la giustificano non valgono.

## Anomalie e outlier *(domanda 133)*

**Le anomalie, o outlier, cioe' osservazioni che si discostano in modo marcato dal
comportamento prevalente dei dati.**

**E qui sta il punto della domanda, perche' l'angolo e' opposto a quello della
regressione.** Nella regressione l'outlier e' **un disturbo** da identificare e
controllare, perche' puo' spostare la retta da solo. **Nel data mining l'anomalia
e' spesso l'oggetto stesso dell'analisi**: si cerca proprio quella. Si chiama
**anomaly detection**, e serve a individuare **frodi, intrusioni informatiche,
guasti di impianto, errori di misura, evasione fiscale, riciclaggio**.

**La frase che risolve la domanda: lo stesso dato anomalo e' rumore da eliminare
quando si vuole stimare una relazione media, ed e' segnale da trovare quando si
vuole scoprire un comportamento eccezionale.**

---

# Movimento 3 — Come si giudica un classificatore

## I quattro esiti *(domanda 248)*

La domanda generatrice: **il modello ha detto si' o no, e aveva ragione o torto?**
Due per due fa **quattro esiti**, e non ce ne sono altri.

**Vero positivo**: il modello dice si' e il caso e' effettivamente positivo.
**Vero negativo**: dice no e il caso e' negativo. **Falso positivo, cioe' il
falso allarme**: dice si' ma il caso e' negativo. **Falso negativo, cioe' il caso
mancato**: dice no ma il caso e' positivo.

**La tabella che li raccoglie si chiama matrice di confusione.**

**Il punto che vale il voto: i due errori non hanno lo stesso costo, e il costo
dipende dall'applicazione.** In uno screening sanitario un **falso negativo** e'
gravissimo, perche' un malato viene rimandato a casa. In un controllo fiscale
automatico un **falso positivo** costa accertamenti inutili, contenzioso e
sfiducia. **Quindi la soglia del classificatore si sceglie in funzione del costo
relativo dei due errori, non per massimizzare l'accuratezza.**

## Sensibilita' e specificita' *(domanda 134)*

**La sensibilita', cioe' la capacita' del modello di individuare i casi
effettivamente positivi**: la quota di positivi reali che il modello riconosce.
**Alta sensibilita' significa pochi falsi negativi.**

**La specificita', cioe' la capacita' del modello di riconoscere correttamente i
casi negativi**: la quota di negativi reali che classifica come negativi. **Alta
specificita' significa pochi falsi positivi.**

**Il trade-off, che e' la sostanza della risposta**: abbassando la soglia il
modello dichiara positivi piu' casi, quindi **la sensibilita' sale e la
specificita' scende**; alzandola succede l'opposto. **Non si massimizzano
entrambe**, e la scelta dipende da quale dei due errori costa di piu'.

**E l'avvertenza che fa colpo: l'accuratezza da sola inganna quando le classi
sono sbilanciate.** Se i casi positivi sono l'uno per cento del totale, un modello
che risponde sempre «no» ha un'accuratezza del novantanove per cento e una
sensibilita' pari a zero: e' perfettamente inutile. **Per questo si valutano
sensibilita' e specificita', e si usa la curva ROC con l'area sottostante.**

## L'analisi delle componenti principali *(domanda 266)*

**La PCA, o analisi delle componenti principali, cioe' una tecnica di riduzione
della dimensionalita' che trasforma molte variabili correlate in un numero minore
di nuove variabili, dette componenti principali, fra loro incorrelate e ordinate
per quota di variabilita' spiegata.**

**L'obiettivo**: ridurre il numero di variabili **perdendo il meno possibile di
informazione**, eliminando la ridondanza che nasce dalla correlazione fra le
variabili originarie.

**L'interpretazione**: la **prima componente e' la direzione lungo la quale i
dati variano di piu'**; ogni componente successiva e' la direzione di massima
variabilita' residua, **ortogonale** alle precedenti. Per dare un significato
sostantivo a una componente si guardano **i pesi delle variabili originarie** su
di essa: se su una componente pesano tutti gli indicatori di reddito e consumo,
quella componente si interpreta come «benessere economico».

**Quante componenti si tengono**: quelle che insieme spiegano una quota
soddisfacente della variabilita' totale.

**A cosa serve nella PA**: costruire **indicatori sintetici** — indici di
deprivazione, di benessere, di rischio — a partire da molti indicatori elementari
correlati; e **risolvere la multicollinearita'** prima di una regressione,
sostituendo variabili fortemente correlate con poche componenti incorrelate.

**I limiti**: le componenti sono **combinazioni** di variabili e non sempre hanno
un significato immediato; e la PCA e' **sensibile alla scala**, quindi le
variabili vanno standardizzate prima di applicarla.

---

# La frase d'attacco

*«La data science si divide in due secondo una sola domanda, se esista o no una
risposta nota da cui imparare: supervisionato per classificazione e regressione,
non supervisionato per clustering, riduzione della dimensionalita' e rilevamento
delle anomalie. Il problema centrale e' sempre lo stesso, generalizzare a dati
nuovi, e per questo si separano train e test set e si usa la validazione
incrociata contro il sovra-adattamento. E un classificatore non si giudica
sull'accuratezza, ma su sensibilita' e specificita', perche' falso positivo e
falso negativo non costano la stessa cosa.»*

# Le nove domande

1. Che cos'e' il bootstrap e come si utilizza per stimare l'incertezza? *(131)*
2. Quali sono le principali tecniche di data science per stimare congetture
   economiche? *(132)*
3. Che cosa sono le anomalie e perche' interessano il data mining? *(133)*
4. Che cosa significano sensibilita' e specificita' nella valutazione dei
   modelli? *(134)*
5. Che cos'e' la cross-validation e a cosa servono train e test set? *(135)*
6. Che cos'e' la classificazione supervisionata? *(136)*
7. Quali rischi comporta il sovra-adattamento? *(137)*
8. Che cosa sono falsi positivi e falsi negativi in un modello di
   classificazione? *(248)*
9. Illustri l'analisi delle componenti principali: obiettivo e interpretazione.
   *(266)*
