#!/usr/bin/env python
# encoding: utf-8
"""
retweetbot.py

Created by Pascal Bruno on 2013-03-30.
Copyright (c) 2013 Pascal Bruno. All rights reserved.

A twitter bot that retweets any tweet containing a
particular hashtag
"""

from twitter import * # Mike Verdone's twitter API wrapper (https://github.com/sixohsix/twitter)
import time

# Get your tokens and keys from dev.twitter.com
OAUTH_TOKEN = ""
OAUTH_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
TWEET_ID_CACHE = "last_seen.txt" # filename where last seen tweet id will be store
HASHTAG = "#haiti" # Desired hashtag to retweet

def __init__():
    last_tweet_id = get_last_seen()

    tweets = t.search.tweets(q=HASHTAG, count=1, since_id=last_tweet_id)

    try:
        tweetid = tweets["statuses"][0]["id"]
        t.statuses.retweet(id=tweetid)
        f = open(TWEET_ID_CACHE, 'w')
        f.write(str(tweetid))
        f.close()
    except:
        pass

def get_last_seen():
    try:
        f = open(TWEET_ID_CACHE, 'r')
        last_tweet_id = f.read()
        f.close()
    except IOError:
        last_tweet_id = None        
    return last_tweet_id

if __name__ == '__main__':
    t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
    while (1):
        __init__()
        time.sleep(15)