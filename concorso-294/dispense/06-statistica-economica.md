# Statistica economica

## Sintesi ragionata sul manuale, per la prova orale

*Concorso RIPAM 294 unità — Codice 02, Area dei funzionari — prova orale del 27 novembre 2026*

Questa dispensa è costruita sulla **Parte IV del manuale** — *Statistica economica* (Simone, edizione per il concorso RIPAM 294) — **pagine stampate 575-648**, lette integralmente. Sono **sette capitoli**, dai numeri indici alla funzione di produzione.

> **Perché questa materia vale più di quanto sembri.** La statistica economica è, fra tutte le materie del tuo bando, **quella che descrive il lavoro che farai**. Non è teoria: è il sistema con cui l'ISTAT misura l'inflazione, costruisce il PIL, destagionalizza gli indicatori congiunturali e alimenta i dati su cui si fonda il DPFP, il Patto di stabilità europeo e la ripartizione dei fondi strutturali. Una commissione RIPAM la ascolta con attenzione diversa rispetto all'econometria, perché qui il candidato sta parlando di **attività istituzionale della pubblica amministrazione italiana**.

**L'impostazione sulle formule è la stessa concordata per econometria**: nessuna derivazione, nessun passaggio algebrico. Qui però c'è una differenza sostanziale che va detta subito. In statistica economica **alcune formule *sono* il contenuto**: l'indice di Laspeyres e quello di Paasche non si possono spiegare senza dire che cosa sta al numeratore e che cosa al denominatore, perché **è esattamente lì che sta la differenza fra i due**. Per questo, in questa dispensa, un piccolo numero di formule compare nel testo — ma **sempre tradotte in italiano e spiegate a parole**, mai dimostrate. Il riepilogo finale, nella Parte IX, le raccoglie tutte con il solito giudizio su quanto valga la pena memorizzarle.

**Come è organizzata.** Le parti seguono i capitoli, ma il peso è molto disuguale, e deliberatamente:

- i **numeri indici** (cap. 1) e la **contabilità nazionale con il SEC 2010** (cap. 2) sono trattati a fondo, perché sono ciò che la commissione chiede davvero e perché il secondo si salda direttamente con la contabilità pubblica;
- le **tavole input-output** (cap. 4) hanno uno spazio ampio ma sono raccontate **come idea economica**, non come algebra matriciale;
- **comparazione internazionale** (cap. 3), **consumi** (cap. 5), **mercato del lavoro** (cap. 6) e **funzione di produzione** (cap. 7) sono trattati con attenzione ai concetti che una commissione può chiedere e ai collegamenti con economia politica.

---

# PARTE I — I NUMERI INDICI DEI PREZZI E DELLE PRODUZIONI

*(Capitolo 1 del manuale, pp. 575-586)*

## 1. Che cos'è la statistica economica

Il manuale apre con una distinzione che vale la pena saper riprodurre, perché è un'ottima frase d'esordio se la prima domanda è generica:

> Nel campo statistico si distingue fra **statistica metodologica**, che è **la parte teorica della statistica**, fondata sui metodi matematici utilizzati per raccogliere e classificare i dati, e **statistica applicata**, che **assume denominazioni diverse secondo le materie cui la scienza statistica si applica**.
>
> Nell'ambito della statistica applicata si individua il ramo della **statistica economica**, il cui contributo alla costruzione di **modelli rappresentativi ed esplicativi del sistema macroeconomico** è stato fondamentale.

## 2. L'ISTAT e i suoi compiti — da sapere alla lettera

Il manuale mette l'ISTAT in apertura assoluta della materia, e non è un caso. È la prima cosa da saper dire.

> L'**Istituto nazionale di statistica (ISTAT)** è un **ente pubblico di ricerca sottoposto alla vigilanza della Presidenza del Consiglio dei ministri**, dotato di **autonomia scientifica, statutaria e regolamentare, nonché organizzativa, finanziaria, patrimoniale e contabile**.

**I quattro compiti più importanti**, da elencare in quest'ordine:

1. **la realizzazione dei censimenti generali**: popolazione e abitazioni, industria e servizi, agricoltura;
2. **la predisposizione e l'esecuzione della maggior parte delle indagini comprese nel programma statistico nazionale**;
3. **l'indirizzo e il coordinamento delle attività statistiche degli enti e uffici facenti parte del Sistema statistico nazionale (SISTAN)**;
4. **la partecipazione al potenziamento del sistema statistico europeo e internazionale**.

> **Il collegamento da fare subito.** L'ISTAT è l'ente di vertice del **SISTAN**, istituito dal **D.Lgs. 322/1989**, che è anche la fonte del **segreto statistico (art. 9)**. Questo aggancia la materia sia al diritto amministrativo (ente pubblico di ricerca, vigilanza della Presidenza del Consiglio, autonomia) sia alla data science (trattamento dei dati, finalità statistiche come base giuridica autonoma nel GDPR). È un ponte che conviene tenere pronto.

## 3. I rapporti statistici

Premessa lessicale che il manuale richiama: per **frequenza assoluta** si intende **il numero di volte in cui una data modalità di un carattere si presenta nel collettivo**; per **intensità** si intende **l'ammontare o la misura di un carattere additivo posseduto dalle unità statistiche**.

**I rapporti statistici consentono di confrontare intensità o frequenze di due fenomeni.** Il manuale insiste su un punto concettuale che merita di essere riportato: *i rapporti posti in essere fra le cifre rappresentanti i due fenomeni **non sono mai fini a se stessi**, ma rappresentano **la traduzione matematica di rapporti logici che esistono fra i due fenomeni***.

**Perché si usano i rapporti e non le differenze** — ed è la ragione che conta:

> Il rapporto **elimina l'effetto esercitato dal denominatore sul numeratore** e soprattutto **elimina l'effetto dell'unità di misura, dando luogo a numeri puri** che ne prescindono. Viceversa, **le differenze fra intensità o frequenze di due fenomeni sono espresse nella medesima unità di misura degli stessi**, e quindi non sono confrontabili fra contesti diversi.

**I quattro tipi di rapporto statistico**, con esempi:

| Tipo | Come si costruisce | Esempi |
|---|---|---|
| **Rapporti di composizione** (o **di parte al tutto**) | intensità o frequenza di un fenomeno **/ intensità o frequenza globale** | la quota di spesa per alimentari sul totale dei consumi |
| **Rapporti di densità** | intensità o frequenza complessiva di un carattere **/ una dimensione spaziale o temporale** | il **grado di affollamento delle abitazioni**, la **densità della popolazione residente** rispetto a un dato ambito territoriale |
| **Rapporti di durata** | consistenza media di un fenomeno **/ il suo flusso di rinnovo** (supposti uguali e costanti i flussi di entrata e di uscita) | la permanenza media in una condizione |
| **Rapporti di ripetizione** | flusso di rinnovo **/ consistenza media** | **il numero di volte in cui il fenomeno si rinnova** nella dimensione temporale stabilita. **Sono il reciproco dei rapporti di durata** |

Fra i rapporti statistici meritano un discorso a parte **i numeri indici**.

## 4. I numeri indici: la classificazione

**La definizione:** i numeri indici si costruiscono **ponendo al denominatore un'intensità (detta *base*) della stessa natura del fenomeno che sta al numeratore**.

**Prima distinzione — rispetto alla natura del confronto:**

- **numeri indici temporali**: consentono di esaminare **la dinamica temporale** di un fenomeno quantitativo, attraverso l'esame delle variazioni relative;
- **numeri indici spaziali (o territoriali)**: consentono di **confrontare fenomeni in situazioni spaziali differenti**.

**Perché contano**, nelle parole del manuale: *i numeri indici costituiscono **uno strumento indispensabile per la misura delle oscillazioni dei prezzi e delle produzioni**, e quindi per descrivere la dinamica di un sistema economico.* Le categorie principali in ambito economico sono quelle **dei prezzi, delle quantità e dei valori**.

**Seconda distinzione — rispetto alla quantità dei fenomeni investigati:**

- **numeri indici semplici (o elementari)**: il rapporto è effettuato fra misurazioni riferite a **un unico fenomeno** — per esempio la variazione relativa del prezzo di un dato prodotto;
- **numeri indici complessi (o ponderati)**: sono costituiti dal rapporto **fra due o più fenomeni eterogenei**. A loro volta si distinguono in:
 - **numeri indici sintetici**, che si ottengono **combinando diversi indici semplici** (per esempio la variazione relativa del prezzo di una categoria di prodotti);
 - **numeri indici composti**, che si ottengono **combinando diversi indici sintetici**.

## 5. I numeri indici semplici

**Le due specie, secondo la base scelta:**

- **a base fissa**: **ciascuna intensità è rapportata a un'unica intensità che resta costante**. Dicono «quanto è cambiato il prezzo rispetto all'anno di riferimento»;
- **a base mobile (o concatenati)**: **ciascuna intensità è rapportata a quella del termine precedente**. Dicono «quanto è cambiato il prezzo rispetto al periodo precedente».

> **La lettura pratica**, che conviene dire perché è ciò che si fa davvero con i dati: **la serie a base fissa misura la variazione cumulata**; **la serie a base mobile misura la variazione periodo su periodo**. Nel linguaggio della congiuntura, l'indice a base mobile corrisponde alla **variazione congiunturale**, mentre il confronto con lo stesso mese dell'anno precedente è la **variazione tendenziale**.

**Il passaggio dall'una all'altra** — il manuale lo mostra in entrambe le direzioni, ed è una cosa che può essere chiesta:

- **da base fissa a base mobile**: si divide **ciascun indice a base fissa per il suo precedente**;
- **da base mobile a base fissa**: si **concatenano** gli indici, cioè li si moltiplica progressivamente fra loro.

### 5.1 Le proprietà dei numeri indici semplici

Cinque, e vale la pena conoscerle perché nel capitolo successivo si scoprirà che **gli indici complessi più usati non le rispettano tutte** — ed è proprio questo il punto critico della materia.

1. **Identità** — se le due intensità confrontate coincidono, **l'indice vale 1**.
2. **Reversibilità delle basi (o delle situazioni)** — **invertendo base e termine confrontato si ottiene il reciproco**. Se il prezzo è cresciuto del 25% da t₀ a t₁, allora da t₁ a t₀ è diminuito esattamente nella misura reciproca.
3. **Reversibilità dei fattori (o decomposizione delle cause)** — è la più interessante dal punto di vista economico. Poiché **un valore è il prodotto di prezzo per quantità (v = p · q)**, allora anche **l'indice di valore deve essere il prodotto dell'indice di prezzo per l'indice di quantità**. Conseguenza operativa: **noti due dei tre indici, il terzo è univocamente determinato**.
4. **Transitività delle basi (o circolarità)** — data una serie di indici a base fissa, **è possibile cambiare la base** senza rifare i calcoli sui dati originari.
5. **Concatenamento** — è possibile passare da una serie a base mobile alla corrispondente serie a base fissa.

> **Perché queste proprietà contano davvero.** Sembrano formalismi, ma sono la **garanzia di coerenza di un sistema di indicatori pubblici**. Se l'indice dei prezzi non fosse transitivo, cambiare l'anno base — cosa che l'ISTAT fa periodicamente — produrrebbe **serie storiche non confrontabili con quelle precedenti**. E se non valesse la decomposizione delle cause, non si potrebbe separare quanto della crescita del valore delle esportazioni sia dovuto ai prezzi e quanto ai volumi: una distinzione su cui si fonda mezza analisi congiunturale.

## 6. I numeri indici complessi — il cuore del capitolo

Qui sta **la parte che una commissione chiede con più probabilità di tutta la materia**: Laspeyres, Paasche e Fisher. Vale la pena saperli distinguere con precisione assoluta.

**Il problema.** Si dispone di prezzi e quantità di **m beni e servizi** in **k situazioni** (tempi, o Paesi). Si vuole calcolare **un indice sintetico che esprima le variazioni d'insieme dei prezzi** (o delle quantità) fra due momenti. Selezionate le voci da inserire, «il problema che rimane da risolvere è **la scelta del criterio in base al quale operare la sintesi**». Due metodi: il **rapporto fra aggregati di valore** e la **media degli indici elementari**.

### 6.1 Il primo metodo: rapporto fra aggregati di valore

Considerando due soli tempi, 0 e n, si possono costruire **quattro aggregati**, due reali e due virtuali — e capire questa distinzione è capire tutto il paragrafo:

| Aggregato | Che cos'è | Natura |
|---|---|---|
| **Σ p₀ q₀** | prezzi dell'epoca 0 × quantità dell'epoca 0 | **valore reale** (la spesa effettiva all'inizio) |
| **Σ pₙ qₙ** | prezzi dell'epoca n × quantità dell'epoca n | **valore reale** (la spesa effettiva alla fine) |
| **Σ p₀ qₙ** | prezzi dell'epoca 0 × quantità dell'epoca n | **valore virtuale** — quanto sarebbe costato il paniere di oggi ai prezzi di ieri |
| **Σ pₙ q₀** | prezzi dell'epoca n × quantità dell'epoca 0 | **valore virtuale** — quanto costerebbe oggi il paniere di ieri |

I due aggregati **virtuali** non corrispondono a nessuna spesa realmente effettuata: sono costruzioni che servono a **isolare l'effetto prezzo dall'effetto quantità**. È esattamente il modo in cui si risponde alla domanda «ma quanto sono aumentati davvero i prezzi, al netto del fatto che la gente ha cambiato abitudini?».

**L'indice di valore** è semplicemente il rapporto fra i due valori reali: quanto è cambiata la spesa complessiva.

### 6.2 Laspeyres e Paasche — la distinzione da non sbagliare mai

Gli indici dei prezzi che si costruiscono sono due, e differiscono **per quale sistema di quantità si usa come ponderazione**:

> **INDICE DEI PREZZI DI LASPEYRES = Σ pₙ q₀ / Σ p₀ q₀**
> Pondera con le **quantità dell'anno BASE**. Risponde alla domanda: *«quanto costa oggi il paniere che si acquistava all'inizio?»*
>
> **INDICE DEI PREZZI DI PAASCHE = Σ pₙ qₙ / Σ p₀ qₙ**
> Pondera con le **quantità dell'anno CORRENTE**. Risponde alla domanda: *«quanto sarebbe costato all'inizio il paniere che si acquista oggi?»*

**Le caratteristiche di ciascuno**, come le espone il manuale:

**Laspeyres** è **a base fissa e a ponderazione fissa**. Da qui i suoi due vantaggi decisivi:

- **agevola e rende più spedito il calcolo**, perché il sistema di ponderazione non va ricalcolato ogni volta;
- **richiede la rilevazione di un solo sistema di quantità di riferimento**, quelle del periodo base.

Il suo metodo di sintesi è denominato **metodo dell'anno base**.

**Paasche** è **a base fissa ma a ponderazione variabile**, perché **per esso muta costantemente l'insieme delle quantità di riferimento**. E qui sta il *trade-off* che il manuale espone con chiarezza:

> Questo, **da un lato, lo rende aggiornato e fedele**; **dall'altro comporta costi di rilevazione elevati**. È quindi conveniente **nelle situazioni in cui si dispone congiuntamente e simultaneamente di prezzi e quantità** — il manuale fa l'esempio delle **contrattazioni borsistiche**.

Il suo metodo di sintesi è denominato **metodo dell'anno dato**.

> **LA FRASE DA SAPERE, perché è letteralmente la risposta a «quale indice usa l'ISTAT?».**
>
> *La maggior parte degli istituti nazionali di statistica, **fra cui l'ISTAT, utilizza l'indice di Laspeyres** come indice complesso di prezzo, **a causa della costanza nel tempo del paniere di beni e servizi di riferimento**. Esso consente di **misurare variazioni di prezzi per un paniere costante di beni**.*
>
> È il punto su cui si regge tutta la misurazione dell'inflazione in Italia e in Europa.

**Gli indici delle quantità** si costruiscono simmetricamente, scambiando il ruolo di prezzi e quantità: **l'indice delle quantità di Laspeyres** pondera con i **prezzi dell'anno base**, quello **di Paasche** con i **prezzi dell'anno corrente**.

**I due indici danno risultati diversi.** Il manuale lo mostra con un esempio numerico: su quattro prodotti di un supermercato, da gennaio a dicembre, **Laspeyres dà +4,32% e Paasche +4,08%**. La differenza non è un errore: è la conseguenza del fatto che **i consumatori spostano i propri acquisti verso i beni che rincarano di meno**, e Paasche, ponderando con le quantità finali, dà più peso proprio a quei beni. Da qui una regola pratica molto utile:

> **In presenza di sostituzione fra beni, Laspeyres tende a SOVRASTIMARE e Paasche a SOTTOSTIMARE la variazione dei prezzi.** È il cosiddetto *substitution bias*, ed è la ragione per cui un indice di tipo Laspeyres tende strutturalmente a dare una misura dell'inflazione leggermente più alta.

### 6.3 Le proprietà degli indici sintetici — e quelle che Laspeyres e Paasche non rispettano

Anche per i numeri indici sintetici si stabiliscono condizioni formali che **dovrebbero** essere soddisfatte. Oltre a **identità**, **reversibilità delle basi**, **reversibilità dei fattori** e **transitività** — già viste per gli indici semplici — se ne aggiungono tre specifiche:

- **Commensurabilità**: l'indice **non varia al variare dell'ordine di grandezza dell'unità di misura usata per le quantità** (se misuro il grano in quintali anziché in chili, l'indice non deve cambiare);
- **Determinatezza**: l'indice **non deve annullarsi o tendere all'infinito se uno dei termini elementari si annulla o tende all'infinito** (un singolo prodotto che esce dal mercato non deve far esplodere l'indice generale);
- **Proporzionalità**: **se i prezzi di tutti i beni variano proporzionalmente, l'indice varia secondo lo stesso coefficiente** (se tutto raddoppia, l'indice raddoppia).

**E poi arriva il punto critico**, che va detto perché è una domanda-trappola perfetta:

> **Gli indici di Laspeyres e di Paasche NON soddisfano le proprietà di:**
> - **reversibilità delle basi**;
> - **transitività**, per cui **il confronto fra due termini qualunque della serie dei numeri indici non è attuabile**;
> - **decomposizione delle cause**.

È un limite serio e concreto: significa che **da una serie di indici di Laspeyres non si può ricavare direttamente il confronto fra due anni intermedi qualsiasi**. È la ragione tecnica per cui gli istituti di statistica ricorrono agli **indici a catena** (*chain-linked*), che ricostruiscono la serie concatenando confronti fra anni contigui — ed è così, per esempio, che l'ISTAT calcola l'indice dei prezzi delle abitazioni.

### 6.4 Il secondo metodo e l'indice di Fisher

Il **secondo metodo di sintesi** — la **media degli indici elementari** — fa entrare ciascun indice elementare nel calcolo **con un suo peso**. Per applicarlo occorre **definire la composizione del paniere**, ossia quali e quante merci far rientrare nel calcolo, e **assegnare coefficienti di importanza ai singoli elementi**.

Da questo approccio nasce il terzo grande indice:

> **INDICE DI FISHER = media geometrica di Laspeyres e Paasche**, cioè **la radice quadrata del loro prodotto.**

Sull'esempio del supermercato: da 1,0432 (Laspeyres) e 1,0408 (Paasche) si ottiene **1,0420**.

**Perché si chiama «indice ideale»** — e perché comunque non si usa:

> L'indice di Fisher è detto **numero indice ideale** in quanto **soddisfa quasi tutte le proprietà formali da Fisher stesso proposte, a eccezione della proprietà di transitività**.
>
> Tuttavia, **nella pratica economica si preferisce usare gli indici di Laspeyres e Paasche — soprattutto il primo — perché in essi compaiono grandezze che hanno precisi significati economici.**

Questa seconda frase è la migliore risposta possibile alla domanda «se Fisher è "ideale", perché l'ISTAT usa Laspeyres?». **Perché Laspeyres è interpretabile**: il suo numeratore è il costo odierno di un paniere concreto e osservabile. Fisher è una media geometrica: matematicamente elegante, economicamente muta.

## 7. Gli indici dei prezzi elaborati dall'ISTAT — il paragrafo più «da concorso»

Il manuale premette la ragione per cui questi indici contano:

> Esprimendo le variazioni nel tempo dei prezzi di un campione di prodotti riferito a un dato periodo scelto come base, tali indici costituiscono **uno dei principali strumenti di analisi dell'andamento di breve periodo dell'economia**, in quanto consentono di **misurare l'inflazione**, ossia **l'aumento persistente del livello dei prezzi con la conseguente diminuzione del potere di acquisto della moneta**.

L'ISTAT elabora **tre tipologie di indici**: relativi alla **fase della produzione**, **al consumo**, e **delle abitazioni.**

### 7.1 Indici dei prezzi alla produzione

**Per l'industria.** Misura le variazioni nel tempo dei prezzi dei **prodotti industriali fabbricati da imprese i cui stabilimenti sono situati sul territorio nazionale** e venduti **sul mercato interno o su quello estero** (a sua volta suddiviso in **Area euro** e **Area non euro**).

L'ISTAT ne calcola **quattro**, relativi ai cosiddetti **raggruppamenti principali di industrie**:

