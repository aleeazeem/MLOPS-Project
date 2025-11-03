# Cheat Sheet
---
## Vectorization
There are two types of performing vectorization on the text for machine learning

### Bag of Words
Represents text as a collection of words (a "bag") without considering word order or meaning
```
Doc1: "movie was good"
Doc2: "movie was bad"

Vocabulary: [movie, was, good, bad]
Doc1 → [1, 1, 1, 0]
Doc2 → [1, 1, 0, 1]
```
### TFIDF
Improves BoW by weighting words based on how important they are in a document relative to all documents.
Common words across documents get lower weight, rare words get higher weight.
- Common words like “movie” or “was” get low scores.
- Informative words like “good” or “bad” get high scores.

---
## Experimnet Steps 
1. Data Loader: Load the data and convert it into dataframe with the help of Pandas
2. Perform Text Clean up: 
    - Lemmatization(reduce words to their base or dictionary)
    - Stop Words Removal
    - Remove numbers
    - Remove urls
    - Remove Puntuation
3. Vectorization: On text column (Review). Perform vectorization using BOW or TFIDF
    ```
    vectorizer = CountVectorizer(max_features=100)  |  vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['review'])
    ```
4. Transform (convert sentiment to number)
    ```
    df['sentiment'] = df['sentiment'].map({'positive':1, 'negative':0})
    ```
5. Split the data for training and testing
    ```
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    ```
6. Enable MLFlow
    ```
    mlflow.set_tracking_uri('https://dagshub.com/user-name/MLOPS-Project.mlflow')
    dagshub.init(repo_owner='user-name', repo_name='MLOPS-Project', mlflow=True)
    mlflow.set_experiment("Logistic Regression Baseline")
    ```
7. Start training and prediction under MLFlow block
    ```
    with mlflow.start_run():
    start_time = time.time()
    try:
        ----- Log Parameters -------
        ---- Perform Training ------
        ---- Perform Prediction ----
        ---- Perform Evaluation ----
    ```
8. All traces and log statements will be captured. Go to MLFlow dashboard and compare it with different runs

## Note - Highly Important:
-  This repo is ML focused not coding or ML focused. You might see some hardcoded values in experiments files
- Do not hard code the values. Use config file in the form of json or yaml file etc.
- The experiment file exp2_bow_vs_tfidf that I created, some how not much hardcoded. It performs training in loop with combination of different params. 
- Use credentials as env variables either by exporting them or using bash_profile. In CICD or in cloud the the crednetials will be picked up from env

