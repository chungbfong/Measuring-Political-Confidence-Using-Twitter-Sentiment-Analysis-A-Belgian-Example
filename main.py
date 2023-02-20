# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from datetime import datetime
import nltk
import json
import tweepy
import preprocessor as p
p.set_options(p.OPT.URL, p.OPT.EMOJI)
import pprint
import re

def load_credentials():
    cred = open('credentials/twitter_credentials.json')
    return cred

def parseItemHandler(parseItemList):
    if parseItemList != None:
        returnList = []
        for p in parseItemList:
            returnList.append(p.match)

        return returnList

    else:
        return None


def query_tweets(client,user,keyword):
    json_list = []

    query_string = ''

    if user != '':
        query_string += 'from:' + user
    if keyword != '':
        query_string += ' ' + keyword

    query_string += ' -is:retweet lang:nl place_country:BE'
    print(query_string)
    tweets = client.search_all_tweets(query=query_string,start_time = "2022-02-15T18:46:19Z",end_time = "2023-2-15T18:46:19Z",max_results=500,tweet_fields=['created_at','id',"author_id","public_metrics"])
    print(len(tweets.data))

    for tweet in tweets.data:
        print(tweet)
        parsed_tweet = p.parse(tweet.text)
        if parsed_tweet.urls :
            print(type(parsed_tweet.urls[0]))
        json_obj = {
            'mentions':parsed_tweet.mentions,
            'hashtags':parsed_tweet.hashtags,
            'urls':parseItemHandler(parsed_tweet.urls),
            'emojis':parseItemHandler(parsed_tweet.emojis),
            'text': ''.join(p.clean(tweet.text)),
            'created_at': tweet.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
            'author_id':tweet.author_id,
            'public_metrics':tweet.public_metrics
        }
        pprint.pprint(json_obj)
        json_list.append(json_obj)
    return json_list

def process_tweet(client,user,keyword):

    filename = keyword if user == "" else user + '_' + keyword
    with open(filename+'.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(query_tweets(client,user,keyword)))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = load_credentials()
    data = json.load(f)

    client = tweepy.Client(data['bearer_token'])
    process_tweet(client,"","migratie")




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
