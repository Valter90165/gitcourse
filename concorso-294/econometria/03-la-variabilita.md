# La variabilità

**Manuale, cap. 1, §6, pp. 280-287.** Spiegata dall'inizio, con un solo esempio
portato fino in fondo.

---

# 1. Perché esiste tutto questo capitolo

Due uffici della stessa amministrazione. Giorni impiegati a pagare cinque
fatture:

| | | | | | | **Media** |
|---|---|---|---|---|---|---|
| **Ufficio A** | 43 | 44 | 45 | 46 | 47 | **45** |
| **Ufficio B** | 10 | 20 | 45 | 70 | 80 | **45** |

**Stessa identica media: 45 giorni.** E sono due uffici completamente diversi.

Nell'ufficio A un fornitore sa che verrà pagato in un mese e mezzo, punto.
Nell'ufficio B può essere pagato in dieci giorni o in ottanta, ed è una lotteria.
**Se fossi un fornitore, la media non ti direbbe nulla di ciò che ti interessa.**

> **Questa è l'intera ragione del §6.** La media risponde alla domanda *dove
> stanno i dati*. Ma due distribuzioni possono stare nello stesso posto ed
> essere opposte. Serve una seconda domanda: **quanto sono sparsi?**

Il manuale la definisce così: gli indici di variabilità sono

> **quantità atte a misurare la tendenza di un fenomeno ad assumere diverse
> modalità quantitative.**

Tradotto: **misurano quanto i dati si discostano fra loro invece di
assomigliarsi.**

---

# 2. La mappa: tre modi diversi di misurare la dispersione

Prima degli strumenti, **la logica**. Il manuale (p. 269) organizza la famiglia
così, e se tieni questa mappa non ti perdi più.

| | L'idea | Gli strumenti |
|---|---|---|
| **A. Misure di posizione** | guardo **solo due punti** della distribuzione | campo di variazione, differenza interquartilica |
| **B. Dispersione intorno a una media** | misuro **quanto ogni dato dista dal centro** | scostamenti semplici medi, devianza, varianza, scarto quadratico medio |
| **C. Disuguaglianza fra i dati** | confronto **ogni dato con tutti gli altri** | differenze medie |

**A è economico ma grossolano. B è il cuore del capitolo. C risponde a una
domanda leggermente diversa.** Vediamoli in quest'ordine.

---

# 3. Famiglia A — guardare solo due punti

## Il campo di variazione

> **È la differenza fra l'intensità massima e l'intensità minima.**

Nel nostro esempio: **A = 47 − 43 = 4 giorni. B = 80 − 10 = 70 giorni.**

Già questo separa i due uffici, e costa un secondo di calcolo. Ma il manuale ne
elenca **tre difetti**, ed è la domanda d'orale tipica:

1. **tiene conto solo dei due valori estremi**, senza considerare la struttura
   interna della distribuzione;
2. **è influenzabile da valori estremi anormali** — un solo caso stravagante lo
   gonfia;
3. **non è determinabile quando la classe iniziale e quella finale sono aperte**
   (del tipo «oltre 80 anni»: se non sai dove finisce, non puoi fare la
   sottrazione).

## La differenza interquartilica

> **È la differenza fra il terzo e il primo quartile: Q₃ − Q₁.**

**Nell'intervallo che individua cade il 50% dei casi** — cioè la metà centrale
della distribuzione.

**Il vantaggio sul campo di variazione**: tagliando via il 25% più basso e il 25%
più alto, **butta fuori proprio i valori estremi** che disturbavano. È
l'equivalente, per la variabilità, di ciò che la mediana è per la posizione: una
misura **robusta**.

**Il difetto, che il manuale dichiara**: al pari del campo di variazione,
**anche questo indice non tiene conto della struttura interna** della
distribuzione. Guarda due punti, sia pure due punti meglio scelti.

---

# 4. Famiglia B — il cuore: la distanza dal centro

Qui si cambia filosofia. **Non più due punti: tutti.**

## L'idea, e il problema che nasce subito

L'idea naturale è questa: per ogni dato calcolo **quanto dista dalla media**
(questo si chiama **scarto**), e poi faccio la media di queste distanze.

Proviamo sull'ufficio A, la cui media è 45:

| Dato | 43 | 44 | 45 | 46 | 47 |
|---|---|---|---|---|---|
| **Scarto dalla media** | −2 | −1 | 0 | +1 | +2 |

Sommiamo gli scarti: −2 −1 + 0 + 1 + 2 = **0**.

Proviamo sull'ufficio B: −35, −25, 0, +25, +35. Somma: **0**.

