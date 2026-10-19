# Econometria — la mappa, e il primo passo

**Manuale, Parte III, pp. 260-359** (Parte 1 della scansione). Questo documento
non riassume il manuale: **spiega che cosa stiamo per fare e perché**, in modo
che ogni pagina che leggerai abbia già un posto dove andare a sistemarsi.

Si legge una volta per intero, e poi si rilegge solo la sezione del passo in cui
ti trovi.

---

# PARTE A — Che cosa andiamo a fare

## Il problema che l'econometria deve risolvere

Parto dal problema vero, perché i sette capitoli che seguono sono **sette
risposte in fila a una sola difficoltà**.

Tu vuoi sapere una cosa del mondo: *i comuni che hanno più personale in
ragioneria pagano prima i fornitori?*

Non puoi rispondere con un esperimento. Non puoi prendere cento comuni, dare a
cinquanta un contabile in più e agli altri no, e guardare che succede. **I
fenomeni economici non si possono ripetere in laboratorio**: hai solo i dati che
la realtà ha già prodotto, una volta sola, e devi cavarci una risposta.

**Tutta l'econometria è la cassetta degli attrezzi per fare questo.** E i sette
capitoli sono gli attrezzi, in ordine di costruzione.

## I sette passi — ognuno nasce da una domanda del precedente

> **Questa è la cosa da imparare per prima e da non dimenticare mai.** Non è un
> elenco di argomenti: è una catena. Chi ha la catena non dimentica gli anelli,
> perché ciascuno è *richiesto* dal precedente.

**Passo 1 — La statistica descrittiva** *(cap. 1, pp. 261-296)*
Hai una tabella di numeri. Troppi per guardarli tutti.
→ **Domanda**: come li riassumo senza tradirli?
→ **Risposta**: con pochi indici — dove stanno in media, quanto sono sparsi, che
forma hanno.

**Passo 2 — Il calcolo delle probabilità** *(cap. 2, pp. 297-303)*
Ma quella tabella non contiene tutto il mondo: contiene **un pezzo** di mondo,
scelto in parte dal caso.
→ **Domanda**: come si ragiona in modo rigoroso su ciò che è incerto?
→ **Risposta**: con le probabilità.

**Passo 3 — Le variabili casuali** *(cap. 3, pp. 304-315)*
→ **Domanda**: come do una forma matematica a «una quantità che dipende dal
caso»?
→ **Risposta**: la variabile casuale — un numero che non conosci in anticipo, ma
di cui conosci **come si distribuisce**. È qui che entrano la normale, la t di
Student, il chi-quadrato: non sono mostri, sono **forme di distribuzione**.

**Passo 4 — La teoria della stima** *(cap. 4, pp. 316-324)*
Ora hai i dati (passo 1) e sai trattare il caso (passi 2-3).
→ **Domanda**: dai dati che ho, che cosa posso dire del mondo intero?
→ **Risposta**: costruisco uno **stimatore**, e mi chiedo se è un buon
stimatore. Qui nascono parole come *corretto*, *efficiente*, *consistente*: sono
**pagelle date agli stimatori**, niente di più.

**Passo 5 — La verifica delle ipotesi** *(cap. 5, pp. 325-329)*
→ **Domanda**: il risultato che ho trovato è reale, o è un caso?
→ **Risposta**: il test. Si parte sempre dall'ipotesi scettica — *«non c'è
nessun effetto»* — e si guarda quanto i dati siano improbabili se quella fosse
vera.

**Passo 6 — I modelli econometrici** *(cap. 6, pp. 330-339)* ← *già fatto*
→ **Domanda**: come metto in relazione **due o più** grandezze economiche?
→ **Risposta**: un modello. Variabili endogene ed esogene, i tre tipi di dati
(cross section, serie storica, panel), i quattro stadi.

**Passo 7 — Il modello di regressione semplice** *(cap. 7, pp. 340-359+)*
← *iniziato fino a p. 344*
→ **Domanda**: qual è il modello più semplice possibile, e come lo stimo
davvero?
→ **Risposta**: una retta. E il metodo per tracciarla si chiama **minimi
quadrati**.

