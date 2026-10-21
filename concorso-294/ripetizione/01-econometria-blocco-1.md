# Blocco 1 da ripetere — Econometria e statistica di base

**Dodici domande realmente uscite all'orale**, con la risposta da dire a voce.
Ogni risposta sta in **30-60 secondi**. Non sono riassunti da leggere: sono
**testi da provare ad alta voce** finché non escono da soli.

**Come si usa.** Leggi la domanda, chiudi il foglio, rispondi a voce. Poi
riapri e confronta. Non conta ripetere le stesse parole: conta che ci siano
**i pezzi segnati in grassetto**.

---

## 1. Che cosa distinguono media, mediana e moda? In quali casi sono utili?
*(domanda 107)*

> La **media aritmetica** è il valore che, sostituito a tutti i dati, **lascia
> invariata la somma**. La **mediana** è il valore che **bipartisce la
> distribuzione**, lasciando metà dei casi a sinistra e metà a destra. La
> **moda** è **la modalità più frequente**.
>
> La differenza che conta è che la media **usa tutti i valori**, e quindi **un
> solo dato estremo la sposta**; mediana e moda guardano una posizione e perciò
> **sono robuste**.
>
> Per questo **sui redditi si pubblica la mediana**: pochi redditi altissimi
> alzano la media di tutti e non spostano la mediana di un centimetro. La moda,
> infine, è **l'unica calcolabile anche su un carattere qualitativo**: non
> esiste la provincia media, ma la provincia più frequente sì.

**I pezzi che devono esserci**: la media usa tutti i dati → sensibile agli
estremi; la mediana bipartisce → robusta; la moda funziona anche sul
qualitativo; l'esempio dei redditi.

---

## 2. Che cosa significa variabile qualitativa, quantitativa, nominale o ordinale?
*(domanda 108)*

> Un carattere è **quantitativo** se si esprime con un numero e genera una
> **variabile statistica**; è **qualitativo** se si esprime con una modalità
> non numerica e genera una **mutabile statistica**.
>
> Le mutabili si distinguono a loro volta: sono **rettilinee** — cioè
> ordinabili — se esiste un ordine naturale o logico fra le modalità, come il
> livello contrattuale; sono **sconnesse** se quell'ordine non c'è, come la
> provincia o il partito votato.
>
> La distinzione non è formale: **decide che cosa si può calcolare**. Sulle
> sconnesse si può solo contare, quindi l'unico indice di posizione è **la
> moda**; sulle rettilinee si può anche ordinare, e quindi **si aggiunge la
> mediana**; la media aritmetica richiede operazioni algebriche e **vuole
> numeri**.

**I pezzi**: variabile = numeri, mutabile = parole; rettilinee vs sconnesse;
contare < ordinare < calcolare.

---

## 3. Differenza tra indagine censuaria e campionaria
*(domanda 281)*

> L'indagine **censuaria** riguarda **l'intera popolazione** oggetto di studio;
> quella **campionaria** ne osserva solo **un sottoinsieme**, il campione.
>
> Il censimento dà il dato esatto ma **costa molto ed è lento**, perciò si fa di
> rado. L'indagine campionaria costa meno ed è **molto più tempestiva**, ma
> introduce **l'errore campionario**: il campione può non rappresentare
> perfettamente la popolazione.
>
> L'esempio istituzionale è la **Rilevazione sulle forze di lavoro** dell'ISTAT,
> che è campionaria e **continua dal 2004**, con diffusione trimestrale.

**I pezzi**: tutta la popolazione vs un sottoinsieme; costo e tempestività
contro errore campionario; l'esempio ISTAT.

---

## 4. Scarto quadratico medio: significato
*(domanda 218)*

> È **l'indice di variabilità più usato**, e misura **quanto in media i dati si
> allontanano dalla loro media aritmetica**.
>
> Si costruisce così: si prendono gli scarti di ogni dato dalla media, ma
> **sommati darebbero sempre zero**, perché la media è il punto di equilibrio.
> Allora **si elevano al quadrato** e si sommano: è la **devianza**. La si
> divide per il numero delle osservazioni e si ottiene la **varianza**. La
> varianza però è espressa **nel quadrato dell'unità di misura**, che non
> significa nulla: se ne estrae la radice e si torna all'unità originaria.
>
> È un **indice di variabilità assoluta**, perché è espresso nella stessa unità
> dei dati.