> **Non è un caso: viene sempre zero.** È una proprietà della media aritmetica —
> è il punto di equilibrio, quindi ciò che sta sotto compensa esattamente ciò
> che sta sopra.
>
> **Quindi la strada ovvia non funziona**, e tutta la famiglia B nasce da un
> unico problema pratico: **come rendo positivi gli scarti**, in modo che non si
> annullino?

**Ci sono due risposte, e sono le due metà del capitolo.**

| La risposta | Dove porta |
|---|---|
| **prendo il valore assoluto** (ignoro il segno) | → gli **scostamenti semplici medi** |
| **li elevo al quadrato** | → **devianza, varianza, scarto quadratico medio** |

---

## 4a. La prima risposta: il valore assoluto

### Scostamento semplice medio dalla media aritmetica (§6.3)

> **È la media aritmetica — semplice o ponderata — dei valori assoluti degli
> scarti dalla media aritmetica.**

Sul nostro esempio:

- **Ufficio A**: gli scarti in valore assoluto sono 2, 1, 0, 1, 2. Somma 6,
  divisa per 5 → **1,2 giorni**.
- **Ufficio B**: 35, 25, 0, 25, 35. Somma 120, divisa per 5 → **24 giorni**.

**Si legge così**: *in media, un ufficio A si discosta di 1,2 giorni dal proprio
tempo medio; un ufficio B di 24.* Una frase che si capisce.

**La differenza rispetto alla famiglia A**, e il manuale la sottolinea: a
differenza del campo di variazione e della differenza interquartilica, **questo
indice tiene conto di tutte le intensità** della distribuzione.

### Scostamento semplice medio dalla mediana (§6.4)

Identico, ma gli scarti si misurano **dalla mediana** invece che dalla media.

> **E qui torna la proprietà che abbiamo visto ieri.** Ricordi? *La somma dei
> valori assoluti degli scarti dalla mediana è minima.*
>
> **Conseguenza diretta: lo scostamento semplice medio dalla mediana è sempre
> minore o uguale a quello dalla media.** Non è una curiosità: è *il motivo* per
> cui il manuale dedica un paragrafo a ciascuno. Saperlo collegare, all'orale,
> vale molto.

**Nota operativa** valida per entrambi: quando i dati sono raggruppati in classi,
**si sostituisce a ciascun valore il valore centrale della classe**.

---

## 4b. La seconda risposta: il quadrato

Questa è la strada che la statistica ha scelto davvero, e il manuale la tratta
in due paragrafi — **in un ordine che conviene invertire** per capirla.

### Devianza (§6.6)

> **È la somma — semplice o ponderata — dei quadrati degli scarti fra le singole
> intensità e la media aritmetica.**

Sul nostro esempio:

- **Ufficio A**: 4 + 1 + 0 + 1 + 4 = **10**
- **Ufficio B**: 1225 + 625 + 0 + 625 + 1225 = **3.700**

**È una somma**, quindi **cresce col numero di osservazioni**: cento uffici
tranquilli avrebbero una devianza più grande di cinque uffici caotici. Da sola
non si può confrontare.

### Varianza (§6.6)

> **È il rapporto fra la devianza e la numerosità N del collettivo.**

Cioè: **la devianza divisa per quanti sono**. È la devianza resa confrontabile.

- **Ufficio A**: 10 / 5 = **2**
- **Ufficio B**: 3.700 / 5 = **740**

**Il problema della varianza, che il manuale dichiara**: è **espressa nel
quadrato dell'unità di misura** del fenomeno. La varianza dell'ufficio A è «2
giorni al quadrato». **Giorni al quadrato non significa niente**, non si può dire
a voce e non si può spiegare a un dirigente.

### Scarto quadratico medio (§6.5)

> **È la media quadratica degli scostamenti fra le singole intensità e la media
> aritmetica.** Ed è, operativamente, **la radice quadrata della varianza**.

- **Ufficio A**: √2 = **1,41 giorni**
- **Ufficio B**: √740 = **27,2 giorni**

**Ed eccoci tornati in giorni.** Questo è tutto il senso della radice: **riporta
la misura nell'unità originaria**, e quindi la rende dicibile.

> **La catena da raccontare all'orale, ed è la risposta completa:**
>
> *«Si parte dagli scarti dalla media, che però sommati danno sempre zero. Si
> elevano al quadrato per renderli positivi, e la loro somma è la **devianza**.
> La devianza dipende da quante osservazioni ci sono, quindi la si divide per
> N e si ottiene la **varianza**. La varianza però è espressa nel quadrato
> dell'unità di misura, quindi se ne estrae la radice e si ottiene lo **scarto
> quadratico medio**, che è nella stessa unità del fenomeno ed è l'indice che
> si usa in pratica.»*
>
> **Quattro frasi, nessuna formula, e hai spiegato metà del capitolo.**

