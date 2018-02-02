import string
import tweepy
import json
import os
import re

target_tag = '#beepboop'

consumer_key = 'XXXX'
consumer_secret = 'XXXX'
access_key = 'XXXX-XXXX'
access_secret = 'XXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

script_dir = os.path.dirname(__file__)
tweet_file = 'data/hex.txt'
tweet_path = os.path.join(script_dir, tweet_file)


class PrintListener(tweepy.StreamListener):

    def on_data(self, data):
        tweet = json.loads(data)
        try:
            z = tweet['text'].encode('ascii', 'ignore')

            post = re.search(
                r'^#(?:[0-9a-fA-F]{3}){1,2}$', z)

            if target_tag in z.decode('ascii'):
                tags = []
                a = ''.join(filter(lambda x: x in string.printable, str(z)))
                for tag in a.split(' '):
                    if tag.startswith('#'):
                        tags.append(tag.strip(','))

                if tags:
                    tags.remove(target_tag)
                    for tag in tags:
                        match = re.search(
                            r'^#(?:[0-9a-fA-F]{3}){1,2}$', tag[:-1])
                        if match:
                            print('Got one!')
                        with open(tweet_path, 'w')as f:
                            f.write(match.group())

        except Exception as e:
            print(e)

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    print('Starting stream')
    listener = PrintListener()
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=[target_tag])
