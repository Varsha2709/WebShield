import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("../datasets/final_multiclass_dataset.csv")

X = data["text"].astype(str)
y = data["label"]

vectorizer = TfidfVectorizer(max_features=5000)

X_vec = vectorizer.fit_transform(X)

model = RandomForestClassifier(n_estimators=300)

model.fit(X_vec, y)

pickle.dump(model, open("rf_model.pkl","wb"))
pickle.dump(vectorizer, open("tfidf_vectorizer.pkl","wb"))

print("Model trained successfully")