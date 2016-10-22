from flask import render_template, request
from FlaskWebProject1 import app
from watson_developer_cloud import AlchemyLanguageV1


@app.route('/')
def home():
    return render_template("index.html")


def analyze_str(textString):
    alchemy_language = AlchemyLanguageV1(api_key='df8f270a6f64bc6cab503b9018b9f4940d12eb76')
    combined_operations = ['doc-emotion', 'doc-sentiment']
    data = alchemy_language.combined(text=textString, extract=combined_operations)
    return data


@app.route('/sentence', methods=["POST"])
def sentence():
    data = request.get_json()
    return data['sentence'], 200