## La frase che tiene insieme tutto

> **Descrivo i dati (1) → ammetto che c'è del caso (2-3) → dal campione risalgo
> al mondo (4) → verifico di non essermi illusa (5) → metto in relazione le
> grandezze (6) → traccio la retta (7).**

Se ti perdi, torna qui. **Ogni cosa che leggerai sta in uno di questi sette
cassetti.**

## Dove sei e dove andiamo

Sei entrata dal **passo 6**, saltando i cinque che lo reggono: è questa la
ragione tecnica del senso di estraneità, e va corretta ripartendo dal passo 1.

Il passo 1 ha anche un secondo vantaggio: **è metà del programma di statistica
economica**. Lo studi una volta e ne copri due.

---

# PARTE B — Il primo passo, spiegato

## La statistica descrittiva (cap. 1, pp. 261-296)

### A che cosa serve, in una riga

**A sostituire tanti numeri con pochi numeri, perdendo il meno possibile.**

Hai 378 comuni e per ciascuno i giorni di pagamento. Sono 378 numeri: nessuno
riesce a pensarli insieme. La statistica descrittiva produce **tre o quattro
numeri** che li rappresentano. Tutto il capitolo è questo mestiere.

### Passo 1.1 — Si comincia sempre da una tabella

Prima di qualunque calcolo, i dati stanno in una tabella fatta così:

| | giorni di pagamento | provincia | addetti in ragioneria |
|---|---|---|---|
| **Roma** | 32 | RM | 48 |
| **Viterbo** | 61 | VT | 6 |
| **Fiuggi** | 54 | FR | 3 |
| … *(378 righe)* | | | |

E qui c'è **la regola che vale per tutto il corso**:

> **L'unità statistica è ciò che occupa UNA RIGA. I caratteri sono le COLONNE.
> Il collettivo è l'insieme di tutte le righe.**

L'unità statistica, qui, è **il comune**. Il collettivo sono **i 378 comuni**.
I caratteri sono **giorni di pagamento, provincia, addetti**.

**Una cosa importante e non ovvia**: l'unità statistica **non è scritta nei
dati, la sceglie chi fa l'indagine**, in base alla domanda. Se la domanda è
*«quali comuni pagano tardi?»* l'unità è il comune e le righe sono 378. Se la
domanda è *«quanto tempo serve per saldare una fattura?»* l'unità è **la
fattura** e le righe diventano milioni. Stesso fenomeno, indagini diverse.

Il manuale distingue anche le unità in **semplici** (una persona), **composte**
(insiemi di unità simili che esistono anche a prescindere: la famiglia,
l'edificio) e **complesse** (insiemi di unità *diverse* che si caratterizzano
nella loro totalità: un processo produttivo).

### Passo 1.2 — Le colonne sono di due tipi, e la differenza decide tutto

| Il carattere è… | Genera una… | Esempio |
|---|---|---|
| **quantitativo** (un numero) | **variabile statistica** | giorni di pagamento, addetti, reddito, età |
| **qualitativo** (una parola) | **mutabile statistica** | provincia, professione, genere di attività |

> **Da ricordare così: mutabile = parole, variabile = numeri.**

**Perché la distinzione conta davvero**, e non è pedanteria: **determina che
cosa puoi calcolare**. Di una colonna di numeri puoi fare la media; della
colonna «provincia» no — non esiste la provincia media. Ogni volta che il
manuale dice «indici per variabili quantitative» ti sta dicendo *questi
strumenti funzionano solo sulle colonne numeriche*.

### Passo 1.3 — Prima di sintetizzare, si conta: le frequenze

**La frequenza è il numero di volte in cui una modalità si presenta.** Il
manuale ne distingue quattro, ed è una scala che sale:

