# Moda e mediana

**Manuale, cap. 1, §5.7-5.9, pp. 276-279.** Con i due esempi numerici svolti dal
libro (Esempio 13 e Esempio 14) ricostruiti per intero.

---

## Dove siamo, e perché queste due stanno insieme

A p. 269 il manuale divide gli indici di posizione in due famiglie:

| | Come si calcolano | Quali sono |
|---|---|---|
| **medie analitiche** | considerando **tutti** i valori della distribuzione | aritmetica, quadratica, armonica, geometrica |
| **medie lasche** | considerando **solo alcuni** elementi della distribuzione | **moda**, **mediana** |

**Moda e mediana sono medie lasche**, e questa non è un'etichetta: è la loro
natura. Non fanno conti su tutti i dati — **guardano una posizione**. La moda
guarda dove i dati si addensano; la mediana guarda chi sta in mezzo alla fila.

> **La conseguenza, che è la cosa più importante di tutto il documento.** Una
> media analitica usa ogni singolo valore, quindi **un solo dato estremo la
> sposta**. Una media lasca no: **è robusta**.
>
> È il motivo per cui sui redditi si pubblica la **mediana** e non la media.
> Entra un miliardario nel collettivo: la media aritmetica di tutti sale, la
> mediana **non si muove di un centimetro**, perché continua a essere il valore
> di chi sta a metà della graduatoria.

---

# PARTE PRIMA — LA MODA

## La definizione

> **La moda è la modalità che presenta la frequenza più alta.**

Cioè: **il valore che si presenta più spesso**. È l'unico indice di posizione che
si può calcolare anche su un **carattere qualitativo** — non esiste la provincia
media né la provincia mediana, ma **la provincia più frequente esiste**. Vale la
pena dirlo all'orale: mostra che hai capito a che cosa serve.

Il manuale distingue **tre casi**, ed è proprio sul terzo che si viene
interrogati.

## Caso 1 — Modalità singole

Si scorrono le modalità **una ad una** e si prende quella con la frequenza
maggiore. Non c'è altro.

## Caso 2 — Dati in classi di **uguale** ampiezza

**La moda cade nella classe avente la frequenza più alta.**

Qui frequenza e densità danno lo stesso risultato, e il manuale lo dice
espressamente: la classe modale è quella che presenta, **indifferentemente**, la
maggiore frequenza **o** la maggiore densità di frequenza. Se le classi sono
larghe uguale, le due strade coincidono.

## Caso 3 — Dati in classi di **diversa** ampiezza ← *il caso d'esame*

**Qui la frequenza da sola inganna**, e bisogna passare alla **densità di
frequenza**.

> **La densità di frequenza è il rapporto fra la frequenza di ciascuna classe e
> l'ampiezza della classe stessa.** Operativamente, il manuale divide la
> frequenza della classe per **il numero di valori del carattere contenuti in
> essa**.
>
> **La moda cade nella classe che presenta il quoziente più alto**, cioè la
> densità di frequenza più alta.

**Perché serve, in una frase.** Una classe larghissima raccoglie tanti casi
**solo perché è larga**, non perché lì i dati si addensino. La densità
corregge esattamente questo: misura **quanti casi per unità di ampiezza**,
cioè l'affollamento reale.

Ed è per questo che il manuale, parlando di caratteri continui, dà alla moda
questa definizione:

> **la moda è quel valore intorno a cui i casi sono addensati in maggior
> misura.**

## L'Esempio 13 del manuale — svolto

Distribuzione delle imprese di un'area per classi di dipendenti.

| Classi di dipendenti | Numero di aziende |
|---|---|
| 10 - 30 | 21 |
| 30 - 50 | 30 |
| 50 - 75 | 35 |
| 75 - 100 | 30 |
| 100 - 150 | 34 |
| 150 - 200 | 13 |
| 200 - 350 | 75 |
| 350 - 600 | **148** |
| **Totale** | **386** |

**Guarda la colonna delle frequenze.** Il massimo è **148**, nella classe
«350-600 dipendenti». Se ti fermassi qui, diresti che la classe modale è quella.
**È la risposta sbagliata**, e il manuale la mette lì apposta.

Il motivo: quella classe è larga **250 valori**, le prime sono larghe venti.
Ovvio che raccolga più casi.

**Ora la tabella corretta.** Per ogni classe: frequenza, numero di valori del
carattere contenuti nella classe, e il loro quoziente.

