import tweepy
import requests
import os
import random
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()

def mainFunction():
    search = 'GossipGirl'
    tweets_number = 10
    twitter_crawl = tweepy.Cursor(api.search, search).items(tweets_number)
    for tweet in twitter_crawl:
        url = "https://imgix.bustle.com/elite-daily/2017/05/08000127/chuck-bass.jpg"
        filename = 'temp.jpg'
        request = requests.get(url, stream=True)
        if request.status_code == 200:
            with open(filename, 'wb') as image:
                for chunk in request:
                    image.write(chunk)
            sn = tweet.user.screen_name
            chuckBassPharses = ["I'm Chuck Bass", "Three letters...", "Don't worry, I'll protect you.", "Always"]
            message = random.choice(chuckBassPharses)
            m = f"@{sn} {message}"
            pic = api.media_upload('temp.jpg')
            api.update_status(m, tweet.id, media_ids=[pic.media_id_string])
            time.sleep(20)
            os.remove(filename)
        else:
            break

if __name__ == "__main__":
    mainFunction()
