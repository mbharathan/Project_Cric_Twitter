import twitter
import os
api = twitter.Api(consumer_key=os.environ.get('CONSUMER_KEY'),
                                          consumer_secret=os.environ.get('CONSUMER_SECRET'),
                                          access_token_key=os.environ.get('ACCESS_TOKEN_KEY'),
                                          access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET'))

status = api.PostUpdate("Hey!")
print("Tweeted as " + status.text)
