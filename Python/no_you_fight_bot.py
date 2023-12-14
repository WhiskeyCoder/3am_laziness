from twython import Twython
import time
import os

APP_KEY = os.environ['APP_KEY_HERE']
APP_SECRET = os.environ['APP_SECRET_HERE']
OAUTH_TOKEN = os.environ['OAUTH_TOKEN_HERE']
OAUTH_TOKEN_SECRET = os.environ['OAUTH_TOKEN_SECRET_HERE']
user = USERNAME

while True:
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    text_to_tweet = (f"@{user} No You!")
    twitter.update_status(status=text_to_tweet)
    print(f"Trolling {user} until they give up")
    time.sleep(5)
