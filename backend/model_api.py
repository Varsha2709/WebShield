
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask,request,jsonify
import pickle
from features.dom_detector import detect_dom_attacks

rf_model=pickle.load(open("../models/rf_model.pkl","rb"))
vectorizer=pickle.load(open("../models/tfidf_vectorizer.pkl","rb"))

app=Flask(__name__)

trusted_sites=["google.com","github.com","openai.com","stackoverflow.com"]

@app.route("/predict",methods=["POST"])
def predict():

 data=request.json
 url=data["url"]
 html=data["html"]

 for site in trusted_sites:
  if site in url:
   return jsonify({"risk_score":0,"attack":"Safe"})

 dom_score,attack=detect_dom_attacks(html)

 text_features=vectorizer.transform([html])
 rf_pred=rf_model.predict(text_features)[0]

 risk=min(100,dom_score+50)

 return jsonify({
 "risk_score":risk,
 "attack":attack if attack!="Safe" else rf_pred
 })

app.run(port=5000)
