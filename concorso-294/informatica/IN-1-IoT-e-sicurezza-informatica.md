# IN-1 — IoT e sicurezza informatica

**Copre 10 domande realmente uscite all'orale**: 254 IoT · 226 sicurezza fisica e
logica · 255 attacchi e contromisure · 209 backup incrementale · 181 data breach
· 183 notifica entro 72 ore · 182 Codice della privacy · 189 e 190 QR code · 267
sicurezza in Excel.

Informatica rende **10 domande per lezione**, il rendimento piu' alto di tutto il
programma, contro 1,7 del diritto amministrativo. Ed e' materia **descrittiva**:
si risponde con definizioni ordinate, non con ragionamenti.

Solo definizioni. Ogni termine attaccato al suo pezzo di definizione.

---

# 1. L'Internet of Things *(domanda 254)*

**L'Internet of Things, cioe' la rete di oggetti fisici dotati di sensori,
software e connettivita', capaci di raccogliere e scambiare dati senza intervento
umano.**

**Gli impieghi nella pubblica amministrazione**: smart city e gestione del
traffico, monitoraggio ambientale, telelettura dei contatori, gestione dei
rifiuti, telemedicina e assistenza domiciliare, manutenzione predittiva di
infrastrutture ed edifici pubblici.

**I rischi, e sono il raccordo con il resto della lezione.** Primo:
**l'ampliamento della superficie d'attacco** — ogni oggetto connesso e' un
possibile punto di ingresso nella rete. Secondo: i dispositivi hanno **risorse
limitate**, quindi sono difficili da aggiornare e restano vulnerabili a lungo,
spesso con **credenziali di default** mai cambiate. Terzo: **il volume di dati
personali** raccolti in modo continuo e silenzioso, che apre problemi di
profilazione e di base giuridica del trattamento.

**La frase di raccordo**: l'IoT moltiplica i punti di ingresso, e per questo la
sicurezza informatica non e' un capitolo a parte ma la condizione del suo
funzionamento.

---

# 2. I tre pilastri della sicurezza

Domanda generatrice di tutta la materia: **che cosa si puo' perdere?** Tre cose,
e non ce n'e' una quarta.

**La riservatezza, cioe' che ai dati acceda solo chi e' autorizzato.**
**L'integrita', cioe' che i dati non siano alterati o distrutti indebitamente.**
**La disponibilita', cioe' che i dati siano accessibili quando servono.**

Ogni minaccia attacca uno di questi tre, e ogni contromisura ne difende uno. E'
la struttura con cui si ordina qualunque risposta sulla sicurezza, compresa la
definizione di data breach del punto 6.

---

# 3. Sicurezza fisica e sicurezza logica *(domanda 226)*

La domanda generatrice: **da dove si entra?** Da una porta, o da una tastiera.

**La sicurezza fisica, cioe' la protezione dall'accesso materiale** a locali,
server, dispositivi e supporti: controllo degli accessi, videosorveglianza,
armadi e rack chiusi, custodia dei supporti rimovibili, e protezione dagli eventi
ambientali — incendio, allagamento, interruzione dell'alimentazione.

**La sicurezza logica, cioe' la protezione dei dati e dei sistemi dall'accesso
non autorizzato per via informatica**: autenticazione, autorizzazione per profili
e minimo privilegio, cifratura, firewall, antivirus, segmentazione della rete,
registrazione dei log.

**La frase che le distingue: la sicurezza fisica protegge il contenitore, la
sicurezza logica protegge il contenuto.**

**E sono complementari, non alternative**, ed e' il punto da aggiungere: la
migliore cifratura non serve se chiunque entra nella sala server, e la porta
blindata non serve se la password e' rimasta quella di default.

---

# 4. Gli attacchi e le contromisure *(domanda 255)*

La domanda chiede **esempi di attacco e contromisure**, quindi va risposta in
forma di elenco ordinato. La domanda generatrice che ordina tutto: **l'attacco
punta alla persona o alla macchina?** Due famiglie.

## Attacchi che puntano alla persona — l'ingegneria sociale

**L'ingegneria sociale, cioe' l'insieme delle tecniche che inducono la vittima a
compiere essa stessa l'azione dannosa**, invece di forzare il sistema.

**Il phishing, cioe' un messaggio che imita un mittente fidato per carpire
credenziali o indurre un pagamento.** Le varianti: **spear phishing** quando e'
mirato su una persona specifica, **smishing** via SMS, **vishing** via telefono,
e la **frode del falso dirigente** (BEC), in cui si impersona un superiore per
ottenere un bonifico urgente.

**Contromisure**: formazione del personale, verifica su un **canale
indipendente** prima di eseguire disposizioni urgenti, regola che le credenziali
non si comunicano mai via email o telefono, e **autenticazione a piu' fattori**,
che rende inutile la sola password rubata.

## Attacchi che puntano alla macchina

**Il malware, cioe' software realizzato per danneggiare o compromettere un
sistema**: virus, worm, trojan, spyware, keylogger.

