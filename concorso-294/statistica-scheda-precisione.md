# Statistica economica — la scheda della precisione

**Per un commissario pignolo.** Concorso RIPAM 294, codice 02 — prova orale del
27 novembre 2026.

Questa scheda non riassume la materia: raccoglie **i punti in cui un esaminatore
pignolo colpisce**. Sono i luoghi dove non basta capire, bisogna dire *il numero
giusto*, *il denominatore giusto*, *la parola giusta*.

Tutto ciò che segue è ripreso dal manuale, **Parte IV, pp. 575-648**. I numeri di
pagina sono quelli stampati sul libro (per questa Parte i marcatori dell'OCR
coincidono con la numerazione stampata: verificato su pp. 578, 590, 610, 614,
636, 648).

---

## Come si risponde a un pignolo

Tre regole, prima del contenuto.

**1. Il numero prima della spiegazione.** Il pignolo non sta cercando se hai
capito: sta cercando se *sai*. «Il tasso di disoccupazione è il rapporto tra i
disoccupati e la forza lavoro» — e *poi* la spiegazione. Non il contrario.

**2. Se una definizione ha una soglia, la soglia fa parte della definizione.**
«Occupato è chi ha lavorato almeno un'ora» non è un dettaglio pedante: è
*esattamente* ciò che distingue la statistica ufficiale dal senso comune, ed è
la cosa che il commissario vuole sentire.

**3. Quando non ricordi un numero, non inventarlo.** Si dice: «la soglia esiste
ed è quella che rende la definizione operativa; il valore preciso non lo ricordo
ora». Un numero sbagliato detto con sicurezza costa molto di più di
un'ammissione. Con un pignolo, costa moltissimo.

---

# 1. Le definizioni ISTAT del mercato del lavoro (pp. 633-635)

**Questo è il primo posto dove si viene puniti.** Sono definizioni operative,
armonizzate a livello europeo, e il manuale le riporta alla lettera.

## Occupati

Persone di **15 anni e più** che, **nella settimana di riferimento**, soddisfano
**almeno uno** di questi requisiti:

1. hanno svolto **almeno un'ora** di lavoro in un'attività che preveda un
   corrispettivo monetario o in natura;
2. hanno svolto **almeno un'ora** di lavoro **non retribuito** nella ditta di un
   familiare nella quale collaborano abitualmente;
3. sono **assenti dal lavoro**, ma l'assenza **non supera i tre mesi**, oppure
   durante l'assenza continuano a percepire **almeno il 50%** della retribuzione.

> **Il punto che il pignolo cerca**: *«almeno un'ora»* e *«almeno uno dei
> requisiti»*. La definizione statistica di occupato è deliberatamente
> larghissima — un'ora di lavoro nella settimana basta. Chi risponde «occupato è
> chi ha un lavoro» ha detto una tautologia, non una definizione.

**Nota il limite d'età**: per gli occupati c'è solo il limite inferiore
(15 anni e più), **nessun limite superiore**.

## Persone in cerca di occupazione (disoccupati)

Persone **non occupate** di età tra **15 e 74 anni** che:

1. sono state **alla ricerca di un lavoro nei trenta giorni** che precedono
   l'intervista **e** si dichiarano **disponibili a lavorare entro le due
   settimane** successive all'intervista;

   *oppure*

2. **inizieranno un lavoro entro tre mesi** dalla data dell'intervista **e** si
   dichiarano disponibili a lavorare entro le due settimane successive
   all'intervista, se possibile per anticiparne l'inizio.

> **I quattro numeri da avere in bocca**: **15-74 anni**, **trenta giorni** di
> ricerca attiva, **due settimane** di disponibilità, **tre mesi** per chi ha già
> un lavoro in arrivo.

**Attenzione alla congiunzione.** Ricerca attiva **e** disponibilità: servono
**entrambe**. Chi cerca ma non è disponibile subito non è un disoccupato
statistico; chi è disponibile ma non cerca nemmeno. Questo è *esattamente* il
genere di dettaglio su cui un pignolo insiste.

**E nota l'asimmetria d'età**: gli occupati sono **15 e più**, i disoccupati
**15-74**. Non è una svista del manuale: è la convenzione.

