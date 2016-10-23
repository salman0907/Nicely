from flask import render_template, request
from FlaskWebProject1 import app
from watson_developer_cloud import AlchemyLanguageV1
from twython import Twython # pip install twython


@app.route('/')
def home():
    return render_template("index.html")


def analyze_str(textString):
    alchemy_language = AlchemyLanguageV1(api_key='df8f270a6f64bc6cab503b9018b9f4940d12eb76')
    combined_operations = ['doc-emotion', 'doc-sentiment']
    data = alchemy_language.combined(text=textString, extract=combined_operations)
    return data


def get_twitter_data(username):
    CONSUMER_KEY = 'xlgtpTpPv6oZ13R6iHJ8J8QuR'
    CONSUMER_SECRET = 'hNCZ5m609j6zPr4z0JnEdXf3pyadubny45QYudZWFGtWt6jqiM'
    ACCESS_KEY = '782417738895495168-XJ4U0VAWg63EVRwKubK7oZMJDFhsqoC'
    ACCESS_SECRET = 'MsuODbwT1z8Yrtvupst9KnEwL7djYbIbApD0tibJYNbq4'

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
    lis = []
    tweets = []
    for i in range(0, 16):
        if len(lis):
            user_timeline = twitter.get_user_timeline(screen_name=username, count=200, include_retweets=False, max_id=lis[-1])
        else:
            user_timeline = twitter.get_user_timeline(screen_name=username, count=200, include_retweets=False)

        for tweet in user_timeline:
            tweets.append(tweet['text'])
            lis.append(tweet['id'])

    return tweets


@app.route('/sentence', methods=["POST"])
def sentence():
    data = request.get_json()
    return data['sentence'], 200