**I pezzi**: gli scarti fanno zero → quadrato → devianza → varianza → radice;
la varianza è in unità al quadrato; è un indice assoluto.

---

## 5. Coefficiente di variazione: confronto della dispersione fra fenomeni su scale diverse
*(domanda 217)*

> È il rapporto fra lo **scarto quadratico medio** e la **media aritmetica**, e
> si esprime di solito in percentuale.
>
> Serve perché **gli indici assoluti non si possono confrontare fra fenomeni
> diversi**: lo scarto quadratico medio dei tempi di pagamento è in giorni,
> quello degli stipendi è in euro, e giorni ed euro non si confrontano.
> Dividendo per la media **le unità si semplificano** e resta **un numero
> puro**.
>
> Esempio: tempi di pagamento con media 45 giorni e scarto quadratico medio 27
> danno **il 60%**; stipendi con media 30.000 euro e scarto quadratico medio
> 6.000 danno **il 20%**. Sono i tempi di pagamento a essere molto più
> variabili, **mentre il numero grezzo diceva il contrario**.

**I pezzi**: s.q.m. diviso media; numero puro; serve a confrontare scale
diverse; l'esempio che si rovescia.

---

## 6. Che effetto hanno gli outlier sui risultati?
*(domanda 121)*

> Un **outlier** è un valore anomalo, molto distante dagli altri. Il suo effetto
> dipende da **quale strumento stai usando**.
>
> Sugli indici che **usano tutti i dati** l'effetto è forte: sposta la **media
> aritmetica**, e **gonfia lo scarto quadratico medio**, perché gli scarti
> vengono elevati al quadrato e **quello lontano pesa moltissimo**. Gonfia anche
> il **campo di variazione**, che guarda solo i due estremi.
>
> Sugli indici **robusti** l'effetto è minimo: **mediana**, **moda** e
> **differenza interquartilica** quasi non se ne accorgono.
>
> In una **regressione** un outlier può **tirare a sé la retta**, perché i minimi
> quadrati minimizzano i quadrati degli scarti e quindi **penalizzano moltissimo
> i punti lontani**. Per questo si guardano sempre i dati prima di stimare.

**I pezzi**: la distinzione indici sensibili / robusti; il quadrato amplifica;
in regressione tira la retta.

---

## 7. Che cos'è un modello econometrico e a cosa serve per la valutazione delle politiche?
*(domanda 113)*

> Un modello è **una rappresentazione formale delle conoscenze su un fenomeno**:
> non una riproduzione esatta, ma **una versione semplificata**, scritta sotto
> forma di una o più equazioni.
>
> Un modello **econometrico** mette in relazione grandezze economiche
> distinguendo le variabili che il modello **spiega** — le endogene — da quelle
> che **prende come date** — le esogene.
>
> Per la valutazione delle politiche serve a rispondere alla domanda centrale:
> **quanta parte del risultato osservato è attribuibile all'intervento** e
> quanta ad altri fattori. Senza un modello si confronta il prima e il dopo e si
> attribuisce alla politica anche ciò che sarebbe successo comunque.

**I pezzi**: rappresentazione formale e semplificata; endogene ed esogene;
attribuire l'effetto all'intervento e non ad altro.

---

## 8. Che cosa sono variabile dipendente e variabile esplicativa?
*(domanda 114)*

> La **dipendente** è **quello che voglio spiegare**; l'**esplicativa** —
> o indipendente — è **quello con cui provo a spiegarlo**.
>
> Esempio: se studio i tempi di pagamento dei comuni in funzione del personale
> in ragioneria, i **giorni di pagamento** sono la dipendente e gli **addetti**
> l'esplicativa.
>
> La scelta **non è nei dati, la fa il ricercatore** in base alla domanda e alla
> teoria: è il modo in cui si dichiara **quale direzione si sta ipotizzando**.

**I pezzi**: cosa spiego / con cosa lo spiego; l'esempio; la scelta è del
ricercatore.

---

## 9. Che cos'è la regressione lineare semplice?
*(domanda 115)*

