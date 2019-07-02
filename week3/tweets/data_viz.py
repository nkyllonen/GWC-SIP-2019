'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!

original starter code:
https://github.com/GirlsFirst/SIP-2018-starter/blob/master/U2-Applications/U2.1-Data/data_vis_project_starter.py
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

DATA_FILE = "tweets_small.json"

'''
get_polarity: build list of polarity values
    tweets(list)    :   list of dictionaries
    tweet_key(str)  :   string of dictionary key
'''
def get_polarity(tweets, tweet_key):
    polarity = []

    # loop through all tweets
    for tweet in tweets:
        text = tweet[tweet_key]
        blob = TextBlob(text)
        polarity.append(blob.polarity)

    return polarity

'''
main: this is our main function where everything happens
'''
def main():
    #Get the JSON data
    with open(DATA_FILE, "r") as tweetFile:
        tweetData = json.load(tweetFile)

    # parse the text of each tweet -- get polarity of each text
    all_polarity = get_polarity(tweetData, "text")

'''
where the program actually starts when you run it
'''
if __name__ == '__main__':
    main()