**Due precisazioni che il manuale aggiunge e che valgono punti:**

- **lo scarto quadratico medio è un indice di variabilità assoluta**, perché è
  espresso nella stessa unità di misura dei dati;
- c'è un legame elegante con le medie che già conosci: **la varianza è la
  differenza fra il quadrato della media quadratica e il quadrato della media
  aritmetica.** È la formula «semplificata» che il manuale usa per non dover
  calcolare tutti gli scarti uno per uno — e nell'**Esempio 15** (altezze di 125
  atleti) la applica proprio così: 34.331,85 − 34.276,82 = **55,03**.

**Una nota tecnica da riconoscere, non da saper fare**: quando i dati sono
raggruppati in classi si usano i valori centrali, e questo introduce
un'approssimazione; per correggerla si applica la **correzione di Sheppard**. Ti
basta sapere che esiste e a che cosa serve.

---

# 5. Assoluto e relativo — la distinzione che vale un voto

Siamo arrivati al punto più importante dopo la catena devianza-varianza-s.q.m.

| | Che cosa sono | Il limite / il pregio |
|---|---|---|
| **indici assoluti** | espressi **nella stessa unità di misura** del fenomeno | descrivono bene **una** distribuzione, ma **non permettono confronti** fra fenomeni diversi |
| **indici relativi** | ottenuti **rapportando** un indice assoluto a un altro parametro: sono **numeri puri**, senza unità di misura | **servono proprio a confrontare** |

**Il problema, con un esempio.** Lo scarto quadratico medio dei giorni di
pagamento è in giorni; quello degli stipendi è in euro. **Quale dei due fenomeni
è più variabile?** La domanda, così, non ha risposta: stai confrontando giorni
con euro.

## Il coefficiente di variabilità

> **È il rapporto fra lo scarto quadratico medio e la media aritmetica.** È un
> **numero puro** e **si esprime generalmente in percentuale**.

Sul nostro esempio:

| | s.q.m. | media | **coefficiente di variabilità** |
|---|---|---|---|
| **Ufficio A** | 1,41 | 45 | **3,1%** |
| **Ufficio B** | 27,2 | 45 | **60,4%** |

**Adesso i numeri parlano da soli**: nell'ufficio A la dispersione vale il 3%
del tempo medio, nell'ufficio B il 60%. E questi due numeri si possono
confrontare **con qualunque altro fenomeno**, misurato in qualunque unità.

> **La frase d'orale**: *«Il coefficiente di variabilità è il rapporto fra lo
> scarto quadratico medio e la media aritmetica. Essendo un numero puro,
> permette di confrontare la variabilità di fenomeni espressi in unità di
> misura diverse, cosa che gli indici assoluti non consentono.»*

## Gli indici rapportati al massimo (§6.8)

C'è un secondo modo di costruire un indice relativo: **rapportare l'indice
assoluto al valore che avrebbe nella distribuzione di massima variabilità** —
quella che il manuale chiama **distribuzione massimante**.

**Il risultato è un indice che varia fra 0 e 1**: vale **0 se la variabilità è
nulla** e **1 se è massima**.

Ti basta sapere **l'idea** — misurare la variabilità osservata come frazione
della massima possibile — e che esiste **per lo s.q.m.** e **per la differenza
media senza ripetizione**. I passaggi algebrici non sono materia da orale.

## La standardizzazione — un ponte verso i capitoli successivi

Il manuale, chiudendo il §6.5, introduce una cosa che sembra minore e invece
tornerà in continuazione: **gli scarti standardizzati**.

> Si prende lo scarto di un dato dalla media e **lo si divide per lo scarto
> quadratico medio**.

**Che cosa ottieni**: un numero che dice **quanti scarti quadratici medi quel
dato è lontano dalla media**. Un ufficio che paga in 72 giorni, in un contesto
con media 45 e s.q.m. 27, sta **a un s.q.m. dalla media**: tanto, ma non
eccezionale.

> **Perché segnartelo adesso.** È il meccanismo su cui si reggeranno la
> distribuzione normale (cap. 3), gli intervalli di confidenza (cap. 4) e i test
> (cap. 5). **Standardizzare significa smettere di misurare in giorni o in euro
> e cominciare a misurare in «quanto è insolito».**

---

# 6. Famiglia C — la disuguaglianza fra i dati (§6.7)

Un'idea diversa dalle precedenti, e il manuale la tiene separata apposta.

