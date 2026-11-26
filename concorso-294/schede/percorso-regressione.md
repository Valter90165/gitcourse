# La regressione nelle due materie — percorso di chiusura

*Costruito il 26 novembre 2026, su richiesta di Silvia: «aiutami a costruire
un percorso per capire queste cose all'interno delle due materie».*
*Fonti: manuale (Parte III, capitoli 6-12 e 16) + elenco dei 375 quesiti attestati.*

---

## LA CHIAVE — un solo strumento, due domande

La retta di regressione e' **la stessa cosa** in econometria e in data science.
Quello che cambia non e' la matematica: e' **la domanda che le rivolgi**.

| | **REGRESSIONE ESPLICATIVA** | **REGRESSIONE PREDITTIVA** |
|---|---|---|
| **Materia** | Econometria | Data science |
| **Domanda** | *Quanto conta X su Y?* | *Quanto bene indovino Y?* |
| **Cosa guardo** | **il coefficiente** | **la previsione** |
| **Dove misuro** | **dentro** il campione | **fuori** campione |
| **Il nemico** | la **distorsione** (variabile omessa, endogeneita') | l'**overfitting** |
| **Il controllo** | le ipotesi del modello, BLUE, errore standard, significativita' | training / validation / test, cross-validation |
| **L'indicatore** | R quadro = quota di varianza spiegata (mai negativo) | MAE, RMSE, R quadro fuori campione (**puo' essere negativo**) |
| **Il successo** | un coefficiente **corretto** | un errore **piccolo su dati nuovi** |

**La frase che tiene tutto insieme:**
> «La regressione e' una sola. In econometria mi interessa il coefficiente e lo
> voglio non distorto. In data science mi interessa la previsione e la voglio
> accurata su dati nuovi. Un modello puo' prevedere benissimo con coefficienti
> privi di senso causale, e un modello causalmente corretto puo' prevedere male.»

Questa frase, da sola, risponde a **quattro quesiti attestati** (112, 129, 212, 374).

---

## LE TRE COLONNE DEI QUESITI ATTESTATI

### Colonna A — il lato esplicativo (econometria)

**Gia' prodotte e tenute** (~15 quesiti): modello econometrico (113), dipendente
ed esplicativa (114), semplice (115) e multipla (118), coefficiente ed errore
standard (117, con grafico), intercetta (290), minimi quadrati, R quadro,
ipotesi del modello (116), BLUE (173/124), varianza grande (123),
multicollinearita', dummy (296), endogeneita' e strumentali (128),
eteroschedasticita', proxy (343), strutture dei dati (353-355), effetti fissi
e casuali (125-126).

**Mai prodotte o deboli — da chiudere:**

| N. | Quesito | Nota |
|---|---|---|
| 119 | Che cosa succede se aggiungo una variabile irrilevante | gemella pericolosa della variabile **omessa** |
| 120 | Che cosa significa cambiare la scala di una variabile | |
| 121 | Che effetto hanno gli outlier sui risultati | fatto in data science a 24, mai in regressione |
| 127 | Autocorrelazione in una serie storica | da riverificare |
| 223 | Che cosa significa «regressione sui residui» | mai aperta |
| 232 | Perche' confrontare valori osservati, stimati e previsti | **snodo**: i tre nomi sono i tre mondi |
| 233 | Come si costruisce un modello a partire dai valori osservati | |
| 172 | I risultati restano uguali su campioni diversi? | |
| 130 | Modello teorico contro modello stimato | |
| 240 | Che cosa si intende per «stimatore osservato» | |
| 317 | Correlazione vicina a zero e relazione non lineare | |
| 320 | **Regressione logistica** e interpretazione dei coefficienti | **mai aperta** |
| 337 | Quartili e percentili nella **regressione quantile** | **mai aperta** |

### Colonna B — il lato predittivo (data science)

**Gia' prodotte:** cross-validation e i tre insiemi (135), overfitting (137),
classificazione supervisionata (136), sensibilita' e specificita' (134),
bias-varianza, **MAE RMSE R quadro fuori campione (371, chiusa il 26 nov con grafico)**.

