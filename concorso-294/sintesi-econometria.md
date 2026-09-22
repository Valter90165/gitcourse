# Sintesi progressiva — Econometria

Cresce a ogni sessione. Copre **solo ciò che è stato effettivamente studiato sul
manuale**, non l'intero programma: serve per memorizzare e ripassare, non per
sostituire la lettura.

**Coperto finora**: manuale Parte III — Capitolo 6 intero (pp. 330-338) e
Capitolo 7 fino a p. 344 (fino all'introduzione dei minimi quadrati).

---

## 1. Che cos'è l'econometria

Applica **metodi statistici e matematici** allo studio dei fenomeni economici,
**elaborando modelli per verificare empiricamente le teorie economiche**.

Sta fra due mondi: **teoria economica** da un lato; **matematica, probabilità e
statistica** dall'altro. L'economia è il *fondamento*, la statistica è
*funzionale*.

## 2. ⭐ Perché non è statistica applicata: la ripetibilità

| | Requisito | Esempio |
|---|---|---|
| **Statistica e probabilità** | il fenomeno deve essere **incerto** *e* **ripetibile** | lancio la moneta 10.000 volte |
| **Econometria** | i dati economici **non sono ripetibili** | il 2023 è andato una volta sola |

> **Da dire all'orale.** *«La statistica nasce sulle scienze naturali, dove
> l'esperimento si ripete nelle stesse condizioni. I fenomeni economici no: il
> consumo aggregato di un anno è **una sola realizzazione**, e quell'anno non
> torna. Serve una disciplina che sappia lavorare su **dati non
> sperimentali**.»*

## 3. I tre tipi di dati — il criterio è soggetti × momenti

| | Soggetti | Momenti | Immagine |
|---|---|---|---|
| **Cross section** | tanti | uno | fotografia di gruppo |
| **Serie storica** | uno | tanti | film di una persona |
| **Panel** | tanti | tanti | tanti film insieme |

**I tre vantaggi del panel**: più osservazioni di una singola serie storica; più
facile studiare i fenomeni in cui il tempo conta; ⭐ **controlla l'eterogeneità
fra le unità**, cioè tutto ciò che rende diversi i soggetti e che non si riesce
a misurare.

## 4. Che cos'è un modello

Una **rappresentazione formale** delle conoscenze su un fenomeno. Non una
riproduzione esatta: **una versione semplificata**. In concreto, un insieme di
equazioni.

## 5. ⭐ I quattro stadi

| Stadio | La domanda |
|---|---|
| **1. Specificazione** | *che forma ha la relazione?* |
| **2. Stima** | *quanto valgono i parametri?* |
| **3. Verifica** | *il modello regge?* |
| **4. Utilizzo** | *che me ne faccio?* |

Nella **specificazione** si risolvono tre problemi: individuare le variabili
(endogene/esogene); scegliere la forma funzionale; introdurre la **componente
stocastica di disturbo**.

La **verifica** riguarda quattro aspetti: specificazione, capacità descrittiva,
conformità alle aspettative teoriche, capacità previsiva.

## 6. Endogene ed esogene

| | | Il criterio |
|---|---|---|
| **Esogena** | influenza il modello ma **non subisce** l'effetto delle sue relazioni | **arriva da fuori, già data** |
| **Endogena** | il suo valore **è generato dal modello** | **sta a sinistra dell'uguale** |

*Endo-* = dentro (nasce dentro il modello). *Eso-* = fuori (entra già
confezionata).

## 7. ⭐ Forma strutturale e forma ridotta

| | Come è fatta | Che cos'è |
|---|---|---|
| **Strutturale** | endogene in funzione **delle esogene E delle altre endogene** | **modello di ANALISI** |
| **Ridotta** | ciascuna endogena in funzione **di parametri, esogene ed esogene ritardate** | **modello di STRATEGIA** |

> **La strutturale descrive com'è fatta l'economia. La ridotta è il cruscotto di
> comando.**

Con Keynes: da `C = a0 + a1·Y` e `Y = C + I + G` — che girano in tondo — si
arriva a `Y = (a0 + I + G) / (1 − a1)`. Con `a1 = 0,75` ogni euro di spesa
pubblica ne produce **4**: è il **moltiplicatore**.

## 8. Le due famiglie di modelli

- **Per serie storiche** — si basano sulla **storia del fenomeno**: ciò che ha
  agito nel passato agirà anche nel futuro;
- **Di regressione** — si basano su una **relazione causa-effetto** fra il
  fenomeno e una o più esplicative.

Dentro la regressione: **semplice** (un regressore) → **multipla** (più
regressori) → **multivariata multipla** (più variabili dipendenti).

---

# Capitolo 7 — La regressione

## 9. Che cos'è

Cerca **un modello che descriva la relazione fra una variabile dipendente e una
o più indipendenti** (o esplicative, o **regressori**). Le esplicative
*«spiegano, prevedono, simulano e controllano»* la dipendente.

**L'immagine**: cento studenti, ore di studio e voto. I punti formano una
**nuvola**, non una riga. La regressione traccia **la retta che riassume la
nuvola**.

⭐ **La scelta di chi sta a destra non è arbitraria**: si sceglie come
indipendente la variabile **«logicamente antecedente»**. È la teoria a dire la
direzione della causalità, non la matematica.

**Galton** — il nome viene da lui: misurando statura dei padri e dei figli
osservò *«una regressione delle altezze dei figli verso la media»*.

## 10. I sei passi per costruire un modello di regressione

1. individuare il **fenomeno**
2. individuare **Y e le esplicative** sulla base della teoria, e raccogliere i dati
3. **formulare il modello**, esplicitando la forma funzionale
4. **stimare i parametri** con un metodo che dia almeno stimatori **consistenti**
5. **verificare** con una serie di test
6. **usare** il modello — descrizione, previsione, interpretazione, controllo

> Se non viene accettato **si torna al punto 1 e si rifà il giro**. È un ciclo,
> non una linea.

Le fasi **più delicate** sono due: la **formulazione-identificazione** e la
**verifica**.

## 11. Le tre cause del «fallimento del modello»

1. **la teorizzazione non regge** alla prova dei fatti — la più difficile da
   individuare, perché ogni modello è per definizione una semplificazione;
2. **la teoria è giusta ma la formulazione è sbagliata** — per esempio un
   modello lineare dove la relazione è non lineare;
3. **i dati non sono idonei** in qualità o quantità, oppure non lo è **il metodo
   di stima**.

## 12. ⭐⭐ Componente deterministica e stocastica

Perché non esiste `Y = f(X)` e basta: non si dispone di tutte le informazioni ma
**solo di un campione**; e ci sono **fenomeni imprevedibili, errori di
misurazione, scarti accidentali**.

```
Y = f(X) + ε          da cui        ε = Y − f(X)
    ↑        ↑
 determin.  stocastica
```

**ε è lo scarto fra le costruzioni teoriche e la realtà osservata**, e ha
*«funzioni compensative per le discrepanze fra il modello e la realtà»*.

Assumendo la relazione **lineare nei parametri**:

```
Y = β0 + β1·X + ε
```

| | Che cos'è | Nell'esempio |
|---|---|---|
| **β0** | intercetta | il voto di chi studia zero ore |
| **β1** | **pendenza — il numero che cerchi** | quanto vale un'ora di studio |
| **ε** | errore | la fortuna, le basi pregresse, la giornata |

> **β1 = 0,4** significa: ogni ora in più porta, **in media**, 0,4 punti.

---

# ✅ Checklist — le otto cose da saper dire

1. Che cos'è l'econometria e **perché non è statistica** (la ripetibilità)
2. I **tre tipi di dati** (soggetti × momenti) e perché il panel è più potente
3. I **quattro stadi**, ciascuno con la sua domanda
4. **Endogena ed esogena**, e il criterio per distinguerle
5. **Strutturale = analisi, ridotta = strategia**
6. Che cos'è **la regressione** e perché la scelta della variabile indipendente
   non è arbitraria
7. **Perché esiste ε** e che cosa rappresenta
8. Che cosa significa **β1** a parole

---

*Sintesi costruita sul manuale, Parte III, capitoli 6 e 7 (fino a p. 344).
Aggiornata al 22 settembre 2026 — sessione 2.*