## Inattivi (popolazione non attiva, non forza lavoro)

Due componenti:

- chi **non è in età lavorativa** (minori di 15 anni);
- chi, **pur essendo in età lavorativa, non è alla ricerca** di un'occupazione:
  casalinghe, studenti, benestanti.

## Lo schema da disegnare a mente

```
                     POPOLAZIONE
                          │
           ┌──────────────┴──────────────┐
      POPOLAZIONE ATTIVA           POPOLAZIONE INATTIVA
      (= FORZA LAVORO)             (= NON FORZA LAVORO)
            │                              │
     ┌──────┴──────┐              ┌────────┴────────┐
  OCCUPATI    DISOCCUPATI    in età lavorativa   non in età
                             ma non in cerca     lavorativa
                                                  (< 15 anni)
```

**Forza lavoro = occupati + persone in cerca di occupazione.** Questa somma è la
chiave di tutto il paragrafo successivo.

---

# 2. I tre tassi e i loro denominatori (p. 634)

Il manuale li dà in tre righe. Sono **la domanda più probabile** dell'intera
Parte IV, e l'errore più frequente è sul **denominatore**.

| Tasso | Formula | Denominatore |
|---|---|---|
| **Tasso di attività** | forza lavoro / popolazione in età lavorativa | popolazione in età lavorativa |
| **Tasso di disoccupazione** | disoccupati / **forza lavoro** | **forza lavoro** |
| **Tasso di occupazione** | occupati / popolazione in età lavorativa | popolazione in età lavorativa |

> **La regola che salva.** Dei tre tassi, **due hanno lo stesso denominatore**
> (popolazione in età lavorativa) e **solo il tasso di disoccupazione** ha per
> denominatore la forza lavoro. Se ricordi questa singola asimmetria, non sbagli
> più.

## La conseguenza che vale un voto in più

**Il tasso di disoccupazione può scendere senza che nessuno abbia trovato
lavoro.** Se un disoccupato si scoraggia e smette di cercare, esce dalla forza
lavoro: cala il numeratore *e* il denominatore, e il tasso scende. Il **tasso di
occupazione**, che ha al denominatore la popolazione in età lavorativa (la quale
non si muove per scoraggiamento), **non ha questo difetto** — ed è per questo
che gli economisti del lavoro lo preferiscono come indicatore di salute del
mercato.

Dirlo trasforma una risposta da 22 in una risposta da 26. È la conseguenza che
dimostra di aver capito *perché* i denominatori sono diversi.

## Perché in Italia è calato il tasso di attività (p. 634)

Il manuale elenca quattro fattori, **due che lo abbassano e due che lo alzano** —
e il pignolo può chiedere proprio la direzione:

| Fattore | Effetto sulla forza lavoro |
|---|---|
| Invecchiamento della popolazione | ↓ (cresce la popolazione inattiva) |
| Prolungamento della durata media degli studi | ↓ (ingresso ritardato) |
| Crescita dell'occupazione femminile | ↑ (meno casalinghe) |
| Immigrazione (prevalentemente giovane e attiva) | ↑ |

---

# 3. Flussi, durata e rilevazione (pp. 634-635)

**Flussi.** Il tasso di disoccupazione sale quando il flusso d'entrata è intenso,
scende quando cresce quello d'uscita. **Se il tasso è stabile, i due flussi si
compensano perfettamente** — non significa che il mercato sia fermo.

**L'osservazione fine sulla durata.** Si esce dalla disoccupazione **non solo
trovando lavoro**: anche tornando nella popolazione inattiva (giovani che
riprendono gli studi, chi si dedica al lavoro domestico), emigrando, o per
decesso. Quindi **la durata media della disoccupazione non coincide con il tempo
necessario a trovare un'occupazione**. È una precisazione da pignolo — e infatti
è nel manuale.

**Disoccupazione di lunga durata**: permanenza **superiore a un anno**.

