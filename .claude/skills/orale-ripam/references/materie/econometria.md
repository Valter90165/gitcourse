# Il programma in 10 sessioni

## Il criterio con cui è costruito

Il manuale dedica 300 pagine a questa materia, ma **le pagine non pesano tutte uguale all'orale**. Questo programma è pesato sul valore d'esame, non sulla lunghezza del capitolo:

- **due sessioni** sulla regressione semplice (giorni 3-4), perché è lo scheletro su cui poggia tutto il resto e perché «mi spieghi che cosa significa quell'R²» è la domanda più probabile dell'intera materia;
- **due sessioni** sulle patologie (giorni 6-7), organizzate come *«che cosa succede quando cade l'ipotesi N»* — il che le rende una conseguenza del giorno 3 anziché un elenco da memorizzare;
- **due sessioni** sulla valutazione controfattuale (giorni 9-10), perché è **il baricentro dichiarato del bando** e perché lì si gioca la differenza fra passare e passare bene;
- **una sola sessione** su serie storiche e panel (giorno 8): sono argomenti ad alto riconoscimento nominale e bassa profondità richiesta. Serve saperli collocare e nominare, non padroneggiarli.

Statistica descrittiva e calcolo delle probabilità (Parti I-V della dispensa) **non hanno una sessione dedicata**: entrano nel giorno 2 solo per la parte che serve a capire la regressione. Studiarle per intero sarebbe tempo tolto al controfattuale, che vale molto di più.

## La curva di difficoltà

I giorni 1-2 sono deliberatamente facili. Servono a costruire il vocabolario e la fiducia: chi parte dal capitolo difficile si convince di non essere portato e molla. I giorni 3-4 sono il vero lavoro. I giorni 6-7 sono i più tecnici. I giorni 9-10 sono i più importanti — e arrivano quando la macchina è calda.

---

# GIORNO 1 — Il vocabolario e la macchina

**Dispensa: §25-31** (Parte VI)

**Obiettivo della sessione.** Alla fine deve saper dire **che cosa fa un econometrico**, con parole sue e senza esitare. È la domanda d'apertura più probabile in assoluto, ed è anche quella che stabilisce il tono di tutto il colloquio.

**Che cosa insegnare**
- i **tre ingredienti**: teoria economica, matematica, statistica — e perché nessuno dei tre da solo basta;
- che cosa distingue l'econometria dalla statistica: **la teoria economica viene prima** e dice quali variabili guardare e con che segno atteso;
- i **tre tipi di dati**: serie storiche, cross section, panel;
- i **quattro stadi** della costruzione di un modello;
- **variabili endogene ed esogene**, **forma strutturale e forma ridotta**;
- perché un modello «fallisce».

**La metafora che funziona.** L'econometria è **il collaudo di una teoria**. La teoria economica dice *«il consumo dovrebbe dipendere dal reddito, e il coefficiente dovrebbe stare fra 0 e 1»*. L'econometria prende i dati e risponde *«sì, e vale 0,78 — con questo margine d'errore»*. Senza la teoria non sapresti nemmeno quali variabili mettere nel modello; senza i dati avresti una teoria invendibile.

**L'errore da prevenire.** Dire che l'econometria «applica la statistica all'economia». È la risposta di chi non ha capito: la statistica descrive, **l'econometria misura relazioni che una teoria ha ipotizzato**. Insisti su questa differenza — è il §25 della dispensa ed è una domanda frequente.

**L'aggancio da costruire.** Forma strutturale e forma ridotta tornano identiche in **politica economica** (dispensa 08, §10), dove servono al *policy maker* per sapere di quanto muovere la leva. Farlo notare subito abitua a ragionare per collegamenti.

---

# GIORNO 2 — Il ragionamento statistico che serve davvero

**Dispensa: §12-16** (Parte IV-V) — solo questi

**Obiettivo.** Deve saper spiegare **che cosa significa che un coefficiente è significativo**. Non calcolarlo: spiegarlo.

