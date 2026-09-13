# 3. Elementi di data science e data mining

> Fascia **sostegno tecnico**. Attenzione a una distinzione che la commissione può
> usare come domanda-trappola: *predire* non è *spiegare*.

## Programma di riferimento

- Il ciclo del progetto di analisi dati: CRISP-DM (business understanding, data
  understanding, preparazione, modellazione, valutazione, deployment)
- Tipi di apprendimento: supervisionato, non supervisionato, per rinforzo (cenni)
- Preparazione dei dati: pulizia, valori mancanti, outlier, feature engineering,
  normalizzazione
- **Overfitting e underfitting**; trade-off distorsione-varianza
- Suddivisione train / validation / test; cross-validation k-fold
- Algoritmi supervisionati: regressione, k-NN, alberi decisionali, random forest,
  gradient boosting, SVM (cenni), reti neurali (cenni)
- Algoritmi non supervisionati: clustering (k-means, gerarchico), riduzione della
  dimensionalità (PCA), regole associative
- **Metriche di valutazione**: matrice di confusione, accuratezza, precisione,
  richiamo, F1, curva ROC e AUC; per la regressione RMSE, MAE, R²
- Record linkage e integrazione di archivi amministrativi
- Interpretabilità e spiegabilità dei modelli; modelli black box nella PA
- Bias algoritmico, equità, protezione dei dati personali

## Domande d'orale probabili

1. Descriva le fasi di un progetto di data mining.
2. Cos'è l'overfitting? Come lo si individua e come lo si contrasta?
3. Spieghi il trade-off distorsione-varianza. Perché un modello più complesso non
   è necessariamente migliore?
4. Perché si separano train e test set? A cosa serve in più il validation set?
5. **In un problema con classi fortemente sbilanciate, perché l'accuratezza è una
   metrica ingannevole? Cosa userebbe al suo posto?** (es. individuare frodi o
   evasione: 99% di accuratezza è banale se il 99% dei casi è regolare)
6. Differenza tra classificazione e clustering. Faccia un esempio d'uso in una PA.
7. Come funziona k-means? Come si sceglie il numero di cluster?
8. A cosa serve l'analisi delle componenti principali?
9. **Un modello predittivo molto accurato ci dice qualcosa sull'effetto causale di
   una variabile? Argomenti.**
10. Quali cautele servono quando un algoritmo supporta decisioni amministrative che
    incidono sui cittadini? (trasparenza, spiegabilità, non discriminazione, GDPR)

## Il collegamento da presidiare

La domanda 9 è il ponte con l'econometria ed è quella su cui molti candidati
scivolano. Sintesi utile da avere pronta: *il data mining ottimizza la capacità
predittiva fuori campione; l'econometria della valutazione identifica un effetto
controfattuale. Un modello può predire benissimo sfruttando correlazioni spurie,
e sarebbe inutile — o dannoso — per decidere se una politica funziona.*

## Sintesi dai capitoli del manuale

<!-- Da riempire -->

## Punti su cui ho esitato