> È il modello che **spiega una variabile dipendente con una sola variabile
> esplicativa**, assumendo fra le due **un legame lineare**: graficamente, una
> retta tracciata dentro la nuvola dei punti osservati.
>
> La retta è descritta da due numeri: l'**intercetta**, cioè **da dove parte**,
> e il **coefficiente angolare**, che dice **di quanto varia la dipendente
> quando l'esplicativa aumenta di una unità**.
>
> A questi si aggiunge un terzo elemento, l'**errore ε**, che è **lo scarto fra
> ciò che il modello prevede e ciò che si osserva**. Esiste perché fra due
> grandezze economiche **non c'è mai un legame deterministico**: si lavora su
> campioni, ci sono errori di misurazione e agiscono fattori che nessuna
> equazione può contenere tutti. **Un modello senza errore sarebbe una finzione.**

**I pezzi**: una sola esplicativa; intercetta e coefficiente angolare; ε e
perché esiste.

---

## 10. Che cosa si intende per coefficiente ed errore standard?
*(domanda 117)*

> Il **coefficiente** è il numero che dice **di quanto varia la dipendente
> quando l'esplicativa aumenta di un'unità**, tenendo fermo il resto. Si legge
> sempre **«in media»**: non vale per il singolo caso, vale sulla media dei casi.
>
> L'**errore standard** misura **quanto quel coefficiente è stimato con
> precisione**: dice di quanto potrebbe cambiare se rifacessi lo stesso studio
> su un altro campione.
>
> Vanno letti **insieme**. Un coefficiente grande con un errore standard grande
> **non è una scoperta**: vuol dire che il dato è troppo incerto per concludere
> qualcosa. Un coefficiente piccolo ma stimato con precisione **può essere molto
> più informativo**.

**I pezzi**: il coefficiente è l'effetto di un'unità in più, «in media»;
l'errore standard è la precisione; vanno letti insieme.

---

## 11. Misure della bontà di adattamento di un modello: quali sono?
*(domanda 211)*

> La principale è l'**R quadro**, o **coefficiente di determinazione**: è **la
> quota della variabilità della dipendente che il modello riesce a spiegare**.
>
> Si ottiene confrontando **la devianza spiegata dalla regressione con la
> devianza totale**. **Va da 0 a 1**: vale 0 quando la retta è orizzontale e la
> variabile esplicativa non aiuta affatto, vale 1 quando tutti i punti stanno
> esattamente sulla retta.
>
> Si legge come percentuale: un R quadro di 0,40 significa che **il modello
> spiega il 40% della variabilità**, e il resto è errore. Accanto all'R quadro
> si guardano l'**R quadro corretto**, che tiene conto del numero di variabili
> inserite, e **l'analisi dei residui**.

**I pezzi**: quota di variabilità spiegata; devianza spiegata su totale; va da
0 a 1; si legge in percentuale.

---

## 12. Gli indici di bontà di adattamento misurano anche la capacità predittiva?
*(domanda 212)*

> **No, ed è una distinzione importante.** L'R quadro misura **quanto bene il
> modello si adatta ai dati con cui è stato stimato**, non quanto bene
> prevedrebbe su dati nuovi.
>
> Il motivo è che **aggiungendo variabili l'R quadro non può che salire**, anche
> se quelle variabili sono irrilevanti: il modello finisce per **inseguire le
> particolarità di quel campione** invece della relazione vera. È il problema del
> **sovra-adattamento**, l'*overfitting*.
>
> Per valutare la capacità predittiva serve **provare il modello su dati che non
> ha mai visto**: si divide il campione in una parte per la stima e una per la
> verifica, oppure si usa la **convalida incrociata**, la *cross-validation*.

**I pezzi**: adattamento ≠ previsione; l'R quadro sale sempre aggiungendo
variabili; overfitting; train/test e cross-validation.

---

# La regola d'oro per tutte e dodici

**Struttura ogni risposta in tre tempi:**

1. **che cos'è** — una frase di definizione;
2. **a che serve o perché esiste** — una frase di senso;
3. **un esempio o una conseguenza** — una frase concreta.

Chi si ferma al primo tempo prende 21. **Chi arriva al terzo prende 26.** E il
terzo tempo è sempre la parte più facile, perché è quella che non richiede
memoria: richiede solo di aver capito.
