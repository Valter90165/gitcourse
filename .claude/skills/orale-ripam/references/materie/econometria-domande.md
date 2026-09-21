# Banca delle domande

Per ogni domanda trovi **che cosa deve contenere una risposta completa**. Non è la risposta da leggere: è la griglia con cui giudicare quella di Valter. Se mancano gli elementi marcati **[decisivo]**, la risposta non è sufficiente per quanto sia ben detta.

Le domande contrassegnate **►** sono quelle a più alta probabilità: se il tempo stringe, sono quelle da non saltare.

---

## Giorno 1 — Vocabolario e macchina

**1.1 ► Che cos'è l'econometria e in che cosa si distingue dalla statistica?**
Tre ingredienti: teoria economica, matematica, statistica. **[decisivo]** La differenza con la statistica: **la teoria viene prima** e dice quali variabili guardare e con quale segno atteso. La statistica descrive ciò che c'è; l'econometria **misura una relazione che una teoria ha ipotizzato**, e la sottopone a verifica.

**1.2 Quali tipi di dati usa l'econometria?**
Serie storiche (stesso soggetto nel tempo), cross section (soggetti diversi in un istante), panel (stessi soggetti nel tempo). Bene se aggiunge che **il panel è il più ricco** e perché — anticipa il giorno 8.

**1.3 I quattro stadi della costruzione di un modello.**
Specificazione, stima, verifica, previsione/uso. Bene se collega ciascuno a una domanda: *che forma ha la relazione? quanto valgono i parametri? il modello regge? che cosa me ne faccio?*

**1.4 ► Distingua forma strutturale e forma ridotta.**
Strutturale: le endogene compaiono anche a destra, il modello riflette la teoria. Ridotta: **ogni endogena espressa solo in funzione delle esogene**. **[decisivo]** A che serve: la ridotta permette di calcolare direttamente l'effetto di una variabile di controllo — è **la forma che serve al decisore**.

**1.5 Perché un modello fallisce?**
Specificazione errata, variabili omesse, dati inadeguati, instabilità dei parametri. Se nomina l'instabilità, ottimo aggancio alla critica di Lucas (politica economica, §15).

---

## Giorno 2 — Il ragionamento statistico

**2.1 Differenza fra stimatore e stima.**
Lo stimatore è **la regola** (una funzione del campione), la stima è **il numero** che esce applicandola. Lo stimatore è una variabile casuale, la stima no.

**2.2 ► Le tre proprietà desiderabili di uno stimatore.**
**Correttezza** (in media colpisce il bersaglio: nessun errore sistematico), **efficienza** (varianza minima fra i corretti: sbaglia poco), **consistenza** (converge al valore vero al crescere del campione). **[decisivo]** Saper dire che correttezza ed efficienza sono **cose diverse**: si può essere corretti e imprecisi.

**2.3 ► Che cosa significa che un coefficiente è significativo al 5%?**
**[decisivo]** Che **se quella variabile non contasse davvero**, un risultato così estremo lo osserverei per caso in meno di cinque casi su cento. **Non** significa che l'effetto sia grande né importante. Se dice «c'è il 95% di probabilità che il coefficiente sia diverso da zero», **correggi: è l'errore classico**.

**2.4 Che cos'è il p-value?**
La probabilità di osservare un risultato **almeno così estremo, DATO che l'ipotesi nulla è vera**. **[decisivo]** Non è la probabilità che H₀ sia vera. Marca l'errore come grave se compare.

**2.5 I due errori, e perché non sono simmetrici.**
Primo tipo: rifiutare H₀ vera (condannare un innocente). Secondo tipo: accettare H₀ falsa. **[decisivo]** Non sono simmetrici perché **fissiamo noi α** al 5%, scegliendo deliberatamente di temere di più il primo. β dipende dalla potenza del test.

---

## Giorno 3 — Regressione semplice I

**3.1 ► Che cosa rappresenta β₁ nel modello Y = β₀ + β₁X + ε?**
**La variazione attesa di Y per una variazione unitaria di X.** **[decisivo]** Nella multipla, **a parità delle altre variabili**. Se questa clausola manca, la risposta è incompleta.

**3.2 Perché c'è il termine di errore?**
Rappresenta tutto ciò che influenza Y e non è nel modello: variabili omesse, errori di misura, casualità intrinseca del comportamento umano. **[decisivo]** È ciò che distingue una relazione **statistica** da una relazione **deterministica**.

