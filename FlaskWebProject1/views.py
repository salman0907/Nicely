from flask import render_template
from FlaskWebProject1 import app
from watson_developer_cloud import AlchemyLanguageV1
from requests_oauthlib import OAuth1
import requests
import json
from datetime import datetime
import pandas as pd
from multiprocessing import Pool


@app.route('/', methods=['GET', "POST"])
def home():
    return render_template("index.html")


@app.route('/g1', methods=['GET', "POST"])
def g1():
    return render_template("dough.html")


@app.route('/g2', methods=['GET', "POST"])
def g2():
    return render_template("g2.html")


@app.route('/buttons', methods=['GET', "POST"])
def buttons():
    return render_template("buttons.html")


def analyze_str(textString):
    alchemy_language = AlchemyLanguageV1(api_key='39ee6f3202c6eecc699264a233b3192c872873e2')
    combined_operations = ['doc-emotion', 'doc-sentiment']
    data = alchemy_language.combined(text=textString, extract=combined_operations, language="english")
    return data


def get_twitter_data(user):
    consumer_key = 'xlgtpTpPv6oZ13R6iHJ8J8QuR'
    consumer_secret = 'hNCZ5m609j6zPr4z0JnEdXf3pyadubny45QYudZWFGtWt6jqiM'
    access_token_key = '782417738895495168-XJ4U0VAWg63EVRwKubK7oZMJDFhsqoC'
    access_token_secret = 'MsuODbwT1z8Yrtvupst9KnEwL7djYbIbApD0tibJYNbq4'

    auth = OAuth1(consumer_key, consumer_secret,
                  access_token_key, access_token_secret)

    get_url = lambda user, max_id: 'https://api.twitter.com/1.1/statuses/user_timeline.json?count=50&include_rts=false&exclude_replies=false&screen_name=%s%s' % (user, ('&max_id=%s' % max_id) if max_id else '')

    mx_id = 0
    # tweets = []
    # for i in range(16):
    j = json.loads(requests.get(get_url(user, mx_id), auth=auth).text)
        # tweets.extend(j)
        # mx_id = tweets[-1]['id']

    # return tweets
    return j


def mp_func(i):
    try:
        st = analyze_str(i['text'])
        fcs = 'favorite_count'
        rcs = 'retweet_count'
        de = st['docEmotions']
        dt = datetime.strptime(i['created_at'], '%a %b %d %H:%M:%S +%f %Y')
        tw = {
                "hour": int(dt.hour),
                "minute": float(dt.minute),
                "st": float(st['docSentiment']['score']),
                "anger": float(de['anger']),
                "disgust": float(de['disgust']),
                "fear": float(de['fear']),
                "joy": float(de['joy']),
                "sadness": float(de['sadness']),
                "alch": st,
                "fc": 0 if fcs not in i else i[fcs],
                "rc": 0 if rcs not in i else i[rcs]
        }
    except:
        tw = {}

    return tw


def sentiment_tweets(tweets):
    # st_tweets = []
    p = Pool(5)
    st_tweets = p.map(mp_func, tweets)
    # for i in tweets:
        # try:
            # st = analyze_str(i['text'])
            # fcs = 'favorite_count'
            # rcs = 'retweet_count'
            # de = st['docEmotions']
            # tw = {
                    # "hour": datetime.strptime(i['created_at'], '%a %b %d %H:%M:%S +%f %Y').hour,
                    # "st": float(st['docSentiment']['score']),
                    # "anger": float(de['anger']),
                    # "disgust": float(de['disgust']),
                    # "fear": float(de['fear']),
                    # "joy": float(de['joy']),
                    # "sadness": float(de['sadness']),
                    # "alch": st,
                    # "fc": 0 if fcs not in st else st[fcs],
                    # "rc": 0 if rcs not in st else st[rcs]
            # }
            # st_tweets.append(tw)
        # except:
            # pass

    return st_tweets

def fast(tweets):
    texts = []
    for i in tweets:
        texts.append(i['text'])
    
    st = analyze_str(texts)
    de = st['docEmotions']
    tw = {
            "anger": float(de['anger']),
            "disgust": float(de['disgust']),
            "fear": float(de['fear']),
            "joy": float(de['joy']),
            "sadness": float(de['sadness']),
    }

    return [tw]


def best_time_to_tweet(df):
    st = df.groupby('hour').mean()['st']
    return {"hour": list(st.index), "st": st.tolist()}


def emotion_breakout(df):
    mn = df.mean()
    # return {
            # "anger": mn['anger'],
            # "disgust": mn['disgust'],
            # "fear": mn['fear'],
            # "joy": mn['joy'],
            # "sadness": mn['sadness']
    # }
    return [mn['anger'], mn['disgust'], mn['fear'], mn['joy'], mn['sadness']]


@app.route("/twitter/emo/<username>", methods=["GET"])
def twitter_emo(username):
    tweets = get_twitter_data(username)
    data = emotion_breakout(pd.DataFrame(fast(tweets)))
    return json.dumps(data), 200


@app.route("/twitter/bt/<username>", methods=["GET"])
def twitter_bt(username):
    tweets = get_twitter_data(username)
    df = pd.DataFrame(sentiment_tweets(tweets))
    df.dropna(inplace=True)
    data = best_time_to_tweet(df)
    return json.dumps(
            {
                "avg": data,
                "points": {
                    'hour': (df['hour']+(df['minute']/60)).tolist(),
                    'st': df['st'].tolist(), 'fc': df['fc'].tolist(),
                    'rf': df['rc'].tolist()
                },
                "emo": emotion_breakout(df)
            }), 200


@app.route('/testme', methods=["GET", "POST"])
def testme():
    return "hey", 200