| N. | Quesito | Nota |
|---|---|---|
| 369 | Training, validation, test; cross-validation stratificata, per gruppi, temporale; **data leakage** | parziale |
| 370 | Matrice di confusione, accuratezza, precisione, **F1, ROC-AUC, PR-AUC**; soglia con classi sbilanciate | parziale |
| 375 | **Monitoraggio dopo la messa in uso: drift**, controlli per sottogruppo, riaddestramento | mai aperta |
| 132 | Tecniche di data science per analizzare congetture economiche | mai aperta |

### Colonna C — I QUATTRO PONTI

Sono i quesiti il cui **intero contenuto** e' la differenza fra i due usi.
Chi ha l'architettura li risponde senza studiarli.

| N. | Quesito | La risposta in una riga |
|---|---|---|
| 112 | Differenza fra stimare sui dati raccolti e valutare su dati nuovi | stimare e' econometria, valutare e' data science |
| 129 | Quando un modello in-sample non si generalizza | overfitting: ha imparato il rumore, non la regolarita' |
| 212 | Un buon adattamento garantisce buone previsioni? | **no** — e' la domanda-trappola del R quadro alto |
| 374 | Test predittivo, test d'ipotesi, valutazione causale | tre domande diverse: *indovino? / e' per caso? / e' stata la politica?* |

---

## IL PERCORSO, IN SEI BLOCCHI

| | Blocco | Contenuto | Tempo |
|---|---|---|---|
| **1** | **L'architettura** | la tabella delle due colonne, detta e ridetta finche' non esce da sola | **20 min** |
| **2** | **Chiudere il lato esplicativo** | 119, 120, 121, 127, 223, 232, 233, 172, 130, 240, 317 | **55 min** |
| **3** | **I quattro ponti** | 112, 129, 212, 374 | **30 min** |
| **4** | **Chiudere il lato predittivo** | 369 (data leakage), 370 (F1, ROC-AUC, PR-AUC, soglia), 375 (drift), 132 | **45 min** |
| **5** | **Le due mai aperte** | 320 regressione logistica · 337 regressione quantile | **30 min** |
| **6** | **Prova a freddo** | 20 domande miste, pescate dalle tre colonne, senza preavviso | **30 min** |

**Totale: circa 3 ore e mezza di lavoro effettivo.**

Non sono tre ore e mezza di studio nuovo: **circa il 70% del materiale e' gia'
prodotto**. Quasi tutto il tempo va in due cose — **riordinare** quello che gia'
sai sotto l'architettura, e **chiudere 24 quesiti** mai detti ad alta voce.

**Distribuzione proposta:**
- **oggi, 26 novembre, pomeriggio** — blocchi 1, 2 e 3 (1h45)
- **domani, 27 novembre, mattina** — blocchi 4, 5 e 6 (1h45)

Il 28 novembre la regressione e' chiusa su entrambi i lati, e restano quattro
giorni pieni per il secondo giro generale.

---

## I DUE ERRORI DA PRESIDIARE

**1. L'R quadro.** Non e' «roba di econometria». Compare nel quesito 371 fra gli
indicatori di valutazione fuori campione. Cambia la lettura, non la materia.

| | dove | come si legge |
|---|---|---|
| **R quadro dentro il campione** | econometria | quota di varianza spiegata — **mai negativo** |
| **R quadro fuori campione** | data science | confronto col modello di riferimento (la media) — **puo' essere negativo** |

**2. Variabile omessa contro variabile irrilevante** (quesito 119).

| | effetto |
|---|---|
| **omessa** (manca una variabile che conta) | **distorce** il coefficiente: e' un problema di correttezza |
| **irrilevante** (ne aggiungo una che non conta) | **non distorce**, ma gonfia la varianza: e' un problema di efficienza |

Gancio: **l'omessa sposta la stima, l'irrilevante la rende incerta.**