**Da cosa dipende la durata**: fase del ciclo economico; flessibilità del mercato
(nei Paesi europei, più regolamentati degli Stati Uniti, la durata è
tendenzialmente maggiore); normativa sociale a favore dei disoccupati (sussidi
generosi possono allungare la durata media — effetto che il manuale giudica
«poco determinante» per l'Italia, dove l'entità del sussidio è modesta).

## La Rilevazione sulle forze di lavoro — i numeri esatti

- condotta dall'**ISTAT**;
- criteri armonizzati a livello europeo, **Regolamento 577/98** del Consiglio
  dell'Unione europea;
- **continua dal 2004**: le informazioni si raccolgono in **tutte le settimane
  dell'anno**, non più in una singola settimana per trimestre;
- i risultati sono comunque **diffusi con cadenza trimestrale**;
- campione: **oltre 250 mila famiglie** residenti, circa **600 mila individui**,
  in circa **1.400 comuni**;
- si intervistano i componenti **che hanno superato i 15 anni**.

> **Il dettaglio più citabile**: *continua dal 2004, diffusione trimestrale*. È
> la coppia che mostra di sapere come funziona davvero la produzione del dato —
> la rilevazione è continua, la *diffusione* no.

---

# 4. I tre tipi di disoccupazione e la legge di Okun (pp. 635-636)

| Tipo | Che cos'è | Il numero |
|---|---|---|
| **Frizionale** | squilibrio momentaneo tra flussi d'entrata e d'uscita: il mercato non funziona in modo perfetto e automatico, c'è chi passa da un'occupazione all'altra o cerca di meglio | stimata tra il **2 e il 5%** |
| **Ciclica (o congiunturale)** | disoccupazione **di breve periodo**: la domanda complessiva di lavoro è scarsa perché il momento congiunturale è sfavorevole | — |
| **Strutturale** | **la più grave e difficile da eliminare**: colpisce interi settori o aree geografiche, squilibri **stabili e permanenti** | — |

**Il test della disoccupazione strutturale**, da citare alla lettera: *«anche se
paradossalmente il salario fosse pari a zero, l'offerta di lavoro risulterebbe
comunque eccedente rispetto alla domanda»*. È la frase che la distingue da tutte
le altre — nelle altre il salario, prima o poi, riequilibra.

**Cause della strutturale**: tecniche produttive *labour saving* (automazione che
sostituisce lavoratori con macchine) **oppure, all'opposto**, insufficienti
livelli di investimento con basso impiego di lavoro in alcuni settori. Gli
esempi del manuale: siderurgia, agricoltura, e in parte il Mezzogiorno.

## Legge di Okun — la formulazione del manuale

> Ogni **diminuzione del PIL di circa il 2-2,5% rispetto al suo valore
> potenziale** comporta un **aumento del tasso di disoccupazione dell'1%**.

**Le due precisazioni che il pignolo aspetta**: è una relazione **empirica**, non
teorica; ed è riferita allo **scostamento dal PIL potenziale**, non alla crescita
in sé. Chi dice «se il PIL cala del 2% la disoccupazione sale dell'1%» ha
dimenticato la parola *potenziale*, ed è proprio lì che viene fermato.

---

# 5. Laspeyres, Paasche, Fisher — numeratore e denominatore (pp. 580-583)

**Qui la formula è il contenuto.** Non c'è modo di distinguere i due indici se
non dicendo *quali quantità stanno ai pesi*.

## Indici dei prezzi

```
                 Σ pₙ · q₀                          Σ pₙ · qₙ
Laspeyres:  L = ───────────          Paasche:  P = ───────────
                 Σ p₀ · q₀                          Σ p₀ · qₙ
```

- **Laspeyres**: pesi = **quantità dell'anno base** (q₀). Ponderazione **fissa**.
  Il metodo di sintesi si chiama **metodo dell'anno base**.
- **Paasche**: pesi = **quantità dell'anno corrente** (qₙ). Ponderazione
  **variabile**. Il metodo si chiama **metodo dell'anno dato**.

## Indici delle quantità

```
                 Σ p₀ · qₙ                          Σ pₙ · qₙ
Laspeyres:  L = ───────────          Paasche:  P = ───────────
                 Σ p₀ · q₀                          Σ pₙ · q₀
```