| Classe | Frequenza | N. di valori | Densità |
|---|---|---|---|
| 10 - 30 | 21 | 21 | 1,000 |
| **31 - 50** | **30** | **20** | **1,500** ← |
| 51 - 75 | 35 | 25 | 1,400 |
| 76 - 100 | 30 | 25 | 1,200 |
| 101 - 150 | 34 | 50 | 0,680 |
| 151 - 200 | 13 | 50 | 0,260 |
| 201 - 350 | 75 | 150 | 0,500 |
| 351 - 600 | 148 | 250 | 0,592 |
| **Totale** | **386** | | |

**Il quoziente massimo è 1,5**, e si rileva per la classe **«31-50
dipendenti»**: quella, e non l'altra, è **la classe modale**.

Guarda che cosa è successo alla classe «351-600»: aveva la frequenza più alta in
assoluto (148) e finisce **al quinto posto per densità** (0,592). Centoquarantotto
aziende sparse su 250 valori sono **meno affollate** di trenta aziende su venti
valori.

> **Da dire all'orale, ed è la risposta completa:** *«Quando le classi hanno
> ampiezza diversa non si può guardare la frequenza, perché una classe più larga
> raccoglie più casi solo in virtù della sua ampiezza. Si usa la densità di
> frequenza, cioè il rapporto fra la frequenza della classe e la sua ampiezza, e
> la classe modale è quella con la densità più alta. Il manuale porta un esempio
> in cui la classe con la frequenza massima non è affatto la classe modale.»*

---

# PARTE SECONDA — LA MEDIANA

## La definizione

> Data una variabile statistica le cui intensità siano ordinate **in senso
> crescente o decrescente**, **la mediana è quell'indice di posizione
> corrispondente al valore che bipartisce la distribuzione, lasciando metà dei
> casi a sinistra e metà a destra.**

**Due parole da non perdere.**

**«Ordinate».** La mediana **non esiste** se prima non metti i dati in fila. È il
primo gesto, ed è quello che la rende un indice *di posizione in graduatoria* e
non un calcolo.

**«Bipartisce».** Non divide in parti uguali di *valore*: divide in due parti
uguali **di numerosità**. Metà dei casi di qua, metà di là.

## Caso A — Dati non raggruppati in classi

Si cerca **il posto centrale**, e ci sono due situazioni.

**Se le osservazioni sono in numero dispari** il posto centrale è **uno solo**, e
la mediana è l'intensità che occupa quel posto.

**Se le osservazioni sono in numero pari** i posti centrali sono **due**, e si
assume come mediana **la media aritmetica delle due intensità** che li occupano.

> Nota curiosa e utile: nel caso pari, **la mediana può essere un valore che non
> compare fra i dati**. Se i due centrali sono 40 e 45, la mediana è 42,5, che
> nessuno ha. Non è un errore: la mediana è una *posizione*, non per forza
> un'osservazione.

## Caso B — Dati raggruppati, carattere **discreto**

Il manuale dà una procedura in cinque passi. Te la riporto così com'è, e poi te
la traduco.

1. **si calcola il posto centrale**, come nel caso dei dati non raggruppati;
2. **sulla base delle frequenze cumulate si determina la classe in cui cade la
   mediana**;
3. si determina **la differenza fra il posto centrale e la frequenza cumulata
   fino alla classe che precede** quella contenente la mediana;
4. si divide **la frequenza della classe mediana per l'ampiezza** della stessa
   classe;
5. si divide **la differenza del punto 3 per il quoziente del punto 4**.

**Che cosa stai facendo davvero.** Il passo 2 ti dice *in quale classe* cade la
mediana. I passi 3-5 ti dicono **quanto avanzare dentro quella classe**: il
risultato è la quantità da **aggiungere all'estremo inferiore della classe
mediana** — come conferma l'esempio svolto del manuale, che infatti parte da 30
e ci somma il resto.

## Caso C — Dati raggruppati, carattere **continuo**

Si considera **la spezzata cumulativa**, cioè il grafico che rappresenta le
frequenze cumulate, e si **interpola** dentro la classe mediana.

Il manuale precisa come si ottiene il risultato: **considerando i triangoli
simili** ABD e AB'D' costruiti sulla spezzata. Non devi saperlo dimostrare — devi
sapere **che il metodo è una proporzione geometrica**: dentro la classe mediana
si assume che i casi siano distribuiti in modo uniforme, e si avanza in
proporzione.

**Gli elementi che entrano nel calcolo**, con i nomi che usa il manuale:

