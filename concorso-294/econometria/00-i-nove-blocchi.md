# Econometria in nove blocchi — la mappa di chiusura

*26 novembre 2026. Copre i 44 quesiti attestati di econometria nell'elenco dei 375.*
*Ordine logico, non ordine del manuale: ogni blocco e' una domanda che apre la successiva.*

| | Blocco | La domanda che risolve | Quesiti | Stato | Tempo |
|---|---|---|---|---|---|
| **1** | **Il linguaggio** — variabili e sintesi | *Con che materiale lavoro?* | 107, 108, 109, 122, 337, 317 | ◐ | 25 min |
| **2** | **La stima e la verifica** | *Da un campione, che cosa posso dire sulla popolazione?* | 110, 111, 123, 124, 173, 240, 244, 131/274 | ✅ | 20 min |
| **3** | **Il modello e la regressione semplice** | *Come lego Y a X?* | 113, 114, 115, 117, 290 | ✅ | 20 min |
| **4** | **La multipla e la specificazione** | *Quali variabili metto dentro?* | 118, 119, 120, 121, 296, multicollinearita' | ◐ | 35 min |
| **5** | **Le ipotesi e le violazioni** | *Quando la stima e' affidabile?* | 116, eteroschedasticita', 127 | ◐ | 25 min |
| **6** | **L'endogeneita' e gli strumenti** | *E se X non e' innocente?* | 128, 222, 343 | ✅ | 20 min |
| **7** | **Le strutture dei dati e i panel** | *Che forma hanno i miei dati?* | 353, 354, 355, 125, 126 | ✅ | 20 min |
| **8** | **Stima contro previsione — il ponte** | *Spiegare o indovinare?* | 112, 129, 130, 172, 212, 223, 232, 233 | **–** | 50 min |
| **9** | **Le estensioni** | *E quando Y non e' un numero qualsiasi?* | 320, 337 quantile, 171 | **–** | 35 min |

**Totale: circa 4 ore di lavoro effettivo.**
Sei blocchi su nove sono gia' costruiti: il tempo vero sta nei blocchi **8 e 9**
(mai aperti) e nelle lacune dei blocchi **1, 4 e 5**.

---

## BLOCCO 1 — Il linguaggio: variabili e sintesi

### La scala di misura, e che cosa ciascuna consente

| Scala | Che cosa distingue | Esempio | Sintesi ammesse |
|---|---|---|---|
| **Nominale** | solo **uguale o diverso** | comune di residenza, titolo di studio come etichetta | **moda** |
| **Ordinale** | anche **maggiore o minore**, ma non di quanto | grado di soddisfazione, fasce di reddito | moda + **mediana**, quartili |
| **Cardinale** | anche **di quanto** | euro, anni, metri quadri | moda, mediana + **media**, scarto quadratico medio |

**La regola:** ogni scala **eredita** le sintesi di quella sotto e ne aggiunge una.
Non si puo' fare la media di una variabile ordinale, perche' le distanze fra le
modalita' non sono definite.

### Le tre sintesi di posizione

- **Moda** — la modalita' piu' frequente. L'unica disponibile per le nominali.
- **Mediana** — il valore che divide la distribuzione ordinata in due meta'.
  Non risente dei valori estremi.
- **Media aritmetica** — somma diviso numero. Tiene conto di tutti i valori,
  e proprio per questo **risente dei valori estremi**.

**Il gancio:** *la media sente tutti, la mediana sente solo il centro.*
Sui redditi, pochi valori altissimi tirano su la media e lasciano ferma la mediana:
e' il motivo per cui il reddito si rappresenta con la **mediana**.

### Quartili, decili, percentili (337)

Tagli che dividono la distribuzione ordinata in parti di **uguale numerosita'**:
tre quartili in quattro parti, nove decili in dieci, novantanove percentili in cento.
Il **secondo quartile coincide con la mediana**. Servono a descrivere la
**forma** della distribuzione, non solo il suo centro.

### Associazione fra variabili qualitative (122)

Con variabili qualitative **non si puo' usare la correlazione**: la correlazione
richiede numeri e una direzione, e qui non ci sono ne' l'uno ne' l'altra.
Si procede cosi':

1. **Tavola di contingenza** — si incrociano le due variabili e si contano le frequenze congiunte.
2. **Confronto con l'indipendenza** — si calcola quali frequenze ci si aspetterebbe
   se le due variabili fossero indipendenti, e si misura quanto le frequenze
   osservate se ne discostano: e' la logica del **chi quadrato**.
3. **Normalizzazione** — il chi quadrato cresce con la numerosita', quindi per
   giudicare l'**intensita'** si usa un indice normalizzato fra 0 e 1,
   come l'**indice di Cramer**.

**Il limite da dire:** l'associazione misura se le due variabili **variano insieme**,
non quale causa quale, e non ha un segno.

### Correlazione nulla e relazione esistente (109, 317)

Il coefficiente di correlazione lineare misura **solo la componente lineare**
della relazione. Se la relazione esiste ma **cambia direzione** — prima cresce,
poi decresce — le due parti si compensano e la correlazione risulta vicina a zero
**pur essendoci una relazione fortissima**.

**La conseguenza operativa:** la correlazione non si legge mai da sola.
Si guarda prima il **grafico di dispersione**, e solo dopo si sceglie la forma del modello.