**Simmetria perfetta**: nell'indice dei prezzi si bloccano le quantità, in quello
delle quantità si bloccano i prezzi — e Laspeyres li blocca **alla base**,
Paasche **all'anno dato**.

> **La frase che li fissa per sempre.** *Laspeyres chiede: quanto costerebbe oggi
> il paniere di allora? Paasche chiede: quanto sarebbe costato allora il paniere
> di oggi?*

## Fisher

```
F = √( L · P )
```

**Media geometrica semplice** di Laspeyres e Paasche. Detto **«numero indice
ideale»** perché soddisfa **quasi tutte** le proprietà formali proposte da Fisher
stesso — **con l'eccezione della transitività**.

L'esempio numerico del manuale (p. 584): L = 1,0432, P = 1,0408, da cui
F = √(1,0432 · 1,0408) = **1,0420**. Fisher sta sempre **in mezzo** ai due.

## Le proprietà — e quelle che Laspeyres e Paasche NON soddisfano

Proprietà richieste agli indici sintetici (p. 581): **identità**, **reversibilità
delle basi**, **commensurabilità**, **determinatezza**, **proporzionalità**,
**reversibilità dei fattori** (o decomposizione delle cause), **transitività
delle basi** (o circolarità).

> **La domanda da pignolo per eccellenza** (p. 582): *quali proprietà NON
> soddisfano Laspeyres e Paasche?* La risposta è **tre**:
>
> 1. **reversibilità delle basi**;
> 2. **transitività** — e quindi il confronto tra due termini qualunque della
>    serie non è attuabile;
> 3. **decomposizione delle cause**.

Chi sa rispondere a questa domanda ha già vinto la materia, perché è
precisamente la cosa che quasi nessuno studia.

## La distorsione — il perché economico

- **Laspeyres sovrastima** la variazione dei prezzi: tenendo ferme le quantità
  della base non coglie la **sostituzione** dei consumatori verso i beni
  diventati relativamente più economici.
- **Paasche sottostima**, per la ragione speculare.
- **Fisher**, stando in mezzo, attenua entrambe le distorsioni.

## Perché l'ISTAT usa Laspeyres

Il manuale lo dice espressamente (p. 581): **la maggior parte degli istituti
nazionali di statistica, ISTAT compreso, utilizza l'indice di Laspeyres** come
indice complesso di prezzo, **per via della costanza del paniere** di beni e
servizi di riferimento: consente di **misurare variazioni di prezzi per un
paniere costante**, e il calcolo ripetuto nel tempo è più agevole perché il
sistema di ponderazione non va rifatto a ogni rilevazione.

Paasche è invece conveniente «ove si dispone congiuntamente e simultaneamente di
prezzi e quantità» — l'esempio del manuale sono le **contrattazioni borsistiche**.

**La chiusura da 27**: *nella pratica economica si preferiscono comunque
Laspeyres e Paasche a Fisher — pur essendo Fisher «ideale» — perché in essi
compaiono grandezze che hanno un preciso significato economico.* Fisher è una
media geometrica: è elegante, ma non corrisponde a nessun paniere reale.

---

# 6. Gli indici dei prezzi dell'ISTAT (pp. 584-586)

**Le tre famiglie** che l'ISTAT elabora:

1. indici dei prezzi relativi alla **fase della produzione**;
2. indici dei prezzi **al consumo**;
3. indice dei prezzi delle **abitazioni** (IPAB).

## Prezzi alla produzione

**Industria**: misura le variazioni dei prezzi dei prodotti industriali
fabbricati da imprese con stabilimenti sul **territorio nazionale**, venduti sul
mercato interno o estero (a sua volta diviso in **Area euro** e **Area non
euro**).

**I quattro raggruppamenti principali di industrie**: beni di **consumo**, beni
**strumentali**, beni **intermedi**, **energia**.

**Servizi**: evoluzione **trimestrale** dei prezzi dei servizi venduti da imprese
residenti in Italia a **imprese e/o enti della pubblica amministrazione**. È un
indice **business to business**: **non considera le transazioni con le
famiglie**. Settori definiti in base al **Regolamento (CE) 1158/05**.

