import pandas as pd
import pickle
import re
from textblob import TextBlob
import nltk
from nltk.classify import NaiveBayesClassifier as classifier
from flask import Flask, jsonify, render_template
from sklearn.externals import joblib
from wtforms import Form, TextAreaField, validators
app = Flask(__name__)

loaded_model = joblib.load('./JupyterNotebooks/model.pkl')

def classify(document):
    label = {0: 'negative', 1: 'positive'}
    X = loaded_vec.transform([document])
    y = loaded_model.predict(X)[0]
    proba = np.max(loaded_model.predict_proba(X))
    return label[y], proba


class ReviewForm(Form):
	moviereview = TextAreaField('',
			[validators.DataRequired(), validators.length(min=15)])

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/analysis")
def analysis():
    form = ReviewForm(request.form)
    return render_template("reviewform.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)