**Che cosa insegnare**
- **stimatore e stima**: il primo è la regola, la seconda il numero che esce. Distinzione che sembra pedante e non lo è;
- le **tre proprietà**: correttezza (non sbaglia sistematicamente), efficienza (sbaglia poco), consistenza (migliora al crescere del campione);
- l'**intervallo di confidenza** e che cosa significa davvero «al 95%»;
- la **logica del test**: ipotesi nulla, ipotesi alternativa, livello di significatività, p-value;
- i **due errori** e perché non sono simmetrici.

**La metafora che funziona.** Il test d'ipotesi è **un processo penale**. L'ipotesi nulla è la presunzione d'innocenza: *«questo coefficiente è zero, questa variabile non conta»*. I dati sono le prove. Rifiutare H₀ significa condannare, e lo si fa solo **oltre ogni ragionevole dubbio** — il 5%. L'**errore di primo tipo** è condannare un innocente, il **secondo tipo** assolvere un colpevole. Il sistema è costruito per temere di più il primo: ecco perché non sono simmetrici.

**L'errore da prevenire — e va marcato come grave.** Dire che il p-value è «la probabilità che l'ipotesi nulla sia vera». È falso ed è **l'errore più diffuso di tutta la statistica applicata**. Il p-value è **la probabilità di osservare un risultato così estremo SE l'ipotesi nulla fosse vera**. La differenza è tutta nel condizionamento, e una commissione tecnica la nota.

**La frase da costruire.** *«Significativo al 5% significa che, se questa variabile davvero non contasse, un risultato così grande lo osserverei per caso in meno di cinque casi su cento. Non significa che l'effetto sia grande, né che sia importante: significa solo che difficilmente è un caso.»*

---

# GIORNO 3 — La regressione semplice I: il modello e le sei ipotesi

**Dispensa: §32-35**

**Obiettivo.** Le **sei ipotesi classiche** con la patologia corrispondente a ciascuna. Non per memoria: perché i giorni 6-7 sono letteralmente *«che cosa succede quando cade la numero N»*, e chi arriva lì senza questo schema deve imparare tutto due volte.

**Che cosa insegnare**
- il modello **Y = β₀ + β₁X + ε** e il significato di ogni pezzo;
- componente **deterministica** e componente **stocastica** — perché l'errore c'è e che cosa rappresenta;
- **che cosa è β₁**: la variazione di Y per una variazione unitaria di X;
- il criterio dei **minimi quadrati**, a parole: la retta che rende minima la somma dei quadrati degli scarti. E **perché i quadrati**: perché scarti di segno opposto non si compensino;
- le **sei ipotesi**, ciascuna con il nome della patologia che nasce dalla sua caduta.

**Il modo di presentare le sei ipotesi che le rende memorabili.** Non come elenco, ma come **tabella a due colonne: l'ipotesi e la malattia**. Linearità → errore di specificazione. Media degli errori nulla → distorsione. Omoschedasticità → **eteroschedasticità** (giorno 6). Assenza di autocorrelazione → **autocorrelazione** (giorno 7). Esogeneità del regressore → **endogeneità** (giorno 7, ed è la più grave). Normalità → problemi nei test. Chi possiede questa tabella ha già in mano la struttura di metà corso.

**L'errore da prevenire.** Confondere **l'errore ε** (teorico, non osservabile, della popolazione) con **il residuo e** (calcolato, osservabile, del campione). La commissione può chiederlo espressamente ed è una distinzione che rivela subito il livello.

---

# GIORNO 4 — La regressione semplice II: leggere un output

**Dispensa: §36-42**

**Obiettivo.** Saper **leggere a voce alta un output di regressione**, riga per riga. È l'esercizio più vicino a ciò che la commissione può mettergli davanti.

**Che cosa insegnare**
- la **scomposizione della devianza**: totale = spiegata + residua;
- l'**R²**: che cos'è, come si interpreta, e — decisivo — **che cosa NON dice**;
- **Gauss-Markov** e il significato di **BLUE**;
- il **test t** sui coefficienti e come si legge;
- cenni di **ANOVA** e test F.