## NIC, FOI, IPCA — le tre differenze

| | **NIC** | **FOI** | **IPCA** |
|---|---|---|---|
| **Nome per esteso** | indice nazionale dei prezzi al consumo per l'**intera collettività** | indice dei prezzi al consumo per le **famiglie di operai e impiegati** | indice dei prezzi al consumo **armonizzato** per i Paesi dell'UE |
| **Popolazione di riferimento** | l'intero sistema economico nazionale | famiglie di **lavoratori dipendenti non agricoli** | confronto tra Paesi UE |
| **A che cosa serve** | misura dell'inflazione **per l'intero sistema economico** | **adeguare periodicamente valori monetari**: affitti, assegni familiari | rendere **confrontabili** i prezzi dei Paesi UE |
| **Origine** | ISTAT | ISTAT | creato da **EUROSTAT** nella **seconda fase dell'UEM**; calcolato e pubblicato dall'ISTAT e **inviato mensilmente a EUROSTAT**, che diffonde poi l'indice sintetico europeo |

**Ciò che hanno in comune, e che va detto**: tutti e tre sono calcolati con
**la formula di Laspeyres**, e **paniere e sistema dei pesi sono aggiornati
annualmente e tenuti fissi per l'intero anno**.

> **Il dettaglio con cui si chiude il discorso**: il FOI è quello che entra nei
> contratti e nelle rivalutazioni monetarie, e si pubblica anche nella variante
> **«senza tabacchi»** — perché non sarebbe corretto che un aumento delle accise
> sui tabacchi rivalutasse gli affitti.

## La classificazione ECOICOP

**European Classification of Individual Consumption by Purpose**, contenuta nel
**Regolamento UE 792/2016** e nel Regolamento di esecuzione **UE 1148/2020**.

Quattro livelli: **divisioni di spesa → gruppi di prodotto → classi di prodotto →
sottoclassi di prodotto**.

- **12 divisioni di spesa** al primo livello;
- **43 gruppi di prodotto** al secondo;
- **i primi due livelli sono comuni ai tre indici NIC, FOI e IPCA**; **dal terzo
  livello in poi il paniere IPCA si differenzia** dagli altri due.

Questa ultima riga è la risposta precisa alla domanda «i tre indici usano lo
stesso paniere?». **No: lo condividono fino al secondo livello.**

## IPAB e indice della produzione industriale

**IPAB** — indice dei prezzi delle abitazioni: immobili residenziali **nuovi o
esistenti** acquistati dalle famiglie, **sia per fini abitativi sia per fini
d'investimento**; cadenza **trimestrale**; due sub-indici (**nuove** ed
**esistenti**); linee guida **EUROSTAT**; calcolato con un **indice a catena di
tipo Laspeyres**.

**Indice della produzione industriale**: misura la variazione nel tempo del
**volume fisico** della produzione dell'**industria in senso stretto**,
**escluse quindi le costruzioni**. Sintesi con la **formula di Laspeyres**; dal
2018 **base 2015 = 100**, classificazione **Ateco 2007**, panel di circa **4.600
imprese**. I dati vengono **destagionalizzati**, cioè depurati dalle fluttuazioni
di carattere stagionale.

> «Volume fisico» e «industria in senso stretto, escluse le costruzioni» sono le
> due espressioni esatte. Un pignolo chiede: *le costruzioni ci sono dentro?*

---

# 7. Il perimetro S13 (pp. 592-593)

**Definizione del SEC 2010.** Il settore delle amministrazioni pubbliche (S13) è
costituito dalle unità istituzionali che agiscono da **produttori di beni e
servizi non destinabili alla vendita** (*non market*), la cui produzione è
destinata a **consumi collettivi e individuali** ed è finanziata da **versamenti
obbligatori** effettuati da unità appartenenti ad altri settori, nonché dalle
unità istituzionali la cui **funzione principale** consiste nella
**redistribuzione del reddito e della ricchezza** del Paese.

## Che cosa è cambiato dal SEC 95 al SEC 2010

