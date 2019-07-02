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
from wordcloud import WordCloud

DATA_FILE = "tweets_small.json"

'''
get_polarity: build list of polarity values [-1.0, 1.0]
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
get_subjectivity: build list of subjectivity values [0.0, 1.0]
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
        total += value

    return total / len(alist)

'''
plot_histogram: plots given data as a histogram
'''
def plot_histogram(data, data_bins, axis_list, title, xlabel, ylabel):
    plt.hist(data, bins=data_bins)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.axis(axis_list)
    plt.grid(True)
    plt.show()

'''
build_wordcloud:
'''
def build_wordcloud(tweets, tweet_key):
    # 1. combine all tweets into one large string
    all_tweets = ""

    for tweet in tweets:
        all_tweets += tweet["text"]

    # 2. create new textblob
    big_blob = TextBlob(all_tweets)

    # 3. build frequency dictionary
    word_freq = big_blob.word_counts
    filtered = {}
    ignored_words = ["and", "about", "http", "https", "the", "with", "your", "will", "from"]

    # filter short words
    for key in word_freq:
        if (len(key) > 3) and (key not in ignored_words):
            filtered[key] = word_freq[key]

    # 4. draw a word cloud
    cloud = WordCloud().generate_from_frequencies(filtered)
    return cloud

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
    #
    # # 3. plot values in a histogram
    # p_bins = [ (x/10) for x in range(-10, 10) ]
    # # p_bins = [-1, -0.5, 0, 0.5, 1.0]      # much simpler bins
    # p_limits = [-1.1, 1.1, 0, len(all_polarity)*(2/3)]
    # plot_histogram(all_polarity, p_bins, p_limits, "Tweet Polarities", "Polarity", "Number of Tweets")
    #
    # # # using different histogram attributes
    # # bins = [-1, -0.5, 0.0, 0.5, 1]      # [x-axis values]
    # # axes = [-1.1, 1.1, 0, 90]            # [min_x, max_x, min_y, max_y]
    # # plot_histogram(all_polarity, bins, axes, "Tweet Polarities", "Polarity", "Number of Tweets")
    #
    # s_bins = [ (x/10) for x in range(0, 10) ]
    # # s_bins = [0, 0.5, 1.0]                # much simpler bins
    # s_limits = [-0.1 , 1.1, 0, len(all_subjectivity)*(2/3)]
    # plot_histogram(all_subjectivity, s_bins, s_limits, "Tweet Subjectivity", "Subjectivity", "Number of Tweets")

    # 4. create a word cloud and display it
    wc = build_wordcloud(tweetData, "text")
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()

'''
where the program actually starts when you run it
'''
if __name__ == '__main__':
    main()
