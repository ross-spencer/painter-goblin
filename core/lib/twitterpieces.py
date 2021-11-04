#!/usr/bin/python
# -*- coding: utf-8 -*

import os

# Twitter pieces
from twitter import read_token_file, Twitter, OAuth, oauth_dance

conkey = (
    "/home/ross-spencer/git/ross-spencer/painter-goblin/core/.twitter-consumer-keys"
)
creds = "/home/ross-spencer/git/ross-spencer/painter-goblin/core/.twitter-paintergoblin-credentials"


def twitter_authentication():
    CONSUMER_KEYS = conkey
    CONSUMER_KEY, CONSUMER_SECRET = read_token_file(CONSUMER_KEYS)

    MY_TWITTER_CREDS = creds
    if not os.path.exists(MY_TWITTER_CREDS):
        oauth_dance("paintergoblin", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

    oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
    twitter = Twitter(
        auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET)
    )

    return twitter


def twitter_image_authentication():
    CONSUMER_KEY, CONSUMER_SECRET = read_token_file(conkey)

    MY_TWITTER_CREDS = os.path.expanduser(creds)
    if not os.path.exists(MY_TWITTER_CREDS):
        oauth_dance("paintergoblin", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

    oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
    twitter = Twitter(
        domain="upload.twitter.com",
        auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET),
    )

    return twitter
