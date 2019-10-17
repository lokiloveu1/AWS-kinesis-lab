import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import pandas as pd
import csv
import re #regular expression
from textblob import TextBlob
import string
import preprocessor as p
import os
import boto3
from TwitterAPI import TwitterAPI
import random


#Twitter credentials for the app
consumer_key = 'RgEBtuy#9zFQd2ZR'
consumer_secret = 'k1mdokyHz4L#g1Wqvfjxjw'
access_token = '86197053544#EIz3INw2a'
access_secret = 'k3HKmYcvW#lmcr5RxyKFe4K'

#pass twitter credentials to tweepy
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = TwitterAPI(consumer_key, consumer_secret, access_token, access_secret)


# Collect tweets
kinesis = boto3.client('kinesis')

r = api.request('statuses/filter', {'locations':'-90,-90,90,90'})
tweets = []
count = 0

for item in r:
        jsonItem = json.dumps(item)
        tweets.append({'Data':jsonItem, 'PartitionKey':str(random.randint(1, 1000))})
        count += 1
        if count == 100:
                print('start streaming...')
                kinesis.put_records(StreamName="twitter", Records=tweets)
                count = 0
                tweets = []


