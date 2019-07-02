import json

DATA_FILE = "tweets_small.json"

def main():
    # open and load JSON data
    # tweetfile = open(DATA_FILE, "r")
    # tweetData = json.load(tweetfile)
    # tweetfile.close()

    # OTHER way to load data
    with open(DATA_FILE, "r") as tweetfile:
        tweetData = json.load(tweetfile)

    # print id of first tweet
    print("Tweet id: ", tweetData[0]["id"])

    # print text of first tweet
    print("Tweet text: ", tweetData[0]["text"])

    # print id of all the tweets
    for i in range(len(tweetData)):
        print("Tweet id: ", tweetData[i]["id"])

    print("\nUsing other for loop:")

    # print ids using for-each loop
    for tweet in tweetData:
        print("Tweet id: " , tweet["id"])

if __name__ == "__main__":
    main()
