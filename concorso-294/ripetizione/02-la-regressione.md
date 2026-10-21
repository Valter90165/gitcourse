# Blocco 2 da ripetere — La regressione

**Su 37 domande di econometria uscite all'orale, una ventina riguardano la
regressione.** È il blocco che decide il voto della materia.

Undici domande, con la risposta da dire a voce. Stesse regole del blocco 1:
leggi la domanda, chiudi il foglio, rispondi **ad alta voce**, poi confronta con
i **pezzi che devono esserci**.

> **Due avvertenze sulle fonti.** Le risposte 3 e 11 trattano argomenti che
> **non ho trovato nelle parti 1 e 2 della scansione**: sono econometria
> standard e sono fra le domande uscite, ma vanno verificate sulla parte del
> manuale non ancora caricata. Tutto il resto è sul libro, e indico la pagina.

---

## 1. Che cos'è un modello econometrico e a cosa serve per la valutazione delle politiche?
*(domanda 113)*

> Un modello è **una rappresentazione formale delle conoscenze su un fenomeno**:
> non una riproduzione esatta della realtà, ma **una versione semplificata**,
> scritta come una o più equazioni.
>
> In un modello econometrico si distinguono le variabili **endogene**, che il
> modello spiega, da quelle **esogene**, che prende come date. E si distingue
> una **parte sistematica**, cioè ciò che il modello spiega, da una **parte
> stocastica**, l'errore, cioè ciò che non spiega.
>
> Per la valutazione delle politiche serve a rispondere alla domanda centrale:
> **quanta parte del risultato osservato è attribuibile all'intervento e quanta
> a tutto il resto.** Senza un modello si confronta il prima con il dopo e si
> attribuisce alla politica anche ciò che sarebbe accaduto comunque.

**I pezzi**: rappresentazione formale e semplificata; endogene/esogene;
sistematica/stocastica; attribuire l'effetto all'intervento.

---

## 2. Che cos'è la regressione lineare multipla, e perché non basta quella semplice?
*(domanda 118)*

> È il modello che spiega la variabile dipendente con **più variabili
> esplicative contemporaneamente**, invece di una sola.
>
> Serve perché **nella realtà le cause sono quasi sempre più d'una**. Se spiego i
> tempi di pagamento dei comuni solo con il personale in ragioneria, attribuisco
> al personale anche l'effetto della dimensione del comune, del software, degli
> arretrati.
>
> **E qui sta la differenza che conta nell'interpretazione**: nella regressione
> multipla ogni coefficiente si legge **«a parità delle altre variabili»**. Dice
> l'effetto di quella variabile **tenendo ferme le altre** — cioè depurato dal
> loro contributo.
>
> **È esattamente il problema della valutazione delle politiche**: distinguere
> l'effetto dell'intervento da quello dei fattori che agiscono insieme a lui.

**I pezzi**: più esplicative insieme; «a parità delle altre»; il legame con la
valutazione.

---

## 3. Che cosa accade se si inserisce una variabile irrilevante nel modello?
*(domanda 119)* — ⚠️ *da verificare sulla parte del manuale non caricata*

> Inserire una variabile che **non c'entra** non rende le stime sbagliate in
> media: **gli stimatori restano non distorti**. Il danno è un altro: **ne
> aumenta la varianza**, cioè **le stime diventano meno precise**, con errori
> standard più grandi.
>
> In più **l'R quadro sale comunque**, anche se la variabile è inutile — e
> questo è ingannevole, perché dà l'impressione di aver migliorato il modello.
> Per questo si guarda **l'R quadro corretto**, che tiene conto del numero di
> variabili inserite.
>
> **Il caso opposto è peggiore**: se si **omette** una variabile rilevante, le
> stime diventano **distorte**, perché il suo effetto viene attribuito alle
> variabili rimaste.

**I pezzi**: irrilevante → non distorte ma meno precise; R quadro sale comunque
→ R quadro corretto; omettere è peggio che aggiungere.

---

## 4. Che cosa indica la proprietà BLUE degli stimatori?
*(domande 124 e 173 — manuale p. 361)*

> **BLUE** sta per **Best Linear Unbiased Estimator**, ed è il contenuto del
> **teorema di Gauss-Markov**, che il manuale enuncia così: *sotto le ipotesi
> classiche del modello di regressione lineare, gli stimatori dei minimi
> quadrati sono **lineari**, **non distorti** e **i più efficienti** nella classe
> degli stimatori lineari e non distorti.*
>
> Le tre parole significano:
> — **lineari**: sono combinazioni lineari delle osservazioni;
> — **non distorti** *(unbiased)*: **in media colpiscono il valore vero**, non
> sbagliano sistematicamente in una direzione;
> — **i più efficienti** *(best)*: fra tutti quelli che hanno le prime due
> proprietà, sono quelli con **la varianza più piccola**, cioè i più precisi.
>
> **È la giustificazione teorica dell'uso dei minimi quadrati**: non si usano
> perché sono comodi, ma perché sotto quelle ipotesi sono i migliori disponibili.
>
> **E il punto critico da aggiungere**: vale **sotto le ipotesi classiche**. Se
> le ipotesi cadono — eteroschedasticità, autocorrelazione, endogeneità — **gli
> stimatori OLS smettono di essere BLUE**.