**Il ransomware, cioe' il malware che cifra i dati della vittima e chiede un
riscatto per restituirli.** E' l'attacco piu' grave per una pubblica
amministrazione, perche' colpisce la **disponibilita'** e blocca il servizio.

**Il DDoS, cioe' la saturazione deliberata di un servizio con un volume enorme di
richieste**, che lo rende indisponibile.

**L'SQL injection, cioe' l'inserimento di comandi nei campi di input** per far
eseguire al database istruzioni non previste. **L'attacco man in the middle,
cioe' l'intercettazione della comunicazione fra due parti** che credono di
parlare direttamente. E lo sfruttamento di **vulnerabilita' note** su sistemi non
aggiornati.

**Contromisure**: aggiornamenti e **patch** tempestive, antivirus e sistemi di
rilevamento, **firewall** e segmentazione della rete, **cifratura** dei dati a
riposo e in transito, **principio del minimo privilegio**, log e monitoraggio, e
**backup** — che per il ransomware e' la contromisura decisiva, perche' permette
di ripristinare senza pagare. **Il riscatto non si paga**: non garantisce la
restituzione e finanzia l'attacco successivo.

## La contromisura trasversale

**L'anello debole e' quasi sempre l'utente, non la tecnologia.** Per questo
formazione e procedure contano quanto gli strumenti, e dirlo chiude bene la
risposta.

---

# 5. Il backup *(domanda 209)*

La domanda generatrice: **copio tutto, o solo le novita'? E rispetto a quando?**
Tre tipi.

**Il backup completo, cioe' la copia di tutti i dati ogni volta.** Occupa molto
spazio e richiede molto tempo, ma il **ripristino e' semplice**: serve una sola
copia.

**Il backup incrementale, cioe' la copia dei soli dati modificati dall'ultimo
backup di qualunque tipo.** E' il piu' rapido e il piu' leggero, ma **il
ripristino richiede il backup completo piu' tutta la catena degli incrementali
successivi**: se manca un anello, il ripristino fallisce.

**Il backup differenziale, cioe' la copia dei dati modificati dall'ultimo backup
completo.** Via di mezzo: piu' pesante dell'incrementale, ma il ripristino
richiede **solo il completo e l'ultimo differenziale**.

**La regola 3-2-1**, da citare perche' e' lo standard: **tre copie dei dati, su
almeno due supporti diversi, di cui una conservata fuori sede.**

**E il punto che fa colpo: un backup non verificato non e' un backup.** Il
ripristino va provato periodicamente, altrimenti si scopre che non funziona
proprio nel momento in cui serve.

---

# 6. Il data breach *(domanda 181)*

**Il data breach, cioe' la violazione di sicurezza che comporta
accidentalmente o in modo illecito la distruzione, la perdita, la modifica, la
divulgazione non autorizzata o l'accesso ai dati personali** trattati.

**Si classifica sui tre pilastri del punto 2**, e dirlo cosi' e' il modo ordinato
di risponderne: **breach di riservatezza** quando c'e' divulgazione o accesso non
autorizzato; **breach di integrita'** quando i dati sono alterati; **breach di
disponibilita'** quando sono perduti o distrutti.

**Il punto da non mancare: non e' soltanto l'attacco informatico esterno.** Sono
data breach anche la perdita di una chiavetta USB, il furto di un portatile,
l'email inviata al destinatario sbagliato, i documenti lasciati accessibili.
**L'origine puo' essere accidentale, e resta una violazione.**

---

# 7. La notifica della violazione *(domanda 183)*

Qui la cosa importante sono **due obblighi distinti, con due soglie diverse**. La
domanda generatrice: **chi va avvisato, quando, e a quale condizione?**

**Notifica al Garante**: entro **72 ore** dal momento in cui il titolare viene a
conoscenza della violazione, **salvo che sia improbabile che la violazione
presenti un rischio** per i diritti e le liberta' delle persone fisiche. Se la
notifica avviene oltre le 72 ore, **il ritardo va motivato**.

**Comunicazione agli interessati**: **senza ingiustificato ritardo**, e soltanto
quando la violazione presenta un **rischio elevato** per i loro diritti e
liberta'.

**Le due soglie sono la risposta**: **rischio** fa scattare il Garante, **rischio
elevato** fa scattare anche gli interessati.

**E in ogni caso il titolare tiene un registro delle violazioni**, comprese
quelle che non ha notificato, con le motivazioni della scelta — e' l'applicazione
del principio di **accountability**. Riferimenti: **articoli 33 e 34 del GDPR**.

---

# 8. Il quadro normativo *(domanda 182)*

**Il Regolamento UE 2016/679, il GDPR, e' la fonte principale**, direttamente
applicabile. **Il Codice della privacy, cioe' il D.Lgs. 196/2003, come modificato
dal D.Lgs. 101/2018** per l'adeguamento al GDPR, e' oggi la normativa nazionale
di raccordo.

**L'autorita' e' il Garante per la protezione dei dati personali.**

