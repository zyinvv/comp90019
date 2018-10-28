import json
import tweepy
from tweepy import Stream

from tweepy.streaming import StreamListener

import time


consumer_key = "mRiNh0EgatebQNGaoXWy6GmPP"
consumer_secret = "1ofB8abdiB5oFf0SBvKZ2246LV9q6b7tFpo5aJgs5nOuKoufgh"
access_token = "987233892175265792-BoTv6Tz7RCbTkTQjlRsTdo7cAeo0sdy"
access_secret = "Y6R3Yubb1mkKTq5wmQDlTONJhO4G31exTX5uDsszcAqef"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

class StdOutListener(StreamListener):


    # This function gets called every time a new tweet is received on the stream
    def on_data(self, data):
        
        # Just write data to one line in the file
        try:
            # Convert the data to a json object (shouldn't do this in production; might slow down and miss tweets)
            all_data = json.loads(data)

            if all_data['lang'] == 'en':
                models = get_models()
                new_data = {}
                new_data["id"] = all_data["id"]
                new_data["text"] = all_data["text"]
                print("1")
                for model in models:
                    if model.lower() in all_data["text"].lower():
                        print("2")
                        tweets = process_tweet(all_data)

                        file.write(data + "\n")
                        f.write(json.dumps(new_data) + "\n")
                        f1.write(json.dumps(tweets) + "\n")
                        break
                    else:
                        continue



                text = all_data["text"]  # The text of the tweet


                #print(text)  # Print it out
        except:
            return True


    def on_error(self, status):
        print(status)

def process_tweet(data):
    tweet = {}
    tweet["id "]= ["id"]
    tweet["text"] = ["text"]
    tweet["user"] = data["user"]
    tweet["entities"] = data["entities"]
    return tweet

def get_models():
    f = open("models.txt")
    models = []
    model = f.readline()
    while(model):
        models.append(model.rstrip("\n"))
        model = f.readline()
    return models

def get_brands():
    f = open("brands.txt")
    brands = []
    brand = f.readline()
    while(brand):
        brands.append(brand.rstrip("\n"))
        brand = f.readline()
    return brands


if __name__ == "__main__":

    items = get_brands()
    while True:
        # Create a file to store output. "a" means append (add on to previous file)
        file = open("tweets1.json", "a")
        f = open("tweets1_texts.json","a")
        f1 = open("tweets1_simple.json", "a")
        # Create the listener
        listener = StdOutListener()

        # Connect to the Twitter stream
        stream = Stream(auth, listener)

        # Terms to track
        try:
            stream.filter(track = items)# Need to create Terms including the brands of phones


        except Exception as e:
            print(e)
            stream.disconnect()
        #time.sleep(60)

    # Close the file
    file.close()