**La metafora per l'R².** L'R² è **la quota di variabilità di Y che il modello riesce a spiegare**. Se vale 0,85, l'85% dell'altalenarsi di Y è catturato dal modello e il 15% resta fuori. Ma — e qui sta il punto che vale i punti — **un R² alto non dice che il modello è giusto, né che la relazione è causale, né che le variabili servono**. Un R² del 95% ottenuto mettendo dentro venti variabili a caso non vale nulla, ed è precisamente per questo che esiste l'**R² corretto** (giorno 5).

**L'errore da prevenire — grave.** *«R² alto quindi il modello è buono.»* È la risposta che separa chi ha capito da chi ha memorizzato. Se Valter la dà, fermalo e chiedi: *«e se avessi messo vent'anni di dati e trenta variabili?»*

**Esercizio da fare in sessione.** Inventa un output di regressione realistico — coefficienti, errori standard, t, p-value, R², F — e faglielo commentare riga per riga come se fosse alla lavagna. Correggi l'ordine con cui lo legge: prima il segno e la grandezza del coefficiente, poi la significatività, poi l'adattamento complessivo. **Mai partire dall'R².**

---

# GIORNO 5 — Interpretare i coefficienti: forme funzionali e dummy

**Dispensa: §45 (per intero), §46-48, §51-52, §54**

**Obiettivo.** Due cose, entrambe ad altissima resa: **dire che cosa significa un coefficiente a seconda della forma funzionale**, e **le variabili dummy** — che sono il ponte verso la valutazione delle politiche.

**Che cosa insegnare**
- le **forme funzionali** con l'interpretazione del coefficiente: lineare (variazione assoluta), **doppio logaritmico = elasticità costante** — il caso più importante, ed è la Cobb-Douglas —, semilogaritmico (variazione percentuale), iperbolico (curva di Phillips);
- il passaggio alla **multipla** e la formula magica **«a parità delle altre variabili»**;
- **R² corretto** e perché esiste;
- le **variabili dummy**: come si costruiscono, la **trappola della dummy** (se ci sono k categorie se ne mettono k−1), e le **interazioni**.

**Perché le dummy contano più di quanto sembri.** Una dummy che vale 1 per chi ha ricevuto un incentivo e 0 per chi no, con il suo coefficiente, **è già una valutazione di politica pubblica in forma elementare**. Il giorno 9 non farà altro che chiedersi *sotto quali condizioni quel coefficiente misuri davvero un effetto causale*. Dirlo esplicitamente qui prepara il terreno e fa vedere il disegno.

**L'errore da prevenire.** Dimenticare **«a parità delle altre variabili»** quando interpreta un coefficiente della multipla. Non è una formula di cortesia: **è il significato stesso del coefficiente parziale**. Ogni volta che la omette, correggi.

---

# GIORNO 6 — Quando le ipotesi cadono I: multicollinearità ed eteroschedasticità

**Dispensa: §55-59, §64-67**

**Obiettivo.** Per ciascuna patologia, saper dire **quattro cose in fila**: che cos'è, perché è un problema, come si diagnostica, che cosa si fa.

**Che cosa insegnare**
- **multicollinearità**: regressori troppo correlati fra loro; gli effetti (stime instabili, errori standard gonfiati, **coefficienti non significativi presi uno per uno ma R² alto**); diagnosi con il **VIF**; i rimedi;
- **eteroschedasticità**: varianza degli errori non costante; **gli stimatori restano corretti ma non sono più efficienti** — quindi il danno è sui test, non sui coefficienti; diagnosi con **Breusch-Pagan**, **Goldfeld-Quandt** e l'esame grafico dei residui; rimedio con **GLS/WLS**.

**La distinzione che vale i punti — insisti.** *«Le stime restano corrette ma non sono più efficienti, e soprattutto gli errori standard sono sbagliati: quindi il problema non è il valore del coefficiente, è che non posso più fidarmi dei test di significatività.»* Chi sa dire questo dimostra di aver capito; chi dice solo «la varianza non è costante» ha ripetuto una definizione.

**Il sintomo che rivela la multicollinearità — è un'ottima cosa da sapere.** Un modello in cui **nessun coefficiente è significativo preso singolarmente ma l'R² è alto e il test F rifiuta**: è la firma della multicollinearità. Le variabili spiegano, ma il modello non riesce ad attribuire il merito a nessuna in particolare.

