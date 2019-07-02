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
get_subjectivity: build list of polarity values
    tweets(list)    :   list of dictionaries
    tweet_key(str)  :   string of dictionary key
'''
def get_subjectivity(tweets, tweet_key):
    subjectivity = []

    # loop through all tweets
    for tweet in tweets:
        text = tweet[tweet_key]
        blob = TextBlob(text)
        subjectivity.append(blob.subjectivity)

    return subjectivity

'''
calc_average: calculate average value
    alist(list)     :   list of floats
'''
def calc_average(alist):
    total = 0

    for value in alist:
        total =+ value

    return total / len(alist)

'''
main: this is our main function where everything happens
'''
def main():
    #Get the JSON data
    with open(DATA_FILE, "r") as tweetFile:
        tweetData = json.load(tweetFile)

    # 1. parse the text of each tweet -- get data from each text
    all_polarity = get_polarity(tweetData, "text")
    all_subjectivity = get_subjectivity(tweetData, "text")

    # 2. calculate averages
    ave_polarity = calc_average(all_polarity)
    ave_subjectivity = calc_average(all_subjectivity)

    print("Average polarity: ", ave_polarity)
    print("Average subjectivity: ", ave_subjectivity)

'''
where the program actually starts when you run it
'''
if __name__ == '__main__':
    main()
