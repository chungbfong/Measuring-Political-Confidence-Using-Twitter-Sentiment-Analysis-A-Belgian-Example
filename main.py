# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import nltk
import json
from twython import Twython
import tweepy


def load_credentials():
    cred = open('credentials/twitter_credentials.json')
    return cred


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = load_credentials()
    data = json.load(f)

    client = tweepy.Client(data['bearer_token'])

    query_string = 'migratie -is:retweet lang:nl place_country:BE'
    tweets = client.search_all_tweets(query=query_string,start_time = "2019-09-29T18:46:19Z",end_time = "2020-10-29T18:46:19Z",max_results=500)
    print(len(tweets.data))

    for tweet in tweets.data:
        print(tweet.text)



    #twitter = Twython(data['api_key'], data['api_key_secret'], oauth_version=2)
    #ACCESS_TOKEN = twitter.obtain_access_token()
    #twitter = Twython(data['api_key'], access_token=ACCESS_TOKEN)
    """
    auth = tweepy.OAuth1UserHandler(
        consumer_key=data['api_key'],
        consumer_secret=data['api_key_secret'],
        access_token=data['access_token'],
        access_token_secret=data['access_token_secret']
    )
    api = tweepy.API(auth)
    
    """
    '''
    auth = tweepy.OAuth2UserHandler(
        consumer_key=data['api_key'],
        consumer_secret=data['api_key_secret'],
        access_token=data['access_token'],
        access_token_secret=data['access_token_secret']
    )
    print(auth)
    '''
    '''
    client = tweepy.Client(bearer_token='REPLACE_ME')

    tweets = tweepy.Cursor(api.search_full_archive, label='FullArchive', query='migratie',
                           fromDate="202008130000").items()
    #results = twitter.cursor(twitter.search, q='migratie', lang='nl',geocode="50.8467887,4.3524356,100km",max_results="500")
    print(type(tweets))
    for result in tweets:
        #print(result['text'], result['lang'],result['geo'], result['created_at'])
        print(result)
    '''