| | **SEC 95** | **SEC 2010** |
|---|---|---|
| Criterio | l'unità entrava in S13 se era **legata o controllata** da una P.A. **e** risultava produttore non di mercato secondo il **test market/non market (test del 50%)** | **al test si aggiunge l'analisi delle condizioni di concorrenzialità** in cui l'unità opera |

**Il test market/non market (test del 50%)** verifica **in quale quota le vendite
coprono i costi di produzione** dell'unità — **compreso il costo del capitale**.

**L'analisi delle condizioni di concorrenzialità** è una **valutazione
qualitativa** su struttura della domanda e dell'offerta: modalità di
affidamento, condizioni contrattuali di fornitura, tipo di attività svolta.

> **Perché conta davvero, e perché dirlo vale.** Il perimetro S13 determina
> **che cosa entra nel debito e nel disavanzo pubblico ai fini dei parametri
> europei**. Non è un tecnicismo statistico: è una classificazione con
> **conseguenze giuridiche e finanziarie dirette**. È il ponte con contabilità
> pubblica, ed è il punto in cui si dimostra di aver capito a che cosa serve il
> lavoro di un funzionario statistico.

**La precisazione onesta del manuale**, da citare se si vuole chiudere bene: la
riclassificazione di alcune unità secondo i nuovi criteri **non ha avuto un
impatto significativo** su disavanzo, debito e altri aggregati.

---

# 8. Le venti domande del pignolo

Le risposte sono sopra. Usa questa lista come autoverifica: **se una risposta non
esce in meno di dieci secondi, quella è una voce da ripassare.**

**Mercato del lavoro**
1. Quante ore di lavoro nella settimana di riferimento bastano per essere
   classificati occupati?
2. Un familiare che lavora **senza retribuzione** nella ditta di famiglia è
   occupato? A quali condizioni?
3. Un lavoratore assente da due mesi è occupato? E uno assente da quattro mesi
   che percepisce il 60% della retribuzione?
4. Quali sono i limiti d'età per gli occupati e quali per i disoccupati? Perché
   sono diversi?
5. Ricerca attiva e disponibilità: servono entrambe o ne basta una?
6. Entro quanti giorni deve essere avvenuta la ricerca? Entro quanto deve
   sussistere la disponibilità?
7. Scriva i tre tassi con i rispettivi denominatori.
8. Il tasso di disoccupazione scende. È necessariamente una buona notizia?
9. Oltre il trattino di quale durata si parla di disoccupazione di lunga durata?
10. La durata della disoccupazione coincide con il tempo necessario a trovare
    lavoro? Perché no?
11. Dal 2004 la Rilevazione sulle forze di lavoro è continua: allora perché i
    dati escono trimestrali?
12. Enunci la legge di Okun. Rispetto a che cosa si misura la caduta del PIL?
13. Che cosa distingue la disoccupazione strutturale da quella ciclica, in una
    frase sola?

**Numeri indici**
14. Scriva l'indice dei prezzi di Laspeyres e quello di Paasche. Che cosa cambia
    al denominatore?
15. Quale dei due sovrastima l'inflazione e perché?
16. Quali tre proprietà **non** sono soddisfatte da Laspeyres e Paasche?
17. Perché Fisher è detto «ideale», e quale proprietà gli manca?
18. Perché l'ISTAT usa Laspeyres e non Fisher, che pure è migliore?

**Indici ISTAT e contabilità nazionale**
19. NIC, FOI e IPCA condividono lo stesso paniere? Fino a quale livello?
20. Qual è il test che decide se un'unità entra nel perimetro S13, e che cosa ha
    aggiunto il SEC 2010 rispetto al SEC 95?

---

## Le sei cose da avere in bocca la sera prima

1. **Un'ora** — la soglia dell'occupato.
2. **15 e più / 15-74** — occupati e disoccupati.
3. **Trenta giorni e due settimane** — ricerca e disponibilità.
4. **Disoccupazione = disoccupati / forza lavoro**; gli altri due tassi hanno al
   denominatore la popolazione in età lavorativa.
5. **Laspeyres pesa alla base, Paasche all'anno dato, Fisher è la media
   geometrica dei due.**
6. **Il test del 50% più la concorrenzialità** — è così che si entra in S13.