| Tipo | Che cos'è | Esempio su 378 comuni |
|---|---|---|
| **assoluta** | quante unità presentano quella modalità | 112 comuni sono in provincia di Roma |
| **relativa** | la frequenza assoluta **divisa per il totale** | 112/378 = 0,296 |
| **percentuale** | la relativa **moltiplicata per 100** | 29,6% |
| **cumulata** | quante unità stanno **fino a** una certa modalità | 240 comuni pagano entro 60 giorni |

> **Perché esistono tutte e quattro.** L'assoluta dice *quanti*; la relativa
> permette di **confrontare collettivi di dimensione diversa** (il 29,6% del
> Lazio si confronta con il 29,6% della Lombardia, i 112 comuni no); la
> cumulata risponde a *«quanti stanno sotto una soglia»*, che è la domanda
> tipica di chi deve fissare un obiettivo.

E due parole che il manuale usa e conviene non confondere:
- **intensità** = la misura di un carattere su un'unità (il peso di una persona,
  gli investimenti di un'azienda);
- **frequenza** = quante volte una modalità si presenta.

Le tabelle, infine, sono **semplici** se riportano un solo carattere,
**multiple** (a più entrate) se ne incrociano due o più.

### Passo 1.4 — Le tre domande che reggono tutto il capitolo

**Questa è la struttura del capitolo 1, e il manuale la dichiara lui stesso a
p. 269.** Davanti a una colonna di numeri si fanno **tre domande, sempre le
stesse**:

| Domanda | Famiglia di indici | Dove |
|---|---|---|
| **1. Dove stanno?** | **indici di posizione** (le medie) | §5, pp. 269-279 |
| **2. Quanto sono sparsi?** | **indici di variabilità** | §6, pp. 280-287 |
| **3. Che forma hanno?** | **indici di forma** | §7, pp. 288-289 |

Se ricordi solo questo del capitolo 1, hai già l'ossatura per rispondere
all'orale. Tutto il resto sono gli strumenti dentro i tre cassetti.

---

### Cassetto 1 — Dove stanno: gli indici di posizione

Il manuale li divide in due, ed è una distinzione che fa impressione se la citi:

| | Come si determinano | Quali sono |
|---|---|---|
| **medie analitiche** | considerando **tutti** i valori della distribuzione | media **aritmetica**, **armonica**, **geometrica**, **quadratica** |
| **medie lasche** | considerando **solo alcuni** elementi | **mediana**, **moda** |

> **Il senso della distinzione.** Una media analitica usa ogni dato, quindi **un
> solo valore estremo la sposta**. Una media lasca guarda la posizione nella
> graduatoria, quindi **è robusta**. È esattamente il motivo per cui, sui
> redditi, si pubblica la **mediana** e non la media: un miliardario alza la
> media di tutti e non sposta la mediana di un centimetro.

Dentro il cassetto trovi anche i **percentili** (§5.9): i valori che tagliano la
distribuzione in centesimi. La mediana è semplicemente **il 50° percentile**.

### Cassetto 2 — Quanto sono sparsi: gli indici di variabilità

Servono a misurare **la tendenza di un fenomeno ad assumere modalità diverse**.
Due comuni che pagano entrambi in 45 giorni in media sono molto diversi se uno
sta sempre fra 40 e 50 e l'altro oscilla fra 10 e 90.

Il manuale li organizza così:

- **misure analitiche**, a loro volta di due specie:
  - quelle che misurano la **dispersione intorno a una media** — gli
    **scostamenti medi** dalla media aritmetica o dalla mediana, la **devianza**
    e la **varianza**;
  - quelle che misurano la **disuguaglianza dei dati fra loro** — le
    **differenze medie**, calcolate confrontando ogni valore con tutti gli
    altri;
- **misure di posizione** — il **campo di variazione** (differenza fra valore
  massimo e minimo) e la **differenza interquartilica**.

**E poi la distinzione che vale un punto all'orale:**

| | Che cosa sono | A che servono |
|---|---|---|
| **indici assoluti** | espressi **nella stessa unità di misura** del fenomeno | descrivono una distribuzione |
| **indici relativi** | ottenuti **rapportando** un indice assoluto a un altro parametro: sono **numeri puri**, senza unità di misura | **confrontare distribuzioni diverse** |