**3.3 ► Che cos'è il metodo dei minimi quadrati?**
Si sceglie la retta che **rende minima la somma dei quadrati degli scarti** fra valori osservati e valori teorici. **[decisivo]** Perché i quadrati: perché scarti di segno opposto **non si compensino** — e secondariamente perché penalizza di più gli errori grandi. Non serve che sappia derivarlo.

**3.4 ► Le sei ipotesi classiche.**
Linearità · media degli errori nulla · omoschedasticità · assenza di autocorrelazione · esogeneità dei regressori · normalità. **[decisivo]** Per almeno tre di esse deve saper dire **quale patologia nasce quando cadono**. Se le recita senza le conseguenze, la risposta è mnemonica.

**3.5 Differenza fra errore e residuo.**
L'errore **ε** è teorico, della popolazione, **non osservabile**. Il residuo **e** è calcolato, del campione, **osservabile**: è la differenza fra valore osservato e valore stimato. **[decisivo]** Il residuo è **la stima campionaria** dell'errore.

---

## Giorno 4 — Regressione semplice II

**4.1 ► Che cosa significa un R² di 0,85?**
Che **l'85% della variabilità di Y è spiegata dal modello**; il 15% resta nei residui. **[decisivo]** E poi — questa parte vale quanto la prima — **che cosa NON dice**: non dice che il modello è ben specificato, non dice che la relazione è causale, non dice che le variabili servono davvero.

**4.2 ► Un R² alto significa che il modello è buono?**
**No.** **[decisivo]** L'R² **cresce sempre** aggiungendo variabili, anche irrilevanti: per questo esiste l'**R² corretto**, che penalizza il numero di regressori. E un R² alto è perfettamente compatibile con un modello mal specificato o con una relazione spuria.

**4.3 La scomposizione della devianza.**
Devianza totale = devianza spiegata + devianza residua. **[decisivo]** L'R² è **il rapporto fra spiegata e totale**.

**4.4 ► Che cosa afferma il teorema di Gauss-Markov?**
Sotto le ipotesi classiche, **lo stimatore OLS è BLUE**: *Best Linear Unbiased Estimator* — **il più efficiente fra gli stimatori lineari e corretti**. **[decisivo]** Deve saper sciogliere l'acronimo e dire che **vale solo sotto le ipotesi**: è precisamente quello che si rompe nei giorni 6-7.

