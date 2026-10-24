# Cosa caricare — stato verificato al 24 ottobre 2026

Il contenitore di sessione viene riciclato: i PDF caricati in chat non
sopravvivono, **il testo estratto sì**. Quindi la domanda giusta non e'
«che file ho caricato», ma **«di che materia esiste il testo ricercabile»**.
Questa e' la verifica fatta sul disco.

## Testo disponibile — niente da fare

| Materia | Parti con testo | Stato |
|---|---|---|
| Econometria (Parte III) | P1, P2, P3, P4 | ✅ completa |
| Statistica economica (Parte IV) | P1, P2, P3 | ✅ completa |
| Scienza delle finanze (Parte V) | P1, P2, P3, P4 | ✅ completa |
| Indice del manuale | — | ✅ |

## Il manuale e' completo

Il tool di Google Drive scarica solo file **sotto i 10 MB**. I volumi
interi del manuale sul Drive (amministrativo 69 MB, econometria 59 MB,
politica economica 47 MB, contabilita' 33 MB, statistica 29 MB, scienze
delle finanze 20 MB) vanno quindi caricati in chat, **a pezzi sotto i
9 MB**.

### 1. Diritto amministrativo — ✅ COMPLETO

Tutte e otto le parti sono disponibili come testo, e tutte con **livello
di testo nativo**: nessun OCR, quindi nessun errore di riconoscimento.

| Parte | pp. | Contenuto |
|---|---|---|
| 1 | 7-16 | cap. 1 fonti · cap. 2 §§ 1-6 |
| 2 | 17-29 | cap. 2 §§ 7-16 |
| 3 | 29-47 | cap. 2 § 18 la competenza · cap. 3 pubblico impiego |
| 4 | 48-67 | cap. 4 atti, provvedimenti, invalidita', autotutela, controlli |
| 5 | 66-83 | cap. 5 procedimento · cap. 6 CAD |
| 6 | 84-101 | cap. 6 CAD · cap. 7 accesso · cap. 8 documentazione |
| 7 | 101-119 | cap. 9 anticorruzione e trasparenza · cap. 10 GDPR |
| 8 | 119-128 | cap. 11 responsabilita' della P.A. |

La parte 3 porta in apertura il **§ 18 del capitolo 2, sulla competenza**,
che chiude due domande del repertorio (competenza per materia, territorio
e grado).

La parte 8 porta anche due cose utili alla programmazione: l'elenco delle
**espansioni online** della Parte I (I beni della P.A., La giustizia
amministrativa, Le situazioni giuridiche soggettive, Il Codice dei
contratti pubblici - D.Lgs. 36/2023) e il **sommario completo della
Parte II**, riportato qui sotto.

### 2. Contabilita' pubblica — COMPLETA

Quattro parti arrivate il 24 ottobre, **pp. 130-257**, undici capitoli.

| File | Fogli | pp. | Capitoli |
|---|---|---|---|
| parte 1 | 25 | 130-179 | 1 natura e fonti · 2 i soggetti · 3 l'azienda composta pubblica · 4 (inizio) |
| parte 2 | 25 | 180-212 | 4 (copertura finanziaria, assestamento) · 5 classificazione di entrate e spese · 6 esecuzione del bilancio |
| parte 3 | 25 | 213-237 | 6 · 7 gestione di tesoreria · 8 i rendiconti · 9 gestione dei beni della P.A. · 10 (inizio) |
| parte 4 | 20 | 238-257 | 10 enti di erogazione · 11 **i controlli nella contabilita' pubblica** |

Le scansioni sono **miste**: alcuni fogli sono doppie pagine ruotate di
90 gradi, altri pagine singole diritte, a volte nello stesso file. Per
questo serve una pipeline che decida foglio per foglio: `ocr_mixed.sh`
rende ogni pagina a 0 e a 270 gradi, ne produce la versione intera e
quella tagliata in due, passa tutte e quattro al riconoscimento ottico e
tiene quella con piu' parole italiane riconoscibili. La variante scelta
e' annotata nel testo accanto a ogni foglio, insieme al punteggio.

⚠️ **La qualita' del testo di contabilita' resta inferiore a quella delle
altre materie**, perche' qui si tratta di fotografie di pagine e non di
un livello di testo nativo. Date, cifre e numeri di legge vanno
verificati sulla pagina prima di citarli in una lezione.

Due espansioni online della materia sono **gia' scaricate dal Drive**:
`L'ordinamento contabile delle Regioni e degli enti locali` e
`La contabilita' di Universita', AUSL e Camere di commercio`.

### 3. Politica economica — COMPLETA

Quattro parti arrivate il 24 ottobre, tutte **scansioni senza livello di
testo**, passate all'OCR (300 dpi, tesseract italiano):

| File | Fogli | pp. | Contenuto |
|---|---|---|---|
| PARTE1 | 20 | 732-751 | fine cap. 1 · cap. 2 La politica economica: **regola di Tinbergen**, **critica di Lucas** · cap. 3 · inizio cap. 4 |
| PARTE2 | 18 | 752-769 | cap. 4 **Il modello reddito-spesa** · cap. 5 **La domanda di moneta** |
| PARTE4 | 9 | 777-785 | cap. 9 **Il modello di domanda e offerta aggregate** |
| PARTE5 | 11 | 786-796 | cap. 10 **La disoccupazione e l'inflazione**: teoria classica, marxista, keynesiana |

Le cuciture combaciano sui confini di capitolo: l'estratto di settembre
chiude a p. 776 con la fine del capitolo sulla sintesi (IS-LM), la PARTE4
apre con la pagina iniziale del capitolo 9, la PARTE5 con quella del
capitolo 10, dove riprende la coda gia' disponibile (pp. 797-845, capp.
10, 11, 12, 19).

**Copertura della Parte VI: pp. 732-845, senza buchi.**

## Preso dal Drive, senza doverlo caricare

Tutti sotto i 10 MB (il limite del tool di Drive), tutti con livello di
testo, nessun OCR necessario:

- `data mining.pdf` — 6 pagine
- `Le situazioni giuridiche soggettive.pdf`
- `L'ordinamento contabile.pdf`
- `Principi contabili generali.pdf`
- `Aggiornamenti normativi di diritto amministrativo.pdf`

Piu' quelli gia' scaricati a settembre: `La giustizia amministrativa.pdf`,
`Decentramento amministrativo.pdf`, `Valutazione d'impatto.pdf`.

### Ancora sul Drive, da prendere quando serviranno

`Lo spoil system` · `I beni della P.A.` · `Il Codice dei contratti
pubblici` · `Il pagamento dei debiti` · `La contabilita' di Universita',
AUSL` · `Le imposte dirette e indirette` · `Aggiornamento alla disciplina
del pubblico impiego` · `D.M. 1-10-2013 principio di competenza
finanziaria` · `D.P.C.M. 18-9-2012`

> Attenzione: il mio accesso a Drive vede l'account
> **valter.romani@61project.it**. File caricati da un altro account Google
> non risultano visibili.
