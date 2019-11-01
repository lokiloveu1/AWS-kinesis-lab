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
#import twitterCreds

#Twitter credentials for the app
consumer_key = 'RgEBtuy#359zFQd2ZR'
consumer_secret = 'k1mdokyHz4L#GeSpNMmpKg1Wqvfjxjw'
access_token = '861970535441326#RcyM8XEIz3INw2a'
access_secret = 'k3HKmYcvWRBo#r5RxyKFe4K'

#pass twitter credentials to tweepy
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# Collect tweets
kinesis_client = boto3.client('kinesis')


class KinesisStreamProducer(tweepy.StreamListener):

	def __init__(self, kinesis_client):
		self.kinesis_client = kinesis_client

	def on_data(self, data):
		tweet = json.loads(data)
		self.kinesis_client.put_record(StreamName='twitter', Data=tweet["text"], PartitionKey="key")
		print("Publishing record to the stream: ", tweet)
		return True

	def on_error(self, status):
		print("Error: " + str(status))

def main():
	mylistener = KinesisStreamProducer(kinesis_client)
	myStream = tweepy.Stream(auth = auth, listener = mylistener)
	myStream.filter(track=['#aws'])
	rint("pushing data into kinesis...")

if __name__ == "__main__":
	main()