| Simbolo | Che cos'è |
|---|---|
| estremo inferiore della classe mediana | da dove si parte |
| ampiezza della classe mediana | quanto è larga |
| frequenza della classe mediana | quanti casi contiene |
| **C** | il posto centrale |
| frequenza cumulata fino alla classe **precedente** | quanti casi sono già alle spalle |

## L'Esempio 14 del manuale — svolto passo per passo

Presenze in un villaggio turistico, per classi di età.

| Classi di età | Frequenza | Frequenza cumulata |
|---|---|---|
| 0 - 20 | 94 | 94 |
| 20 - 30 | 104 | 198 |
| **30 - 50** | **132** | **330** ← |
| 50 - 60 | 121 | 451 |
| 60 - 80 | 70 | 521 |
| oltre 80 | 18 | 539 |
| **Totale** | **539** | |

**Passo 1 — il posto centrale.** Le osservazioni sono **539, numero dispari**.
Il posto centrale è **270**.

**Passo 2 — in quale classe cade.** Si scorre la colonna delle **frequenze
cumulate**: fino alla seconda classe siamo a 198, quindi il 270° non c'è ancora;
alla terza siamo a 330, e il 270° è compreso. **La classe mediana è la terza:
«età fra i 30 e i 50 anni».**

> Qui il manuale usa un'immagine che conviene rubare: *il turista che presenta
> l'età mediana è il 270°*. Non un'età: **una persona in fila**.

**Passo 3 — quanto avanzare.** Dentro quella classe bisogna andare avanti di
**270 − 198 = 72** posti.

**Passo 4 — in proporzione.** La classe è larga **20 anni** e contiene **132**
persone. Avanzare di 72 posti su 132 significa percorrere 72/132 della classe,
cioè **20 × (72/132) = 10,91 anni**.

**Passo 5 — il risultato.** Si parte dall'estremo inferiore della classe, **30**,
e si aggiunge:

> **Me = 30 + 10,91 = 40,91** → **l'età mediana stimata è 40,91 anni.**

**La parola «stimata» non è decorativa.** È una stima perché, non conoscendo le
età una per una ma solo la classe, **si assume che dentro la classe 30-50 le
persone siano distribuite uniformemente**. Dirlo all'orale è il dettaglio che
separa chi ha applicato una procedura da chi l'ha capita.

## Le due proprietà della mediana

Il manuale ne enuncia due, e **la seconda è quella che vale un voto in più**.

**Prima proprietà.** Considerando gli scarti dei dati dalla mediana, **il numero
degli scarti di segno positivo è uguale al numero degli scarti di segno
negativo.** È la definizione stessa, vista dall'altro lato: se metà dei casi sta
sotto e metà sopra, gli scarti si bilanciano **come numero**.

**Seconda proprietà.** **La somma dei valori assoluti degli scarti dalla mediana
è minima.** Il manuale lo precisa: scegliendo un qualsiasi altro numero al posto
della mediana, quella somma viene più grande.

> **Che cosa significa, in parole, e perché impressiona.** La mediana è **il
> punto che minimizza la distanza complessiva da tutti i dati**, se le distanze
> si misurano in valore assoluto.
>
> Un'immagine da usare all'orale: *dovendo aprire un unico sportello che serva
> tutti i comuni disposti lungo una strada, il punto che rende minima la somma
> dei chilometri percorsi da tutti non è il punto medio della strada — è il
> punto mediano, quello che lascia metà dei comuni da un lato e metà
> dall'altro.*
>
> **E il collegamento che chiude il discorso**: la media aritmetica gode della
> proprietà analoga, ma rispetto agli scarti **al quadrato**. Mediana ↔ valori
> assoluti; media ↔ quadrati. È per questo che la media è sensibile agli estremi
> e la mediana no: **il quadrato amplifica i valori lontani, il valore assoluto
> no.**

---

# PARTE TERZA — I PERCENTILI (§5.9)

> **I percentili sono indici di posizione che suddividono la distribuzione in
> due parti, lasciando da un lato una data percentuale dei casi e dall'altro la
> restante percentuale.**

La mediana, vista così, è semplicemente **il caso 50/50**.

**I numeri esatti — ed è precisamente il tipo di cosa che un commissario pignolo
chiede:**

| | Quanti sono | Che cosa fanno |
|---|---|---|
| **terzili** | **2** | T₁ lascia a sinistra il **33,3%**; T₂ lascia a sinistra il **66,7%** |
| **quartili** | **3** | Q₁ → **25%**; **Q₂ → 50%, e coincide con la mediana**; Q₃ → **75%** |
| **decili** | **9** | tagliano in dieci parti |
| **centili** | **99** | tagliano in cento parti |