**I pezzi**: Best Linear Unbiased Estimator; Gauss-Markov; le tre parole
tradotte; vale solo sotto le ipotesi.

---

## 5. Che cosa significa uno stimatore con grande varianza?
*(domanda 123)*

> Significa che **la stima è instabile**: se rifacessi lo stesso studio su un
> altro campione, otterrei un valore sensibilmente diverso.
>
> La conseguenza pratica è che **l'errore standard è grande** e **gli intervalli
> di confidenza sono ampi**: il dato esiste, ma **dice poco**, perché il valore
> vero potrebbe stare in un intervallo troppo largo per decidere qualcosa.
>
> **Da non confondere con la distorsione**: uno stimatore con grande varianza
> può essere perfettamente **non distorto** — in media colpisce il bersaglio, ma
> **il singolo colpo può finire lontano**.

**I pezzi**: instabilità fra campioni; errore standard e intervalli ampi;
varianza ≠ distorsione.

---

## 6. Differenza fra distorsione e varianza di uno stimatore. Il trade-off.
*(domanda 244)*

> Sono **due modi diversi di sbagliare**.
>
> La **distorsione** *(bias)* è un errore **sistematico**: lo stimatore sbaglia
> **sempre nella stessa direzione**, e non migliora aumentando i dati.
> La **varianza** è un errore **di instabilità**: in media è giusto, ma **oscilla
> molto** da un campione all'altro.
>
> **L'immagine del bersaglio**: un tiratore distorto centra sempre lo stesso
> punto, ma fuori dal centro. Un tiratore con grande varianza sparge i colpi
> tutt'intorno al centro.
>
> **Il trade-off**: un modello **molto semplice** rischia la distorsione, perché
> trascura pezzi di realtà. Un modello **molto complesso** riduce la distorsione
> ma **aumenta la varianza**, perché insegue anche il rumore del campione. La
> scelta del modello è il punto di equilibrio fra i due errori.

**I pezzi**: sistematico vs instabile; l'immagine del bersaglio; semplice ↔
distorsione, complesso ↔ varianza.

---

## 7. Che cosa sono endogeneità e variabili strumentali?
*(domande 128 e 222 — manuale pp. 440-441)* — **la domanda più importante del blocco**

> Una delle ipotesi del modello è che **le variabili esplicative siano
> indipendenti dall'errore**: in quel caso si dicono **esogene**. Quando invece
> **esiste un legame fra i regressori e l'errore**, si ha **endogeneità dei
> regressori**, e **la stima del parametro non è più corretta né consistente**.
>
> Il manuale indica **tre cause**:
> — **l'omissione di un'altra variabile esplicativa**;
> — **errori di misurazione** delle variabili indipendenti;
> — **simultaneità** fra le variabili, o autocorrelazione nei modelli dinamici.
>
> **L'esempio del manuale per l'omissione**: si stima l'effetto dell'istruzione
> sul salario senza poter osservare **l'abilità individuale**, che non è
> misurabile. L'abilità finisce nell'errore ed è correlata con l'istruzione:
> il coefficiente dell'istruzione **si prende anche il merito dell'abilità**.
>
> **L'esempio per la simultaneità**: prezzo e quantità di un bene sono
> determinati **congiuntamente** dall'equilibrio fra domanda e offerta, e non si
> riesce a distinguere l'effetto dei due.
>
> **Il rimedio sono le variabili strumentali**, in inglese *instrumental
> variables*. Si cerca una variabile che soddisfi **tre condizioni**:
> — **rilevanza**: dev'essere **correlata con il regressore endogeno**;
> — **esogeneità**: dev'essere **incorrelata con i disturbi**;
> — **esclusione**: **non deve influenzare direttamente la variabile
> dipendente**.
>
> L'esempio del manuale: per l'offerta di un bene alimentare si usano i
> **fattori meteorologici**, che influenzano l'offerta ma **non la domanda**.

**I pezzi**: legame fra regressori ed errore; le tre cause; l'esempio
istruzione-abilità; le tre condizioni con i loro nomi.

> **Perché è la domanda più importante**: l'endogeneità è **il motivo per cui
> correlazione non significa causalità**, ed è il problema centrale della
> valutazione d'impatto. È il punto in cui econometria e bando si toccano.

---

## 8. Quando una stima non si generalizza a dati nuovi? Che cos'è l'analisi di robustezza?
*(domande 129, 273)*