---

# GIORNO 7 — Quando le ipotesi cadono II: autocorrelazione ed endogeneità

**Dispensa: §68, §63**

**Obiettivo.** L'**endogeneità** è la patologia più grave e **il ponte verso i giorni 9-10**. Va capita, non nominata.

**Che cosa insegnare**
- **autocorrelazione**: errori correlati nel tempo; tipica delle serie storiche; **Durbin-Watson** e la sua regola di lettura; **Breusch-Godfrey**; rimedi (Cochrane-Orcutt, Hildreth-Lu);
- **endogeneità**: il regressore è correlato con l'errore. **Qui l'OLS è distorto E inconsistente** — cioè non migliora nemmeno aumentando i dati. È la differenza che rende questa patologia più grave delle altre due;
- le **tre cause**: variabili omesse, errori di misura, simultaneità;
- le **variabili strumentali** e le **tre condizioni** che uno strumento deve soddisfare: rilevanza, esogeneità, esclusione.

**La metafora per le variabili strumentali.** Uno strumento è **una leva che muove X ma non tocca Y se non passando per X**. Se voglio misurare l'effetto dell'istruzione sul reddito, la distanza da casa all'università più vicina è un candidato: **influenza quanto studi** (rilevanza), ma **non c'è ragione che influenzi il tuo reddito se non attraverso l'istruzione** (esclusione). Serve perché l'istruzione è endogena: chi studia di più ha anche caratteristiche non osservate — famiglia, capacità — che influenzano il reddito per conto loro.

**Il collegamento da fare esplicitamente.** *«Il problema che le variabili strumentali risolvono è esattamente il problema della valutazione controfattuale: distinguere la correlazione dalla causalità quando chi riceve il trattamento non è scelto a caso.»* Detto qui, il giorno 9 comincia già in discesa.

---

# GIORNO 8 — Dati nel tempo e dati nello spazio

**Dispensa: §73-79 (serie storiche), §80-85 (panel)**

**Obiettivo.** Sessione **di collocamento, non di padronanza**. Deve saper nominare e situare, con una frase corretta per ciascun argomento. Non spendere tempo in dettagli: il ritorno d'esame è basso.

**Che cosa insegnare — serie storiche**
- le **quattro componenti**: trend, ciclo, stagionalità, accidentale;
- i modelli decompositivi (additivo, moltiplicativo);
- **AR, MA, ARMA, ARIMA** — solo l'idea: il valore di oggi spiegato dai valori passati o dagli errori passati;
- la **procedura di Box-Jenkins in cinque passi**: identificazione, stima, verifica, previsione;
- **TRAMO-SEATS dell'ISTAT** — il paragrafo più «da concorso» del capitolo, perché è **la procedura che l'istituto nazionale di statistica usa davvero** per la destagionalizzazione. Progetto SARA, 1997; in uso dal febbraio 1999.

**Che cosa insegnare — panel**
- che cos'è un panel e **perché conviene**: segue gli stessi soggetti nel tempo, quindi **controlla le caratteristiche non osservate che non cambiano**;
- **effetti fissi** (stimatore *within*) ed **effetti casuali**;
- il ***trade-off***: effetti fissi sempre consistenti ma meno efficienti; effetti casuali più efficienti ma solo se l'effetto individuale non è correlato con i regressori;
- il **test di Hausman**, che è precisamente il test di quella condizione.

**Perché TRAMO-SEATS vale una menzione all'orale.** Nominarlo dimostra di sapere **come si fa il lavoro in un'amministrazione statistica**, non solo come si fa in teoria. In un concorso per funzionari, questa è credibilità istituzionale — la stessa cosa che vale citare l'art. 53 Cost. in scienza delle finanze.

---

# GIORNO 9 — La valutazione controfattuale I: il problema e le ipotesi

**Dispensa: §86-90, §91 (parte su propensity score)**

**Obiettivo.** Qui si decide il voto. Deve possedere **il problema fondamentale dell'inferenza causale** e saperlo spiegare a qualcuno che non lo conosce.