> **La regola che li tiene insieme:** per dividere una distribuzione in *k*
> parti servono **k − 1** tagli. Due terzili per tre parti, tre quartili per
> quattro, nove decili per dieci, novantanove centili per cento. Se ricordi
> questa riga non sbagli mai il numero.

**E la cosa da dire sempre: Q₂ è la mediana.** Sono lo stesso valore chiamato in
due modi.

---

# IL CONFRONTO FINALE

| | **Moda** | **Mediana** | **Media aritmetica** |
|---|---|---|---|
| **Che cos'è** | la modalità più frequente | il valore che bipartisce la distribuzione | il valore che conserva la somma |
| **Famiglia** | media lasca | media lasca | media analitica |
| **Usa tutti i dati?** | no | no | **sì** |
| **Sensibile agli estremi?** | no | no | **sì** |
| **Si può calcolare su un carattere qualitativo?** | **sì** | no | no |
| **Proprietà notevole** | indica dove i casi sono più addensati | **minimizza la somma degli scarti in valore assoluto** | minimizza la somma degli scarti al quadrato |

**Quando si usa quale — la regola pratica:**

- **la moda**, quando interessa **il caso tipico**, o quando il carattere è
  qualitativo e le altre due non esistono;
- **la mediana**, quando la distribuzione è **asimmetrica** o contiene valori
  estremi: redditi, patrimoni, tempi di attesa;
- **la media aritmetica**, quando interessa **il totale** e la distribuzione è
  ragionevolmente simmetrica.

---

# LE DOMANDE D'ORALE, CON LE RISPOSTE GIÀ FORMULATE

**1. Che cos'è la mediana?**
> *«È l'indice di posizione che, in una distribuzione ordinata in senso
> crescente o decrescente, bipartisce la distribuzione lasciando metà dei casi a
> sinistra e metà a destra. È una media lasca, perché non usa tutti i valori ma
> solo la posizione centrale — e per questo è robusta rispetto ai valori
> estremi.»*

**2. Come si trova con un numero pari di osservazioni?**
> *«I posti centrali diventano due, e si assume come mediana la media aritmetica
> delle due intensità che li occupano. Può quindi risultare un valore che non
> compare fra i dati osservati.»*

**3. Che cos'è la classe modale quando le classi hanno ampiezza diversa?**
> *«Non è la classe con la frequenza più alta: è quella con la densità di
> frequenza più alta, cioè il rapporto fra la frequenza della classe e la sua
> ampiezza. Altrimenti si premierebbe una classe solo perché è più larga.»*

**4. Perché sui redditi si usa la mediana?**
> *«Perché la distribuzione dei redditi è fortemente asimmetrica. La media
> aritmetica usa tutti i valori e viene trascinata verso l'alto da pochi redditi
> molto elevati; la mediana guarda solo chi sta a metà della graduatoria e non
> ne risente. La mediana descrive l'italiano tipico, la media no.»*

**5. Qual è la proprietà più importante della mediana?**
> *«Che la somma dei valori assoluti degli scarti dalla mediana è minima: nessun
> altro valore rende quella somma più piccola. È il corrispettivo, in valore
> assoluto, della proprietà che la media aritmetica ha rispetto agli scarti al
> quadrato.»*

**6. Quanti sono i quartili?**
> *«Tre, e il secondo coincide con la mediana. In generale, per dividere una
> distribuzione in k parti servono k − 1 valori: due terzili, tre quartili, nove
> decili, novantanove centili.»*

---

# LE SEI COSE DA RICORDARE

1. **Moda e mediana sono medie lasche**: non usano tutti i dati, e per questo
   **sono robuste**.
2. **La moda è l'unica** che funziona anche sui caratteri qualitativi.
3. **Classi di ampiezza diversa → densità di frequenza**, non frequenza. Nel
   manuale la classe con 148 aziende **non** è la classe modale.
4. **Mediana**: si ordina, si trova il posto centrale, e se le osservazioni sono
   pari si fa la media dei due centrali.
5. **Dentro la classe mediana si avanza in proporzione** — ed è una **stima**,
   perché si assume la distribuzione uniforme dentro la classe.
6. **La mediana minimizza la somma degli scarti in valore assoluto**; la media
   aritmetica minimizza quella degli scarti al quadrato. **Qui sta tutta la
   differenza fra le due.**
