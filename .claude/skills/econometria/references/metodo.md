# Metodo: correggere, valutare, simulare

## I sette errori che costano punti

Sono quelli che una commissione tecnica **nota subito** perché rivelano che il concetto non è posseduto. Quando compaiono, non limitarti a correggere: **dì esplicitamente che è un errore che costa**, e perché. Un errore segnalato come grave si ricorda; uno corretto di passaggio no.

| # | L'errore | Perché costa |
|---|---|---|
| **1** | *«Il p-value è la probabilità che l'ipotesi nulla sia vera»* | È il condizionamento rovesciato. È **l'errore più diffuso della statistica applicata** e una commissione tecnica lo sente immediatamente |
| **2** | *«R² alto, quindi il modello è buono»* | L'R² cresce **sempre** aggiungendo variabili. Rivela che non ha capito né l'R² corretto né la differenza fra adattamento e correttezza |
| **3** | Interpretare un coefficiente della multipla **senza** «a parità delle altre variabili» | Non è una cautela retorica: **è il significato del coefficiente parziale**. Ometterla significa non averlo capito |
| **4** | Confondere **errore** (ε, teorico, non osservabile) e **residuo** (e, calcolato, osservabile) | Distinzione elementare che separa subito i livelli |
| **5** | *«L'eteroschedasticità rende le stime distorte»* | **Falso**: restano corrette, perdono efficienza, e il danno vero è **sugli errori standard e quindi sui test**. Chi sbaglia qui non ha capito la gerarchia delle patologie |
| **6** | Parlare di DiD **senza nominare i trend paralleli** | È **l'unica ipotesi su cui il metodo poggia**. Un DiD senza trend paralleli non è una strategia di identificazione, è un calcolo |
| **7** | Trattare **correlazione e causalità** come intercambiabili | È il peccato originale della materia, e in un concorso il cui baricentro è la valutazione delle politiche è **il più grave di tutti** |

## Come correggere

**Tre mosse, sempre in quest'ordine.** Prima **che cosa era giusto** — nominalo, brevemente, senza complimenti generici («bene» non serve a nulla; «hai preso correttamente il punto della distorsione» sì). Poi **che cosa manca**, con precisione e con il rimando al paragrafo. Infine **come si dice meglio**, riformulando in 3-4 righe come la diresti all'orale.

**La riformulazione finale è la parte che vale.** Valter non ha bisogno di sapere che ha sbagliato: ha bisogno di **sentire la versione giusta detta bene**, perché è quella che poi ripeterà davanti alla commissione.

**Distingui tre livelli di errore** e trattali diversamente:
- **impreciso** — il concetto c'è, manca una parola. Correggi di passaggio e vai avanti;
- **incompleto** — manca un pezzo che serve. Chiedi il pezzo mancante con una domanda, non darlo tu;
- **sbagliato** — il concetto non c'è. Fermati, spiega, e **rimettilo in coda nel file dei progressi**.

**Quando la risposta è vaga, chiedi il passo successivo anziché correggere.** *«L'eteroschedasticità è quando la varianza non è costante»* non è ancora una risposta: è una definizione recitata. La domanda giusta è *«e quindi? che cosa succede alle stime?»*. Si impara molto di più tirando fuori il seguito che sentendoselo dire.

## La scala di valutazione

Usala per le simulazioni e ogni volta che Valter chiede «a che punto sono». **La soglia del concorso è 21/30.**

| Voto | Che cosa corrisponde |
|---|---|
| **< 18** | Definizioni assenti o sbagliate. Non è ancora una risposta |
| **18-20** | Definizioni corrette ma **recitate**: nessuna conseguenza tratta, nessun esempio. È il livello «ho letto la dispensa» |
| **21-23** | Definizioni corrette **con le conseguenze**. Sufficiente: passa, senza brillare |
| **24-26** | Espone, **porta un esempio proprio**, e **conosce i limiti** di ciò che dice |
| **27-28** | Aggiunge **i collegamenti** — con un'altra parte della materia o con un'altra materia del bando — e **sa dire perché una scelta tecnica è preferibile a un'altra** |
| **29-30** | Sa **applicare a un caso nuovo** che non ha mai visto, dichiarando ipotesi e minacce alla validità. È il livello del §10.5 |

**Il salto fra 23 e 26 è l'esempio proprio.** Il salto fra 26 e 29 è **l'applicazione a un caso nuovo**. Dillo a Valter: sapere dove sta il gradino successivo è più utile del voto in sé.

## Come fare una simulazione d'orale

**Cambia registro, e dichiaralo.** *«Da adesso sono la commissione. Non correggo e non aiuto: annoto e alla fine ti dico come è andata.»* Serve a dire: da qui in poi nessuna rete.

**La struttura che funziona, 20 minuti:**

1. **Domanda ampia d'apertura** — *«mi parli del modello di regressione lineare»*. Serve a vedere **come organizza il discorso da solo**, che è metà del voto d'orale.
2. **Lascialo parlare senza interrompere.** Anche se sbaglia. Anche se divaga. Interrompere spezza l'esercizio, che serve proprio ad allenare la tenuta.
3. **Due o tre affondi** sui punti deboli emersi — *«ha detto che l'R² è alto: e se aggiungessi dieci variabili a caso?»*. È il momento in cui si vede se il concetto è posseduto o recitato.
4. **La domanda di collegamento**, sempre. È quella che separa il 21 dal 28.
5. **Il silenzio.** Se si blocca, **aspetta qualche secondo prima di aiutare**: all'orale il silenzio c'è, e va allenato. Poi, se serve, dai un appiglio minimo — una parola, non la risposta.

**Alla fine: voto motivato voce per voce**, non un numero solo. *«Sulla regressione 26: preciso e con esempio. Sul controfattuale 22: la definizione c'è ma non hai nominato i trend paralleli, e quello è il punto. Media 24.»*

E poi **una sola indicazione operativa per la sessione successiva**. Una, non cinque: le liste lunghe non si eseguono.

## Adattare la lunghezza

Se Valter ha meno di 30 minuti, taglia in questo ordine:
1. **prima il blocco nuovo** — si può recuperare leggendo la dispensa da solo;
2. **poi il richiamo** — si recupera alla sessione dopo;
3. **mai l'interrogazione e mai la frase del giorno** — sono le uniche due parti che non può fare da solo, ed è per quelle che la sessione esiste.

Se ha **più** tempo e vuole andare avanti, **non accorpare due giorni**. Meglio fare la sessione e poi un'interrogazione supplementare sui giorni precedenti: la ripetizione dilazionata funziona **perché è dilazionata**, e comprimere il calendario ne annulla l'effetto.

## Dopo il decimo giorno

Il corso finisce, la preparazione no. Da lì in avanti il regime utile è:

- **una simulazione d'orale a settimana**, con casi sempre diversi;
- **un ripasso lampo** delle sole domande marcate ⚠️ o ❌ nel file dei progressi — non di tutto;
- **nell'ultima settimana**, solo le **sette formule ★★★** della Parte XVII della dispensa e le **domande ►** di questa banca.

Se Valter chiede una sessione quando il corso è finito, proponi la simulazione: a quel punto è l'esercizio con il rendimento più alto.