**Che cosa insegnare**
- **fattuale e controfattuale**: che cosa è successo e che cosa sarebbe successo senza l'intervento;
- il **modello causale di Rubin (1974)** e l'**ATT**;
- **il problema fondamentale**: di ogni singolo soggetto osserviamo **un solo esito**. Il controfattuale non è difficile da misurare: **è impossibile da osservare**. Tutto il resto della materia è il tentativo di costruirne una buona approssimazione;
- i **due metodi ingenui** e le loro distorsioni: il **prima-dopo** (confuso dalla dinamica spontanea) e il **confronto fra partecipanti e non partecipanti** (confuso dal ***selection bias***);
- le **ipotesi fondamentali**: **SUTVA**, ***common support***, **CIA**;
- il **propensity score** di Rosenbaum e Rubin, con i quattro algoritmi di *matching*.

**La metafora che regge tutto il giorno.** Un corso di formazione per disoccupati. I partecipanti trovano lavoro nel 40% dei casi, i non partecipanti nel 25%. **Il corso funziona?** Non lo sappiamo: chi si iscrive a un corso è probabilmente **più motivato**, e sarebbe stato più bravo a trovare lavoro anche senza. Quel 15 punti di differenza è **effetto del corso + effetto della motivazione**, e non sappiamo come dividerlo. **È il selection bias**, e tutta la materia è costruita per neutralizzarlo.

**L'errore da prevenire — grave.** Dire che il controfattuale «si stima con i dati prima dell'intervento». È il metodo prima-dopo, ed è **uno dei due metodi ingenui**: confonde l'effetto della politica con tutto ciò che sarebbe cambiato comunque. Se il PIL cresce dopo l'incentivo, non sai se è per l'incentivo o per la ripresa.

---

# GIORNO 10 — La valutazione controfattuale II: le strategie + simulazione

**Dispensa: §91 (per intero), §92**

**Obiettivo.** Le **tre strategie** con i loro presupposti, e — nella seconda metà — **la simulazione d'orale completa**.

**Che cosa insegnare**
- **RCT**, l'assegnazione casuale: il *gold standard*, perché risolve il *selection bias* per costruzione, e i suoi limiti pratici ed etici;
- **differenza-nelle-differenze**: il meccanismo delle due differenze, e **l'ipotesi dei trend paralleli** — che è tutto ciò su cui il metodo poggia, e va nominata sempre;
- **regressione discontinua (RDD)**: la soglia, e perché chi sta appena sopra e appena sotto è confrontabile;
- i **quattro aspetti dell'interpretazione**: *lock-in*, *compliance*, attrito, comunicazione dei risultati.

**Il DiD spiegato in modo che resti.** Due gruppi, due momenti. Prendo la variazione del gruppo trattato e **le sottraggo la variazione del gruppo di controllo**. La prima differenza toglie tutto ciò che è fisso nei gruppi; la seconda toglie tutto ciò che è cambiato per tutti. **Quel che resta è l'effetto.** Regge su una sola ipotesi: **che senza l'intervento i due gruppi avrebbero continuato a muoversi in parallelo**. Non è verificabile per il periodo del trattamento — si controlla sui periodi precedenti.

**La seconda metà della sessione: simulazione.** 20 minuti in modalità commissione, con il caso integrato:

> *«Il Governo introduce un credito d'imposta per le assunzioni nel Mezzogiorno. Le viene chiesto di valutarne l'efficacia. Come procede?»*

Una risposta completa contiene: la **domanda di valutazione** ben posta; il **controfattuale** e perché non si osserva; la **strategia scelta con la sua giustificazione** (qui il DiD è naturale — c'è una data e c'è un'area geografica — ma un RDD sulla soglia dimensionale d'impresa è altrettanto difendibile); **l'ipotesi identificante dichiarata** e come si controlla; **le minacce alla validità**; e **che cosa si risponde al committente**, che è la parte che quasi tutti dimenticano e che in un concorso per funzionari pesa.

Alla fine: **voto motivato**, con la scala di `../metodo.md`, e il piano dei giorni successivi.