1. **beni di consumo** (mobili, motocicli, apparecchi per la riproduzione del suono e dell'immagine, prodotti alimentari e bevande, prodotti farmaceutici);
2. **beni strumentali** (macchine, motori, apparecchi di misurazione e controllo);
3. **beni intermedi** (prodotti chimici, metalli, apparecchi elettrici);
4. **energia**.

**Per i servizi.** Misura l'**evoluzione trimestrale** dei prezzi dei servizi venduti da imprese residenti in Italia a una clientela costituita da **imprese e/o enti della pubblica amministrazione**. Si tratta quindi di un indice ***business to business***: considera **solo le transazioni fra imprese o fra imprese ed enti pubblici**, **mentre non tiene conto di quelle che coinvolgono le famiglie**. È calcolato per i settori definiti dal **Regolamento (CE) 1158/2005** — trasporto merci su strada, trasporto marittimo, aereo, magazzinaggio, servizi postali, telecomunicazioni, produzione di software e consulenza informatica, studi legali e di contabilità, architettura e ingegneria, pubblicità, ricerca e selezione del personale, vigilanza, pulizia.

### 7.2 Gli indici dei prezzi al consumo — i tre acronimi da sapere

**Che cosa misurano:** le variazioni nel tempo, rispetto a un periodo scelto come base, **dei prezzi di un paniere di beni e servizi acquistabili sul mercato e destinati al consumo finale delle famiglie presenti sul territorio nazionale**.

Sono **tre**, e la distinzione fra loro è una domanda d'esame quasi certa:

| Sigla | Nome per esteso | Che cosa misura e a che cosa serve |
|---|---|---|
| **NIC** | **Indice Nazionale dei prezzi al Consumo per l'intera collettività** | Fornisce **una misura dell'inflazione a livello dell'intero sistema economico nazionale**. È l'indice «della collettività nazionale considerata come un'unica grande famiglia» |
| **FOI** | **Indice dei prezzi al consumo per le Famiglie di Operai e Impiegati** | Misura le variazioni dei prezzi al dettaglio dei beni e servizi **correntemente acquistati dalle famiglie dei lavoratori dipendenti non agricoli**. **È usato per adeguare periodicamente i valori monetari, come affitti o assegni familiari** |
| **IPCA** | **Indice dei Prezzi al Consumo Armonizzato** per i Paesi dell'Unione Europea | **Creato da EUROSTAT** per **rendere confrontabili i prezzi dei Paesi dell'UE** nel corso della seconda fase dell'Unione Economica e Monetaria. **È calcolato e pubblicato dall'ISTAT e inviato mensilmente a EUROSTAT**, che a sua volta diffonde gli indici armonizzati dei singoli Paesi ed **elabora e diffonde l'indice sintetico europeo**, calcolato sulla base dei primi |

> **Il FOI è quello che incontrerai nel lavoro.** È l'indice con cui si rivalutano i canoni di locazione, gli assegni, e in generale i valori monetari previsti da contratti e norme. Se in commissione ti chiedono «a che serve concretamente un indice dei prezzi in un ufficio pubblico», la risposta è questa. E l'**IPCA** è quello che conta in sede europea: **è l'indice su cui la BCE misura il rispetto dell'obiettivo di inflazione**.

**Come sono calcolati** — e qui si chiude il cerchio con il paragrafo 6:

> Sono calcolati **utilizzando l'indice di Laspeyres**, in cui **sia il paniere sia il sistema dei pesi sono aggiornati annualmente e tenuti fissi per l'intero anno**.

È la soluzione pratica al limite di Laspeyres: si tiene il paniere fisso entro l'anno (per avere la costanza necessaria al confronto) ma **lo si aggiorna ogni anno** (per non perdere il contatto con la realtà dei consumi), concatenando poi le serie annuali.

**La classificazione ECOICOP.** La classificazione adottata è la **European Classification of Individual Consumption by Purpose (ECOICOP)**, contenuta nel **Regolamento quadro europeo UE 2016/792** sugli indici armonizzati dei prezzi al consumo e sull'indice dei prezzi delle abitazioni, e nel relativo **Regolamento di esecuzione UE 2020/1148**. Prevede **quattro livelli di disaggregazione**: **divisioni di spesa, gruppi di prodotto, classi di prodotto e sottoclassi di prodotto**.

**Le 12 divisioni di spesa** — il primo livello. Vale la pena averle presenti, perché una commissione può chiedere «che cosa c'è nel paniere ISTAT»:

1. prodotti alimentari e bevande analcoliche;
2. bevande alcoliche e tabacchi;
3. abbigliamento e calzature;
4. abitazione, acqua, elettricità e combustibili;
5. mobili, articoli e servizi per la casa;
6. servizi sanitari e spese per la salute;
7. trasporti;
8. comunicazioni;
9. ricreazione, spettacoli e cultura;
10. istruzione;
11. servizi ricettivi e di ristorazione;
12. altri beni e servizi.

**La gerarchia completa**, per dare l'idea della granularità del lavoro statistico: i primi due livelli sono comuni ai tre indici (12 divisioni, **43 gruppi di prodotto**); dal terzo livello in poi **il paniere IPCA si differenzia dagli altri due**. Per **NIC e FOI**: 43 gruppi → **102 classi** → **232 sottoclassi** → **310 segmenti di consumo** → **418 aggregati** → **1.014 prodotti** → **1.731 prodotti elementari**. Per l'**IPCA**: 101 classi, 231 sottoclassi, 309 segmenti, 422 aggregati, 1.033 prodotti, **1.751 prodotti elementari**.

Non serve memorizzare i numeri: serve **saper dire che il paniere arriva a oltre 1.700 prodotti elementari**, il che rende immediatamente l'idea di che cosa significhi misurare l'inflazione.

### 7.3 L'indice dei prezzi delle abitazioni (IPAB)

Misura **la variazione nel tempo dei prezzi degli immobili residenziali nuovi o esistenti** (appartamenti, case unifamiliari, case a schiera) **acquistati dalle famiglie, sia per fini abitativi sia per fini d'investimento**.

Da sapere:

- ha **cadenza trimestrale**;
- si compone di **due sub-indici**: prezzi delle **abitazioni nuove** e prezzi delle **abitazioni esistenti**;
- è costruito **secondo le linee guida di EUROSTAT**, per garantire la comparabilità fra Paesi;
- è calcolato **utilizzando l'indice a catena del tipo Laspeyres**.

## 8. L'indice della produzione industriale

Chiude il capitolo, ed è **l'indicatore congiunturale per eccellenza**.

**Che cosa misura:** **la variazione nel tempo del volume fisico della produzione dell'industria in senso stretto**, **escluso quindi il settore delle costruzioni**.

**Come è costruito:**

- si basa su una **rilevazione statistica campionaria condotta presso le imprese**, che misura **il volume di produzione dei beni inclusi in un paniere rappresentativo di prodotti**;
- si calcolano **indici per voci di prodotto**, poi sintetizzati in **indici per attività economica utilizzando la formula di Laspeyres**;
- **dal 2018** è calcolato con **base 2015 = 100** e con riferimento alla classificazione delle attività economiche **Ateco 2007**, basandosi su un panel di **circa 4.600 imprese**;
- **l'ISTAT lo destagionalizza**, cioè depura la serie storica **dalle fluttuazioni di carattere stagionale**.

> **Il ponte con econometria, da fare esplicitamente.** La destagionalizzazione qui menzionata è esattamente la **procedura TRAMO-SEATS** studiata nel capitolo 14 della Parte III: TRAMO pretratta la serie (giorni lavorativi, festività mobili, *outlier*) e identifica un modello ARIMA, SEATS estrae le componenti. **E l'indice della produzione industriale è proprio l'esempio che il manuale di econometria usa** per illustrare la procedura, perché è «uno di quelli che presenta le maggiori fluttuazioni stagionali». Se riesci a collegare i due capitoli in commissione, dimostri di aver studiato il programma come un sistema e non come materie separate.

---

# PARTE II — LA CONTABILITÀ NAZIONALE E IL SEC 2010

*(Capitolo 2 del manuale, pp. 587-599)*

Questo è **il capitolo più lungo e più importante** della materia, e per il tuo bando vale doppio: si salda direttamente con **contabilità pubblica** (il conto economico consolidato delle amministrazioni pubbliche, il Patto di stabilità, i parametri di Maastricht) e con **scienza delle finanze**. Vale la pena padroneggiarlo.

## 9. Che cos'è la contabilità nazionale

**La definizione**, da sapere quasi alla lettera perché è densa e completa:

> La **contabilità nazionale** è una **tecnica di sintesi statistica** che descrive l'attività economica di un Paese o di una circoscrizione territoriale **attraverso un quadro contabile coerente**. Ha per oggetto **l'osservazione quantitativa e lo studio statistico del sistema economico** o dei sub-sistemi che lo compongono a diversi livelli territoriali, **sotto forma di una completa e sistematica presentazione dei flussi economici e finanziari** che si verificano fra gruppi significativi di operatori, **e delle consistenze finali dei beni reali e finanziari**. Determina alcuni **parametri fondamentali sullo stato di salute dell'economia**, come il **PIL** (Prodotto interno lordo) o il **RN** (Reddito nazionale).

Due elementi da notare: **«quadro contabile coerente»** — la coerenza è il valore che giustifica tutto l'edificio — e la doppia natura **flussi / consistenze**, che tornerà come distinzione tecnica al paragrafo 14.

## 10. Il circuito economico

In un approccio macroeconomico l'analisi si conduce **in termini di flusso** e tende a dimostrare **l'interdipendenza fra le diverse variabili del sistema**. La rappresentazione dei flussi di prodotti, redditi o capitali che si stabiliscono fra i diversi soggetti assume il nome di **circuito economico**.

**Lo schema elementare a due agenti** — famiglie e imprese — che il manuale disegna, e che è utilissimo da saper descrivere a voce:

> Le **famiglie domandano beni e servizi** e le **imprese li offrono**: è il **mercato dei beni e servizi**, lungo il quale scorre in senso opposto **la spesa**.
> Le **famiglie offrono fattori produttivi** (lavoro, capitale) e le **imprese li domandano**: è il **mercato dei fattori**, lungo il quale scorre in senso opposto **il reddito**.
>
> Il circuito si chiude: **la spesa delle famiglie è il ricavo delle imprese; il costo dei fattori per le imprese è il reddito delle famiglie.** È questa circolarità che rende possibile misurare la stessa grandezza — il PIL — da tre lati diversi (produzione, reddito, spesa) ottenendo lo stesso numero.

Questa visione è alla base della contabilità nazionale moderna, che mette in evidenza **i diversi stadi del processo economico**: **produzione, formazione, distribuzione, redistribuzione e utilizzazione del reddito, accumulazione finanziaria e non finanziaria**.

**La storia**, breve ma da citare perché fa impressione:

- nel **XVII secolo**, grazie alle opere di **William Petty** e **Gregory King**, vennero allestiti **conti nazionali approssimativi per l'Inghilterra**;
- nel **1758** il fisiocratico francese **François Quesnay**, nel ***Tableau économique***, sviluppò **un modello di circuito economico** atto a porre in evidenza le relazioni fra soggetti economici.

> **Tienilo a mente**: il *Tableau* di Quesnay tornerà al capitolo 4 come **antenato diretto delle tavole input-output di Leontief**. È lo stesso filo che attraversa due secoli e mezzo.

## 11. I conti nazionali: a che cosa servono davvero

**La definizione operativa:**

> I conti nazionali sono considerati **il principale strumento di misurazione della situazione economica complessiva di un Paese**. Sono utilizzati per estrapolare informazioni sull'economia di una nazione **da parte sia degli organi di governo sia di altri soggetti economici e sociali**, che le usano come base per le proprie decisioni, e **rappresentano un punto di riferimento per i mezzi di informazione, le imprese e la ricerca accademica**.

**I quattro indicatori chiave e il loro uso istituzionale** — questa tabella è **oro puro per l'orale**, perché mostra che i numeri della statistica economica hanno **conseguenze giuridiche e finanziarie dirette**:

| Indicatore | A che cosa serve concretamente |
|---|---|
| **Rapporto deficit/PIL e rapporto debito/PIL** | Sono **due dei parametri di Maastricht**; servono a **definire la situazione della finanza pubblica degli Stati dell'UE** |
| **Reddito nazionale lordo** | È utilizzato dalle istituzioni europee per **determinare il contributo di ciascun Paese al bilancio dell'Unione** |
| **PIL pro capite regionale** | È usato per **definire i fondi strutturali da destinare alle regioni dell'UE** |
| **Tasso di variazione trimestrale del PIL** | È **uno dei principali indicatori di riferimento della politica monetaria** dell'Unione Monetaria Europea |

Il manuale sottolinea la posta in gioco: *il valore di tali indicatori **può influenzare gli andamenti e le sorti istituzionali, politiche, finanziarie ed economiche di un Paese** e diventa fondamentale soprattutto nell'ambito delle politiche europee, in quanto fornisce **indicazioni cruciali per la *governance* sia dell'UE nel suo complesso sia di ogni Stato membro*.

> **La frase da portare in commissione.** *La contabilità nazionale non è una rilevazione neutrale: **da come si misura il PIL dipende quanto ciascuno Stato versa al bilancio europeo e quanti fondi strutturali riceve ciascuna regione**. È per questo che le regole di misurazione sono fissate da un regolamento europeo direttamente applicabile e non da una scelta tecnica nazionale.* È il punto in cui statistica, diritto europeo e finanza pubblica si toccano.

**La ridefinizione della contabilità nazionale** che il manuale dà, una volta chiarito il ruolo dei conti:

> Una **disciplina statistica** che ha per oggetto **l'analisi, la valutazione e la rappresentazione in termini quantitativi del risultato dell'attività economica** di un Paese, di un sistema economico o dei sub-sistemi che lo compongono a diversi livelli territoriali, **in un preciso arco temporale**.

**Il problema della disomogeneità.** Un passaggio che vale la pena riportare, perché è realistico e mostra perché serviva un'armonizzazione. A livello europeo e internazionale **esiste una forte disomogeneità fra i dati relativi alle economie dei singoli Stati**, non solo per la disparità di crescita (Paesi sviluppati, in rapida crescita, in via di sviluppo) ma anche perché **i dati vengono attinti da fonti diverse**: in Italia si usano dati ISTAT e Banca d'Italia; per le statistiche europee la BCE ed EUROSTAT; per i Paesi sviluppati l'OCSE; per i Paesi in via di sviluppo la Banca mondiale, la FAO, l'UNDP.

**Le tre conclusioni sullo stato di salute dei Paesi** che il manuale trae, e che sono un bel materiale per una risposta di respiro:

1. **alcune economie convergono, altre divergono**;
2. **ai tradizionali fattori considerati determinanti per lo sviluppo se ne affiancano altri** — immateriali, ambientali, umani — **prima ignorati**;
3. **devono essere considerati anche i problemi economici determinati dalla demografia e dal modello sociale** di un Paese.

**Le sette funzioni della contabilità nazionale** — un elenco molto spendibile:

1. **osservare razionalmente la realtà** e offrire strumenti a chi cerca le relazioni fra cause ed effetti;
2. **fornire dati a chi formula previsioni**;
3. **individuare gli strumenti utili alla gestione e al controllo di un'economia**;
4. **misurare gli effetti degli interventi** operati dai diversi gruppi di operatori pubblici e privati;
5. **confrontare le economie nel tempo e nello spazio**;
6. **avere una misura del grado di globalizzazione** dei sistemi economici;
7. **misurare gli effetti sul benessere economico** nelle diverse condizioni di reddito e sociali.

> Il punto 4 è **letteralmente valutazione delle politiche pubbliche**. Vale la pena nominarlo.

## 12. Dal SEC 95 al SEC 2010 — la cronologia da sapere

**La definizione del SEC**, che il manuale riporta testualmente dall'ISTAT e che conviene saper citare:

> «Il **Sistema europeo dei conti nazionali e regionali (SEC)** è **lo schema di riferimento per la misurazione dell'attività economica e finanziaria di un sistema economico**, delle sue componenti e delle relazioni che fra di esse si instaurano in un determinato periodo di tempo. **Oggetto della misura sono le transazioni poste in essere dagli agenti economici** (definiti **unità istituzionali**) nei rapporti con le altre unità **residenti** sul territorio economico o con quelle **non residenti**.» (ISTAT)

**La cronologia**, che una commissione può chiedere in forma di date:

| Anno | Evento |
|---|---|
| **1970** | **EUROSTAT** (Istituto Statistico delle Comunità Europee) mette a punto il **SEC** — *Sistema europeo dei conti economici integrati* — analizzando i diversi sistemi di contabilità nazionale, **con particolare riferimento al modello francese** |
| **1974** | Il SEC, applicato dapprima in via sperimentale, è **adottato definitivamente da tutti i Paesi membri, fra cui l'Italia** |
| **1996** | **Regolamento (CE) 2223 del 25 giugno 1996**: il sistema è modificato coerentemente con il **System of National Accounts (SNA)** redatto dall'ONU e da altre istituzioni internazionali |
| **1999** | **Tutti gli Stati membri dell'UE adottano il SEC 95** — *Sistema europeo dei conti nazionali e regionali*, acronimo adottato dall'ISTAT |
| **2008** | Ultima versione dello **SNA** delle Nazioni Unite |
| **2013** | **Regolamento (UE) 549/2013** del Consiglio: definizione del **SEC 2010** |
| **2014** | **Il SEC 2010 sostituisce il SEC 95** |

**Che cosa fa il SEC 2010:** definisce, in modo **coerente con le linee guida stabilite nello SNA 2008**, **i principi e i metodi di contabilità nazionale a livello europeo**, e **fissa in maniera sistematica e dettagliata il modo in cui si misurano le grandezze rappresentative di un'economia**.

**La struttura del regolamento:** si compone di **due allegati (A e B)** e si articola in **24 capitoli**: **i primi 13 richiamano la struttura e i concetti del SEC 95**, mentre **i successivi descrivono aspetti del sistema dei conti che rispecchiano gli sviluppi nella misurazione delle moderne economie**.

**La forza giuridica** — punto da non trascurare, perché è il collegamento con il diritto:

> Le metodologie introdotte dal SEC **sono diventate regole stringenti a cui tutti i Paesi UE si sono uniformati**. Il regolamento prevede inoltre **un programma di trasmissione obbligatoria dei dati**, stabilendo **il dettaglio dei dati che ciascun Paese deve rendere disponibile e la relativa tempistica di trasmissione**.

Si tratta di un **regolamento**, quindi **direttamente applicabile** negli Stati membri senza necessità di recepimento: la contabilità nazionale italiana è, giuridicamente, esecuzione di diritto europeo.

**Come si costruiscono le stime, e la revisione.** Si utilizza l'insieme dei dati derivati dalle **rilevazioni ISTAT**, integrate con informazioni provenienti da **archivi amministrativi e indagini di fonte esterna, pubblica e privata**. Le stime sono sottoposte a **revisioni ordinarie (annuali) e straordinarie (generalmente quinquennali)**.

## 13. Le novità del SEC 2010 — il paragrafo che fa la differenza

Il manuale elenca le principali modifiche. Sono **otto**, e almeno le prime tre vanno sapute con precisione perché **hanno avuto effetti diretti sul PIL italiano e sui conti pubblici**.

### 13.1 La capitalizzazione delle spese in Ricerca e Sviluppo — l'innovazione più significativa

> **L'innovazione più significativa introdotta dal SEC 2010 è il riconoscimento della spesa per ricerca e sviluppo (R&S) come una SPESA DI INVESTIMENTO**, da cui deriva la creazione di **prodotti della proprietà intellettuale** (formazione di capitale fisso). In pratica, tali spese sono considerate **un elemento acceleratore per la crescita di un Paese**.

**Il cambiamento, in una riga:** con il **SEC 95** le spese in R&S erano **costo intermedio** del soggetto che le effettuava — e quindi **sparivano nel calcolo del valore aggiunto**; con il **SEC 2010** diventano **parte della domanda finale e contribuiscono alla formazione del PIL**.

**Ma con una distinzione importante secondo la natura del soggetto:**

- **soggetto NON appartenente alla pubblica amministrazione**: è corretto aspettarsi **effetti sul PIL e sul Reddito Nazionale**, che aumenteranno **di un ammontare pari all'importo dell'investimento riconosciuto**. Se le spese di R&S sono realizzate **in house** sono considerate investimento perché concorrono alla formazione di capitale fisso; se invece il soggetto **acquista prodotti di proprietà intellettuale all'esterno** — a meno che la R&S non sia la sua attività principale — la spesa è considerata **investimento esterno**;
- **soggetto appartenente alla pubblica amministrazione**: qui il manuale segnala una sottigliezza che merita attenzione. Poiché **la produzione della P.A. si misura come somma dei costi**, le specificità della contabilità pubblica **potrebbero determinare un effetto NULLO sul PIL nell'anno di produzione o acquisizione** dei prodotti di R&S. **Gli effetti si registreranno negli anni successivi, a causa dei costi di ammortamento** legati alle nuove attività immateriali generate o acquisite.

> **Perché questa è una bella risposta d'orale.** Mostra che **una regola contabile può cambiare il PIL di un Paese senza che nulla sia cambiato nell'economia reale**. Il passaggio al SEC 2010 ha innalzato il livello del PIL italiano — e quindi ha migliorato meccanicamente **i rapporti deficit/PIL e debito/PIL**, che sono i parametri di Maastricht. È un esempio perfetto di quanto la misurazione statistica sia una scelta con conseguenze politiche.

### 13.2 Le spese per armamenti

**Il cambiamento:**

- con il **SEC 95**, **solo le spese per attrezzature militari che avevano un equivalente uso civile** (aeroporti, porti, strade, ospedali) erano registrate **come investimenti lordi**; **il resto delle spese in armamenti** (veicoli, navi da guerra, sottomarini, aerei militari, carri armati, lanciamissili) **era visto come consumo intermedio**;
- con il **SEC 2010** la definizione si amplia e **include tutte le armi e i mezzi militari privi di equivalente civile**, purché **utilizzati continuamente per più di un anno nella produzione di servizi di difesa**. Gli **articoli monouso** — munizioni, missili, razzi, bombe — sono considerati **scorte militari**.

La ratio, dice il manuale: **la definizione di immobilizzazioni in ambito militare è stata armonizzata con la definizione generale valida per tutti gli altri settori economici**.

**L'effetto sui conti**, che è una finezza da citare: gli effetti su PIL e valore aggiunto si registreranno **negli anni successivi all'acquisto**, come conseguenza degli ammortamenti. **L'impatto sull'indebitamento netto è invece NULLO**, perché **la minore spesa per consumi intermedi è compensata dall'aumento della spesa per investimenti**.

### 13.3 Il perimetro delle amministrazioni pubbliche — il punto più rilevante per il tuo bando

> La delimitazione del perimetro delle amministrazioni pubbliche **è fondamentale ai fini della costruzione del conto economico consolidato delle amministrazioni pubbliche, il quale costituisce il riferimento per gli aggregati trasmessi alla Commissione europea in applicazione del Patto di stabilità e di crescita.**

**La definizione del settore S13**, testuale nel SEC 2010 e da sapere:

> Il **settore delle amministrazioni pubbliche (S13)** è «costituito dalle **unità istituzionali che agiscono da produttori di beni e servizi non destinabili alla vendita (*non market*)**, la cui produzione è destinata a **consumi collettivi e individuali** e sono **finanziate da versamenti obbligatori** effettuati da unità appartenenti ad altri settori, nonché dalle **unità istituzionali la cui funzione principale consiste nella redistribuzione del reddito e della ricchezza del Paese**».

**Come cambia il criterio di classificazione:**

- con il **SEC 95** un'unità entrava nel settore P.A. se erano soddisfatte **due condizioni**: essere **legata a un'amministrazione pubblica o controllata da essa**, ed essere **definita produttore non di mercato** secondo il ***test market/non market* (test del 50%)**;
- con il **SEC 2010** occorre invece **verificarne il comportamento economico** attraverso **due verifiche**: l'applicazione del **test market/non market** **E** **l'analisi delle condizioni di concorrenzialità in cui essa opera**.

**Il test market/non market** è funzionale alla distinzione fra produttori di beni e servizi destinabili alla vendita e non, e **verifica in quale quota le vendite coprono i costi di produzione (compreso il costo del capitale)** dell'unità considerata. La soglia è il **50%**.

**Le condizioni di concorrenzialità** vanno verificate **mediante valutazioni qualitative** che riguardano **la struttura della domanda e dell'offerta**: **le modalità di affidamento, le condizioni contrattuali di fornitura, il tipo di attività svolta**.

Il manuale conclude che la ridefinizione ha comportato la riclassificazione di alcune unità, ma che **l'impatto sul disavanzo pubblico, sul debito e sugli altri aggregati non può dirsi significativo**.

> **Perché questo è il paragrafo che devi conoscere meglio di tutti in questo capitolo.** *Chi sta dentro il perimetro S13 concorre al deficit e al debito che l'Italia comunica a Bruxelles.* Decidere se una società partecipata, un'agenzia o un ente strumentale sia «dentro» o «fuori» **non è una questione contabile: è una questione che sposta i numeri su cui si misura il rispetto del Patto di stabilità**. Ed è esattamente il tipo di problema su cui lavora un funzionario dell'area economico-statistica. Se colleghi questo al **conto economico consolidato delle amministrazioni pubbliche** studiato in contabilità pubblica, e all'**elenco ISTAT delle unità S13** pubblicato annualmente in Gazzetta Ufficiale, hai fatto una risposta che vale molto.

### 13.4 Le altre cinque novità

**La terza risorsa propria UE basata sull'IVA.** Con il SEC 95 era registrata **come imposta indiretta pagata direttamente dai contribuenti al resto del mondo** — e **non transitava per il conto economico delle amministrazioni pubbliche**. Con il SEC 2010 è registrata **come spesa fra i trasferimenti correnti pagati dagli Stati membri all'UE**. **Nessun impatto sul deficit**, perché aumentano in egual misura sia l'IVA in entrata sia le spese correnti.

**I «super dividendi»**, cioè **i dividendi in eccesso rispetto a quelli distribuiti in media da un'impresa**. Con il SEC 2010 sono considerati **pagamenti eccezionali e prelievi di capitale** — e non più reddito corrente. Il SEC 95 **non si occupava della valutazione della coerenza fra i dividendi distribuiti e il reddito d'impresa**. È una regola anti-elusione contabile: impedisce a uno Stato di migliorare il proprio deficit facendosi distribuire dividendi straordinari dalle proprie partecipate.

**I crediti d'imposta.** Con il SEC 95 **tutti i crediti concorrevano a ridurre il livello delle imposte**. Con il SEC 2010 si distingue fra:

- **crediti non pagabili** — utilizzabili **soltanto entro i limiti del debito d'imposta**;
- **crediti pagabili** — utilizzabili **oltre il limite del debito d'imposta**.

**Solo i crediti pagabili sono classificati per l'intero importo come SPESA** — configurando in tal caso **un sussidio** — indipendentemente da quanta parte riduca il debito d'imposta e quanta sia pagata direttamente ai beneficiari.

> **Nota di attualità che vale la pena avere pronta.** È **esattamente questa regola** ad aver determinato la classificazione dei crediti d'imposta edilizi italiani (il cosiddetto *superbonus*) come **spesa immediata** anziché come minori entrate spalmate negli anni, con l'effetto di far emergere l'intero onere sul deficit dell'anno di maturazione. È il caso più discusso di applicazione del SEC 2010 in Italia.

**Le operazioni in derivati.** Con il SEC 2010 **il calcolo dell'indebitamento netto delle amministrazioni pubbliche è stato uniformato** ed **è calcolato sempre allo stesso modo anche ai fini della procedura per i disavanzi eccessivi** prevista in ambito UE.

**Le società veicolo.** Sono introdotte **regole più stringenti** sulle società **che hanno per oggetto esclusivo la realizzazione di operazioni di cartolarizzazione** e che emettono strumenti finanziari negoziabili. In particolare: **le passività assunte dalle società veicolo non residenti controllate dalle amministrazioni pubbliche devono essere iscritte nei conti delle amministrazioni pubbliche**. Anche questa è una norma anti-elusione: impedisce di «parcheggiare» debito pubblico fuori dal perimetro.

**Importazioni ed esportazioni: il criterio della proprietà economica.** I flussi sono registrati **quando si verifica il trasferimento della proprietà di un bene**, **a prescindere dal fatto che vi sia un corrispondente movimento fisico da un Paese all'altro**. Cambiano di conseguenza due attività:

- il ***merchanting*** — la vendita a un non residente, da parte di un residente, di un bene acquistato da un altro non residente — che è ora registrato **all'interno del commercio di beni anziché di servizi**;
- il ***processing*** — i flussi di beni inviati o ricevuti dall'estero **per essere sottoposti a lavorazione senza cambio di proprietà** — che è ora **escluso dai beni**, mentre **le attività di lavorazione connesse sono contabilizzate nella voce servizi**.

**L'effetto netto di queste modifiche sul PIL è quasi pari a zero**, ma cambia la composizione delle poste.

**Il settore finanziario** è **disaggregato in comparti** che rispecchiano la sua attuale complessità e forniscono maggiore coerenza con il sistema statistico finanziario **della BCE e del Fondo monetario internazionale**. I **servizi assicurativi** passano da trasferimenti correnti a **trasferimenti in conto capitale**, il che **rende meno volatile la stima del servizio prestato dalle imprese di assicurazione**; sono introdotte nuove regole per la **contabilizzazione dei diritti pensionistici**.

**Le attività illegali.** Un punto che colpisce sempre e che vale la pena citare:

> Con il passaggio al SEC 2010, in sede europea **si è deciso di applicare in maniera omogenea le regole del sistema che impongono l'inclusione nei conti del reddito prodotto dall'attività di commercializzazione di sostanze stupefacenti, di esercizio della prostituzione e di contrabbando di alcool e sigarette.**

La ragione non è morale ma di **comparabilità**: in alcuni Paesi queste attività sono legali e già contabilizzate, in altri no; includerle ovunque elimina una distorsione nei confronti internazionali. E c'è un criterio tecnico preciso, che vedremo al paragrafo 15: **un'attività illegale è registrabile come operazione solo se tutte le unità partecipanti intervengono contestualmente** — quindi lo spaccio sì, il furto no.

**Il filo conduttore di tutte le modifiche**, nelle parole del manuale: *la ricerca di **una maggiore coerenza fra gli standard utilizzati dai Paesi**, per garantire **un'armonizzazione dei criteri di misurazione e di confronto** fra le contabilità nazionali dei diversi Stati.*

## 14. Le cinque caratteristiche del sistema

Il manuale organizza la descrizione tecnica del SEC su **cinque punti**, che sono anche una scaletta di risposta perfetta:

1. **la definizione di operatori residenti nel territorio economico**;
2. **la classificazione degli operatori**;
3. **la classificazione delle operazioni economiche** (flussi e consistenze);
4. **la struttura dei conti e la definizione degli aggregati**;
5. **il quadro delle interdipendenze fra gli operatori economici**.

### 14.1 La residenza — un concetto ECONOMICO, non giuridico

Questo è un punto che la commissione apprezza perché è controintuitivo:

> Il SEC si riferisce a un concetto di residenza **di tipo economico e non giuridico**: si considerano **residenti le unità che hanno il CENTRO DI INTERESSE nel territorio economico**, ossia **che svolgono operazioni economiche per un periodo di tempo relativamente lungo (almeno un anno)**.

**E il territorio economico può essere diverso dal territorio geografico o politico-amministrativo.** Vi rientrano:

- il **territorio geografico**;
- le **zone franche**, fra cui magazzini e fabbriche sotto controllo doganale;
- le **zone franche territoriali situate all'estero e utilizzate dalle amministrazioni pubbliche** del Paese;
- le **acque territoriali**;
- **navi, aerei e piattaforme galleggianti appartenenti a unità residenti**;
- i **giacimenti in acque internazionali sfruttati da unità residenti**.

**Non vi rientrano** invece **le zone franche extraterritoriali sedi di ambasciate, consolati e basi militari**.

**Le unità «fittiziamente residenti»**, che il SEC 2010 tratta come unità istituzionali:

a) **le parti di unità non residenti che hanno un centro di interesse economico prevalente** nel territorio economico del Paese (cioè che vi effettuano operazioni per un anno o più);
b) **le unità non residenti proprietarie di terreni o fabbricati** nel territorio economico del Paese, **limitatamente alle operazioni connesse a tali terreni o fabbricati**.