> **Perché serve.** La varianza dei giorni di pagamento è in «giorni²»; quella
> degli stipendi in «euro²». Non puoi dire quale fenomeno sia più variabile. Se
> invece li rendi numeri puri, il confronto diventa possibile. **È tutto qui il
> senso degli indici relativi.**

In coda al cassetto ci sono gli **indici di concentrazione** (§6.9), che
rispondono a una domanda diversa e molto «da funzionario»: *quanto il totale è
concentrato in poche unità?* È la famiglia del rapporto di Gini.

### Cassetto 3 — Che forma hanno: gli indici di forma

Sono quantità che indicano **la forma della curva** che rappresenta la
distribuzione. Due soli:

- **asimmetria** (§7.1): la distribuzione pende a destra o a sinistra? Una coda
  lunga a destra significa pochi valori molto alti — tipico dei redditi.
- **curtosi** (§7.2): la curva è appuntita o schiacciata? Cioè: i valori estremi
  sono rari o frequenti?

### Le due code del capitolo

**§8 — I rapporti statistici** (p. 290). Il rapporto fra due grandezze, ed è il
ponte diretto con statistica economica: **rapporti di composizione** (parte sul
tutto), **di derivazione**, **di coesistenza**.

**§9 e §11 — Due caratteri insieme** (pp. 292-296). Qui si smette di guardare
una colonna alla volta e si guardano **due colonne insieme**: distribuzioni
doppie, e poi **la regressione**.

> **E questo è il ponte verso il passo 7.** Il §11 del capitolo 1 introduce già
> l'idea della regressione, che il capitolo 7 svilupperà per intero. Quando ci
> arriveremo, non sarà materiale nuovo: sarà una vecchia conoscenza,
> approfondita.

---

## Come leggere il capitolo 1 — sei blocchi da venti minuti

| Blocco | Pagine | Contenuto |
|---|---|---|
| **1** | **261-264** | indagine, unità, caratteri, tabelle, frequenze ✅ *fatto* |
| **2** | 265-268 | rappresentazioni grafiche (ortogrammi, istogrammi) |
| **3** | 269-279 | **le medie e la mediana** — il cassetto 1 |
| **4** | 280-287 | **variabilità, varianza, concentrazione** — il cassetto 2 |
| **5** | 288-291 | forma e rapporti statistici — il cassetto 3 |
| **6** | 292-296 | distribuzioni doppie e l'anticipo sulla regressione |

**Prima di ogni blocco, rileggi la riga della tabella delle tre domande.** Serve
a sapere in quale cassetto stai mettendo quello che leggi: è l'unico vero
antidoto alla sensazione di accumulare cose scollegate.

---

## Le sole formule che servono (e si guardano alla fine, non ora)

Questa pagina resta qui, ferma, e si legge **solo dopo** aver letto i sei
blocchi. Non serve impararla adesso e non serve saperla scrivere: serve a
riconoscerla.

| Indice | Che cosa fa |
|---|---|
| **media aritmetica** | somma dei valori diviso il loro numero |
| **mediana** | il valore che sta in mezzo alla graduatoria |
| **campo di variazione** | valore massimo − valore minimo |
| **devianza** | somma degli scarti dalla media, elevati al quadrato |
| **varianza** | la devianza divisa per il numero di osservazioni |
| **scarto quadratico medio** | la radice quadrata della varianza — **riporta la misura nell'unità originaria** |
| **coefficiente di variazione** | scarto quadratico medio diviso la media — **un numero puro, per confrontare** |

> **Perché si eleva al quadrato nella devianza.** Non è un vezzo matematico: gli
> scarti dalla media sono metà positivi e metà negativi, e **sommandoli
> otterresti sempre zero**. Il quadrato li rende tutti positivi. E la radice
> finale serve solo a tornare in giorni, in euro, in anni — cioè a riavere un
> numero che si può dire a voce.

**Questa, all'orale, è la risposta.** Non la formula: **la ragione della
formula.**
