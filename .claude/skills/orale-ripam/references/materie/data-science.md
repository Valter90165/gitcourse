# Data science e data mining — 3 sessioni

**Dispensa 04** (27 pp). Fascia: **sostegno tecnico**.

**Il carattere della materia.** La scheda Simone su Drive copre **solo l'impianto metodologico** ed è lunga sei pagine; il resto della dispensa è **integrazione dichiarata come tale**. Non è materia da manuale: è materia da **saper collocare**, con una robusta appendice sulla P.A. italiana che è la parte che conta di più per questo concorso.

---

## Sessione 1 — Il processo: KDD e CRISP-DM
**Dispensa §1-10**

Definizioni; **data science, data mining e KDD a confronto**; **le cinque fasi del KDD**; **i sei passi operativi**; il **modello CRISP-DM** e le sue sei fasi; il confronto finale.

**Il punto che vale.** **CRISP-DM è ciclico, non lineare**: dalla valutazione si torna alla comprensione del business. È la differenza fra un progetto analitico e una relazione scritta una volta per tutte — e in un'amministrazione è precisamente il punto.

## Sessione 2 — Dati, pre-processing, algoritmi
**Dispensa §11-30 circa**

Tassonomia dei dati e **scale di misura**; **le sei dimensioni della qualità**; **le cinque V** dei big data; **valori mancanti** (MCAR/MAR/MNAR), **outlier**, normalizzazione, variabili categoriali, **riduzione dimensionale** e maledizione della dimensionalità, **bilanciamento delle classi**; le **tre famiglie** del machine learning; **bias-varianza**; validazione; gli algoritmi fondamentali; **matrice di confusione, ROC-AUC, silhouette**.

**La cosa da far pesare.** **Il pre-processing è la parte lunga del lavoro** — tipicamente l'80% del tempo. Un candidato che parla solo di algoritmi rivela di non aver mai lavorato su dati veri. **Chi parla di dati mancanti e sbilanciamento delle classi ha credibilità.**

**L'errore da prevenire.** Confondere **accuratezza** e utilità del modello. Su dati sbilanciati al 99/1, un modello che dice sempre «no» ha il 99% di accuratezza ed è inutile. **Per questo esistono precisione, richiamo e ROC-AUC.**

## Sessione 3 — Dati e algoritmi nella P.A. italiana
**Dispensa: la parte finale**

**CAD e PDND**; **open data** e D.Lgs. 200/2021; **text mining** sugli atti; usi concreti nel settore pubblico; **i tre principi del Consiglio di Stato** (sentenze 2270/2019 e 8472/2019: conoscibilità, non esclusività della decisione algoritmica, non discriminazione); **art. 22 GDPR**; **AI Act**; **bias algoritmico**; **SISTAN e segreto statistico**.

**Perché questa sessione vale le altre due insieme.** È l'unica in cui la materia diventa **diritto amministrativo applicato all'algoritmo**, ed è il terreno su cui una commissione per funzionari pubblici vuole vedere maturità. **I tre principi del Consiglio di Stato sono la cosa da sapere a memoria.**

**Il collegamento.** L'**asimmetria informativa** di scienza delle finanze §21 è il problema che i dati risolvono; l'**evasione fiscale** è affrontata con *anomaly detection*; i **fabbisogni standard** sono costruiti con modelli di regressione. **La data science non è una materia a sé: è il come si fa il resto.**
