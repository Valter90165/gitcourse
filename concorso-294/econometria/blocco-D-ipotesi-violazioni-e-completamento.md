# Blocco D — il completamento della regressione

Quello che restava del blocco regressione: **le ipotesi del modello classico, le
violazioni, l'endogeneita', e le domande di coda.** Circa **12 domande del
repertorio**.

Era il materiale previsto per il 7 novembre (EC-3 e la rassegna EC-8/EC-9/EC-11/
EC-12), anticipato a oggi per tenere la regressione tutta insieme.

Solo definizioni, nessun esempio. Ogni termine attaccato al suo pezzo di
definizione.

---

## La spina del blocco

**Prima le ipotesi, poi una violazione per ogni ipotesi che cade.**

Non si memorizza una lista di violazioni: si memorizzano **le ipotesi**, e poi
ci si chiede **«quale ipotesi e' caduta?»**. Ogni risposta e' una violazione con
il suo nome, la sua conseguenza e il suo rimedio.

---

# 1. Le ipotesi del modello classico *(domanda 116)*

La domanda generatrice: **che cosa deve valere perche' i minimi quadrati
funzionino?** Cinque cose, piu' una che serve ad altro.

**Linearita' nei parametri, cioe' la relazione deve essere lineare nei
coefficienti** da stimare.

**Esogeneita', cioe' il termine di errore non deve essere correlato con le
variabili esplicative.** E' l'ipotesi piu' importante delle cinque: se cade,
cade la correttezza della stima.

**Omoschedasticita', cioe' la varianza dell'errore deve essere costante** al
variare delle esplicative.

**Assenza di autocorrelazione, cioe' gli errori non devono essere correlati fra
loro.**

**Assenza di multicollinearita' perfetta, cioe' nessuna esplicativa deve essere
esattamente ricostruibile dalle altre** — altrimenti il modello non e' stimabile.

E poi la sesta, che **non serve a BLUE**: **la normalita' dell'errore**. Serve
per i test e per gli intervalli di confidenza, non per la proprieta' di essere
il migliore stimatore lineare non distorto. Tenerle distinte fa colpo, perche'
molti le accorpano.

**Se le cinque valgono, lo stimatore dei minimi quadrati e' BLUE.**

---

# 2. Le violazioni — una per ipotesi

## La frase che vale tutto il blocco

**Eteroschedasticita' e autocorrelazione rompono l'efficienza e i test;
l'endogeneita' rompe la correttezza.** Se all'orale si dice solo questa, si ha
gia' preso il punto.

## Cade l'omoschedasticita' → eteroschedasticita' *(EC-8)*

**Eteroschedasticita', cioe' la varianza dell'errore non e' costante ma cambia
al variare delle esplicative.**

**Conseguenze, e sono due, da dire separate.** Lo stimatore **resta non
distorto** — i coefficienti sono ancora centrati sul valore giusto. Ma **non e'
piu' a varianza minima**, cioe' perde la proprieta' «best», e soprattutto **gli
errori standard calcolati sono sbagliati**: quindi la statistica t e i test di
significativita' non sono piu' affidabili. Il problema non e' il coefficiente,
e' il giudizio sul coefficiente.

**Rimedi**: gli **errori standard robusti**, che correggono il calcolo della
precisione lasciando i coefficienti dove sono; oppure i **minimi quadrati
ponderati**.

## Cade l'assenza di autocorrelazione → autocorrelazione *(domanda 127)*

**Autocorrelazione, cioe' gli errori di periodi diversi sono correlati fra
loro.** E' tipica delle **serie storiche**, dove un disturbo di un periodo si
trascina in quello successivo.

**Conseguenze: le stesse dell'eteroschedasticita'.** Stimatore non distorto, ma
non efficiente, e **errori standard sbagliati**: quasi sempre sottostimati,
quindi si rischia di dichiarare significativo un coefficiente che non lo e'.

**Rimedi**: errori standard robusti all'autocorrelazione, o modelli che
specificano esplicitamente la dinamica temporale.

## Cade l'esogeneita' → endogeneita' *(domande 128 e 222)*

**Endogeneita', cioe' una variabile esplicativa e' correlata con il termine di
errore.**

**Questa e' la violazione grave**, e la differenza va detta chiaramente: **lo
stimatore diventa distorto e inconsistente.** «Inconsistente» significa che **la
distorsione non si attenua aumentando i dati**: con un milione di osservazioni il
numero resta sbagliato. Nelle altre due violazioni i coefficienti erano giusti e
i test sbagliati; qui **e' il coefficiente a essere sbagliato**, e quindi non e'
piu' interpretabile come effetto.

**Perche' una esplicativa puo' essere correlata con l'errore?** Domanda
generatrice, tre risposte. **Variabili omesse**: una causa rilevante lasciata
fuori finisce nell'errore ed e' correlata con l'esplicativa inclusa. **Errori di
misura** nell'esplicativa. **Simultaneita' o causalita' inversa**: la dipendente
influenza a sua volta l'esplicativa.

---

# 3. Le variabili strumentali *(domanda 128)*

**Variabile strumentale, cioe' una variabile usata per isolare la parte
esogena di un'esplicativa endogena.**