**I soggetti**: il **titolare del trattamento**, che decide finalita' e mezzi; il
**responsabile del trattamento**, che tratta per conto del titolare;
l'**interessato**, la persona cui i dati si riferiscono; e il **responsabile
della protezione dei dati**, il DPO, **obbligatorio per le pubbliche
amministrazioni**.

**I principi**: liceita', correttezza e trasparenza · limitazione della finalita'
· **minimizzazione** · esattezza · limitazione della conservazione · integrita' e
riservatezza · **accountability**, cioe' la responsabilizzazione del titolare, che
deve non solo rispettare le regole ma **essere in grado di dimostrarlo**.

**I diritti dell'interessato**: accesso, rettifica, cancellazione — il diritto
all'oblio —, limitazione, portabilita', opposizione.

*Approfondimento previsto nella rassegna DA-5 del 12 novembre.*

---

# 9. Il QR code *(domande 189 e 190)*

**Il QR code, cioe' un codice a barre bidimensionale che contiene informazioni
leggibili da una fotocamera.**

**A cosa serve nella PA** *(189)*: collegare un documento cartaceo a una risorsa
digitale, verificare l'autenticita' di un certificato o di un'attestazione,
avviare un pagamento tramite **pagoPA**, gestire biglietti, accessi e
prenotazioni.

**Puo' essere usato in una procedura di autenticazione?** *(190)* **Si', e di
fatto lo e'** — e' il caso dell'accesso con SPID da computer confermato
dall'applicazione sullo smartphone. **Ma con cautele precise, e il motivo di
fondo e' uno: il QR code non e' leggibile dall'uomo**, quindi l'utente non puo'
vedere dove lo sta portando prima di inquadrarlo.

**Il rischio specifico si chiama quishing, cioe' il phishing veicolato da QR code
malevoli**, spesso apposti fisicamente sopra quelli legittimi su manifesti,
sportelli o parcometri.

**Le cautele**: il QR code **non deve essere l'unico fattore** di autenticazione,
ma va combinato con il possesso del dispositivo e con un PIN o un dato biometrico
— cioe' dentro un'**autenticazione a piu' fattori**; i codici devono essere
**generati dinamicamente e con scadenza breve**, non statici; l'utente deve poter
**verificare l'indirizzo** prima di confermare; la comunicazione deve avvenire su
**canale cifrato**; e sui supporti fisici pubblici va verificato che il codice non
sia stato sostituito.

---

# 10. La sicurezza in Excel *(domanda 267)*

La domanda generatrice: **proteggo il file, i dati, o chi lo apre?**

**Proteggere il file**: la **password di apertura**, che **cifra effettivamente il
file**, e la **password di modifica**, che e' molto piu' debole perche' **non
cifra** e impedisce solo il salvataggio sullo stesso file.

**Proteggere il contenuto**: la **protezione del foglio e della cartella di
lavoro**, che blocca celle, formule e struttura, con lo **sblocco delle sole celle
di input**; e la **convalida dei dati**, che impedisce l'inserimento di valori non
ammessi.

**Proteggere chi lo apre**: la **disabilitazione delle macro**, con esecuzione
consentita solo a quelle **firmate digitalmente** e provenienti da fonti fidate —
le macro sono un vettore classico di malware; e la **visualizzazione protetta**
per i file scaricati da internet o ricevuti per posta.

**Prima di condividere**: **rimozione dei metadati e del contenuto nascosto** —
righe, colonne e fogli nascosti, commenti, autori —, controllo dei
**collegamenti esterni**, e preferenza per la **condivisione con permessi** su
spazio cloud dell'amministrazione invece dell'invio del file per email.

**Il punto concettuale, ed e' quello che distingue la risposta: la protezione del
foglio non e' cifratura.** Serve a prevenire **modifiche accidentali**, non a
garantire la riservatezza. **Solo la password di apertura protegge davvero i
dati.**

---

# La frase d'attacco

*«La sicurezza informatica difende tre cose — riservatezza, integrita' e
disponibilita' — su due fronti, quello fisico che protegge il contenitore e
quello logico che protegge il contenuto; gli attacchi puntano o alla macchina,
con malware e ransomware, o alla persona, con l'ingegneria sociale, e poiche'
l'anello debole e' quasi sempre l'utente la formazione conta quanto la
tecnologia.»*

# Le dieci domande

1. Che cosa si intende per Internet of Things? *(254)*
2. Qual e' la differenza fra sicurezza fisica e sicurezza logica? *(226)*
3. Come si difende un'amministrazione dagli attacchi informatici? Illustri esempi
   di attacco e le relative contromisure. *(255)*
4. Che cos'e' un backup incrementale? *(209)*
5. Che cos'e' un data breach? *(181)*
6. In caso di violazione dei dati personali, quali obblighi di notifica sorgono,
   verso chi ed entro quali termini? *(183)*
7. Ci parli del Codice della privacy e della tutela dei dati personali. *(182)*
8. A cosa serve un QR code? *(189)*
9. Un QR code puo' essere impiegato in una procedura di autenticazione? Con quali
   cautele? *(190)*
10. Quali strumenti e precauzioni garantiscono la sicurezza in Excel? *(267)*
