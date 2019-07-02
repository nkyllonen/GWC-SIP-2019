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
make_textblob: example function -- change this however you want!
'''
def make_textblob(string):
    # Textblob sample:
    tb = TextBlob(string)
    return tb

'''
main: this is our main function where everything happens
'''
def main():
    #Get the JSON data
    with open(DATA_FILE, "r") as tweetFile:
        tweetData = json.load(tweetFile)

    blob = make_textblob("You are a brilliant computer scientist.")
    print(blob.polarity)

if __name__ == '__main__':
    main()