Il **totale dell'economia** è definito in termini di unità residenti; le operazioni delle unità residenti con unità non residenti sono raggruppate nel **conto del resto del mondo**.

### 14.2 La classificazione degli operatori: settori istituzionali e branche

Il SEC opera una **duplice** classificazione:

- **unità e settori istituzionali**, intendendo per tali **le entità economiche che possono essere proprietarie di beni e attività, assumere passività, esercitare attività economiche e intervenire in operazioni con altre unità per conto proprio**;
- **branche di attività economica**, se si vogliono porre in evidenza **le relazioni fra gruppi di operatori di tipo tecnico-economico** e in base al **tipo di attività esercitata**.

> **La distinzione, in una frase da dire all'orale.** *I **settori istituzionali** raggruppano i soggetti in base a **chi sono e come si finanziano** — è l'ottica del comportamento economico. Le **branche** li raggruppano in base a **che cosa producono** — è l'ottica tecnico-produttiva. La contabilità nazionale usa i primi; **l'analisi input-output usa le seconde**.*

**I SEI SETTORI ISTITUZIONALI** — con funzione principale e risorsa prevalente. Questa tabella va saputa:

| Settore istituzionale | Funzione principale | Risorse prevalenti |
|---|---|---|
| **Società non finanziarie** | Produrre **beni e servizi non finanziari destinabili alla vendita** | **Entrate derivanti dalle vendite** |
| **Società finanziarie** | **Finanziare e assicurare** (intermediazione finanziaria e attività finanziarie ausiliarie) | **Fondi provenienti da assunzioni di passività** |
| **Amministrazioni pubbliche (S13)** | Produrre **servizi collettivi** non destinabili alla vendita, per consumi collettivi e individuali | **Versamenti obbligatori** effettuati direttamente o indirettamente da unità di altri settori |
| **Istituzioni senza scopo di lucro al servizio delle famiglie (ISP)** | Produrre **servizi non destinabili alla vendita per consumi finali di tipo individuale** (destinati a famiglie o gruppi di famiglie) | **Versamenti volontari** delle famiglie nella funzione di consumatori, **pagamenti delle amministrazioni pubbliche**, **redditi da capitale** |
| **Famiglie** | Duplice: **produrre** beni e servizi (come imprenditori) e **consumare** beni e servizi | **Remunerazione dei fattori della produzione**, **trasferimenti** dagli altri settori; **benefici dal consumo** |
| **Resto del mondo** | **Settore *sui generis***, non caratterizzato da funzione principale né da risorse prevalenti | Raggruppa **le unità istituzionali non residenti che effettuano operazioni con unità residenti** |

Nota sulle **famiglie**: il SEC le definisce **sia come consumatori sia come imprenditori**. Nella funzione di consumatori sono «piccoli gruppi di persone che **condividono la stessa abitazione, mettono in comune i loro redditi e il loro patrimonio e consumano collettivamente alcuni tipi di beni e servizi**, come l'abitazione e i pasti».

**Le unità di attività economica a livello locale (UAE locali) e le branche.** L'unità elementare per l'analisi produttiva è l'**unità di attività economica a livello locale (U_AEL)**: **una cellula operativa di tipo funzionale** — lo stabilimento, il reparto di produzione — cioè **un'unità di produzione caratterizzata da strutture dei costi, processi di produzione e prodotti omogenei**.

Il problema pratico che il manuale segnala: **la maggior parte di tali unità non realizza produzioni concernenti un solo processo**; accanto a un'**attività principale** si individua un'**attività secondaria** non omogenea rispetto alla prima. Per porre in evidenza le relazioni tecnico-economiche **è indispensabile scindere le differenti attività**.

Un'**unità istituzionale può includere una o più UAE locali**, mentre **una UAE locale può appartenere a una sola unità istituzionale**.

Un raggruppamento di unità di produzione omogenea costituisce una **BRANCA di attività economica**, secondo la classificazione internazionale **NACE Rev. 2** — atta a soddisfare l'esigenza di **un linguaggio comune di classificazione a livello comunitario**. Una branca è quindi **un gruppo di UAE locali che esercitano un tipo di attività identico o simile**, **indipendentemente dal fatto che le unità istituzionali cui appartengono producano prodotti destinabili o non destinabili alla vendita**.

> **Nota terminologica utile:** la NACE è la classificazione europea; la sua versione italiana, usata dall'ISTAT, è l'**Ateco** — la stessa citata al paragrafo 8 a proposito dell'indice della produzione industriale (**Ateco 2007**).

### 14.3 Flussi e consistenze, e le operazioni

**La distinzione fondamentale:**

- i **FLUSSI** rappresentano **le modificazioni di valore economico** — creazione, trasformazione, scambio, trasferimento o scomparsa del valore — ossia **le variazioni di attività o passività**, e **si riferiscono ad azioni ed effetti di eventi che si verificano entro un determinato periodo di tempo**;
- le **CONSISTENZE (o *stock*)** misurano **il valore delle attività o delle passività in un preciso momento**.

> **La formula per ricordarla:** *il flusso è un film, la consistenza è una fotografia.* Il PIL è un flusso (quanto si è prodotto in un anno); il debito pubblico è una consistenza (quanto si deve al 31 dicembre). Confonderli è l'errore più comune nel commentare i dati economici.

I flussi si distinguono in **operazioni** e **altre variazioni delle attività e passività**.

**Le quattro categorie di operazioni:**

1. **operazioni su prodotti** (beni e servizi), che descrivono **l'origine** (produzione interna o importazione) e **la destinazione** (consumi intermedi, consumi finali, formazione del capitale o esportazioni);
2. **operazioni di distribuzione e redistribuzione del reddito e della ricchezza**, attraverso cui si attua **la distribuzione fra i fattori della produzione del valore aggiunto** sotto forma di **redditi primari**, e **la redistribuzione fra settori istituzionali**;
3. **operazioni finanziarie**, che **modificano le consistenze dei crediti e dei debiti** di ciascun settore verso gli altri;
4. **altre operazioni**, come **gli ammortamenti** o le **acquisizioni meno cessioni di attività finanziarie non prodotte**.

**Tre ulteriori distinzioni:**

- **unilaterali / bilaterali**: fra le prime i **trasferimenti**; fra le seconde le operazioni sui prodotti e quelle finanziarie, che riguardano l'interazione fra due o più unità;
- **monetarie / non monetarie**, a seconda che comportino o meno scambio di denaro;
- **con contropartita** (a fronte di qualcosa si ottiene qualcos'altro) o **senza contropartita** (a fronte di un'azione non si ottiene nulla in cambio).

**Le tre modificazioni nella registrazione** — un passaggio tecnico ma con esempi belli:

