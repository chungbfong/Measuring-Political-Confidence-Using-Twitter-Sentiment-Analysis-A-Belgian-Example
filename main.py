# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import nltk
import json
from twython import Twython


def load_credentials():
    cred = open('credentials/twitter_credentials.json')
    return cred


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = load_credentials()
    data = json.load(f)
    twitter = Twython(data['api_key'], data['api_key_secret'], oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    twitter = Twython(data['api_key'], access_token=ACCESS_TOKEN)
    results = twitter.cursor(twitter.search, q='migratie')
    for result in results:
        print(result['text'], result['lang'],result['geo'])