Finora abbiamo sempre misurato **la distanza dei dati da un centro**. Le
**differenze medie** fanno un'altra cosa: **confrontano i dati a due a due, fra
loro**, senza passare da nessuna media.

> **La differenza media è un indice assoluto di variabilità che misura la
> disuguaglianza media fra le intensità di una variabile statistica, ottenuta
> confrontando tutti i termini a due a due.**

E ne esistono due versioni, che si distinguono per un dettaglio:

| | Il confronto di un termine con se stesso | Quanti confronti |
|---|---|---|
| **con ripetizione** | **incluso** | N² |
| **senza ripetizione** | **escluso** | N² − N = N(N−1) |

**Perché la distinzione esiste, in parole.** Confrontare un valore con se stesso
dà sempre zero. Quei confronti nulli sono N, e includerli o no cambia il
denominatore — quindi cambia il risultato. **Con ripetizione il risultato è più
piccolo**, perché gli N zeri «diluiscono» la media.

> **Il senso di questa famiglia**: risponde alla domanda *«quanto sono diversi
> fra loro?»* invece di *«quanto sono lontani dal centro?»*. Sono due domande
> parenti ma non identiche — ed è questa la ragione per cui il manuale distingue
> fin da p. 269 le misure di **dispersione** da quelle di **disuguaglianza**.

---

# 7. La concentrazione (§6.9) — un caso a parte

Il manuale la presenta come **un aspetto della variabilità**, ma con una
limitazione netta che è **la cosa da ricordare**:

> **La concentrazione ha senso solo per caratteri additivi e trasferibili** —
> come il reddito o il capitale azionario — **vale a dire se la sua intensità
> globale o una sua parte possono essere possedute da una o più unità.**

**Tradotto**: ha senso chiedersi *quanto del totale è in mano a pochi?* solo se
quel totale è una cosa che si può ammucchiare e passare di mano. **Il reddito
sì, l'altezza no**: non esiste il «totale delle altezze» che qualcuno possa
possedere.

E il concetto opposto:

> **Un carattere si dice equidistribuito se non è concentrato in assoluto**, vale
> a dire se determinate frazioni del suo ammontare appartengono a uguali
> frazioni di unità statistiche.

Cioè: il 10% delle unità possiede il 10% del totale, il 20% ne possiede il 20%,
e così via. **Perfetta uguaglianza.**

Gli strumenti sono il **rapporto di concentrazione** e **l'indice di Gini**, che
il manuale distingue (il secondo non tiene conto di un elemento di cui tiene
conto il primo). Per l'orale basta **sapere che misurano quanto il totale è
distribuito in modo diseguale**, e il vincolo dei caratteri **additivi e
trasferibili**, che è la vera domanda da pignolo.

---

# L'ALBERO COMPLETO, IN UNA PAGINA

```
                    QUANTO SONO SPARSI I DATI?
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
   guardo due punti     distanza dal centro    confronto a due a due
        │                      │                      │
  campo di variazione          │              DIFFERENZE MEDIE
  differenza interquartilica   │              · con ripetizione
                               │              · senza ripetizione
                    gli scarti danno somma zero
                               │
              ┌────────────────┴────────────────┐
         valore assoluto                    quadrato
              │                                 │
   scostamento semplice medio              DEVIANZA
   · dalla media aritmetica                    │ : N
   · dalla mediana  ← il minimo            VARIANZA
                                               │ √
                                     SCARTO QUADRATICO MEDIO
                                               │ : media
                                   COEFFICIENTE DI VARIABILITÀ
                                        (numero puro)
```

---

# LE OTTO COSE DA RICORDARE

1. **La media non basta**: due distribuzioni con la stessa media possono essere
   opposte. La variabilità è la seconda domanda.
2. **Campo di variazione e differenza interquartilica guardano solo due punti** e
   non vedono la struttura interna. Il campo di variazione, in più, **non esiste
   se le classi estreme sono aperte**.
3. **Gli scarti dalla media sommati danno sempre zero.** Tutto il resto del
   capitolo nasce da questo problema.
4. **Due vie d'uscita**: valore assoluto → scostamenti semplici medi; quadrato →
   devianza, varianza, s.q.m.
5. **La catena**: scarti → al quadrato → **devianza** → diviso N → **varianza** →
   radice → **scarto quadratico medio**.
6. **La varianza è in unità al quadrato e non si può dire a voce**; lo scarto
   quadratico medio sì. È per questo che si fa la radice.
7. **Assoluto vs relativo**: gli assoluti descrivono, i relativi **confrontano**.
   Il **coefficiente di variabilità** è s.q.m. diviso media, è un numero puro e
   si esprime in percentuale.
8. **La concentrazione vale solo per caratteri additivi e trasferibili.**