- **DIROTTAMENTO**: un'operazione fra due soggetti **viene registrata come se avvenisse per il tramite di un terzo**, con la conseguenza che **un'unica operazione è registrata come due operazioni distinte** (un'operazione fra A e C diventa una fra A e B e una fra B e C);
- **FRAZIONAMENTO**: un'operazione che **appare alle parti come unica è registrata come due o più operazioni classificate in modo diverso** — l'esempio è **il pagamento dei premi di assicurazione**, che si scompone in servizio assicurativo e trasferimento;
- **RICONOSCIMENTO DELLA PARTE PRINCIPALE**: in caso di **attività delegate**, quando **un'unità effettua un'operazione per conto di un'altra (il mandante) che ne sopporta il costo**, l'operazione è registrata **esclusivamente nei conti del mandante**.

**Le attività illegali e il criterio della contestualità.** Come anticipato:

> Le attività economiche illegali **possono essere considerate operazioni, ma solo quando tutte le unità partecipanti all'attività intervengono contestualmente**. Così **l'acquisto o la vendita di droga può essere registrata come operazione**, perché prevede la presenza di almeno due soggetti interessati allo scambio; **un furto, invece, anche se è attività illecita, non può mai essere registrato come operazione, perché chi subisce il furto non ha alcun interesse a essere derubato.**

È una distinzione elegante e memorabile: **la contabilità nazionale registra scambi volontari, non trasferimenti coattivi**. Le variazioni di volume delle attività e passività e i guadagni e le perdite in conto capitale, pur modificando attività e passività, **non sono determinati da operazioni**.

### 14.4 La struttura dei conti e gli aggregati

**I TRE GRUPPI DI CONTI** del SEC 2010:

1. **conti delle operazioni correnti** — si riferiscono alla **formazione, distribuzione e redistribuzione del reddito**, nonché alla **sua utilizzazione sotto forma di consumi finali**, e **consentono di calcolare il risparmio**;
2. **conti dell'accumulazione** — analizzano **le componenti che concorrono alle variazioni delle attività e delle passività** e permettono di registrare **le variazioni del patrimonio netto**;
3. **conti patrimoniali** — presentano **le attività e passività totali all'inizio e alla fine del periodo contabile, con il rispettivo patrimonio netto**.

Questi conti sono **preceduti dal conto di equilibrio di beni e servizi** e **seguiti dai conti del Resto del mondo**.

**Il conto di equilibrio dei beni e servizi** illustra, per l'economia nel complesso o per gruppi di prodotti, **il totale delle risorse e degli impieghi**. Presenta **in forma tabulare un'identità contabile, secondo la quale l'offerta è pari alla domanda** per tutti i prodotti.

**Il conto del Resto del mondo**, a differenza degli altri, **non presenta tutte le operazioni effettuate nel Resto del mondo, ma solo quelle per le quali esiste una controparte nell'economia nazionale** oggetto di misurazione.

**GLI AGGREGATI ECONOMICI** sono **grandezze sintetiche che misurano il risultato dell'insieme delle operazioni svolte da tutte le unità economiche del sistema**. Si distinguono in due tipologie:

- **aggregati connessi direttamente alle operazioni** del sistema dei conti: **produzione di beni e servizi, consumi finali, investimenti fissi lordi, redditi da lavoro dipendente**;
- **aggregati che rappresentano saldi contabili**: **valore aggiunto, prodotto interno lordo, risultato lordo di gestione** — che possono essere espressi **al lordo o al netto degli ammortamenti**.

**La definizione di PIL secondo il SEC:**

> Il **PIL** è **uno degli aggregati fondamentali del SEC** e misura **il totale delle attività economiche esercitate su un territorio economico che comportano la produzione di prodotti o l'erogazione di servizi atti a soddisfare la domanda finale dell'economia**.

### 14.5 Le modalità di registrazione: partita doppia, partita quadrupla, competenza

**La struttura dei conti:**

- le **ENTRATE** si registrano **nella sezione di DESTRA**: rappresentano le **risorse** nei conti delle operazioni correnti, oppure **passività e patrimonio netto** nei conti finanziari;
- le **USCITE** si registrano **nella sezione di SINISTRA**: rappresentano gli **impieghi** nei conti delle operazioni correnti, oppure **attività** nei conti finanziari.

**Partita doppia e partita quadrupla** — la distinzione da sapere:

> Tutte le poste sono registrate secondo le regole della **partita doppia**, per cui ciascuna è contabilizzata **due volte**: una volta come **risorse** (o variazioni passive) e una come **impieghi** (o variazioni attive).
>
> **Nella pratica, tuttavia, i conti nazionali sono basati sul criterio della PARTITA QUADRUPLA**, in quanto **la maggior parte delle operazioni concerne due operatori, per cui devono essere contabilizzate due volte per ciascuno di essi.**

**Il principio della competenza:**

> Tutti i flussi sono contabilizzati in base al **principio della competenza**, il che implica che **un'operazione sia registrata nel momento in cui un valore economico è creato, trasformato o eliminato, o crediti e obbligazioni insorgono, sono trasformati o vengono estinti** — **non** quando avviene il pagamento.

> **Il collegamento con contabilità pubblica.** È esattamente la distinzione **competenza / cassa** che governa il bilancio dello Stato, e la ragione per cui il **saldo di finanza pubblica rilevante in sede europea — l'indebitamento netto — è un saldo di competenza economica**, diverso sia dal saldo di competenza giuridica sia dal fabbisogno di cassa. Nominarlo è un buon modo di mostrare che le due materie comunicano.

**La valutazione.** Ad eccezione di alcune variabili, **tutti i flussi e gli stock sono espressi in termini monetari**. Il concetto base adottato dal SEC è quello dei **prezzi di mercato**, per cui **gli impieghi sono valutati ai prezzi di acquisto** e **la produzione ai prezzi base di vendita**.

**La valutazione a prezzi costanti** consiste nel **computare i flussi e gli stock di un periodo contabile ai prezzi di un periodo anteriore**, allo scopo di **depurarli ed evidenziare la misura del volume fisico dei flussi**. È il ponte diretto con il capitolo 3.

### 14.6 Il quadro delle interdipendenze

**Il quadro delle interdipendenze fra gli operatori economici disaggrega l'economia nazionale** per mettere in evidenza **le operazioni su tutti i beni e servizi fra le branche di attività economica e i consumatori finali** in un dato periodo. Si presenta in due forme:

**1. Tavole delle risorse e degli impieghi.** Presentano **l'intera economia per branche di attività economica e per prodotti**, ponendo l'accento sul settore o sulla singola produzione. Illustrano **le relazioni fra le componenti del valore aggiunto lordo, gli input delle branche e l'offerta e la domanda di prodotti**. La loro compilazione **permette di rispettare il principio della coerenza** cui è ispirato il SEC 2010 e, **se opportunamente bilanciate**, assicura la coerenza nel collegamento fra i principali conti: **il conto di equilibrio dei beni e servizi, il conto della produzione e quello della generazione dei redditi primari**.

**2. Tavole input-output simmetriche.** Sono compilate **sulla base dei dati ricavati dalle tavole delle risorse e degli impieghi e da altre fonti aggiuntive**, allo scopo di **costituire la base teorica per successive analisi**.

È il punto di raccordo con il capitolo 4, dove queste tavole diventano l'oggetto principale.

---

# PARTE III — LA COMPARAZIONE NEL TEMPO E NELLO SPAZIO

*(Capitolo 3 del manuale, pp. 600-604)*

Capitolo breve ma con due concetti che vale la pena saper maneggiare: **il deflatore del PIL** e **le parità del potere d'acquisto**.

## 15. Il problema

> Il problema della comparazione degli aggregati economici sussiste **allorché si vogliano misurare le variazioni registrate in termini reali**, cioè **a prescindere da variazioni monetarie** — e allora si parla di **comparazione nel tempo** — **oppure quando si vogliano operare confronti di aggregati economici per studi comparati sulle attività economiche di Paesi diversi** — e allora si parla di **comparazione nello spazio**.

**Perché i confronti internazionali interessano**, e qui c'è un motivo che non è solo accademico: *l'interesse nasce non solo dall'esigenza di effettuare studi comparati sullo sviluppo economico, ma anche **dalla necessità di disporre di misure per stabilire un'equa ripartizione nel concorso al finanziamento di organismi internazionali***.

## 16. La comparazione nel tempo: i tre metodi e il deflatore

I confronti nel tempo implicano **la trasformazione dei valori espressi a prezzi correnti in valori a prezzi costanti**, atti a esprimere **la misura del volume fisico dei flussi**. Il manuale espone **tre metodi**:

| Metodo | Quando è applicabile | Come funziona |
|---|---|---|
| **1. Metodo DIRETTO** | Solo **se si posseggono i dati su prezzi e quantità relativi alle componenti elementari** di ciascun aggregato | Si calcola direttamente **Σ p₀ qₜ**, cioè le quantità correnti valutate ai prezzi dell'anno base |
| **2. DEFLAZIONE** | Se si dispone di **un idoneo indice dei PREZZI** dei beni e servizi costituenti l'aggregato | Si **divide il valore a prezzi correnti per l'indice dei prezzi** |
| **3. Metodo dell'indice delle QUANTITÀ** | Se si dispone di **un idoneo indice delle QUANTITÀ** | Si **moltiplica il valore a prezzi costanti per l'indice delle quantità** |

**L'ISTAT pubblica gli aggregati dei conti nazionali sia ai prezzi correnti sia ai prezzi di un anno scelto come base.**

## 17. Il deflatore implicito — il concetto chiave del capitolo

> **Rapportando gli aggregati espressi a prezzi correnti ai corrispondenti aggregati espressi a prezzi costanti**, e moltiplicando i quozienti per 100, si ottengono i cosiddetti **DEFLATORI IMPLICITI** (o **indici dei prezzi impliciti**).

**Perché conta:**

> La procedura è di **notevole importanza nelle manovre di politica economica**, in quanto **consente di calcolare i tassi di crescita delle corrispondenti grandezze reali**. Il deflatore implicito è impiegato per **depurare gli aggregati dalle variazioni nel tempo dovute all'inflazione**.

**Il deflatore del PIL** si ottiene quindi come **rapporto fra PIL a prezzi correnti (PIL nominale) e PIL a prezzi costanti (PIL reale)**, moltiplicato per 100.

Il manuale ricorda anche come si costruisce il PIL dal lato della spesa: **dal conto economico delle risorse e degli impieghi risulta che il PIL di un anno t è dato dalla somma degli impieghi — consumi nazionali, investimenti fissi lordi, variazione delle scorte e degli oggetti di valore, esportazioni di beni e servizi — meno le importazioni di beni e servizi.**

**Come si legge il risultato.** Nell'esempio del manuale, ponendo 2000 = 100, i deflatori crescono progressivamente: **il confronto con i risultati evidenzia le effettive variazioni intervenute nel PIL e non quelle dovute a mutamenti nei prezzi**.

> **La distinzione che conviene saper fare — ed è una domanda d'orale eccellente.**
>
> **Deflatore del PIL e indice dei prezzi al consumo NON sono la stessa cosa**, e le differenze sono tre:
>
> 1. **il paniere**: l'indice dei prezzi al consumo copre **i beni acquistati dalle famiglie**, anche se importati; il deflatore del PIL copre **tutti i beni prodotti internamente**, compresi investimenti e spesa pubblica, **ma esclude le importazioni**;
> 2. **la ponderazione**: l'indice dei prezzi al consumo è un **Laspeyres** a paniere fisso; il deflatore del PIL è un **indice implicito di tipo Paasche**, perché il rapporto fra nominale e reale pondera automaticamente con le quantità correnti;
> 3. **la conseguenza**: un rincaro del petrolio importato **fa salire l'indice dei prezzi al consumo** ma **non il deflatore del PIL** (anzi, può farlo scendere). È il motivo per cui nelle crisi energetiche i due indicatori divergono vistosamente.

## 18. La comparazione nello spazio: ICP, ECP e le parità del potere d'acquisto

### 18.1 Perché i tassi di cambio non bastano

Il manuale è chiaro sul fatto che il problema **non è semplice**, per due ragioni: **gli aggregati sono espressi in diverse unità di misura**, e **diverso è l'ambito in cui si calcolano**, per differenze nei gusti, negli stili di vita.

Il confronto potrebbe teoricamente essere effettuato **ricorrendo ai tassi di cambio**, traducendo gli aggregati in una comune unità monetaria. Ma:

> Tale metodo presenta **limiti notevoli**, in quanto **risente di fattori economici, finanziari e politici a livello nazionale e internazionale.**

I tassi di cambio sono determinati dai mercati finanziari e riflettono flussi di capitale, aspettative, interventi delle banche centrali: **non misurano il potere d'acquisto interno delle monete**.

### 18.2 Le parità del potere d'acquisto (PPA)

> Le **parità del potere d'acquisto (PPA)** sono **i tassi di conversione economica che eliminano le differenze nei livelli di prezzo fra i Paesi**, e **sono dati dai rapporti fra gli ammontari di moneta nazionale necessari per acquistare lo stesso paniere di prodotti comparabili e rappresentativi nei diversi Paesi** considerati.

I singoli rapporti di prezzo (o **parità**) ottenuti per ogni prodotto del paniere **sono aggregati** fino a ottenere la parità complessiva. Si parla di **parità del potere d'acquisto** quando ci si riferisce a **un intero paniere dei consumi**; per operare i confronti si ricorre a **una media aritmetica ponderata** che sintetizza le parità elementari.

La PPA serve come **deflatore spaziale del PIL** e dei suoi componenti, che **riflette solo le differenze nel livello dei prezzi fra i Paesi**.

### 18.3 I due programmi internazionali

**ICP — *International Comparison Program*.** La storia, con le date:

- **proposto dall'Istituto Statistico delle Nazioni Unite (ISNU) nel 1968**;
- **elaborato grazie ai contributi della Ford Foundation e della World Bank**;
- **mosse le basi da un modesto confronto fra 10 Paesi nel 1970**;
- **allo stato attuale coinvolge 107 Paesi**.

**ECP — *European Comparison Program*.** Introdotto **nell'ambito dell'ICP**, è il programma per il quale **EUROSTAT conduce, per un numero crescente di Paesi europei, indagini sui confronti internazionali dei prezzi**. La cadenza: **dopo il 1970 le indagini assunsero cadenza quinquennale**; **dal 1991 la cadenza delle rilevazioni è diventata annuale**.

> **Perché conta per il tuo bando.** L'obiettivo dichiarato è **il confronto in volume del PIL e dei suoi componenti dal lato degli impieghi, quali definiti nel quadro del SEC 2010**. E il **PIL pro capite in PPA** è **la grandezza su cui l'Unione europea classifica le regioni ai fini dei fondi strutturali** — le regioni «meno sviluppate», «in transizione» e «più sviluppate» si distinguono in base a soglie del 75% e del 100% della media UE. È di nuovo il punto in cui un metodo statistico determina un'allocazione finanziaria.

### 18.4 Confronti binari e confronti multipli

**Confronti binari.** Fra due Paesi, i beni e servizi del paniere possono essere aggregati con sintesi di tipo **Laspeyres** e **Paasche** — la stessa logica del capitolo 1, ma con i Paesi al posto dei tempi:

- se si usa **la struttura dei consumi del Paese base** → indice di tipo **Laspeyres**;
- se si usa **la struttura dei consumi del Paese di riferimento** → indice di tipo **Paasche**.

Per ovviare agli inconvenienti dei due si può ricorrere, come al solito, **alla loro media geometrica, cioè all'indice di Fisher**.

**Confronti multipli.** Qui emerge il problema decisivo:

> Anche nei confronti multipli si può utilizzare l'indice di Fisher, **ma l'unico inconveniente è rappresentato dal fatto che esso non gode della proprietà di TRANSITIVITÀ, che nei confronti fra più di due Paesi è di fondamentale importanza.**

Perché è fondamentale? Perché **senza transitività, confrontare Italia e Germania direttamente darebbe un risultato diverso dal confrontarle passando per la Francia** — un'incoerenza inaccettabile in una classifica internazionale.

Si distinguono quindi:

- **approccio binario**, in cui il calcolo avviene **con riferimento a una coppia di Paesi** → **metodo EKS**;
- **approccio multilaterale**, in cui il calcolo avviene **contemporaneamente** e si deve **ipotizzare un paniere comune per gli n Paesi** → **metodi GK e G**.

### 18.5 I tre metodi: EKS, Geary-Khamis, Gerardi

**METODO EKS.** Approntato dagli statistici **Éltető, Köves e Szulc**. Muove da **una matrice di indici di Fisher, ognuno definito per una coppia di Paesi**, e si prefigge di calcolare **un indice che soddisfi la proprietà di transitività**, risolvendo un problema di minimo. L'interpretazione, che è quella da riportare:

> L'indice EKS può essere interpretato come **una media geometrica di tutti i confronti fra il Paese i e il Paese j attraverso tutti i possibili collegamenti indiretti**, ed è fornito dalla **radice n-esima del prodotto del quadrato del confronto diretto per i corrispondenti confronti indiretti**.

**La matrice ottenuta consente confronti multilaterali che prescindono dal tipo di base scelta.** In parole semplici: **si forza la transitività prendendo la media di tutti i percorsi possibili**.

**METODO GEARY-KHAMIS (GK).** Si definiscono **fattori di conversione** mediante i quali i prezzi sono convertiti in una **moneta comune detta *standard di potere d'acquisto***. Si calcolano poi **prezzi medi internazionali** e, per ciascun Paese, il **rapporto fra il valore del suo paniere ai prezzi medi internazionali e il valore dello stesso paniere ai prezzi locali**. **Gli indici GK godono della proprietà di transitività.**

**METODO GERARDI (G).** Nasce da un limite dei due precedenti:

> I due indici appena esaminati **non godono di una proprietà fondamentale, la PROPRIETÀ ADDITIVA**, per la quale **la somma delle parità che si riferiscono a sub-aggregati deve essere pari alla parità globale**.

L'additività conta perché, senza di essa, **i confronti sulle componenti del PIL non sommano al confronto sul PIL totale** — di nuovo un'incoerenza inaccettabile per una statistica ufficiale. **Gerardi** ha proposto un indice analogo a GK ma che **usa come prezzo medio la media geometrica semplice dei prezzi dei diversi Paesi**.

> **Come riassumere questo paragrafo all'orale, senza perdersi negli acronimi.** *Confrontare i PIL di Paesi diversi con i tassi di cambio è sbagliato, perché i cambi riflettono i mercati finanziari e non il potere d'acquisto interno. Si usano allora le **parità del potere d'acquisto**, calcolate confrontando il costo di uno stesso paniere. Con due Paesi bastano Laspeyres, Paasche e Fisher; con più Paesi serve la **transitività**, che Fisher non ha — e da qui i metodi **EKS** (media di tutti i confronti indiretti) e **Geary-Khamis** (prezzi medi internazionali), cui **Gerardi** aggiunge l'**additività**. Il programma mondiale è l'**ICP** delle Nazioni Unite, quello europeo l'**ECP** di EUROSTAT.*

---

# PARTE IV — L'ANALISI DELLE INTERDIPENDENZE ECONOMICHE: LE TAVOLE INPUT-OUTPUT

*(Capitolo 4 del manuale, pp. 605-620)*

Il capitolo più lungo della materia dopo quello sulla contabilità nazionale, e quello con la matematica più pesante. **Lo racconto come idea economica**, perché è così che va esposto in commissione: l'algebra matriciale serve a calcolarlo, non a capirlo.

## 19. Che cos'è e a che cosa serve

**La definizione del campo:**

> L'**analisi delle interdipendenze economiche o settoriali** si occupa **dello studio delle relazioni che sussistono fra i diversi settori economici** e, in particolare, **fornisce una misura empirica dei flussi di beni e servizi che intercorrono a livello di settori produttivi**, evidenziando **i legami di interdipendenza sussistenti fra gli stessi**.

**La differenza rispetto alla contabilità nazionale** — ed è **la cosa da dire per prima**, perché spiega perché esiste un capitolo separato:

> A differenza della contabilità nazionale, **che è interessata ai risultati economici FINALI**, questo tipo di analisi **è volto verso i risultati economici che si ottengono nei settori che producono BENI E SERVIZI INTERMEDI**, il cui valore, **essendo incorporato nei beni finali, non è considerato dalla contabilità nazionale**.
>
> Gli effetti conseguenti a una variazione della domanda di un settore **si propagano in tutti gli altri settori**, e **la loro entità dipende dal grado di interdipendenza fra gli stessi**.

In altre parole: il PIL conta solo il valore aggiunto, per non contare due volte gli stessi beni. Ma così **perde di vista la struttura dell'economia** — chi compra da chi, chi dipende da chi. L'input-output recupera esattamente quell'informazione.

**Lo strumento:**

> Lo strumento di analisi più importante è la **tavola input-output (tavola I-O)**, o **tavola delle interdipendenze settoriali**, o **tavola intersettoriale dell'economia**. Essa **intende i sistemi economici nazionali come divisi in settori, misura e prevede gli scambi fra un settore e l'altro** — ossia **i flussi intermedi** — **sulla base di coefficienti tecnici**, esprimendo le relazioni **con un sistema di equazioni**.

## 20. La storia: da Quesnay a Leontief

Da sapere, perché è breve e fa sempre effetto:

> La **prima tavola input-output** fu elaborata nella prima metà del secolo scorso dall'economista russo **Wassily Leontief**, **su dati della contabilità nazionale statunitense**, e per la sua costruzione **si è aggiudicato il premio Nobel per l'economia nel 1973**.
>
> Leontief realizzò l'idea del fisiocratico **François Quesnay**, che **nel 1758, nel *Tableau économique*, per primo indagò le relazioni economiche esistenti fra classi sociali e settori produttivi**, considerando l'economia **come un insieme di settori**. Nel *Tableau* i settori produttivi sono due: **quello primario** (agricoltura e industria estrattiva) e **quello secondario** (manifatture e commercio).

**A che cosa serve concretamente la tavola:**

> Una tavola I-O è **un quadro contabile che evidenzia un elevato numero di relazioni esistenti nel sistema economico** e costituisce **la base di un modello utilizzato a fini interpretativi e previsivi**. Consente, mediante specifici procedimenti statistico-matematici, di **stimare le ripercussioni sul livello di produzione e sui fabbisogni delle singole branche provocate da modificazioni della domanda finale** (consumi, investimenti, esportazioni); **ciò permette di effettuare previsioni e di supportare decisioni di politica economica o di programmazione.**

> **La frase da tenere pronta.** *La tavola input-output è lo strumento con cui si risponde alla domanda: «se lo Stato spende un miliardo in edilizia, quanta produzione aggiuntiva genera complessivamente nell'economia, considerando che l'edilizia comprerà cemento, il cemento comprerà energia, l'energia comprerà servizi?». È **la base statistica del concetto di moltiplicatore settoriale**, e quindi uno strumento di valutazione ex ante delle politiche di spesa.*

## 21. La struttura di una tavola input-output

**Il presupposto e la sua approssimazione.** Concettualmente lo schema di Leontief presuppone che **ogni settore produca un solo bene**; ma nella costruzione concreta **l'aggregazione è inevitabile**, e si effettua **definendo raggruppamenti omogenei dal punto di vista tecnico-produttivo**. I settori possono essere quindi industrie, diversi livelli di aggregazione delle stesse, o imprese; **l'unità elementare di riferimento è la BRANCA**.

Il manuale sottolinea un punto metodologico importante:

> A differenza dei conti istituzionali di un Paese, **l'analisi delle operazioni effettuata per branca riguarda relazioni ECONOMICO-TECNICHE e non di COMPORTAMENTO**, per cui **risulta possibile solo fino al livello del risultato di gestione.**

I dati necessari sono **i flussi di prodotti da ciascun settore a sé stesso e agli altri**, quantificati **per un dato intervallo di tempo, generalmente un anno**.

**LE TRE SEZIONI DELLA TAVOLA** — questa è la struttura da saper descrivere:

| Sezione | Che cosa contiene |
|---|---|
| **1. Tavola degli IMPIEGHI INTERMEDI** | È **la matrice input-output vera e propria**: una **tabella a doppia entrata in cui sono indicate per riga e per colonna le medesime branche** |
| **2. Tavola degli IMPIEGHI FINALI** (a destra della prima) | Riporta **per colonna, per branca di origine, gli usi finali delle risorse**: **consumi, investimenti, variazioni delle scorte** e — se il sistema è aperto — **esportazioni**. Nell'ultima colonna, **il totale degli impieghi** |
| **3. Tavola degli IMPIEGHI PRIMARI E DELLE RISORSE** (sotto la prima) | Registra **i costi relativi ai fattori primari**: righe intestate alle **componenti del valore aggiunto**. L'ultima riga è **il totale delle risorse** |

**Come si legge** — ed è la chiave di lettura che va detta:

> Si parte dal raggruppamento delle imprese per settori omogenei (industria, agricoltura, servizi), riportati nella tabella a doppia entrata:
> - **sulla COLONNA come settore ACQUIRENTE**;
> - **sulla RIGA come settore VENDITORE**.
>
> Ciò in considerazione del fatto che **ogni settore economico allo stesso tempo acquista beni o servizi (*input*) dagli altri settori e vende loro la propria produzione (*output*)**.

**I reimpieghi.** La tavola indica anche i cosiddetti **reimpieghi**: **i beni o servizi utilizzati dallo stesso settore che li ha prodotti**, cioè i valori che stanno **nelle caselle corrispondenti a righe e colonne intestate allo stesso settore** — la diagonale principale.

**Le componenti del valore aggiunto**, che occupano la terza sezione: **salari e stipendi lordi (w), oneri sociali (s), altri redditi (k), ammortamenti (d), imposte indirette nette (t)**. La loro somma è il **valore aggiunto ai prezzi di mercato** della branca.

**Due precisazioni sui prezzi** che il manuale dà e che è bene riportare, perché mostrano la cura con cui si costruisce una statistica ufficiale:

- la produzione è valutata **ai prezzi *départ-usine***, cioè **comprensivi dei prezzi alla produzione e delle imposte indirette sulla produzione o sul primo scambio**, e quindi **non influenzati dai margini di distribuzione**;
- le importazioni sono valutate **ai prezzi *départ-douane***, cioè **comprensivi delle imposte sui beni e servizi importati**.

## 22. Le relazioni contabili: le tre equazioni

Da una tavola input-output si ricavano **tre relazioni fondamentali**. Non serve l'algebra: serve capire **che cosa dice ciascuna e in che direzione si legge la tavola**.

> **1. EQUAZIONI DI BILANCIO — si leggono per RIGHE.**
> Evidenziano **come la produzione di una branca (l'offerta totale della branca) si ripartisce fra impieghi intermedi e impieghi finali**.
> *In parole: tutto quello che un settore produce, o lo vendo ad altri settori come input, o finisce nella domanda finale.*
>
> **2. EQUAZIONI DEI COSTI — si leggono per COLONNE.**
> Evidenziano **la struttura dei costi di produzione, comprensiva dei costi dei beni e servizi intermedi e dei costi dei fattori primari**.
> *In parole: tutto quello che un settore incassa, o l'ha speso per comprare input da altri settori, o è andato a remunerare lavoro, capitale e imposte.*
>
> **3. EQUAZIONE DI EQUILIBRIO — combina le due.**
> Per una stessa branca, considerata **allo stesso tempo branca di origine e branca di destinazione**, esprime **l'uguaglianza fra impieghi intermedi e finali della branca (leggendo la tavola per righe) e valore della produzione della medesima branca (leggendo per colonne)**.

**L'aggregazione al sistema.** Sommando le equazioni di equilibrio su tutte le branche si ottiene il **conto di equilibrio di beni e servizi per il complesso delle branche**, che stabilisce:

> **L'uguaglianza fra il valore complessivo delle risorse destinate agli impieghi finali e il valore complessivo delle risorse primarie (incluse le importazioni).**

E sostituendo le componenti della domanda finale, si ottiene l'identità:

> **valore aggiunto + importazioni = consumi + investimenti + variazione scorte + esportazioni**

che il manuale identifica come **il conto economico delle risorse e degli impieghi** — cioè, in sostanza, **l'identità del PIL dal lato dell'offerta e dal lato della domanda**.

> **Il punto da cogliere.** L'input-output **non è un mondo separato dalla contabilità nazionale: ci si salda esattamente**. Sommando le righe si ritrova il PIL dal lato della domanda; sommando le colonne si ritrova il PIL dal lato del valore aggiunto. La tavola è, in un certo senso, **la contabilità nazionale "aperta"** — con dentro tutto ciò che la sintesi aggregata nasconde.

## 23. I coefficienti tecnici e l'ipotesi di tecnologia lineare

Qui sta il salto **dalla contabilità al modello**.

**L'ipotesi fondamentale:**

> Ciò che interessa verificare sono le implicazioni dell'ipotesi che **la quantità di input utilizzata in ogni attività produttiva sia PROPORZIONALE al volume dell'output**. Tale ipotesi è denominata **IPOTESI DI TECNOLOGIA LINEARE**.

Da essa nascono i coefficienti, che sono **il rapporto fra l'input che la branca i fornisce alla branca j e la produzione totale della branca j**:

- **COEFFICIENTI TECNICI**, se i flussi sono espressi **in termini di quantità**: indicano **quante unità fisiche di un bene o servizio derivanti dalla branca i sono necessarie per produrre una unità fisica nella branca j**;
- **COEFFICIENTI DI SPESA**, se i flussi sono espressi **in termini di valore**: indicano **quante unità monetarie di un bene o servizio derivanti dalla branca i sono necessarie per produrre una unità monetaria della branca j**. Generalmente i flussi sono espressi ai prezzi *départ-usine*.

> **Che cos'è davvero un coefficiente tecnico.** È **la ricetta del settore**: dice quanto acciaio, quanta energia, quanti servizi servono per fare un'automobile. Ed è per questo che l'ipotesi di linearità è forte: assume che la ricetta **non cambi con la scala di produzione** — **nessuna economia di scala** — e **non cambi per effetto dei prezzi relativi** — **nessuna sostituzione fra input**. Sono ipotesi restrittive, e vale la pena dirlo in commissione: è ciò che distingue un candidato che ha capito il modello da uno che l'ha imparato.

**Le tre matrici di coefficienti** che si costruiscono:

1. **matrice dei coefficienti di fabbisogno diretto degli input di PRODUZIONE INTERNA** — quadrata, di ordine n×n, con termini non negativi. **Leggendola per colonna si individuano i beni o servizi di produzione interna di cui necessita ciascuna branca**;
2. **matrice dei coefficienti di fabbisogno diretto degli input di IMPORTAZIONE** — anch'essa n×n. **Leggendola per colonna si individuano i beni o servizi di importazione di cui necessita ciascuna branca**;
3. **matrice dei coefficienti di fabbisogno diretto degli INPUT PRIMARI** — rettangolare, di ordine r×n, dove r sono **le componenti del valore aggiunto**. **Leggendola per colonna si individuano gli input primari per ciascuna unità di prodotto.**

## 24. La matrice di Leontief e i coefficienti di attivazione — il risultato centrale

**L'obiettivo:**

> Uno degli obiettivi dell'analisi delle interdipendenze settoriali è **determinare i livelli futuri di produzione sulla base dei livelli noti della domanda finale**, nell'ipotesi di **costanza dei coefficienti**.

Riorganizzando il sistema delle equazioni di bilancio si ottiene una matrice, **[I − a]**, nota come **MATRICE DI LEONTIEF**. Se tale matrice **ammette l'inversa**, è possibile **determinare i livelli di produzione in funzione della domanda finale**.

**L'inversa di Leontief** è la protagonista di tutto il capitolo:

> La matrice **A = [I − a]⁻¹** è nota come **matrice dei coefficienti di fabbisogno DIRETTO E INDIRETTO degli input di produzione interna**, o anche come **MATRICE DEI COEFFICIENTI DI ATTIVAZIONE**, in quanto **il suo generico elemento indica la variazione di produzione della branca i necessaria per soddisfare un incremento UNITARIO di domanda finale della branca j.**

> **Questa è l'idea da portare all'orale, e vale l'intero capitolo.**
>
> *La matrice dei coefficienti tecnici dice quanto un settore compra **direttamente** dagli altri. Ma se aumenta la domanda di automobili, l'industria automobilistica compra più acciaio; l'acciaio, per produrre di più, compra più energia; l'energia compra più servizi — e così via, **all'infinito**. **L'inversa di Leontief somma tutti questi giri**: i suoi elementi sono i **coefficienti di attivazione**, che dicono di quanto deve crescere la produzione di ogni settore perché la domanda finale di un settore cresca di un'unità.*
>
> *In una parola: **i coefficienti di attivazione sono i MOLTIPLICATORI SETTORIALI**. Sono ciò che si usa per stimare quanta produzione, quanto valore aggiunto e quanta occupazione genera un investimento pubblico — a monte e lungo tutta la filiera.*

**Le altre due applicazioni** che il manuale sviluppa in parallelo, con la stessa logica:

- **la matrice dei coefficienti di fabbisogno diretto e indiretto degli input di IMPORTAZIONE**, il cui elemento generico **indica il fabbisogno di importazione di beni e servizi necessari, sia direttamente sia indirettamente, a secondare una domanda finale unitaria** di una branca. È lo strumento con cui si risponde a: *«quanto di questo stimolo alla domanda finisce all'estero invece che nell'economia nazionale?»*;
- **la matrice dei coefficienti di fabbisogno degli INPUT DI RISORSE PRIMARIE**, che **indica ognuna delle componenti del valore aggiunto necessaria a produrre un'unità della domanda finale**. È lo strumento con cui si stima **l'impatto su salari, profitti e gettito fiscale** — e, con opportuni coefficienti di lavoro, **l'impatto occupazionale**.

**Una nota di realismo sulla costruzione delle tavole**, che il manuale dà e che vale la pena riportare: *il procedimento diretto di costruzione di una tavola input-output **non è semplice da applicare**, per cui generalmente **si ricorre a un metodo approssimato**, che muove dai flussi intermedi di una **matrice base di un anno anteriore** e li aggiorna **sulla base delle variazioni subite a causa dei prezzi e di altri fattori**.* Le tavole I-O sono infatti costose e si producono con qualche anno di ritardo.

## 25. Gli indici di integrazione settoriale

La tavola serve anche a **misurare quanto un'economia è integrata**. I primi indici furono proposti da **Chenery e Watanabe**, e sono due, speculari:

> **INDICE DEI COLLEGAMENTI A VALLE (*forward linkage*), w** — misura **la quota di VENDITE di prodotti intermedi sul prodotto totale della branca**.
> - **w alto** → la branca si contraddistingue per **un'elevata incidenza relativa di vendita di output destinato ad usi intermedi** sul totale del venduto: **è una branca a monte della filiera, che alimenta le altre** (energia, materie prime, servizi alle imprese);
> - **w basso** → la branca vende prevalentemente alla domanda finale.
>
> **INDICE DEI COLLEGAMENTI A MONTE (*backward linkage*), u** — misura **la quota di ACQUISTI di prodotti intermedi sul prodotto totale della branca**.
> - **u alto** → la branca **si qualifica come ATTIVITÀ DI TRASFORMAZIONE**: compra molto dagli altri;
> - **u basso** → la branca **si qualifica come ATTIVITÀ PRIMARIA**: produce quasi tutto da sé.

**L'indice sintetico.** Per il sistema economico nel complesso **i due indici coincidono**, e danno un unico indice che **misura il grado di interdipendenza del complesso delle attività economiche**. Questo indice **costituisce il termine di confronto dei due indicatori parziali, i quali si definiscono alti o bassi a seconda del valore assunto rispetto all'indice sintetico**.

> **A che cosa servono davvero.** A individuare i **settori chiave** di un'economia: quelli che hanno **sia collegamenti a monte sia a valle elevati** sono i settori il cui sviluppo trascina l'intero sistema — ed è su questi che una politica industriale, in linea teorica, dovrebbe concentrarsi. È un concetto che si presta bene a una risposta sulla programmazione economica.

**Le tecniche di triangolarizzazione.** Consentono di **misurare il grado di interdipendenza fra settori attribuendo una struttura gerarchica agli stessi ed evidenziando la direzione degli scambi**. L'operazione consiste nello **spostare righe e colonne della matrice in modo da posizionare i coefficienti tendenti a zero al di sopra della diagonale principale**. La triangolarizzazione **si dice perfetta** se, stabilita una struttura gerarchica di tipo lineare, tutti i flussi si collocano da un solo lato della diagonale. Le tecniche si basano sull'esame delle **permutazioni possibili di righe e colonne**, in modo da **rendere massimo il numero dei flussi positivi al di sotto della diagonale principale**.

> **Che cosa significa, in concreto.** Una matrice perfettamente triangolarizzabile descriverebbe **un'economia "a cascata"**: le materie prime alimentano l'industria di base, che alimenta la manifattura, che alimenta i servizi, senza ritorni all'indietro. **Quanto più una matrice reale si discosta da questa forma, tanto più l'economia è circolare e interdipendente.** È una misura della complessità di un sistema produttivo.

## 26. Il modello input-output dei prezzi

La tavola può essere usata non solo per le quantità ma anche **per misurare gli effetti sui prezzi degli output di ciascuna branca a seguito di variazioni dei costi in una data branca**.

**LE QUATTRO IPOTESI DEL MODELLO** — un elenco molto utile, perché espone chiaramente i limiti:

1. **ipotesi di tecnologia lineare**;
2. **ipotesi di costanza dei coefficienti tecnici** che, dice il manuale, **adoperando il linguaggio economico si traduce nell'ASSENZA DI ECONOMIE DI SCALA**;
3. **ipotesi di produzione di un solo prodotto omogeneo da parte di ciascuna branca**;
4. **ipotesi di costanza del prezzo di vendita di un bene o servizio rispetto alla branca acquirente** (nessuna discriminazione di prezzo fra clienti).

**Come funziona.** Il passaggio da una tavola I-O, i cui flussi sono espressi in valore, a un modello economico **richiede di scindere la componente prezzo dalla componente quantità**. Fatto questo, si ottiene una relazione in cui **il prezzo di ciascuna branca dipende dai prezzi degli input che essa acquista e dalla remunerazione dei suoi input primari**. La matrice inversa che ne risulta **identifica gli effetti, sia diretti sia indiretti, del prezzo di una branca sulle altre branche** — l'esatto analogo dei coefficienti di attivazione, ma sui prezzi.

> **L'applicazione concreta è immediata e attualissima:** *quanto si trasmette all'indice generale dei prezzi un rincaro del 20% dell'energia?* Il modello input-output dei prezzi risponde tracciando la propagazione lungo tutte le filiere — **l'energia entra nella chimica, la chimica nella plastica, la plastica negli imballaggi, gli imballaggi negli alimentari**. È lo strumento con cui si stimano gli effetti di secondo impatto di uno shock sui costi.

**Il superamento dell'ipotesi sul valore aggiunto.** Il manuale segnala che **l'ipotesi che il valore aggiunto sia indipendente dai prezzi è stata considerata inaccettabile**, e ne mostra il superamento **scindendo il valore aggiunto nelle sue due componenti: salari e profitti**. Introducendo **il salario unitario, la quantità di lavoro per unità di prodotto, il valore del capitale anticipato e il saggio di profitto**, si ottiene un sistema in cui **i prezzi sono espressi non in funzione del valore aggiunto ma del salario unitario e del saggio di profitto**.

> È un passaggio teoricamente denso che vale la pena nominare, perché **è il punto in cui il modello input-output incontra la teoria della distribuzione**: i prezzi relativi dipendono dalla tecnica *e* dalla ripartizione fra salari e profitti. È l'impostazione di Sraffa, e citarla — anche solo di sfuggita — mostra spessore.

## 27. L'analisi multiregionale

L'ultima estensione del capitolo, e quella più rilevante per un funzionario pubblico italiano.

**La premessa**, che il manuale svolge con una bella frase: *il modello di comunità indipendenti isolate, autosufficienti, **è superato**; al contrario **oggi la regola è quella della comunità dipendente, interconnessa con altre comunità**, che subisce influenze e che a sua volta influenza le scelte economiche di altre.*

**Che cos'è una «regione»:** il termine è da intendersi **in senso lato** e può indicare **entità territoriali di vario ordine**: singole nazioni, gruppi di nazioni, parti di nazioni. L'analisi statistica identifica le regioni **sulla base di criteri di delimitazione prefissati**; in questo contesto per regione si intende **un'area economica integrata**.

**I due modi di evidenziare le interdipendenze regionali:**

- **il primo focalizza l'attenzione su ciascuna regione, considerando tutte le altre come esogene**;
- **il secondo — che è quello che si adotta nella realtà — considera tutte le regioni come parti di un sistema interdipendente**.

**La tavola input-output multiregionale** rappresenta i flussi come **una matrice a blocchi**, in cui **ciascun blocco si riferisce a un'area**. E qui c'è il punto da capire:

> **Gli insiemi di elementi collocati sulla DIAGONALE PRINCIPALE della matrice a blocchi costituiscono le consuete matrici intersettoriali regionali, da cui si rilevano gli scambi INTRA-regionali; tutte le altre matrici rilevano gli scambi INTER-regionali.**

In altre parole: **sulla diagonale c'è ciò che ogni regione produce e consuma al proprio interno; fuori dalla diagonale c'è il commercio fra regioni**.

**I QUATTRO COEFFICIENTI del modello multiregionale**, ciascuno con il proprio significato:

| Coefficiente | Che cosa misura |
|---|---|
| **Coefficiente di scambio INTRA-regionale** | La frazione di input intermedio **della branca i della regione r** sul totale dei beni prodotti **dalla branca j della stessa regione r** |
| **Coefficiente di scambio INTER-regionale** | La frazione di bene o servizio **della branca j della regione r** sul totale della produzione **della branca j della regione s** |
| **Coefficiente di spesa regionale** | L'ammontare di beni o servizi prodotti dalla branca i della regione r, **sia prodotti sia importati**, necessari a produrre **un'unità di prodotto della branca j nella regione s** |
| **Coefficiente di acquisto regionale** (*trading coefficient*) | La frazione di bene o servizio della branca i della regione r **sul totale dei beni provenienti da TUTTE le regioni** attinenti alla branca i e **acquistati dalla branca j della regione s** |

**Le due caratteristiche del modello aperto** che le equazioni devono rispettare:

- **l'esistenza di legami fra interdipendenze di branca e interdipendenze regionali**;
- **la mancanza di identità fra produzione intermedia e domanda intermedia, e fra produzione finale e domanda finale** — cioè: **ciò che una regione produce non coincide con ciò che consuma**, e la differenza è commercio interregionale.

Di conseguenza, nell'equazione di bilancio occorre **distinguere fra regione e branca PRODUTTRICE e regione e branca UTILIZZATRICE**.

> **Perché questo paragrafo vale per il tuo bando.** *Le tavole input-output multiregionali sono lo strumento con cui si valuta **l'impatto territoriale della spesa pubblica**: quando si finanzia un'opera nel Mezzogiorno, quanta parte dell'attivazione produttiva resta nel Mezzogiorno e quanta «risale» verso le regioni che forniscono i beni intermedi? È una domanda su cui si gioca la **politica di coesione**, e la risposta sta esattamente nei coefficienti inter-regionali.* Se colleghi questo alla ripartizione dei fondi strutturali basata sul PIL pro capite regionale (paragrafo 11) e alla valutazione controfattuale delle politiche (econometria, cap. 16), hai costruito un discorso che tiene insieme tre materie del bando.

## 28. Le matrici di contabilità sociale (SAM)

Chiude il capitolo 4 ed è un argomento che vale la pena conoscere perché **è il ponte fra l'analisi produttiva e la distribuzione del reddito**.

**Perché nascono:**

> Lo schema di tavola delle interdipendenze strutturale presentato **non tiene conto delle ulteriori fasi di distribuzione e utilizzazione del reddito**. Per soddisfare una simile esigenza, nella seconda metà del secolo scorso è stata elaborata la **matrice di contabilità sociale — SAM, *Social Accounting Matrix*** — che è **uno schema di interdipendenza economica**.

**A che cosa servono:** *le matrici SAM sono spesso applicate alle analisi delle **interrelazioni fra struttura di un sistema economico e distribuzione e impiego del reddito fra gruppi di famiglie**, intesi come gruppi socio-economici.*

**Che cosa contiene una SAM.** È **una struttura disaggregata che consente di riorganizzare i prospetti della contabilità nazionale e di evidenziare gli effetti di fattori esogeni sul sistema economico**, considerando:

- **attività produttive, prodotti e fattori produttivi** (lavoro e capitale, a loro volta disaggregati);
- **settori istituzionali**: **famiglie** (per quanto concerne la distribuzione del reddito), **imprese** e **Pubblica Amministrazione**;
- **Resto del mondo**.

Il manuale avverte che **la struttura delle SAM non è standardizzata ma è funzionale alle esigenze dell'analisi**.

**La struttura formale.** Una SAM è **una matrice quadrata le cui colonne e righe rappresentano, rispettivamente, le uscite e le entrate degli agenti economici**; il generico elemento rappresenta **un flusso monetario dall'agente j all'agente i**. Continuando a seguire le convenzioni della contabilità a doppia entrata, **la somma delle entrate deve uguagliare la somma delle uscite**, ossia **la somma di riga deve uguagliare la corrispondente somma di colonna**.

**La distinzione fondamentale — conti esogeni e conti endogeni:**

> - Sono **ESOGENI** il **conto del Resto del mondo** e il **conto della formazione del capitale nel breve periodo**;
> - sono **ENDOGENI** il **conto delle Istituzioni**, il **settore delle famiglie** e il **prodotto totale delle differenti attività produttive**.

**Come si usa la SAM:**

> Il sistema socioeconomico rappresentato da una SAM **è affetto da cambiamenti esogeni e *iniezioni***, vale a dire **misure di bilancio operate dalle istituzioni** e **cambiamenti che avvengono nel resto del mondo**, che influiscono non solo sulle esportazioni ma anche sulla dimensione degli investimenti privati. **Gli effetti, diretti e indiretti, di questi cambiamenti sui conti endogeni sono stimati dal MODELLO DEI MOLTIPLICATORI CONTABILI.**

**I moltiplicatori contabili globali.** Con lo stesso meccanismo algebrico visto per l'inversa di Leontief, si ottiene **la matrice dei moltiplicatori contabili globali**, che:

> **Consente di valutare gli effetti, diretti e indiretti, SUI REDDITI DI OGNI GRUPPO DI OPERATORI che derivano da un'immissione nei conti esogeni.**

> **La differenza fra input-output e SAM, in una frase da dire all'orale.**
>
> *La tavola input-output dice **quanta produzione** genera una spesa pubblica, settore per settore. La SAM dice **a chi va il reddito** che quella produzione genera: quanto ai salari e quanto ai profitti, quanto alle famiglie povere e quanto a quelle ricche, quanto allo Stato in forma di gettito. **È lo strumento con cui si valuta l'impatto DISTRIBUTIVO di una politica economica**, e non solo quello aggregato.*
>
> È un collegamento fortissimo con **scienza delle finanze** (effetti redistributivi dell'intervento pubblico) e con **valutazione delle politiche pubbliche** (chi vince e chi perde da una misura).

---

# PARTE V — L'ANALISI DEI CONSUMI

*(Capitolo 5 del manuale, pp. 622-632)*

## 29. Consumo e reddito: l'impostazione

**Perché il consumo è la variabile centrale:**

> Il consumo rappresenta **la componente più importante della domanda aggregata** e costituisce **la variabile fondamentale nei modelli esplicativi e interpretativi delle fluttuazioni del reddito**.

**L'analisi si divide in due parti**, e la distinzione è chiara:

- **la prima riguarda la decisione del consumatore sulla quota di reddito da spendere (C) e quella da risparmiare (S)**: è l'identità **Y = C + S**;
- **la seconda riguarda il modo in cui il consumatore suddivide la spesa totale fra i vari beni e servizi disponibili**.

## 30. La funzione di consumo keynesiana

**L'impostazione di Keynes (1936):**

> Vi è **una stretta relazione fra reddito e consumo**, nel senso che **all'aumentare del reddito aumenta anche il consumo**. La somma che la collettività spende in consumi **dipende in parte dall'ammontare del suo reddito, in parte da altre circostanze oggettive concomitanti, in parte dai bisogni soggettivi e dalle propensioni e abitudini psicologiche degli individui che la compongono**.

**La vera novità dell'analisi keynesiana**, che il manuale sottolinea come tale:

> Aver evidenziato che **all'aumentare del reddito la spesa per consumi NON aumenta nella stessa proporzione**, in quanto, **una volta soddisfatti i bisogni primari, le famiglie tenderanno ad accrescere la quota di reddito risparmiata**. Ciò spiega, secondo l'economista, **la sistematica inferiorità della domanda aggregata rispetto all'offerta aggregata.**

> È da qui che discende l'intero impianto keynesiano: se la domanda è strutturalmente insufficiente, **l'equilibrio di piena occupazione non è automatico**, e serve un intervento pubblico che colmi il divario. Vale la pena dirlo, perché collega statistica economica ed economia politica in una frase sola.

## 31. La legge di Engel — da sapere con gli esempi

Gli studi sulla relazione fra reddito e consumo risalgono **al XIX secolo**, quando lo statistico tedesco **Ernst Engel**, analizzando le spese di consumo delle famiglie in relazione al loro reddito, definì quella che è nota come **legge di Engel**:

> **Tanto più una famiglia è povera, tanto maggiore è la quota di reddito destinata all'acquisto di beni di prima necessità**, come i generi alimentari.

**Le tre categorie di beni** che ne discendono, con gli esempi del manuale:

| Categoria | Comportamento rispetto al reddito | Esempi |
|---|---|---|
| **Beni di prima necessità** | Al crescere del reddito la spesa **aumenta MENO che proporzionalmente**: «oltre una certa soglia, se una famiglia vede raddoppiare il proprio reddito difficilmente raddoppierà anche il consumo di questi beni» | **il pane, il latte** |
| **Beni INFERIORI** | Presentano addirittura **una relazione INVERSA rispetto al reddito**: disponendo di maggiori risorse, le famiglie **cessano di consumarli**, preferendo beni di qualità superiore | **la polenta, le patate** consumate in sostituzione della carne; oggi, **tagli di carne di bassa qualità** |
| **Beni SUPERIORI o di LUSSO** | Oltre certi livelli di reddito, **l'aumento della domanda è PIÙ CHE proporzionale** rispetto all'aumento del reddito | **le automobili**, **le spese per il tempo libero** |

> **Il collegamento tecnico che vale la pena fare.** Le tre categorie si distinguono esattamente per **il valore dell'elasticità del consumo rispetto al reddito**: **inferiore a 1 e positiva** per i beni necessari, **NEGATIVA** per i beni inferiori, **superiore a 1** per i beni di lusso. La legge di Engel non è un'osservazione empirica isolata: **è una classificazione basata su un indicatore statistico preciso**.
>
> E c'è un'applicazione concreta che una commissione apprezza: **la quota di spesa alimentare sul totale dei consumi è usata come indicatore di povertà relativa** — è il cosiddetto *coefficiente di Engel*. Più è alta, più la popolazione è povera.

## 32. Le fonti statistiche

**Le tre fonti** che il manuale elenca per l'analisi dei consumi:

1. **le serie storiche della contabilità nazionale** (capitolo 2);
2. **le indagini sui bilanci familiari**, che consentono di evidenziare **quanto spendono le famiglie per i singoli consumi**;
3. i ***consumer panel*** — una fonte «che si va diffondendo negli ultimi anni»: **campioni di consumatori permanenti e rappresentativi che forniscono in via continuativa informazioni dettagliate sui loro acquisti di beni di largo consumo**, attraverso società specializzate. Queste dispongono di **efficaci sistemi di raccolta dati — lettori ottici, agende di acquisto — per ogni unità campionaria**, e sono quindi in grado di **registrare ogni prodotto acquistato e le corrispondenti caratteristiche**.

> **Nota, perché è un ottimo collegamento con data science.** Un *consumer panel* è, tecnicamente, **un dato panel** nel senso del capitolo 15 di econometria: stesse unità osservate nel tempo. E la raccolta tramite lettori ottici è **un caso di dato generato automaticamente** — il passaggio dalle indagini campionarie tradizionali ai *big data* transazionali. È esattamente la trasformazione che sta attraversando la statistica ufficiale, che usa sempre più **fonti amministrative e *scanner data*** al posto delle rilevazioni sul campo.

**Le difficoltà di rilevazione**, che il manuale segnala con onestà:

> **La rilevazione dei redditi familiari presenta molte difficoltà**, per cui nelle indagini correnti **si rinuncia ad acquisire tali dati a favore delle sole spese familiari**. È ovvio che **la divergenza rispetto alle analisi basate sul reddito dipende dall'entità del risparmio familiare**.

E una precauzione tecnica: **per eliminare l'effetto della diversa composizione delle famiglie** — dato l'alto grado di correlazione fra tale grandezza e il reddito familiare — **si considerano sia i consumi PRO CAPITE sia il reddito PRO CAPITE**.

Infine, l'avvertenza di realismo: *il consumo di un dato settore **non è influenzato solo dal reddito** ma da numerosi altri fattori — **il prezzo del bene, il prezzo dei generi sostitutivi** — dai quali si prescinde per evitare costi elevati nelle rilevazioni e tempi lunghi.*

## 33. Le tre grandezze fondamentali

Qui sta il nucleo tecnico del capitolo, e sono **tre concetti che vanno saputi con precisione**, perché tornano in economia politica e in econometria.

### 33.1 Propensione marginale al consumo

> La **propensione marginale al consumo** misura **la variazione dei consumi indotta da una variazione di un'unità (monetaria) di reddito disponibile, supponendo un immutato livello dei prezzi**.

**Il ragionamento sul suo valore**, che il manuale svolge in tre passi:

1. all'aumentare del reddito **si ha un incremento dei consumi**: ΔY > 0 → ΔC > 0;
2. **a livelli di reddito più alti l'incremento dei consumi sarà proporzionalmente inferiore**: 0 < ΔC < ΔY;
3. **da cui: 0 < ΔC/ΔY < 1**.

> **In altri termini, la PROPENSIONE MARGINALE AL CONSUMO ASSUME VALORI COMPRESI FRA 0 E 1.**

### 33.2 Propensione media al consumo

> La **propensione media al consumo** è data dal **rapporto fra i consumi totali di una collettività e il reddito complessivamente disponibile** in un dato intervallo di tempo. **Misura la quota di reddito destinata al consumo per ogni unità monetaria di reddito.**

### 33.3 Elasticità del consumo rispetto al reddito

> L'**elasticità del consumo rispetto al reddito** è definita dal **rapporto fra la variazione RELATIVA della spesa globale per l'acquisto di beni e servizi e la variazione RELATIVA del reddito**, e vale: **0 < E(Y) < 1**.

**La relazione fra le tre**, che è il risultato da ricordare perché unifica il paragrafo:

> **ELASTICITÀ = PROPENSIONE MARGINALE / PROPENSIONE MEDIA**

Poiché per Keynes la propensione marginale è minore della propensione media (si consuma meno di quanto mediamente si consumi, all'aumentare del reddito), **l'elasticità risulta minore di 1** — che è esattamente la legge di Engel espressa in formula.

**La formula logaritmica.** Si dimostra facilmente che l'elasticità è uguale al **rapporto fra la derivata logaritmica della funzione di consumo e la derivata logaritmica del reddito**; passando da variazioni infinitesime a variazioni finite, diventa **il rapporto fra il logaritmo del rapporto dei consumi in due istanti successivi e il logaritmo del rapporto dei redditi negli stessi istanti**.

**L'esempio del manuale**, che è semplice e vale la pena saper rifare a mente: con **Y** che passa da 1.930 a 2.050 (+6,2%) e **C** da 700 a 735 (+5%), l'elasticità è **0,81** — il consumo cresce meno del reddito, coerentemente con la teoria.

> **Il collegamento con econometria.** L'elasticità come **rapporto di derivate logaritmiche** è esattamente ciò che rende il **modello doppio-logaritmico** (cap. 8 della Parte III) così utile: in quel modello **il coefficiente È l'elasticità**, costante lungo tutta la curva. E infatti, come si vedrà al paragrafo 35, la funzione di consumo doppio-logaritmica è proprio quella a elasticità costante.

## 34. I vincoli che ogni funzione di consumo deve rispettare

Prima di elencare le forme funzionali, il manuale fissa **tre vincoli** che ogni modello deve soddisfare. Sono un ottimo esempio di **come la teoria economica disciplini la specificazione statistica**:

1. **la propensione marginale deve essere compresa fra 0 e 1**;
2. **l'elasticità del consumo rispetto al reddito deve essere compresa fra 0 e 1**;
3. **la funzione deve riferirsi ad aggregati espressi a PREZZI COSTANTI**. Gli aggregati sono esprimibili anche a prezzi correnti, **ma in tal caso si deve introdurre l'indice dei prezzi come ulteriore variabile del modello**.

## 35. Le sei forme funzionali

Il manuale presenta sei funzioni di consumo, ciascuna con propensioni ed elasticità. **Non serve memorizzare le formule**: serve **riconoscere che cosa caratterizza ciascuna**. Questa tabella è il modo più efficiente di studiarle.

| Funzione | Caratteristica distintiva |
|---|---|
| **LINEARE** — C = β₀ + β₁Y | **La propensione marginale al consumo è COSTANTE**, qualunque sia il livello di spesa totale; **l'elasticità tende all'unità** al crescere del reddito. È la funzione keynesiana elementare: β₀ è la componente autonoma, β₁ la propensione marginale, con 0 < β₁ < 1 |
| **IPERBOLICA** — C = β₀ − β₁/Y | Per le sue proprietà matematiche **consente di evidenziare il LIVELLO DI SATURAZIONE β₀** (asintoto orizzontale); **la propensione marginale è inversamente proporzionale al QUADRATO del reddito totale**. È la forma adatta ai beni di prima necessità, che tendono a un tetto |
| **SEMILOGARITMICA** — C = β₀ + β₁ log Y | **La propensione marginale è inversamente proporzionale al reddito totale.** Il manuale la definisce **«fondamentale per l'analisi keynesiana in quanto presume un livello di spesa iniziale sempre positivo»** |
| **SIGMOIDALE** — log C = β₀ − β₁/Y | **Passa per l'origine**, che è un suo punto limite, e **presenta un asintoto orizzontale che delimita il livello di saturazione**. **L'elasticità è inversamente proporzionale al reddito** |
| **DOPPIO-LOGARITMICA** — log C = β₀ + β₁ log Y | **PRESENTA ELASTICITÀ COSTANTE**, pari a β₁. È la forma che si usa quando si vuole stimare direttamente l'elasticità |
| **Funzione di LESER** — C = β₀ + β₁Y + β₂ log Y | La sua caratteristica è **«presentare elevata adattabilità per valori eccezionali del reddito (o spesa) totale»**: cioè si comporta bene anche alle code della distribuzione |

> **Come si sceglie la forma.** Il manuale è realistico: *il problema della specificazione **non è sempre risolvibile dall'osservazione del diagramma a dispersione dei dati empirici**, ma, grazie all'esperienza dello statistico, **è di facile soluzione**.* È un'ammissione onesta: la scelta della forma funzionale ha una componente di giudizio.
>
> E per la stima: *i metodi più utilizzati sono senza dubbio **il metodo dei minimi quadrati e il metodo della massima verosimiglianza***. Le funzioni non lineari si affrontano **linearizzandole** con i logaritmi — esattamente la procedura vista nel capitolo 8 di econometria.

## 36. Le funzioni a variabili ritardate e le teorie alternative

### 36.1 La funzione a variabili ritardate

> Una funzione del consumo a variabili ritardate presume che **il consumo al tempo t sia funzione non solo del reddito corrente, ma anche del reddito ritardato** di una o più unità temporali.

**E qui c'è la distinzione da sapere**, perché è economicamente rilevante:

> - **il coefficiente del reddito CORRENTE è la PROPENSIONE MARGINALE AL CONSUMO DI BREVE PERIODO**, e misura **l'effetto a breve termine di una variazione unitaria del reddito corrente, supposto immutato il reddito passato**;
> - **la SOMMA di tutti i coefficienti è la PROPENSIONE MARGINALE AL CONSUMO DI LUNGO PERIODO**, e misura **l'effetto a lungo termine di una variazione unitaria di tutti i redditi**.

**Una proprietà utile:** *l'influenza delle variabili ritardate **è meno significativa col passare del tempo**, nel senso che i coefficienti **sono di norma decrescenti e sono generalmente rappresentati dai termini di una progressione geometrica decrescente**.* È esattamente la struttura di un modello a **ritardi distribuiti geometricamente**.

Il modello si può estendere sostituendo al reddito ritardato **le abitudini al consumo** — introducendo cioè **il consumo del periodo precedente** fra le variabili esplicative. È il modello di *habit persistence*, che cattura l'idea che le abitudini di spesa siano vischiose.

### 36.2 La teoria del reddito permanente di Friedman

> Secondo la **teoria del reddito permanente**, dovuta all'analisi dell'economista statunitense **Milton Friedman**, la domanda di beni di consumo **è composta da due parti**: una, **PERMANENTE**, **è stabile**; l'altra, **FLUTTUANTE o TRANSITORIA**, **dipende dalla congiuntura**.

**Il meccanismo:**

- il **consumo permanente** è **funzione del REDDITO PERMANENTE**, cioè **del flusso di reddito goduto stabilmente nel passato e che ci si attende per l'avvenire**;
- il consumo permanente **rappresenta i beni di consumo non durevoli e i servizi dei beni di consumo durevoli**;
- **Friedman suggerisce di esprimere il reddito permanente come MEDIA ARITMETICA PONDERATA DEI REDDITI PASSATI, CON PESI DECRESCENTI GEOMETRICAMENTE.**

**Il risultato teorico centrale**, e va detto perché è il punto della teoria:

> Nella teoria del reddito permanente **la propensione marginale al consumo è UGUALE alla propensione media al consumo**. Da ciò discende che **l'ELASTICITÀ del consumo permanente rispetto al reddito permanente è UGUALE ALL'UNITÀ.**

> **Perché questo è importante, e come dirlo.** *Keynes prevede che la propensione media al consumo **diminuisca** al crescere del reddito, e quindi che l'elasticità sia minore di uno. Friedman dice l'opposto: rispetto al **reddito permanente**, la propensione media **è costante** e l'elasticità **è esattamente uno**. La discrepanza empirica — la propensione media sembra calare nei dati trasversali ma è stabile nelle serie storiche di lungo periodo — **si spiega proprio con la componente transitoria**: chi in un dato anno ha un reddito eccezionalmente alto risparmia la parte transitoria, e appare quindi come un "gran risparmiatore" anche se la sua propensione permanente è normale.*
>
> È il **paradosso di Kuznets** e la sua soluzione. Saperlo raccontare in trenta secondi, senza formule, è esattamente il tipo di risposta che distingue.

**La chiusura realistica del manuale:** *è difficile definire il modello «migliore» di funzione del consumo; una decisione coerente consiste **nell'estendere l'analisi sia alla rappresentazione grafica dei dati sia agli strumenti tipici dell'inferenza statistica**, che si muovono dalla stima dei parametri alla **valutazione della conformità del modello ai dati empirici**.*

---

# PARTE VI — L'ANALISI DEL MERCATO DEL LAVORO

*(Capitolo 6 del manuale, pp. 633-636)*

Capitolo breve ma **ad altissima probabilità d'esame**, per due ragioni: le definizioni sono precise e verificabili, e il mercato del lavoro è **il terreno per eccellenza delle politiche pubbliche valutabili**.

## 37. Le definizioni ufficiali — da sapere alla lettera

Questa è la parte da memorizzare con precisione assoluta, perché **sono definizioni statistiche armonizzate a livello europeo** e una commissione può chiederle testualmente.

**La popolazione si divide in due categorie:**

### 37.1 Popolazione ATTIVA (o forza lavoro)

> **Pari alla somma degli OCCUPATI e delle PERSONE IN CERCA DI OCCUPAZIONE.**

**Gli OCCUPATI** sono **le persone di 15 anni e più** che, nella settimana di riferimento, soddisfano **almeno uno** dei seguenti requisiti:

1. **hanno svolto almeno UN'ORA di lavoro** in una qualsiasi attività che preveda **un corrispettivo monetario o in natura**;
2. **hanno svolto almeno un'ora di lavoro NON RETRIBUITO nella ditta di un familiare** nella quale collaborano abitualmente;
3. **sono assenti dal lavoro** ma **l'assenza non supera i tre mesi**, oppure **durante l'assenza continuano a percepire almeno il 50% della retribuzione**.

**Le PERSONE IN CERCA DI OCCUPAZIONE (o disoccupati)** comprendono **le persone non occupate fra 15 e 74 anni** che:

1. **sono state alla ricerca di un lavoro nei TRENTA giorni che precedono l'intervista** **e** **si dichiarano disponibili a lavorare entro le DUE SETTIMANE successive** all'intervista;
2. oppure **inizieranno un lavoro entro tre mesi dalla data dell'intervista** **e** **si dichiarano disponibili a lavorare entro le due settimane successive**, se possibile per anticipare l'inizio del lavoro.

### 37.2 Popolazione INATTIVA (o non forza lavoro)

> **Composta da coloro che NON sono in età lavorativa (perché minori di 15 anni) e da coloro che, PUR ESSENDO in età lavorativa, NON SONO ALLA RICERCA di un'occupazione** — come **le casalinghe, gli studenti e i benestanti**.

> **I tre punti che fanno la differenza in commissione, e che vanno detti spontaneamente:**
>
> 1. **Basta UN'ORA di lavoro nella settimana di riferimento per essere classificati occupati.** È un criterio internazionale (ILO) che serve alla comparabilità, ma che **rende il tasso di occupazione insensibile alla qualità e alla quantità del lavoro**. È la ragione per cui accanto ad esso si guardano le **unità di lavoro equivalenti a tempo pieno (ULA)** e il **tasso di sottoccupazione**.
> 2. **La disoccupazione statistica richiede TRE requisiti simultanei**: non lavorare, **aver cercato attivamente** negli ultimi 30 giorni, **essere disponibili** entro due settimane. Chi non cerca perché scoraggiato **non è disoccupato: è inattivo**. Questo è cruciale: **nelle recessioni una parte della disoccupazione "scompare" statisticamente perché si trasforma in inattività** (l'effetto *scoraggiamento*), e il tasso di disoccupazione può paradossalmente migliorare mentre l'economia peggiora.
> 3. **Le classi d'età sono diverse**: gli occupati sono **15 anni e più** (senza limite superiore), i disoccupati **15-74 anni**. Notarlo dimostra attenzione.

## 38. I tre tassi fondamentali

Sono **rapporti statistici** — nel senso del paragrafo 3 — e vanno saputi con il denominatore esatto, perché **è il denominatore a distinguerli**:

> **TASSO DI ATTIVITÀ = forza lavoro / popolazione in età lavorativa**
> *Quanta parte della popolazione in età da lavoro si presenta sul mercato.*
>
> **TASSO DI OCCUPAZIONE = occupati / popolazione in età lavorativa**
> *Quanta parte della popolazione in età da lavoro effettivamente lavora.*
>
> **TASSO DI DISOCCUPAZIONE = disoccupati / FORZA LAVORO**
> *«La percentuale degli appartenenti alla forza lavoro che non lavorano».*

> **L'errore da non fare mai, ed è una trappola classica.** **Il tasso di disoccupazione ha al denominatore la FORZA LAVORO, non la popolazione.** Gli altri due hanno al denominatore la popolazione in età lavorativa. Confonderli porta a conclusioni sbagliate, perché **un tasso di disoccupazione basso può convivere con un tasso di occupazione bassissimo** se molte persone sono inattive — che è esattamente **il caso italiano**, e in particolare quello del Mezzogiorno e dell'occupazione femminile. Se in commissione fai questa osservazione, hai detto la cosa più intelligente che si possa dire sul mercato del lavoro italiano.

## 39. Le determinanti del tasso di attività

Il tasso di attività **dipende da molti fattori di natura demografica, sociale e culturale**. Il manuale segnala che **molti Paesi industrializzati, fra cui l'Italia, hanno registrato un progressivo calo del tasso di attività**, e ne elenca **quattro cause** — due che lo abbassano e due che lo alzano:

| Fattore | Effetto sul tasso di attività |
|---|---|
| **Progressivo invecchiamento della popolazione** — per effetto dell'allungamento della vita media | **↓** Cresce la popolazione inattiva e diminuisce la forza lavoro |
| **Prolungamento della durata media degli studi** da parte dei giovani, che ritardano l'ingresso sul mercato | **↓** Stesso effetto |
| **Crescita dell'occupazione femminile** e conseguente riduzione del numero di casalinghe | **↑** Progressivo aumento della forza lavoro |
| **Immigrazioni**, costituite prevalentemente da giovani attivamente alla ricerca di un'occupazione | **↑** Aumento della forza lavoro |

## 40. Flussi e durata della disoccupazione

Un paragrafo che merita attenzione, perché introduce **una visione dinamica** che va oltre la fotografia dei tassi.

**I flussi.** Osservando il mercato del lavoro in un intervallo di tempo **si registrano ampi movimenti in entrata e in uscita dalla disoccupazione**:

- **flussi di ENTRATA**: chi **aveva un'occupazione e l'ha persa**; chi **entra per la prima volta nel mercato del lavoro**; **gli immigrati in cerca di lavoro**;
- **flussi di USCITA**: chi **trova lavoro**; ma anche chi **ritorna a far parte della popolazione non attiva** (giovani disoccupati che riprendono gli studi, donne che decidono di dedicarsi al lavoro casalingo); chi **emigra all'estero**; **i deceduti**.

**La relazione fondamentale:**

> **Tanto più intenso è il flusso d'entrata, tanto più è elevato il tasso di disoccupazione, che al contrario si riduce quando aumentano i flussi in uscita. Se il tasso di disoccupazione è stabile, significa che i flussi in entrata e in uscita si compensano perfettamente.**

**La durata.** Il tasso di disoccupazione è influenzato **anche dalla durata della disoccupazione**, cioè **dal tempo durante il quale un individuo, in media, si trova nella condizione di disoccupato**. Il manuale fa un'osservazione fine:

> Questa durata **non corrisponde necessariamente al tempo occorrente per trovare un'occupazione**, perché **si esce dalla condizione di disoccupato non solo perché si trova lavoro, ma anche per altre ragioni.**

**Le tre determinanti della durata:**

1. **le fasi del ciclo economico**: il tempo medio **può essere breve nelle fasi di espansione, molto lungo nelle fasi di recessione**. Quando **la permanenza nella condizione supera un anno** si parla di **DISOCCUPAZIONE DI LUNGA DURATA**;
2. **la flessibilità del mercato del lavoro**: nei Paesi europei, che presentano in genere **una maggiore regolamentazione** rispetto ad altri sistemi (gli Stati Uniti), **la durata è di solito maggiore** — e questo **vale soprattutto per i giovani che si affacciano per la prima volta sul mercato**;
3. **la normativa sociale a favore dei disoccupati**: la presenza di **sussidi di disoccupazione o altre forme di sostegno di una certa entità potrebbe disincentivare gli individui ad accettare qualsiasi occupazione venga loro offerta, prolungando la durata media**. Inoltre, **quando l'ammontare dei sussidi non è molto inferiore al reddito percepito lavorando, le imprese possono essere più disposte a sospendere i lavoratori in presenza di un calo temporaneo della domanda, per riassumerli in momenti più favorevoli**.

Il manuale aggiunge però un correttivo di realismo: **questi effetti sono poco determinanti per i Paesi, come l'Italia, in cui l'entità del sussidio di disoccupazione è del tutto irrilevante**.

> **Il collegamento con la valutazione delle politiche.** Questo è **letteralmente** il terreno su cui si applicano i metodi del capitolo 16 di econometria. La domanda «i sussidi di disoccupazione allungano la durata della disoccupazione?» è una domanda **causale**, non descrittiva, e si risponde con un **RDD** su una soglia di accesso al sussidio, o con un **DiD** su una riforma che ha cambiato le regole. L'esempio norvegese di **Kostøl e Mogstad (2014)** studiato in econometria riguarda **esattamente questo tema**. Se colleghi i due capitoli, la risposta diventa molto forte.

## 41. I tre tipi di disoccupazione

**La teoria economica distingue generalmente fra tre tipi**, e questa tripartizione è quasi certamente una domanda d'esame:

### 41.1 Disoccupazione FRIZIONALE

> Una **condizione momentanea** di disoccupazione che si crea **a seguito dello squilibrio fra flussi di entrata e flussi di uscita dal mercato del lavoro**. Può accadere che sul mercato vi siano, **contemporaneamente, posti di lavoro liberi da un lato e disoccupati dall'altro**: ciò dipende dal fatto che **il mercato del lavoro non funziona in modo perfetto e automatico ma presenta alcune FRIZIONI**.

In qualunque momento si stimi il tasso di disoccupazione, vi saranno **lavoratori in attesa di passare da un'occupazione a un'altra**, **persone che cercano un'occupazione migliore**, **individui temporaneamente inattivi perché in attesa di iniziare un'attività**.

> **Il dato da ricordare: il tasso di disoccupazione frizionale può variare da Paese a Paese ma generalmente si stima che sia COMPRESO FRA IL 2 E IL 5%.**

È la ragione per cui **la piena occupazione non significa disoccupazione zero**: una quota frizionale è fisiologica e perfino desiderabile, perché segnala un mercato in cui le persone si muovono.

### 41.2 Disoccupazione CICLICA (o congiunturale)

> È considerata **disoccupazione di BREVE PERIODO** e si determina **quando la domanda complessiva di lavoro è scarsa perché il momento congiunturale è sfavorevole**. Si manifesta soprattutto **nelle fasi di recessione economica**, quando **la domanda di beni e servizi è bassa, le imprese riducono la produzione e quindi anche l'occupazione ne risente**.

**LA LEGGE DI OKUN** — da sapere con il numero, perché è precisa e citabile:

> Dal nome dell'economista americano che studiò **la relazione empirica esistente fra crescita reale e variazioni della disoccupazione**: **ogni diminuzione del PIL di circa il 2-2,5% rispetto al suo valore potenziale comporta un aumento del tasso di disoccupazione dell'1%.**

> **Perché la legge di Okun è un bell'esempio da portare all'orale.** È **una regolarità empirica, non un teorema**: è stata *stimata* econometricamente su serie storiche, e il suo coefficiente **varia fra Paesi e fra epoche** a seconda della rigidità del mercato del lavoro. È quindi un esempio perfetto di che cosa fa l'econometria: **misura una relazione che la teoria suggerisce ma non quantifica**. E si collega direttamente al concetto di **PIL potenziale** e di ***output gap***, che sono le grandezze su cui si fonda la **regola di spesa del nuovo Patto di stabilità europeo** — argomento di contabilità pubblica.

### 41.3 Disoccupazione STRUTTURALE

> È **quella più grave e più difficile da eliminare**, perché **colpisce interi settori industriali o aree geografiche di un Paese** e si manifesta **con squilibri STABILI E PERMANENTI fra domanda e offerta di lavoro**. In questi casi, **anche se paradossalmente il salario fosse pari a zero, l'offerta di lavoro risulterebbe comunque eccedente rispetto alla domanda.**

**Gli esempi del manuale**, tutti italiani e tutti spendibili: **l'industria siderurgica**, **il settore agricolo**, e — «per alcuni aspetti» — **la disoccupazione esistente nel Mezzogiorno**.

**Le due cause**, che sono opposte fra loro:

- **l'introduzione di tecniche produttive *labour saving***, che **sostituiscono i lavoratori con le macchine**, come accade con l'automazione dei processi produttivi;
- **al contrario**, **insufficienti livelli di investimento**, con conseguente **basso impiego di lavoro in alcuni settori produttivi**.

> **La distinzione che conta per le politiche, e che vale la pena esplicitare.** *Alla disoccupazione **ciclica** si risponde con **politiche di sostegno della domanda aggregata** — è il terreno keynesiano. Alla disoccupazione **strutturale** le politiche di domanda non servono a nulla: serve **politica industriale, formazione, riqualificazione, mobilità territoriale**. Alla disoccupazione **frizionale** servono **servizi per l'impiego efficienti**, cioè migliore incontro fra domanda e offerta. **Confondere il tipo di disoccupazione significa sbagliare la politica**, ed è il motivo per cui la diagnosi statistica viene prima dell'intervento.*

## 42. La rilevazione ISTAT sulle forze di lavoro

Il paragrafo più «istituzionale» del capitolo, e quindi uno di quelli che conviene saper esporre bene.

**Il contesto generale:** i dati su occupazione e disoccupazione **sono prodotti dagli Istituti di Statistica dei Paesi attraverso indagini compiute presso un campione di famiglie, normalmente a cadenza trimestrale**, e sono considerati «molto importanti per valutare lo stato di salute generale di un'economia», in quanto **le variazioni del tasso di disoccupazione sono spesso considerate come segnali di caduta o di ripresa** di un sistema economico.

**La «Rilevazione sulle forze di lavoro» dell'ISTAT** — i dettagli da sapere:

| Elemento | Dato |
|---|---|
| **Base giuridica** | **Regolamento (CE) 577/98** del Consiglio dell'Unione europea, che fissa **criteri armonizzati a livello europeo** |
| **Natura** | Indagine **campionaria** su **un campione ponderato di famiglie** |
| **Continuità** | **Dal 2004 è CONTINUA**: le informazioni sono raccolte **in tutte le settimane dell'anno** e non più in una singola settimana per trimestre |
| **Diffusione** | I risultati **continuano a essere diffusi con cadenza TRIMESTRALE** |
| **Dimensione del campione** | **Oltre 250 mila famiglie** residenti in Italia ogni anno, per un totale di **circa 600 mila individui**, distribuite in **circa 1.400 comuni** |
| **Oggetto della domanda** | Quale sia stata **l'attività lavorativa nella «settimana di riferimento»** |
| **Chi è intervistato** | **Tutti i componenti della famiglia selezionata in età da lavoro**, ossia **quelli che hanno superato i 15 anni** |

> **Perché il passaggio alla rilevazione continua nel 2004 è una finezza che vale la pena citare.** Rilevare **una sola settimana per trimestre** significa esporsi a **effetti di calendario e a shock casuali di quella specifica settimana**; distribuire la rilevazione **su tutte le 52 settimane** produce una stima molto più robusta e **permette una destagionalizzazione corretta** — il che chiude il cerchio con TRAMO-SEATS e il capitolo 14 di econometria. È un esempio concreto di **come il disegno campionario determini la qualità dell'indicatore**.

---

# PARTE VII — MISURE DELLA PRODUZIONE E DELLA PRODUTTIVITÀ

*(Capitolo 7 del manuale, pp. 637-648)*

L'ultimo capitolo della materia, e quello più vicino all'economia politica. Contiene la **funzione di produzione**, la **Cobb-Douglas**, gli **indicatori di produttività** e la **funzione di Solow**.

## 43. La funzione di produzione

**La definizione:**

> La **funzione di produzione** indica **la MASSIMA quantità di prodotto (*output*) che è possibile ottenere in una data unità di tempo attraverso una data combinazione di fattori produttivi (*input*)** immessi nel processo di produzione nella stessa unità di tempo: materie prime, capitale, lavoro.

Nota la parola **massima**: la funzione di produzione descrive la **frontiera dell'efficienza tecnica**, non la produzione effettiva. È una precisazione che conviene fare.

**Le due ipotesi semplificatrici** su cui la specificazione è fondata:

- **ipotesi di SOSTITUIBILITÀ dei fattori**;
- **ipotesi di INFINITA DIVISIBILITÀ dei fattori e dei prodotti**.

Grazie a esse **la funzione risulta continua e ammette derivate parziali del primo e del secondo ordine continue** — cioè è matematicamente trattabile.

**L'aggregazione.** Poiché **è praticamente impossibile includere nella funzione di produzione tutte le variabili che effettivamente riguardano un processo produttivo**, generalmente **si fa riferimento ai soli fattori CAPITALE e LAVORO**, e si scrive **Y = F(K, L)**.

## 44. Produttività marginale, media e saggio marginale di sostituzione

**PRODUTTIVITÀ MARGINALE di un input.** È **la derivata parziale della funzione rispetto a quell'input** e misura:

> La **variazione infinitesima del prodotto conseguente a una variazione infinitesima di un input, MANTENENDO COSTANTI GLI ALTRI INPUT**.

- la **produttività marginale del CAPITALE** misura la variazione di output conseguente a una variazione dei servizi dell'input capitale, **supposto l'input lavoro costante**. **Graficamente è il coefficiente angolare della funzione di produzione Y = F(K)**;
- la **produttività marginale del LAVORO** misura la variazione di output conseguente a una variazione dei servizi dell'input lavoro, **supposto l'input capitale costante**. **Graficamente è il coefficiente angolare della funzione Y = F(L)**.

**PRODUTTIVITÀ MEDIA.** È **il rapporto fra la quantità di prodotto totale e la quantità di ciascun fattore produttivo impiegato**, e misura **il prodotto per unità di capitale** e **il prodotto per unità di lavoro**.

**SAGGIO MARGINALE DI SOSTITUZIONE TECNICA (MRST).** È **il rapporto fra i prodotti marginali dei fattori**, e

> **Definisce il grado di sostituibilità dei fattori della produzione**, ossia **la variazione infinitesima dell'input lavoro a seguito della variazione infinitesima dell'input capitale, MANTENENDO COSTANTE IL LIVELLO DELL'OUTPUT.**

**Il suo limite**, e il motivo per cui serve un'altra grandezza: *il saggio marginale di sostituzione tecnica **è una grandezza che dipende strettamente dalle unità di misura delle variabili considerate**; per questo ad esso **si preferisce un numero puro**, nella fattispecie **l'elasticità di sostituzione**.*

È lo stesso principio già incontrato al paragrafo 3 a proposito dei rapporti statistici: **si preferisce sempre un numero puro a una grandezza dimensionale**, perché è confrontabile.

**ELASTICITÀ DI SOSTITUZIONE.** Premessa: per **INTENSITÀ DI CAPITALE** si intende **l'incidenza del fattore capitale nel processo produttivo in rapporto al grado di utilizzo degli altri fattori**, cioè il rapporto **K/L**. L'elasticità di sostituzione:

> **Rappresenta le variazioni dell'intensità di capitale al variare dei prezzi relativi**, ossia **indica in quale proporzione si sostituisce il fattore lavoro con il fattore capitale al crescere del prezzo relativo del lavoro rispetto a quello del capitale.**

Il manuale aggiunge il ponte con la teoria economica: **poiché in regime di concorrenza perfetta i prezzi dei fattori uguagliano le rispettive produttività marginali**, l'elasticità di sostituzione si può riscrivere in funzione del saggio marginale di sostituzione tecnica.

## 45. I rendimenti di scala

> I **rendimenti di scala** indicano **la relazione esistente fra una variazione degli input impiegati e la corrispondente variazione dell'output**. Mostrano **che cosa accade al livello della produzione quando TUTTI i fattori produttivi variano nella STESSA proporzione**, e consentono di capire **se il processo produttivo diviene più o meno efficiente al crescere della scala produttiva**.

**I tre casi**, con le spiegazioni economiche che il manuale dà — e che sono la parte che conviene saper raccontare:

| Tipo | Che cosa accade | Perché |
|---|---|---|
| **COSTANTI** | **L'output varia nella stessa proporzione degli input**: raddoppiando tutti i fattori, la produzione raddoppia | — |
| **CRESCENTI** | **L'output varia in misura PIÙ che proporzionale**: raddoppiando i fattori la produzione, per esempio, triplica. «La crescita della dimensione di impresa risulta in tal caso vantaggiosa» | **Alcune tecniche produttive possono essere utilizzate solo se la produzione è elevata**; inoltre **in un'impresa più grande il lavoro può essere diviso su un numero maggiore di lavoratori e ciascuno può SPECIALIZZARSI in una particolare mansione** |
| **DECRESCENTI** | **L'output varia in misura MENO che proporzionale**: raddoppiando i fattori, l'output aumenta meno del doppio | **Incrementare la scala della produzione equivale ad aumentare le difficoltà di GESTIONE E DI ORGANIZZAZIONE** |

> Nota che le ragioni dei rendimenti crescenti sono **tecniche e organizzative** (indivisibilità degli impianti, divisione del lavoro), mentre quelle dei rendimenti decrescenti sono **manageriali**. È una distinzione che vale la pena fare, perché mostra che i rendimenti di scala non sono un fatto puramente matematico.

## 46. La massimizzazione del profitto: i due regimi di mercato

Il manuale distingue due situazioni, ed è un passaggio che collega statistica e microeconomia.

**In concorrenza perfetta** sia dei prodotti sia dei fattori — **quindi con prezzi predeterminati** — l'imprenditore sceglie gli input **in modo da massimizzare il profitto, rappresentato dalla differenza fra ricavi e costi**. Le quantità ottimali si trovano **ponendo uguali a zero le derivate parziali della funzione di profitto**; il risultato economico, noto dalla microeconomia, è che **ciascun fattore va impiegato fino al punto in cui il valore della sua produttività marginale eguaglia il suo prezzo**.

**In assenza di concorrenza perfetta** i prezzi **devono essere considerati variabili ENDOGENE, poiché con la propria azione un imprenditore può influire sulle condizioni di mercato**. Il problema si riformula:

> Supposto che siano dati il livello di prodotto, il prezzo del prodotto e i prezzi dei fattori, **MASSIMIZZARE IL PROFITTO EQUIVALE A MINIMIZZARE I COSTI dei fattori di produzione sotto il vincolo della funzione di produzione.**

È un **problema di minimo condizionato**, che si risolve **ricorrendo al metodo dei MOLTIPLICATORI DI LAGRANGE** — «una particolare tecnica che consente di massimizzare o minimizzare una funzione sottoposta a determinati vincoli». Il manuale spiega anche il ruolo del moltiplicatore: **per evitare che modifichi il valore della funzione obiettivo, è necessario che il suo intervento sia nullo, ma che comunque tenga conto del vincolo**.

## 47. La funzione di produzione aggregata: dal micro al macro

Un passaggio metodologico che vale la pena riportare perché **è esattamente ciò che distingue la statistica economica dalla microeconomia**:

> L'analisi statistica studia **fenomeni di massa**, ossia **fenomeni che interessano una collettività**, più che fenomeni concernenti singoli individui, imprese, stabilimenti. Sotto una serie di ipotesi semplificatrici è possibile **trasporre i concetti da un contesto MICROeconomico a uno MACROeconomico, considerando il sistema delle imprese come un unico aggregato**. Si tratta di **funzioni aggregate di produzione**, in grado di **descrivere il comportamento dell'intero sistema economico nazionale o di suoi settori**.

**I tre compiti dell'analisi statistica** una volta individuata la relazione: **la specificazione della forma funzionale**, **la misura delle variabili** e **la stima dei parametri**.

**I DUE PROBLEMI** che il manuale segnala, e che sono onesti e istruttivi:

**1. Il progresso tecnico.** *A complicare la scelta di una specifica forma è **il progresso tecnico incalzante**, che **implica mutamenti nelle produttività, cui consegue un mutamento nei parametri** che compaiono nella funzione.* **La soluzione proposta: inserire la variabile tempo**, in modo da **limitare la validità della funzione prescelta a uno specifico intervallo temporale**.

**2. La misurazione dei fattori.** *Altro problema rilevante consiste nella **scelta e quantificazione di fattori della produzione non facilmente misurabili**.*

**Le fonti dei dati e i loro problemi** — questo passaggio è molto utile perché mostra il lavoro concreto dello statistico economico:

| Variabile | Come si misura | Problema |
|---|---|---|
| **PRODOTTO** | Flusso di beni e servizi prodotti in un dato intervallo, espresso in **unità fisiche omogenee**. I dati sono forniti dalla **contabilità nazionale** (prodotto lordo o netto) | Essendo espresso **in termini di valore**, **deve essere DEFLAZIONATO ricorrendo a indici di prezzo** — il che rimanda al capitolo 3 |
| **LAVORO** | Due tipologie di dati dalle statistiche ufficiali: **le unità fisiche di lavoratori occupati a una certa data** (dati cross section), oppure **il numero di ORE LAVORATE** in un dato intervallo | Le due misure non sono equivalenti: le ore catturano anche l'intensità dell'impiego, le teste no |
| **CAPITALE** | Si dovrebbe considerare **l'entità dei SERVIZI resi dal fattore**; tuttavia **si fa riferimento a stime dello STOCK di capitale espresso a prezzi costanti** | **Questo metodo NON tiene conto della diversa vita residua dei beni** — un impianto nuovo e uno quasi obsoleto contano ugualmente |

> **È un ottimo esempio da citare sul divario fra concetto teorico e misura statistica.** La teoria parla di *servizi del capitale*; la statistica misura lo *stock di capitale*, perché è l'unica cosa osservabile. Questo **scarto fra ciò che si vorrebbe misurare e ciò che si può misurare** è il problema centrale della statistica economica, e saperlo nominare vale molto in commissione.

## 48. La funzione di produzione Cobb-Douglas

> Esistono diverse elaborazioni della funzione di produzione, ma **la più utilizzata è quella proposta dall'economista Douglas e dal matematico Cobb**.

Il manuale ne dà **due formulazioni: una STATICA e una DINAMICA**.

### 48.1 Formulazione statica e le sue proprietà

> **Y = a · L^α · K^β**

dove **a > 0 è una costante di dimensione** — che **scompare se le tre variabili sono espresse sotto forma di indici** — e **indica in che misura l'attività produttiva è efficiente**, nel senso che **misura la scala della produzione**.

**LE SEI PROPRIETÀ**, che vanno sapute perché ciascuna è un possibile spunto di domanda:

**1. È omogenea di grado α + β.** Moltiplicando ciascun fattore per una costante reale positiva t, **la produzione risulta moltiplicata per t^(α+β)**. Di conseguenza:

> **LA SOMMA α + β MISURA I RENDIMENTI DI SCALA:**
> - **α + β = 1** → gli elementi produttivi variano tutti nella stessa proporzione → **rendimenti di scala COSTANTI**;
> - **α + β > 1** → **rendimenti di scala CRESCENTI**;
> - **α + β < 1** → **rendimenti di scala DECRESCENTI**.

**2. Le produttività marginali** dei due fattori si ottengono derivando rispetto a ciascuno di essi.

**3. Il saggio marginale di sostituzione tecnica** risulta proporzionale al rapporto **K/L**.

**4. Le elasticità dei fattori** — la proprietà più importante:

> α e β sono **i rapporti fra produttività marginale e produttività media** di ciascun fattore, e **rappresentano la VARIAZIONE PERCENTUALE del livello di output conseguente a una variazione percentuale unitaria dell'input** di lavoro e di capitale rispettivamente.
>
> Precisamente: **α (o β) indica di quanto aumenta o diminuisce in percentuale Y quando, a parità di prestazioni di K (o L), quelle di L (o K) aumentano o diminuiscono nella misura dell'1%.**

**5. Le quote di prodotto.** Qui il manuale sviluppa un risultato teorico importante:

> Se la funzione è **omogenea di grado 1** — quindi **in presenza di rendimenti di scala costanti** — e si è **in regime di concorrenza perfetta**, allora, **ricorrendo al TEOREMA DI EULERO**, si ottiene che **le quote ASSOLUTE di prodotto che competono a ciascun fattore sono PROPORZIONALI al prodotto**, mentre **le quote RELATIVE sono COSTANTI**.
>
> E soprattutto: **LE QUOTE RELATIVE DI PRODOTTO, PER CIASCUN FATTORE, SONO UGUALI ALLE CORRISPONDENTI ELASTICITÀ DEI FATTORI.**

> **Perché questo risultato è notevole, e come dirlo.** *In una Cobb-Douglas a rendimenti costanti e in concorrenza perfetta, **il parametro α non è solo un'elasticità tecnica: è la QUOTA DEL PRODOTTO CHE VA AL LAVORO**, e β la quota che va al capitale. Il che significa che **stimando una funzione di produzione si stima anche la distribuzione del reddito fra salari e profitti**, e che quella distribuzione risulta **costante** — indipendente dalla scala e dai prezzi.*
>
> *È un risultato storicamente importantissimo — la «costanza della quota dei salari» fu a lungo considerata un fatto stilizzato dell'economia — e **oggi è messo in discussione**, perché la quota del lavoro sul PIL è in calo in quasi tutti i Paesi avanzati da decenni. È esattamente il tipo di osservazione che, portata in commissione, mostra di aver capito il modello e non solo di averlo imparato.*

**6. L'elasticità di sostituzione è uguale all'unità.** È **la caratteristica distintiva della Cobb-Douglas** e anche il suo principale limite: impone che la sostituibilità fra capitale e lavoro sia sempre esattamente unitaria, il che è un'assunzione forte. È la ragione per cui esistono forme funzionali più generali (la CES, a elasticità di sostituzione costante ma non necessariamente pari a 1).

**7. La linearizzazione** — il punto operativo:

> **Si ottiene facilmente ricorrendo ai LOGARITMI: log Y = log a + α log L + β log K.**
>
> Grazie alle serie storiche di prodotto, capitale e lavoro, **l'espressione così ottenuta consente la stima dei parametri attraverso il metodo dei MINIMI QUADRATI.**

> **Il collegamento con econometria è diretto e vale la pena farlo.** Questa è **esattamente** la procedura studiata al capitolo 8 della Parte III: una funzione **non lineare ma LINEARIZZABILE**, che con i logaritmi diventa una **regressione multipla doppio-logaritmica** stimabile con OLS, **i cui coefficienti sono direttamente le elasticità**. E l'ipotesi di rendimenti costanti (α + β = 1) **è un vincolo lineare sui parametri, testabile con un test F**. Le due materie qui non si limitano a toccarsi: raccontano la stessa cosa da due lati.

### 48.2 Formulazione dinamica

> Una formulazione di tipo dinamico **tiene conto delle conseguenze di un PROGRESSO TECNICO**, rappresentate da **aumenti autonomi di efficienza tecnologica** — cioè **aumenti di efficienza dei fattori dovuti a invenzioni tecnologiche, a riqualificazioni delle forze di lavoro**. Essi sono sintetizzati, generalmente, **da un termine di trend, che può essere ESPONENZIALE**.

Si ottiene così **Y = a · L^α · K^β · e^(λt)**, dove **λ è l'elasticità della produzione rispetto al tempo**.

**Con l'ulteriore ipotesi di rendimenti di scala costanti** (α + β = 1), e introducendo **il prodotto per unità di lavoro (Pul), y = Y/L**, e **l'intensità di capitale, k = K/L**, si ottiene una forma che esprime **la produttività del lavoro in funzione dell'intensità di capitale e del tempo**. È la forma che si userà nel paragrafo sulla funzione di Solow.

**La critica.** Il manuale riporta anche un'obiezione: *la visione esposta è stata criticata soprattutto in considerazione del fatto che **l'ammodernamento delle condizioni di produzione, consentendo l'utilizzo delle macchine, ha determinato un rapporto di impiego dei fattori COSTANTE**, nel senso che **un mutamento nella loro utilizzazione finirebbe per comportare un cambiamento nell'intero processo produttivo**.* È, in sostanza, la critica alla sostituibilità continua fra fattori: in molti processi reali la tecnica è a **coefficienti fissi**, e cambiare il rapporto capitale/lavoro significa cambiare impianto, non regolare una manopola.

## 49. Gli indicatori di produttività

**La definizione generale:**

> In generale, la **produttività** di un sistema produttivo o di un suo settore è **il rapporto fra il RISULTATO ottenuto dall'attività produttiva e i FATTORI PRODUTTIVI impiegati**.

**Il problema della misura**, che il manuale espone bene: *matematicamente due grandezze possono essere rapportate solo se **espresse nella medesima unità di misura**. L'ideale sarebbe esprimere numeratore e denominatore **in unità fisiche omogenee**, ma, **trattandosi di grandezze per natura diverse, si ricorre ai concetti di valore**.* Le variabili si considerano quindi **a prezzi costanti**, ottenuti moltiplicando le quantità per i prezzi di un'epoca assunta come base.

**LA CLASSIFICAZIONE** — da sapere perché è netta:

> - **PRODUTTIVITÀ PARZIALE** — calcolata **considerando un solo fattore, mantenendo immutati gli altri**. A sua volta si distingue in **GENERICA** e **SPECIFICA**;
> - **PRODUTTIVITÀ GLOBALE** — **considera tutti i fattori CONGIUNTAMENTE**.

### 49.1 Produttività parziale generica

> È data dal **rapporto fra il VALORE A PREZZI COSTANTI della produzione in un dato intervallo temporale e il VOLUME o la QUANTITÀ di fattore (lavoro o capitale) impiegato** nella produzione.

**I due indicatori e i loro nomi ufficiali:**

- **PUL — PRODOTTO PER UNITÀ DI LAVORO**: la produttività parziale generica del lavoro;
- **PUC — PRODOTTO PER UNITÀ DI CAPITALE**: la produttività parziale generica del capitale.

**Come si costruisce il Pul**, in concreto: **al numeratore il VALORE AGGIUNTO TOTALE del periodo**; **al denominatore il numero complessivo di ORE LAVORATE** — oppure, in alternativa, **il numero totale di persone occupate**. Rapportando il Pul del tempo corrente a quello del tempo base si ottiene **l'INDICE DI PRODUTTIVITÀ PARZIALE GENERICA DEL LAVORO**.

> **Il Pul è il numero che fa discutere l'Italia da vent'anni.** La stagnazione della produttività del lavoro italiana rispetto agli altri Paesi europei è **il** tema della politica economica nazionale, ed è misurata esattamente così. Saper dire che cos'è il Pul e come si costruisce — valore aggiunto su ore lavorate, a prezzi costanti — è una risposta molto solida.

### 49.2 Produttività parziale specifica

> È data dal **rapporto fra la QUOTA DEL VALORE della produzione atta a REMUNERARE il fattore e il valore o la quantità di fattore impiegato** nel processo.

Per l'input lavoro, **al numeratore** entrano:

- **il REDDITO DA LAVORO DIPENDENTE**, costituito dalle **retribuzioni lorde e dai contributi sociali effettivi e/o figurativi**;
- **il REDDITO DA LAVORO AUTONOMO**, che **può essere calcolato stimando il reddito medio da lavoro attribuibile a ogni lavoratore indipendente** — «che, spesso, si presume uguale a quello dei lavoratori dipendenti appartenenti allo stesso settore di attività» — **e moltiplicandolo per il numero degli indipendenti**.

**Al denominatore**, **il reddito complessivo, facilmente determinabile dai conti economici del Paese**.

> **Nota metodologica interessante.** L'imputazione del reddito da lavoro autonomo per analogia con i dipendenti dello stesso settore è **una convenzione statistica necessaria** — il reddito degli autonomi non si osserva separatamente da quello del capitale — **ma è anche una fonte di incertezza**, particolarmente rilevante in un Paese come l'Italia dove la quota di lavoro autonomo è fra le più alte d'Europa. È il tipo di dettaglio che dimostra di aver letto e non sfogliato.

### 49.3 Produttività globale dei fattori

> È data dal **rapporto fra il valore della produzione e il valore di TUTTI i fattori impiegati** nel processo.

**Come si costruisce in pratica.** Teoricamente dovrebbe tener conto di tutti i fattori; nella pratica, sulla base di ipotesi semplificatrici, si aggregano due grandezze:

- il **CAPITALE MATERIALE**, considerato come **stock di ricchezza di capitale materiale**. Ai fini del calcolo si considerano **prevalentemente beni durevoli quali impianti, macchinari**. L'aggregazione **è complessa in quanto si tratta di beni non omogenei**: si suppone allora di **suddividere lo stock in gruppi di beni omogenei**, e **la somma dei prodotti del numero di unità di ciascun gruppo per i rispettivi prezzi** dà il valore dello stock;
- il **CAPITALE UMANO**, considerato come **stock di ricchezza di capitale umano**, il cui valore **è più facile da stimare**: si ottiene dalla **somma dei prodotti del numero di lavoratori di ciascuna qualifica per il valore medio unitario dei lavoratori con quella qualifica**.

**Il meccanismo dell'indice.** Indicando con **α e β le quote di reddito spettanti rispettivamente al lavoro e al capitale** (con β = 1 − α), si definiscono:

- la **produttività specifica del capitale umano**, che **indica il reddito percepito per ogni unità monetaria di capitale umano utilizzato**;
- la **produttività specifica del capitale materiale**, che **indica il reddito percepito per ogni unità monetaria di capitale materiale utilizzato**.

Poiché **il prodotto netto si ripartisce fra lavoro e capitale**, si può definire **un REDDITO TEORICO (POTENZIALE) al tempo corrente**, ottenuto **facendo variare SOLO il numero di unità di lavoro e di capitale impiegate** — cioè **mantenendo ferma la produttività**. E allora:

> **L'INDICE DELLA PRODUTTIVITÀ GLOBALE è il rapporto fra il prodotto netto EFFETTIVAMENTE realizzato e quel reddito teorico.**
>
> Equivalentemente, si ottiene come **rapporto fra l'INDICE DI VOLUME DELLA PRODUZIONE e l'INDICE DI VOLUME DEI FATTORI.**

> **L'idea, detta in modo semplice:** *si calcola quanto si sarebbe prodotto **impiegando i fattori nella quantità osservata oggi ma con l'efficienza di ieri**; il confronto con la produzione effettiva **isola il guadagno di efficienza**. La produttività globale è quindi, per costruzione, **ciò che resta della crescita una volta sottratto il contributo dell'aumento dei fattori**.* È esattamente il concetto che il paragrafo successivo formalizza con Solow.

## 50. La funzione di produzione di Solow e il residuo

L'ultimo paragrafo del manuale, e la chiusura naturale della materia.

**Che cosa fa:**

> La funzione di produzione di **Solow** consente di stabilire **in che misura la variazione nel tempo della produttività media del lavoro sia dovuta:**
> - **all'AUMENTO DI CAPITALE PER UNITÀ DI LAVORO**, che comporta **uno spostamento LUNGO la funzione di produzione**;
> - **oppure al PROGRESSO TECNICO**, che comporta **uno spostamento VERSO L'ALTO della funzione di produzione.**

> **Questa distinzione geometrica — LUNGO la curva contro VERSO L'ALTO — è il cuore dell'intero paragrafo, ed è il modo migliore di esporlo.** *Se un'economia produce di più per lavoratore, può essere perché **ha dato a ciascun lavoratore più macchine** (movimento lungo la curva: è **capital deepening**), oppure perché **con le stesse macchine e gli stessi lavoratori riesce a produrre di più** (spostamento della curva: è **progresso tecnico**). **Solo la seconda è crescita sostenibile nel lungo periodo**, perché la prima incontra i rendimenti decrescenti del capitale.*

**La forma della funzione.** Si scrive **Y = F(K, L, T)**, dove **si è inserita la variabile temporale T per rappresentare il mutamento che la funzione subisce nel tempo a causa del progresso tecnico**.

### 50.1 Il progresso tecnico neutrale

**La definizione, che è precisa e va saputa:**

> Il progresso tecnico si dice **NEUTRALE** se **le trasposizioni della funzione di produzione dovute al progresso tecnico LASCIANO INALTERATO IL SAGGIO MARGINALE DI SOSTITUZIONE fra i fattori.**

Cioè: il progresso tecnico **aumenta la produttività di entrambi i fattori nella stessa misura**, senza favorire il capitale a scapito del lavoro o viceversa. È un'ipotesi comoda ma forte, e vale la pena notarlo: **se il progresso tecnico fosse *labour saving*, la neutralità cadrebbe** — ed è esattamente la questione che si pone oggi con l'automazione e l'intelligenza artificiale.

**La forma analitica:** si scrive **Y = A(t) · F(K, L)**, dove **A(t) è un fattore da stimare e rappresenta gli effetti, nel tempo, di tutti i mutamenti conseguenti al progresso tecnico**.

### 50.2 La scomposizione della crescita

Il manuale svolge il passaggio tecnico, che si può riassumere così senza formule:

> Ipotizzando una **F(K, L) di tipo Cobb-Douglas di grado α + β = 1** — quindi **lineare omogenea** — e un **mercato di concorrenza perfetta**, in cui **le elasticità dei fattori coincidono con le loro quote di prodotto α e β**, si ottiene, in termini di differenze finite:
>
> **(variazione % del progresso tecnico) = (variazione % del prodotto) − β · (variazione % del capitale) − α · (variazione % del lavoro)**

**Introducendo poi il prodotto per unità di lavoro (y = Y/L) e l'intensità di capitale (k = K/L)**, la relazione si semplifica ulteriormente:

> **(variazione % del progresso tecnico) = (variazione % del Pul) − β · (variazione % dell'intensità di capitale)**

> **QUESTO È IL RESIDUO DI SOLOW, e va nominato così.** *Il progresso tecnico **non si misura direttamente**: si ottiene **per differenza**, sottraendo alla crescita della produttività del lavoro la parte spiegata dall'aumento di capitale per addetto. È per questo che si chiama **residuo**, ed è anche per questo che è stato definito ironicamente **«la misura della nostra ignoranza»**: contiene tutto ciò che non sappiamo attribuire ai fattori misurati — tecnologia, ma anche qualità delle istituzioni, efficienza organizzativa, capitale umano non misurato, ed errori di misura.*
>
> È una chiusura perfetta per la materia, perché mostra che **la statistica economica misura per differenza ciò che non sa osservare direttamente** — ed è consapevole di farlo.

### 50.3 L'indice del progresso tecnico e la funzione ridotta

**Come si costruisce l'indice:**

> La funzione **A(t) è definita INDICE DEL PROGRESSO TECNICO** e può essere ottenuta, **anno per anno, attraverso un procedimento ricorrente** in cui, **partendo da un anno base e ponendo A(0) = 1**, il valore per l'anno successivo si ottiene applicando la variazione relativa calcolata.

**La funzione ridotta di produzione** — l'ultima definizione del manuale:

> Ottenuto per ogni anno il valore dell'indice del progresso tecnico, **il rapporto, anno per anno, fra i valori osservati del Pul, desunti da serie storiche, e l'indice del progresso tecnico, dà luogo alla cosiddetta FUNZIONE RIDOTTA DI PRODUZIONE**, la cui specifica forma funzionale **dipende dall'andamento assunto dai dati empirici** e **il cui significato è quello di misurare l'incremento del prodotto per unità di lavoro PRESCINDENDO DALL'EFFETTO DEL PROGRESSO TECNICO.**

> **Come chiudere una risposta su questo capitolo.** *La funzione di produzione di Solow permette di rispondere alla domanda più importante della politica economica di lungo periodo: **la nostra economia cresce perché accumula, o perché innova?** La prima strada si esaurisce, per i rendimenti decrescenti del capitale; la seconda no. **La misurazione statistica del residuo è quindi il modo in cui si diagnostica la sostenibilità di un modello di crescita** — ed è la ragione per cui la stagnazione della produttività totale dei fattori in Italia è considerata il problema economico strutturale del Paese.*

---

# PARTE VIII — LE DODICI FORMULE FONDAMENTALI

Come per econometria, le raccolgo qui perché tu possa valutarle in blocco. In questa materia però le formule sono **poche e quasi tutte semplici**: sono rapporti, non derivazioni. Il giudizio su ciascuna è esplicito.

## Le sei da sapere davvero

**1. Il rapporto statistico**
> **R = x / y**

*Che cosa dice:* consente il confronto fra due fenomeni **eliminando l'effetto dell'unità di misura**, dando luogo a **numeri puri**. Le differenze, al contrario, restano espresse nell'unità di misura originaria.
**★★★ Il concetto, non la formula.** È la premessa di tutta la materia.

**2. L'indice dei prezzi di LASPEYRES**
> **L = Σ pₙ q₀ / Σ p₀ q₀** — si pondera con le **quantità dell'anno BASE**

*Che cosa dice:* **quanto costa oggi il paniere che si acquistava all'inizio.** È **a ponderazione fissa**, quindi facile da calcolare e con un solo sistema di quantità da rilevare. **È l'indice usato dall'ISTAT** per NIC, FOI, IPCA, indice della produzione industriale e IPAB.
**★★★ Indispensabile.** Se ricordi una sola formula di tutta la materia, questa.

**3. L'indice dei prezzi di PAASCHE**
> **P = Σ pₙ qₙ / Σ p₀ qₙ** — si pondera con le **quantità dell'anno CORRENTE**

*Che cosa dice:* **quanto sarebbe costato all'inizio il paniere che si acquista oggi.** È **a ponderazione variabile**: più aggiornato e fedele, ma costoso, perché richiede di rilevare le quantità ogni volta.
**★★★ Indispensabile**, e va ricordata **insieme** a Laspeyres, perché **la differenza fra le due è il contenuto**.

**4. L'indice di FISHER**
> **F = √(L × P)** — **media geometrica di Laspeyres e Paasche**

*Che cosa dice:* è il **«numero indice ideale»** perché **soddisfa quasi tutte le proprietà formali, tranne la transitività**. Non si usa nella pratica **perché non ha un significato economico diretto**.
**★★ Facile, tanto vale saperla.**

**5. Il deflatore implicito**
> **Deflatore = (valore a prezzi correnti / valore a prezzi costanti) × 100**

*Che cosa dice:* è **l'indice dei prezzi che emerge implicitamente** dal confronto fra nominale e reale. **Serve a depurare gli aggregati dall'inflazione** e a calcolare i tassi di crescita delle grandezze reali. Il **deflatore del PIL** è il caso più importante.
**★★★ Indispensabile.**

**6. I tre tassi del mercato del lavoro**
> **Tasso di ATTIVITÀ = forza lavoro / popolazione in età lavorativa**
> **Tasso di OCCUPAZIONE = occupati / popolazione in età lavorativa**
> **Tasso di DISOCCUPAZIONE = disoccupati / FORZA LAVORO**

*Che cosa dicono:* il denominatore **è ciò che li distingue**. Attenzione: **solo il tasso di disoccupazione ha al denominatore la forza lavoro.**
**★★★ Indispensabili, e vanno sapute con il denominatore esatto.**

## Le tre da conoscere

**7. Le tre grandezze del consumo**
> **Propensione MARGINALE = ΔC / ΔY** (compresa fra 0 e 1)
> **Propensione MEDIA = C / Y**
> **ELASTICITÀ = propensione marginale / propensione media** (compresa fra 0 e 1)

*Che cosa dicono:* la marginale è **quanto si consuma dell'ultimo euro guadagnato**; la media è **la quota di reddito consumata**; l'elasticità è **di quanto varia percentualmente il consumo per una variazione percentuale del reddito**.
**★★ Utili**, soprattutto la relazione fra le tre.

**8. La funzione Cobb-Douglas**
> **Y = a · L^α · K^β**, linearizzabile come **log Y = log a + α log L + β log K**

*Che cosa dice:* **α e β sono le elasticità** dei fattori; **la loro somma misura i rendimenti di scala** (= 1 costanti, > 1 crescenti, < 1 decrescenti); in concorrenza perfetta e a rendimenti costanti **coincidono con le quote distributive**. L'elasticità di sostituzione è **sempre pari a 1**.
**★★★ per il collegamento con econometria**, dove la stessa funzione si stima con OLS in forma doppio-logaritmica.

**9. Il Pul e il residuo di Solow**
> **Pul = valore aggiunto / ore lavorate** (a prezzi costanti)
> **variazione % del progresso tecnico = variazione % del Pul − β · variazione % dell'intensità di capitale**

*Che cosa dicono:* il **Pul** è la produttività del lavoro; il **residuo di Solow** è **ciò che resta della sua crescita una volta sottratto il contributo dell'aumento di capitale per addetto**.
**★★ Il concetto è importante**, la formula no.

## Le tre da lasciar perdere (ma di cui sapere il nome)

**10. L'inversa di Leontief** — **A = [I − a]⁻¹**. Da sapere solo che **i suoi elementi sono i COEFFICIENTI DI ATTIVAZIONE**, che indicano **di quanto deve crescere la produzione di ogni settore perché la domanda finale di un settore cresca di un'unità** — cioè **i moltiplicatori settoriali**. ★ Il concetto, non l'algebra.

**11. Gli indici di Chenery-Watanabe** — l'indice **w** dei collegamenti **a valle** (quota di vendite intermedie) e l'indice **u** dei collegamenti **a monte** (quota di acquisti intermedi). Servono a individuare **i settori chiave** dell'economia. ★ Il concetto.

**12. I metodi di comparazione spaziale** — **EKS** (media geometrica di tutti i confronti indiretti, garantisce la **transitività**), **Geary-Khamis** (prezzi medi internazionali, anch'esso transitivo), **Gerardi** (aggiunge l'**additività**). ★ I nomi e a che cosa servono, niente di più.

---

# PARTE IX — QUARANTACINQUE DOMANDE D'ORALE CON TRACCIA DI RISPOSTA

Le **dieci contrassegnate con ►** sono quelle a più alta probabilità.

## Numeri indici (Parte I)

1. **Che cos'è la statistica economica?** — Il ramo della **statistica applicata** il cui contributo alla costruzione di **modelli rappresentativi ed esplicativi del sistema macroeconomico** è stato fondamentale. Si distingue dalla **statistica metodologica**, che è la parte teorica.
2. ► **Qual è il ruolo dell'ISTAT?** — **Ente pubblico di ricerca sottoposto alla vigilanza della Presidenza del Consiglio dei ministri**, con autonomia scientifica, statutaria, regolamentare, organizzativa, finanziaria, patrimoniale e contabile. Quattro compiti: **censimenti generali**, **indagini del programma statistico nazionale**, **indirizzo e coordinamento del SISTAN**, **partecipazione al sistema statistico europeo e internazionale**.
3. **Che cosa sono i rapporti statistici e perché si usano?** — Consentono di **confrontare intensità o frequenze di due fenomeni**, eliminando **l'effetto dell'unità di misura** e producendo **numeri puri**. Quattro tipi: **composizione, densità, durata, ripetizione** (questi ultimi due sono l'uno il reciproco dell'altro).
4. **Come si classificano i numeri indici?** — **Temporali / spaziali**; **semplici (elementari) / complessi (ponderati)**, e questi ultimi in **sintetici** (combinazione di indici semplici) e **composti** (combinazione di sintetici). Gli indici semplici sono **a base fissa** o **a base mobile (concatenati)**.
5. **Quali proprietà devono avere i numeri indici?** — **Identità, reversibilità delle basi, reversibilità dei fattori** (l'indice di valore è il prodotto dell'indice dei prezzi per quello delle quantità), **transitività (circolarità)**. Per i sintetici si aggiungono **commensurabilità, determinatezza, proporzionalità**.
6. ► **Qual è la differenza fra Laspeyres e Paasche?** — **Laspeyres pondera con le quantità dell'anno base** ed è quindi **a ponderazione fissa**: agevola il calcolo, richiede un solo sistema di quantità, ed è **il metodo dell'anno base**. **Paasche pondera con le quantità correnti**: è **più aggiornato e fedele ma comporta costi di rilevazione elevati**, ed è **il metodo dell'anno dato**. **L'ISTAT usa Laspeyres**, per la costanza nel tempo del paniere. Aggiungi che **entrambi non rispettano reversibilità delle basi, transitività e decomposizione delle cause**.
7. **Che cos'è l'indice di Fisher e perché non si usa?** — La **media geometrica di Laspeyres e Paasche**, detta **numero indice ideale** perché soddisfa quasi tutte le proprietà formali **tranne la transitività**. Non si usa perché **negli indici di Laspeyres e Paasche compaiono grandezze che hanno precisi significati economici**, mentre Fisher è solo una media.
8. ► **Quali indici dei prezzi al consumo calcola l'ISTAT?** — Tre: **NIC** (intera collettività, misura l'inflazione dell'intero sistema economico), **FOI** (famiglie di operai e impiegati, **usato per adeguare affitti e assegni**), **IPCA** (armonizzato, **creato da EUROSTAT per la comparabilità europea**, inviato mensilmente a EUROSTAT che elabora l'indice sintetico europeo). Tutti calcolati **con la formula di Laspeyres**, con **paniere e pesi aggiornati annualmente e tenuti fissi per l'anno**. Classificazione **ECOICOP** (Reg. UE 2016/792), **12 divisioni di spesa** e oltre **1.700 prodotti elementari**.
9. **Che cosa misura l'indice della produzione industriale?** — **La variazione nel tempo del volume fisico della produzione dell'industria in senso stretto, escluse le costruzioni**. Rilevazione **campionaria** su **circa 4.600 imprese**, **base 2015 = 100**, classificazione **Ateco 2007**, sintesi con **formula di Laspeyres**, e **destagionalizzato** dall'ISTAT.

## Contabilità nazionale e SEC (Parte II)

10. ► **Che cos'è la contabilità nazionale?** — Una **tecnica di sintesi statistica** che descrive l'attività economica di un Paese **attraverso un quadro contabile coerente**, avendo per oggetto **i flussi economici e finanziari fra gruppi di operatori e le consistenze finali dei beni reali e finanziari**, e determinando parametri come **PIL e Reddito nazionale**.
11. **Che cos'è il circuito economico?** — La rappresentazione dei **flussi di prodotti, redditi e capitali** fra i soggetti. Nello schema elementare, famiglie e imprese si scambiano **beni e servizi** su un mercato e **fattori produttivi** sull'altro; la spesa delle une è il ricavo delle altre. Formalizzato per la prima volta da **Quesnay nel *Tableau économique* (1758)**.
12. ► **A che cosa servono concretamente i conti nazionali?** — A calcolare quattro indicatori con effetti giuridici e finanziari diretti: **deficit/PIL e debito/PIL** (parametri di Maastricht), **Reddito nazionale lordo** (contributo al bilancio UE), **PIL pro capite regionale** (fondi strutturali), **variazione trimestrale del PIL** (politica monetaria).
13. **Che cos'è il SEC e qual è la sua cronologia?** — Lo **schema di riferimento per la misurazione dell'attività economica e finanziaria**. **1970**: EUROSTAT lo mette a punto; **1974**: adottato da tutti i Paesi membri, Italia inclusa; **1996**: Reg. CE 2223, coerenza con lo SNA dell'ONU; **1999**: tutti gli Stati adottano il **SEC 95**; **Reg. UE 549/2013**, in vigore **dal 2014**: **SEC 2010**.
14. ► **Quali sono le principali novità del SEC 2010?** — **La capitalizzazione delle spese in R&S** (l'innovazione più significativa: da consumo intermedio a investimento, **contribuiscono al PIL**); **le spese per armamenti** come investimento; **la revisione del perimetro delle amministrazioni pubbliche**; **la terza risorsa IVA**, **i super dividendi**, **i crediti d'imposta pagabili come spesa**, **i derivati**, **le società veicolo**; **il criterio della proprietà economica** per import ed export; **l'inclusione delle attività illegali**.
15. ► **Come si definisce il perimetro delle amministrazioni pubbliche?** — Il **settore S13** comprende le unità che **producono beni e servizi non destinabili alla vendita**, **finanziate da versamenti obbligatori**, più quelle la cui funzione principale è **la redistribuzione del reddito e della ricchezza**. Con il SEC 2010 servono **due verifiche**: il **test market/non market (test del 50%)** **e** **l'analisi delle condizioni di concorrenzialità**. È il perimetro che **determina il conto economico consolidato trasmesso alla Commissione europea in applicazione del Patto di stabilità**.
16. **Che cos'è la residenza secondo il SEC?** — Un concetto **economico e non giuridico**: sono residenti **le unità che hanno il centro di interesse nel territorio economico**, svolgendovi operazioni **per almeno un anno**. Il **territorio economico** comprende zone franche, acque territoriali, navi e aerei di unità residenti, ma **non le zone franche extraterritoriali sedi di ambasciate, consolati e basi militari**.
17. ► **Quali sono i settori istituzionali?** — Sei: **società non finanziarie**, **società finanziarie**, **amministrazioni pubbliche**, **istituzioni senza scopo di lucro al servizio delle famiglie**, **famiglie**, **resto del mondo** (settore *sui generis*). Si distinguono per **funzione principale** e **risorsa prevalente**.
18. **Che differenza c'è fra settori istituzionali e branche?** — I **settori istituzionali** raggruppano i soggetti per **comportamento economico** (chi sono, come si finanziano); le **branche** per **attività tecnico-produttiva** (che cosa producono). L'unità elementare delle branche è **l'unità di attività economica a livello locale**, classificata secondo la **NACE Rev. 2** (in Italia **Ateco**).
19. **Che differenza c'è fra flussi e consistenze?** — I **flussi** sono **modificazioni di valore economico entro un periodo di tempo**; le **consistenze (stock)** misurano **il valore in un preciso momento**. Il PIL è un flusso, il debito pubblico una consistenza.
20. **Un furto è un'operazione per il SEC?** — **No.** Le attività illegali sono registrabili **solo quando tutte le unità partecipanti intervengono contestualmente**: la compravendita di droga sì, **il furto no, perché chi lo subisce non ha alcun interesse a essere derubato**.
21. **Come si registrano i flussi nella contabilità nazionale?** — Secondo le regole della **partita doppia**, ma **nella pratica con la PARTITA QUADRUPLA**, perché la maggior parte delle operazioni **coinvolge due operatori** e va contabilizzata due volte per ciascuno. Tutti i flussi seguono il **principio della competenza**. Gli impieghi si valutano **ai prezzi di acquisto**, la produzione **ai prezzi base di vendita**.

## Comparazione (Parte III)

22. ► **Che cos'è il deflatore del PIL e in che cosa differisce dall'indice dei prezzi al consumo?** — È il **rapporto fra PIL nominale e PIL reale × 100**, e depura gli aggregati dall'inflazione. Differisce dall'indice dei prezzi al consumo per **il paniere** (tutto il prodotto interno contro i soli consumi delle famiglie; il deflatore **esclude le importazioni**), per **la ponderazione** (il deflatore è implicitamente **di tipo Paasche**, l'indice dei prezzi al consumo è **Laspeyres**), e di conseguenza **divergono quando rincarano i beni importati**.
23. **Perché non si usano i tassi di cambio per confrontare i PIL?** — Perché **risentono di fattori economici, finanziari e politici** e non riflettono il potere d'acquisto interno. Si usano invece le **parità del potere d'acquisto (PPA)**: **i tassi di conversione economica che eliminano le differenze nei livelli di prezzo fra Paesi**, dati dal rapporto fra gli ammontari di moneta nazionale necessari per acquistare **lo stesso paniere**.
24. **Che cosa sono ICP ed ECP?** — L'**International Comparison Program**, proposto dall'**ISNU nel 1968**, partito da **10 Paesi nel 1970** e oggi esteso a **107 Paesi**; e l'**European Comparison Program**, per il quale **EUROSTAT** conduce le indagini europee, **a cadenza annuale dal 1991**.
25. **Perché nei confronti multipli serve la transitività?** — Perché altrimenti **il confronto diretto fra due Paesi darebbe un risultato diverso dal confronto passando per un terzo**. Fisher non è transitivo; lo sono **EKS** (media geometrica di tutti i confronti indiretti) e **Geary-Khamis** (prezzi medi internazionali). **Gerardi** aggiunge la **proprietà additiva**, per cui **la somma delle parità dei sub-aggregati eguaglia la parità globale**.

## Input-output (Parte IV)

26. ► **Che cos'è una tavola input-output e a che cosa serve?** — Lo strumento dell'**analisi delle interdipendenze settoriali**, che studia **i flussi di beni e servizi fra settori produttivi**. A differenza della contabilità nazionale, **interessata ai risultati finali**, guarda **ai beni e servizi INTERMEDI**, il cui valore, incorporato nei beni finali, la contabilità nazionale non considera. Consente di **stimare le ripercussioni sulla produzione provocate da modificazioni della domanda finale**, e quindi **di supportare decisioni di politica economica**.
27. **Chi ha inventato le tavole input-output?** — **Wassily Leontief**, su dati della contabilità nazionale statunitense, **premio Nobel per l'economia nel 1973**; realizzando l'idea di **Quesnay** (*Tableau économique*, 1758).
28. **Com'è strutturata una tavola input-output?** — **Tre sezioni**: la **tavola degli impieghi intermedi** (la matrice vera e propria, a doppia entrata con le stesse branche per riga e per colonna), la **tavola degli impieghi finali** (consumi, investimenti, scorte, esportazioni), la **tavola degli impieghi primari e delle risorse** (componenti del valore aggiunto). Si legge **per riga il settore venditore, per colonna il settore acquirente**; sulla diagonale, **i reimpieghi**.
29. **Quali relazioni contabili si ricavano?** — Le **equazioni di bilancio** (per righe: come la produzione si ripartisce fra impieghi intermedi e finali), le **equazioni dei costi** (per colonne: la struttura dei costi), l'**equazione di equilibrio** (che le combina). Sommando su tutte le branche si ottiene **l'identità fra valore aggiunto più importazioni e domanda finale** — cioè **il conto economico delle risorse e degli impieghi**.
30. ► **Che cos'è la matrice di Leontief e che cosa sono i coefficienti di attivazione?** — La matrice **[I − a]**; la sua **inversa** è la **matrice dei coefficienti di fabbisogno DIRETTO E INDIRETTO**, detta anche **matrice dei coefficienti di attivazione**, perché **ciascun elemento indica la variazione di produzione di una branca necessaria a soddisfare un incremento unitario di domanda finale di un'altra**. Sono, in sostanza, **i moltiplicatori settoriali**: sommano l'effetto diretto e tutti gli effetti indiretti lungo la filiera.
31. **Qual è l'ipotesi fondamentale del modello e quali sono i suoi limiti?** — L'**ipotesi di TECNOLOGIA LINEARE**: la quantità di input è **proporzionale al volume dell'output**. Implica **assenza di economie di scala** e **assenza di sostituibilità fra input**. Le altre ipotesi del modello dei prezzi sono la **costanza dei coefficienti tecnici**, la **produzione di un solo prodotto omogeneo per branca** e la **costanza del prezzo di vendita rispetto alla branca acquirente**.
32. **Che cosa sono gli indici di integrazione settoriale?** — Proposti da **Chenery e Watanabe**: l'indice dei **collegamenti a valle (w)**, che misura **la quota di vendite intermedie sul prodotto totale**, e quello dei **collegamenti a monte (u)**, che misura **la quota di acquisti intermedi**. Un **u alto** qualifica una **attività di trasformazione**, un **u basso** un'**attività primaria**. Per il sistema nel complesso i due coincidono e danno **il grado di interdipendenza dell'economia**.
33. **Che cos'è una SAM?** — La **matrice di contabilità sociale**, che integra la tavola input-output **con le fasi di distribuzione e utilizzazione del reddito**, considerando attività produttive, fattori, settori istituzionali (famiglie, imprese, P.A.) e resto del mondo. Distingue **conti esogeni** (resto del mondo, formazione del capitale nel breve periodo) e **conti endogeni**, e produce i **moltiplicatori contabili globali**, che valutano gli effetti **sui redditi di ogni gruppo di operatori**. È lo strumento per valutare l'**impatto distributivo** di una politica.

## Consumi (Parte V)

34. **Che cos'è la funzione di consumo keynesiana?** — La relazione fra consumo e reddito posta in evidenza da **Keynes (1936)**. La novità sta nell'aver evidenziato che **all'aumentare del reddito la spesa per consumi non aumenta nella stessa proporzione**, perché soddisfatti i bisogni primari **le famiglie accrescono la quota risparmiata**: da qui **la sistematica inferiorità della domanda aggregata rispetto all'offerta**.
35. ► **Che cos'è la legge di Engel?** — Formulata dallo statistico tedesco **Ernst Engel** nel XIX secolo: **tanto più una famiglia è povera, tanto maggiore è la quota di reddito destinata a beni di prima necessità**. Ne discendono **tre categorie di beni**: **necessari** (elasticità fra 0 e 1), **inferiori** (elasticità **negativa**: al crescere del reddito se ne riduce il consumo), **superiori o di lusso** (elasticità maggiore di 1). La **quota di spesa alimentare è usata come indicatore di povertà**.
36. ► **Che cosa sono propensione marginale, propensione media ed elasticità?** — La **marginale** è la **variazione dei consumi indotta da una variazione unitaria di reddito**, ed è **compresa fra 0 e 1**. La **media** è **la quota di reddito destinata al consumo**. L'**elasticità** è il **rapporto fra le due**, e per Keynes è **minore di 1**.
37. **Quali forme funzionali può avere la funzione di consumo?** — **Lineare** (propensione marginale costante), **iperbolica** (evidenzia il **livello di saturazione**), **semilogaritmica** (presume una spesa iniziale sempre positiva, «fondamentale per l'analisi keynesiana»), **sigmoidale** (passa per l'origine, con asintoto di saturazione), **doppio-logaritmica** (**elasticità costante**), **di Leser** (elevata adattabilità per valori eccezionali del reddito).
38. **Che differenza c'è fra propensione marginale di breve e di lungo periodo?** — In un modello **a variabili ritardate**, il coefficiente del **reddito corrente** è la propensione **di breve periodo**; la **somma di tutti i coefficienti** è quella **di lungo periodo**. I coefficienti dei ritardi sono **di norma decrescenti secondo una progressione geometrica**.
39. ► **Che cos'è la teoria del reddito permanente?** — Dovuta a **Milton Friedman**: il consumo si compone di una parte **permanente**, stabile, funzione del **reddito permanente** — «il flusso di reddito goduto stabilmente nel passato e che ci si attende per l'avvenire», stimato come **media ponderata dei redditi passati con pesi decrescenti geometricamente** — e di una parte **transitoria**, che dipende dalla congiuntura. Il risultato: **propensione marginale uguale a propensione media** ed **elasticità pari a 1**, in contrasto con Keynes.

## Mercato del lavoro (Parte VI)

40. ► **Chi è occupato e chi è disoccupato secondo l'ISTAT?** — **Occupati**: persone di **15 anni e più** che nella settimana di riferimento hanno svolto **almeno un'ora di lavoro retribuito**, o **almeno un'ora non retribuita nella ditta di un familiare**, o sono **assenti da non più di tre mesi** o percependo **almeno il 50% della retribuzione**. **Disoccupati**: persone non occupate fra **15 e 74 anni** che **hanno cercato lavoro nei 30 giorni precedenti** **e** **sono disponibili entro due settimane**, oppure **inizieranno un lavoro entro tre mesi** e sono ugualmente disponibili.
41. ► **Quali sono i tre tassi e che cosa li distingue?** — **Attività** = forza lavoro / popolazione in età lavorativa; **occupazione** = occupati / popolazione in età lavorativa; **disoccupazione** = disoccupati / **forza lavoro**. Aggiungi l'osservazione decisiva: **un tasso di disoccupazione basso può convivere con un tasso di occupazione bassissimo** se l'inattività è alta — **il caso italiano**.
42. ► **Quali tipi di disoccupazione distingue la teoria economica?** — **Frizionale** (momentanea, dovuta alle frizioni del mercato; **stimata fra il 2 e il 5%**), **ciclica o congiunturale** (di breve periodo, legata alla domanda aggregata; qui si cita la **legge di Okun**: una caduta del PIL del **2-2,5%** rispetto al potenziale fa salire la disoccupazione dell'**1%**), **strutturale** (la più grave: squilibri **stabili e permanenti**, per settori o aree geografiche; cause opposte — **tecniche *labour saving*** o **insufficienti investimenti**). A ciascun tipo corrisponde una politica diversa.
43. **Che cos'è la Rilevazione sulle forze di lavoro?** — L'indagine campionaria ISTAT, fondata sul **Regolamento (CE) 577/98**, **continua dal 2004** (dati raccolti in tutte le settimane dell'anno, non più una per trimestre) ma **diffusa trimestralmente**. Intervista **oltre 250 mila famiglie** all'anno (**circa 600 mila individui**) in **circa 1.400 comuni**, chiedendo l'attività lavorativa nella **settimana di riferimento**.

## Produzione e produttività (Parte VII)

44. ► **Che cos'è la funzione Cobb-Douglas e quali proprietà ha?** — **Y = a L^α K^β**. **α e β sono le elasticità dei fattori**; **la loro somma misura i rendimenti di scala**; **l'elasticità di sostituzione è pari a 1**; **in concorrenza perfetta e a rendimenti costanti le elasticità coincidono con le quote distributive** (teorema di Eulero); **si linearizza con i logaritmi** e si stima **con i minimi quadrati**. La versione **dinamica** aggiunge **un termine di trend esponenziale** per il progresso tecnico.
45. ► **Che cosa sono la produttività parziale e quella globale, e che cos'è il residuo di Solow?** — La **parziale generica** è il rapporto fra valore della produzione a prezzi costanti e quantità di un fattore: **Pul** per il lavoro, **Puc** per il capitale. La **parziale specifica** rapporta la **quota di valore che remunera il fattore** al fattore stesso. La **globale** considera **tutti i fattori congiuntamente**, ed è il rapporto fra **indice di volume della produzione** e **indice di volume dei fattori**. La funzione di **Solow** separa **lo spostamento LUNGO la funzione** (aumento di capitale per addetto) dallo **spostamento VERSO L'ALTO** (progresso tecnico): quest'ultimo, ottenuto **per differenza**, è il **residuo di Solow**, e dà luogo all'**indice del progresso tecnico** e alla **funzione ridotta di produzione**.

---

# PARTE X — COLLEGAMENTI CON LE ALTRE MATERIE DEL BANDO

Questa materia è la più «connessa» di tutto il programma. Ecco i ponti più solidi.

**Con la contabilità pubblica.** Il collegamento è strutturale, non accidentale: **il conto economico consolidato delle amministrazioni pubbliche** che si studia in contabilità pubblica **è costruito secondo le regole del SEC 2010**, e **il perimetro S13 determina quali enti vi rientrino**. L'**indebitamento netto** — il saldo rilevante per il Patto di stabilità — è **un saldo di competenza economica secondo il SEC**, diverso dal saldo di competenza giuridica e dal fabbisogno di cassa. E i **parametri di Maastricht** sono rapporti fra grandezze di contabilità nazionale. Se sai dire che **l'elenco ISTAT delle unità S13 è pubblicato annualmente in Gazzetta Ufficiale** e determina chi è soggetto ai vincoli di finanza pubblica, hai fatto un collegamento perfetto.

**Con l'econometria.** Fittissimo, in entrambe le direzioni:
- la **destagionalizzazione** degli indicatori congiunturali (statistica economica, cap. 1) **è** la procedura **TRAMO-SEATS** (econometria, cap. 14), e l'**indice della produzione industriale** è l'esempio che il manuale di econometria usa;
- la **Cobb-Douglas** (statistica economica, cap. 7) **è** l'esempio di **modello doppio-logaritmico** stimabile con OLS (econometria, cap. 8), e l'ipotesi di rendimenti costanti è **un vincolo lineare testabile con un test F**;
- l'**elasticità del consumo** (cap. 5) è la stessa grandezza che in econometria si stima come **coefficiente di una regressione doppio-logaritmica**;
- i ***consumer panel*** (cap. 5) sono **dati panel** nel senso del capitolo 15 di econometria;
- la **funzione di consumo keynesiana** è **l'esempio guida** del capitolo 6 di econometria sui modelli econometrici.

**Con la valutazione delle politiche pubbliche.** Tre agganci forti:
- l'input-output e la SAM forniscono i **moltiplicatori** con cui si fa **valutazione EX ANTE** dell'impatto di una spesa pubblica — produzione attivata, valore aggiunto, occupazione, e con la SAM anche **impatto distributivo**;
- il **mercato del lavoro** è il terreno classico della valutazione **EX POST**: l'effetto dei sussidi sulla durata della disoccupazione, l'effetto delle politiche attive sul reimpiego, si misurano con **DiD, RDD e matching**;
- l'input-output **multiregionale** risponde alla domanda su **quanta parte dell'attivazione generata da un investimento nel Mezzogiorno resti nel Mezzogiorno** — che è il cuore della **politica di coesione**.

**Con l'economia politica e la scienza delle finanze.** La **funzione di consumo**, la **legge di Engel**, i **rendimenti di scala**, la **legge di Okun**, la **teoria del reddito permanente**, la **funzione di produzione di Solow**: sono tutti concetti di teoria economica che qui compaiono **nella loro veste misurabile**. Il messaggio da trasmettere è che **la statistica economica è il punto in cui la teoria economica diventa numero** — e quindi il punto in cui può essere confermata o smentita.

**Con il diritto amministrativo.** Tre punti concreti: **l'ISTAT come ente pubblico di ricerca** sottoposto a vigilanza della Presidenza del Consiglio, con autonomia plurima; il **SISTAN** e il **D.Lgs. 322/1989**, con il **segreto statistico** dell'art. 9; e il fatto che **il SEC 2010 è un REGOLAMENTO europeo direttamente applicabile** — la contabilità nazionale italiana è, giuridicamente, **esecuzione di diritto dell'Unione**, non scelta tecnica nazionale.

**Con la data science.** Il passaggio in corso nella statistica ufficiale: dalle **indagini campionarie** alle **fonti amministrative** e agli ***scanner data*** dei *consumer panel*. È lo stesso tema dei *big data* e della qualità del dato studiato nella dispensa di data mining — con l'aggiunta, qui, del vincolo del **segreto statistico** e della **finalità statistica** come base giuridica autonoma nel GDPR.

---

# PARTE XI — COME PORTARE QUESTA MATERIA ALL'ORALE

**Le tre cose da sapere prima di tutto**, se il tempo è poco: **(1)** Laspeyres, Paasche, Fisher e quale usa l'ISTAT; **(2)** il SEC 2010, le sue novità e il perimetro S13; **(3)** le definizioni di occupato e disoccupato e i tre tassi con i denominatori giusti.

**Il registro giusto.** A differenza dell'econometria, qui **non stai spiegando un metodo: stai descrivendo un'istituzione**. La statistica economica è **il sistema informativo su cui si fondano le decisioni pubbliche**, e va raccontata così — con l'ISTAT, EUROSTAT, i regolamenti europei, le date. Una commissione RIPAM apprezza molto questo taglio, perché è il taglio di chi si vede già a lavorare in un'amministrazione.

**Le tre frasi che funzionano sempre:**

1. *«L'ISTAT usa l'indice di Laspeyres per la costanza nel tempo del paniere di riferimento: consente di misurare variazioni di prezzo a paniere costante, e il paniere viene aggiornato ogni anno e tenuto fisso per l'intero anno.»*
2. *«Il perimetro del settore S13 non è una questione contabile: determina quali enti concorrono al deficit e al debito che l'Italia comunica alla Commissione europea in applicazione del Patto di stabilità.»*
3. *«Il tasso di disoccupazione ha al denominatore la forza lavoro, non la popolazione: per questo può risultare basso anche dove il tasso di occupazione è bassissimo, se l'inattività è alta.»*

**Quando non ricordi un numero.** Non inventarlo. Di' l'ordine di grandezza e il concetto: *«il paniere ISTAT arriva a oltre mille prodotti elementari»* va benissimo, *«1.731 prodotti elementari»* è meglio ma non indispensabile. Le cose che invece **vanno sapute esatte** sono poche: **un'ora di lavoro** per essere occupati, **30 giorni** di ricerca e **due settimane** di disponibilità per essere disoccupati, **15-74 anni**, **2-5%** di disoccupazione frizionale, **2-2,5% per 1%** nella legge di Okun.

**Il modo di chiudere una risposta.** Quasi ogni argomento di questa materia si può chiudere dicendo **a che cosa serve il numero a chi deve decidere**. L'indice dei prezzi serve a rivalutare gli assegni; i conti nazionali a calcolare il contributo al bilancio UE; le tavole input-output a stimare l'effetto di un investimento pubblico; i tassi del mercato del lavoro a disegnare le politiche attive. **È questo che distingue un candidato che ha studiato statistica da uno che ha capito a che cosa serve un istituto nazionale di statistica.**

---

*Dispensa elaborata sul manuale Simone — Parte IV «Statistica economica», capitoli 1-7 (pp. 575-648), letta integralmente. Le formule sono state raccolte nella Parte VIII, salvo quelle — in particolare gli indici di Laspeyres e Paasche — la cui struttura è essa stessa il contenuto da apprendere. Aggiornata al 15 settembre 2026.*