**Deve soddisfare due condizioni, e vanno dette entrambe.**

**Rilevanza**: deve essere **correlata con l'esplicativa endogena**, altrimenti
non ha nulla da cui estrarre informazione.

**Esogeneita'**, o condizione di esclusione: **non deve essere correlata con il
termine di errore**, cioe' non deve influenzare la dipendente se non attraverso
l'esplicativa endogena.

**La logica**: lo strumento fornisce una variazione dell'esplicativa che e'
«pulita», perche' non dipende dall'errore. Si usa solo quella variazione per
stimare l'effetto, e il coefficiente torna interpretabile.

---

# 4. La scala delle variabili *(domanda 120)*

**Cambiare la scala di una variabile, cioe' cambiarne l'unita' di misura.**

**La risposta e' che non cambia nulla di sostanziale.** Il coefficiente cambia in
modo proporzionale, perche' e' espresso in quelle unita', ma **la statistica t,
la significativita' e l'R quadro restano identici**. E' una riespressione, non un
modello diverso.

**Il collegamento che vale il punto**: e' proprio per questo che **il
coefficiente va sempre letto con la sua unita' di misura** — da solo, il numero
non significa niente.

**I coefficienti standardizzati** servono al problema opposto: permettono di
confrontare l'importanza relativa di variabili misurate in unita' diverse.

---

# 5. Modello teorico e modello stimato *(domanda 130)*

**Il modello teorico, cioe' la relazione come si suppone valga nella
popolazione**, con i parametri veri — che **non sono osservabili**. Contiene il
**termine di errore**.

**Il modello stimato, cioe' quello ottenuto sui dati del campione**, con i
coefficienti stimati al posto dei parametri veri. Contiene i **residui**.

**La frase che li lega**: il modello teorico e' **cio' che si vuole conoscere**,
il modello stimato e' **cio' che si riesce a misurare**. E' la stessa distinzione
di errore e residuo, vista al livello del modello intero.

---

# 6. Stima, previsione e robustezza *(domande 232, 233, 273, 172)*

**Dati di stima e dati di verifica**: si stima il modello su una parte dei dati e
si controlla su una parte tenuta da parte. Serve perche' **l'adattamento sui dati
di stima non dice nulla sulla capacita' di previsione**.

**Perche' confrontare valori osservati e valori previsti**: perche' quel
confronto **misura l'errore di previsione**, che e' la cosa che l'R quadro
calcolato dentro il campione non misura.

**Analisi di robustezza, cioe' rifare la stima cambiando specificazione,
campione o periodo, e verificare se il risultato tiene.** Se cambiando
qualche scelta il coefficiente cambia segno o perde significativita', **il
risultato non e' robusto** e non va presentato come conclusione.

---

# 7. Il bootstrap *(domanda 274)*

**Bootstrap, cioe' una tecnica di ricampionamento: dal campione osservato si
estraggono molti campioni con reinserimento, si ristima il modello su ciascuno, e
dalla distribuzione delle stime ottenute si ricavano errore standard e intervalli
di confidenza.**

**A che serve**: a misurare la precisione di una stima **quando la formula
teorica dell'errore standard non e' disponibile, oppure quando le ipotesi che la
giustificano non valgono.** In pratica sostituisce il calcolo teorico con una
simulazione fatta sui dati stessi.

---

# 8. Gli outlier *(domanda 121)*

**Outlier, cioe' osservazioni molto distanti dal resto della distribuzione.**

**L'effetto sulla regressione, e il collegamento e' diretto**: poiche' i minimi
quadrati **minimizzano la somma dei quadrati** dei residui, un'osservazione molto
lontana pesa in modo sproporzionato e **puo' spostare la retta da sola**. E' lo
stesso meccanismo che rende utile elevare al quadrato, visto come difetto:
l'elevamento al quadrato punisce gli errori grandi, e quindi un dato anomalo
diventa capace di dettare la retta.

**Cosa si fa**: identificarli, verificare se sono **errori di misura** o
osservazioni genuine, e confrontare la stima **con e senza** — che e' a sua volta
un'analisi di robustezza.

---

# La frase d'attacco del blocco

*«I minimi quadrati sono il migliore stimatore lineare non distorto solo se
valgono le ipotesi del modello classico; quando cade l'omoschedasticita' o
l'assenza di autocorrelazione i coefficienti restano corretti e sbagliano i
test, mentre quando cade l'esogeneita' e' il coefficiente stesso a essere
distorto, e per recuperarlo servono le variabili strumentali.»*

# Le domande

1. Quali ipotesi devono essere rispettate in un modello di regressione?
2. Che cos'e' l'eteroschedasticita' e quali conseguenze ha?
3. Che cosa significa autocorrelazione in una serie storica?
4. Che cosa si intende per endogeneita' e perche' e' un problema piu' grave
   dell'eteroschedasticita'?
5. Che cosa sono le variabili strumentali e quali condizioni devono soddisfare?
6. Che cosa significa cambiare la scala di una variabile?
7. Quali differenze esistono fra modello teorico e modello stimato?
8. Che cos'e' l'analisi di robustezza?
9. Che cos'e' il bootstrap statistico e a cosa serve?
10. Che effetto hanno gli outlier sui risultati di una regressione?