**4.5 Come si legge un output di regressione?**
Ordine corretto: **segno e grandezza del coefficiente** (ha il segno che la teoria prevede? l'ordine di grandezza è plausibile?) → **significatività** (t e p-value) → **adattamento complessivo** (R², F). **[decisivo]** Partire dall'R² è l'ordine sbagliato: il coefficiente è la risposta alla domanda economica, l'R² è solo una misura di quanto resta fuori.

---

## Giorno 5 — Forme funzionali e dummy

**5.1 ► Nel modello doppio logaritmico, che cosa rappresenta il coefficiente?**
**L'elasticità** — la variazione percentuale di Y per una variazione dell'1% di X. **[decisivo]** Ed è **costante** lungo tutta la curva, che è la ragione per cui questa forma è così usata. È la forma della **Cobb-Douglas**.

**5.2 Che cosa cambia nel semilogaritmico?**
Se il log è solo su Y, il coefficiente è **la variazione percentuale di Y** per una variazione unitaria (assoluta) di X. Utile per tassi di crescita.

**5.3 ► Che cosa significa «a parità delle altre variabili»?**
Che il coefficiente misura **l'effetto di quella variabile tenendo ferme tutte le altre del modello** — cioè al netto di ciò che le altre spiegano. **[decisivo]** È **il significato stesso del coefficiente parziale**, non una cautela retorica.

**5.4 ► Che cosa sono le variabili dummy e qual è la trappola?**
Variabili 0/1 che rappresentano caratteristiche qualitative. **[decisivo] La trappola**: con k categorie se ne inseriscono **k−1**, altrimenti si cade in collinearità perfetta. La categoria esclusa è **il riferimento**, e i coefficienti vanno letti rispetto a quella.

**5.5 A che serve un'interazione?**
A far sì che **l'effetto di una variabile dipenda dal livello di un'altra**. Ottimo se collega: *«un'interazione fra dummy di trattamento e dummy di periodo è esattamente la differenza-nelle-differenze»* — è il ponte al giorno 10.

---

## Giorno 6 — Multicollinearità ed eteroschedasticità

**6.1 ► Che cos'è la multicollinearità e perché è un problema?**
Regressori fortemente correlati fra loro. **[decisivo]** Il danno: **stime instabili ed errori standard gonfiati**, quindi coefficienti che risultano non significativi anche quando la variabile conta. **Il modello spiega, ma non riesce ad attribuire il merito.**

**6.2 Come si diagnostica?**
Matrice di correlazione, **VIF** (valori sopra 5-10 segnalano un problema), numero di condizionamento. **[decisivo]** Il sintomo rivelatore: **nessun coefficiente significativo singolarmente, ma R² alto e test F che rifiuta**.

**6.3 ► Che cos'è l'eteroschedasticità e che danno fa?**
Varianza degli errori non costante. **[decisivo] Gli stimatori restano corretti ma non sono più efficienti**, e soprattutto **gli errori standard sono sbagliati**: quindi il problema **non è il valore del coefficiente, è che i test di significatività non sono più affidabili**. Se dice solo «la varianza non è costante», chiedi il seguito.

**6.4 Come si diagnostica l'eteroschedasticità?**
Esame grafico dei residui (il tipico «cono»), **Breusch-Pagan**, **Goldfeld-Quandt**, White.

**6.5 Che cosa si fa?**
**GLS/WLS** — ponderare le osservazioni in modo inverso alla loro varianza. In pratica, oggi, spesso si usano **errori standard robusti**, che correggono i test lasciando le stime OLS.

---

## Giorno 7 — Autocorrelazione ed endogeneità

**7.1 Che cos'è l'autocorrelazione?**
Errori correlati fra loro nel tempo. Tipica delle **serie storiche**. Stessa struttura di danno dell'eteroschedasticità: **stime corrette, ma test inaffidabili**.

**7.2 Come si diagnostica?**
**Durbin-Watson** — valore intorno a 2 significa assenza, vicino a 0 autocorrelazione positiva, vicino a 4 negativa. **Breusch-Godfrey** è più generale. Rimedi: Cochrane-Orcutt, Hildreth-Lu.

**7.3 ► Che cos'è l'endogeneità e perché è più grave delle altre patologie?**
Il regressore è **correlato con il termine d'errore**. **[decisivo]** È più grave perché **l'OLS diventa distorto E inconsistente**: a differenza di eteroschedasticità e autocorrelazione, **il problema non si risolve aumentando i dati**.

**7.4 ► Le tre cause dell'endogeneità.**
**Variabili omesse** (una variabile rilevante finisce nell'errore ed è correlata con X), **errori di misura** su X, **simultaneità** (X e Y si determinano a vicenda). Ottimo se porta un esempio per ciascuna.

**7.5 ► Che cos'è una variabile strumentale e quali condizioni deve soddisfare?**
Una variabile che influenza X ma non Y se non attraverso X. **[decisivo]** Le tre condizioni: **rilevanza** (correlata con X), **esogeneità** (incorrelata con l'errore), **esclusione** (non influenza Y direttamente). Chiedi sempre un esempio: se non sa produrne uno, il concetto non è posseduto.

---

## Giorno 8 — Serie storiche e panel

**8.1 Le quattro componenti di una serie storica.**
Trend, ciclo, stagionalità, componente accidentale. Modelli additivo e moltiplicativo.

**8.2 Che cosa sono i modelli ARIMA?**
AR: il valore di oggi spiegato dai **valori passati**. MA: dagli **errori passati**. ARMA li combina; ARIMA aggiunge la **differenziazione** per rendere stazionaria la serie. Non serve di più.

**8.3 La procedura di Box-Jenkins.**
Cinque passi: stazionarizzazione, **identificazione** (ACF e PACF), stima, **verifica** sui residui, previsione. È un processo **iterativo**, non lineare.

**8.4 ► Che cos'è TRAMO-SEATS e perché conta?**
La procedura di **destagionalizzazione usata dall'ISTAT**. TRAMO pre-tratta la serie (valori anomali, dati mancanti), SEATS scompone. **[decisivo]** Perché conta: **è come si fa il lavoro davvero in un'amministrazione statistica**. Progetto SARA 1997, in uso dal febbraio 1999.

**8.5 ► Effetti fissi o effetti casuali? Come si sceglie?**
Effetti fissi: **sempre consistenti**, ma consumano gradi di libertà e non stimano variabili invarianti nel tempo. Effetti casuali: **più efficienti**, ma **solo se l'effetto individuale non è correlato con i regressori**. **[decisivo]** Si sceglie con il **test di Hausman**, che verifica precisamente quella correlazione.

---

## Giorno 9 — Controfattuale I

**9.1 ► Che cos'è il controfattuale?**
**Che cosa sarebbe successo ai destinatari se la politica non ci fosse stata.** **[decisivo]** E subito: **è impossibile da osservare**, perché di ogni soggetto vediamo un solo esito. Non è difficile: è impossibile. **Tutta la materia è il tentativo di costruirne una buona approssimazione.**

**9.2 ► Che cos'è l'ATT?**
*Average Treatment effect on the Treated*: **l'effetto medio del trattamento sui trattati** — la differenza fra l'esito osservato dei trattati e quello che gli stessi trattati avrebbero avuto senza trattamento.

**9.3 ► I due metodi ingenui e le loro distorsioni.**
**Prima-dopo**: confonde l'effetto della politica con **la dinamica spontanea** — tutto ciò che sarebbe cambiato comunque. **Partecipanti contro non partecipanti**: confonde l'effetto con il ***selection bias***, perché chi partecipa è sistematicamente diverso. **[decisivo]** Deve saper nominare entrambe le distorsioni, non solo i metodi.

**9.4 ► Che cos'è il selection bias? Me ne dia un esempio.**
La distorsione che nasce quando **chi riceve il trattamento differisce sistematicamente da chi non lo riceve**, per caratteristiche che influenzano anche l'esito. L'esempio del corso di formazione: i partecipanti sono **più motivati**, e avrebbero trovato lavoro più facilmente anche senza il corso.

**9.5 ► Le ipotesi fondamentali del metodo controfattuale.**
**SUTVA** (il trattamento di uno non influenza l'esito degli altri — cade se ci sono effetti di spiazzamento), ***common support*** (per ogni trattato deve esistere un non trattato comparabile), **CIA** (condizionatamente alle variabili osservate, l'assegnazione è come casuale).

**9.6 Che cos'è il propensity score?**
La **probabilità stimata di ricevere il trattamento** date le caratteristiche osservate. Di Rosenbaum e Rubin. Serve a **ridurre molte variabili a un solo numero** su cui appaiare trattati e non trattati. **[decisivo]** Il limite: **corregge solo per ciò che si osserva** — se la selezione avviene su caratteristiche non osservate (la motivazione), il *matching* non basta.

---

## Giorno 10 — Controfattuale II

**10.1 ► Che cos'è la differenza-nelle-differenze e su quale ipotesi poggia?**
Due gruppi, due momenti: si prende la variazione dei trattati e **le si sottrae la variazione dei controlli**. **[decisivo]** L'ipotesi: **trend paralleli** — senza l'intervento i due gruppi avrebbero continuato a muoversi in parallelo. Non è verificabile nel periodo di trattamento; **si controlla sui periodi precedenti**. Se omette i trend paralleli, la risposta è gravemente incompleta.

**10.2 ► Perché l'assegnazione casuale risolve il problema?**
Perché **rende i due gruppi equivalenti in media su tutto** — osservato e non osservato. **[decisivo]** È l'unico metodo che neutralizza anche le caratteristiche che non misuriamo. I limiti: costi, tempi, e soprattutto problemi **etici e politici** nell'escludere qualcuno da un beneficio.

**10.3 ► Che cos'è la regressione discontinua?**
Si sfrutta una **soglia** che determina l'accesso al trattamento. **[decisivo]** L'idea: chi sta **appena sopra e appena sotto** la soglia è sostanzialmente identico, salvo il trattamento — quindi il confronto locale è credibile. Il limite: **l'effetto stimato vale solo intorno alla soglia**, non per tutta la popolazione.

**10.4 Che cos'è l'effetto di lock-in?**
I partecipanti a un programma, mentre vi sono impegnati, **riducono la ricerca di lavoro**: nel breve periodo l'effetto misurato può risultare negativo pur essendo il programma efficace. **[decisivo]** Implica che **il momento della misurazione conta**.

**10.5 ►► LA DOMANDA DI COLLEGAMENTO — il Governo introduce un credito d'imposta per le assunzioni al Sud. Come ne valuta l'efficacia?**
Griglia per giudicare:
1. **la domanda di valutazione** posta bene (di che effetto parliamo? su chi? in che orizzonte?);
2. **il controfattuale nominato** e detto che non si osserva;
3. **la strategia scelta con giustificazione** — DiD è naturale (c'è una data e un'area); RDD è difendibile se c'è una soglia dimensionale; se propone un RCT, deve riconoscerne l'impraticabilità politica;
4. **l'ipotesi identificante dichiarata** e come la controlla (trend pre-intervento);
5. **le minacce**: effetti di spiazzamento fra imprese confinanti (**cade la SUTVA**), anticipazione, sostituzione fra tipi di contratto;
6. **che cosa si risponde al committente** — la parte che quasi tutti dimenticano, e che in un concorso per funzionari pesa quanto la tecnica.

**Una risposta che copre 1-4 vale 24-26. Una che copre tutto vale 28-30.**
