import pandas as pd
import pickle
import re
import numpy as np
from textblob import TextBlob
import nltk
from nltk.classify import NaiveBayesClassifier as classifier
from flask import Flask, request, jsonify, render_template

#Tokenize Sentences properly
def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

app = Flask(__name__)

@app.route('/doShit/', methods=['POST'])
def doShit():
    content = request.json["data"]
    print(content)
    
    email = content["input"]

    loaded_model = pickle.load(open("notebooks/Classifier.pickle", 'rb'))
    result = loaded_model.prob_classify(format_sentence(email))

    aDick = {}

    for label in result.samples():
        aDick[label] = result.prob(label)

    aDick["Sentiment"] = TextBlob(email).sentiment.polarity
    aDick["Subjectivity"] = TextBlob(email).sentiment.subjectivity

    prediction = aDick
    return jsonify({"prediction" : prediction})

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/email")
def email():
    """Return the homepage."""
    return render_template("email.html")

@app.route("/data")
def data():
    """Return the homepage."""
    return render_template("data.html")

@app.route("/tableau")
def tableau():
    """Return the homepage."""
    return render_template("tableau.html")

@app.route("/about")
def about():
    """Return the homepage."""
    return render_template("about.html")

@app.route("/analytics")
def analytics():
    """Return the homepage."""
    return render_template("analytics.html")

@app.route("/resources")
def resources():
    """Return the homepage."""
    return render_template("resources.html")

@app.route("/getEnronData")
def getEnronData():
    df = pd.read_csv("static/data/email_sentiment.csv")
    return df[0:500].to_json(orient="records")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)