> Una stima **in-sample** misura quanto il modello si adatta **ai dati con cui è
> stato costruito**. Non garantisce nulla sulla capacità di funzionare su dati
> nuovi.
>
> Il motivo è il **sovra-adattamento**, l'*overfitting*: un modello troppo ricco
> finisce per **inseguire le particolarità di quel campione** — il rumore —
> invece della relazione vera. Su quei dati va benissimo; su altri crolla.
>
> Per verificarlo si **divide il campione**: una parte serve alla stima, una
> parte, mai vista dal modello, serve alla verifica. Oppure si usa la **convalida
> incrociata**, la *cross-validation*, che ripete questa divisione più volte.
>
> L'**analisi di robustezza** fa una cosa parallela: **si rifà la stima
> cambiando qualcosa** — il periodo, il sottogruppo, le variabili di controllo,
> la forma funzionale — e si guarda **se il risultato regge**. Un risultato che
> cambia segno al primo controllo non è un risultato.

**I pezzi**: in-sample ≠ previsione; overfitting; train/test e cross-validation;
robustezza = cambiare qualcosa e vedere se tiene.

---

## 9. Quali differenze esistono fra modello teorico e modello stimato?
*(domanda 130)*

> Il **modello teorico** è la relazione che la teoria economica ipotizza fra le
> grandezze: contiene **parametri incogniti**, indicati con lettere greche, e
> riguarda **l'intera popolazione**.
>
> Il **modello stimato** è quello che si ottiene **applicando un metodo di stima
> a un campione**: al posto dei parametri veri ci sono le **stime**, cioè numeri
> calcolati sui dati.
>
> **La differenza fondamentale è che il modello teorico è uno, le stime
> cambiano**: su un altro campione otterrei numeri diversi. Per questo accanto a
> ogni stima si riporta **l'errore standard**, che ne dichiara l'incertezza.
>
> E c'è una differenza di ruolo: **il modello teorico dice che cosa ci si
> aspetta e perché**; il modello stimato dice **che cosa i dati effettivamente
> mostrano**. Confrontarli è il modo in cui una teoria viene messa alla prova —
> ed è, in fondo, **il mestiere dell'econometria**.

**I pezzi**: parametri veri vs stime; popolazione vs campione; le stime cambiano
→ errore standard; il confronto è la verifica della teoria.

---

## 10. Che cosa significa cambiare la scala di una variabile?
*(domanda 120)*

> Significa **esprimere la stessa grandezza in un'unità di misura diversa**: il
> reddito in migliaia di euro invece che in euro, la spesa in milioni invece che
> in unità.
>
> **L'effetto è solo sui numeri, non sulla sostanza.** Il coefficiente cambia in
> modo proporzionale — se esprimo il reddito in migliaia, il coefficiente si
> moltiplica per mille — ma **l'R quadro non cambia**, **la significatività non
> cambia**, e **le conclusioni restano identiche**.
>
> **È l'errore tipico di chi legge una tabella senza guardare l'unità di
> misura**: due coefficienti di grandezza molto diversa possono dire esattamente
> la stessa cosa. **Prima di commentare un coefficiente bisogna sempre chiedersi
> in che unità sono espresse le variabili.**

**I pezzi**: stessa grandezza, unità diversa; il coefficiente cambia
proporzionalmente, le conclusioni no; guardare sempre l'unità di misura.

---

## 11. Che cosa sono i modelli a effetti fissi e a effetti casuali?
*(domande 125 e 126)* — ⚠️ *da verificare sulla parte del manuale non caricata*

> Sono due modi di trattare i **dati panel**, cioè i dati che seguono **più
> soggetti nel tempo** — per esempio cento comuni osservati per cinque anni.
>
> Il problema che risolvono è **l'eterogeneità non osservata**: ogni comune ha
> caratteristiche proprie e stabili — la cultura amministrativa, la qualità
> della macchina organizzativa — che **influenzano il risultato ma non si
> riescono a misurare**.
>
> Nel modello a **effetti fissi** si assegna a ciascun soggetto **un termine
> proprio**, che cattura tutto ciò che in lui è stabile nel tempo. In pratica
> **si confronta ogni comune con se stesso** nei vari anni, eliminando le sue
> caratteristiche fisse. Si usa quando quelle caratteristiche **possono essere
> correlate con le variabili esplicative**.
>
> Nel modello a **effetti casuali** l'eterogeneità è trattata come una
> **componente casuale**, che si assume **incorrelata con le variabili
> esplicative**. È più efficiente, ma **solo se quell'ipotesi regge**.
>
> **La scelta fra i due dipende da quell'ipotesi**: se l'eterogeneità individuale
> è correlata con i regressori, gli effetti casuali danno stime distorte e
> servono gli effetti fissi.

**I pezzi**: dati panel; eterogeneità non osservata; fissi = confronto del
soggetto con se stesso; casuali = più efficienti ma richiedono incorrelazione.

---

# La frase che tiene insieme tutto il blocco

Se dovessi riassumere l'intero capitolo in una frase da dire alla commissione:

> *«La regressione serve a misurare quanto una variabile incide su un'altra. I
> minimi quadrati danno la stima migliore possibile — **sotto certe ipotesi**. Il
> mestiere dell'econometrista non è calcolare quella stima: è **sapere quando
> quelle ipotesi cadono, e che cosa fare allora**.»*

**Tutte le domande di questo blocco sono variazioni su quella frase.**
