import json
import tweepy
from tweepy import Stream

from tweepy.streaming import StreamListener

import time

consumer_key = 'mRiNh0EgatebQNGaoXWy6GmPP'
consumer_secret = '1ofB8abdiB5oFf0SBvKZ2246LV9q6b7tFpo5aJgs5nOuKoufgh'
access_token = '987233892175265792-BoTv6Tz7RCbTkTQjlRsTdo7cAeo0sdy'
access_secret = 'Y6R3Yubb1mkKTq5wmQDlTONJhO4G31exTX5uDsszcAqef'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

brand = ["acer","alcatel","allview","amazon","amoi","iphone","archos","asus","at&t",\
         "benefon","benq","benq_siemens","bird","blackberry","blackview","blu",\
         "bosch","bq","casio","cat","celkon","chea","coolpad","dell","ee","emporia",\
         "energizer","ericsson","eten","fujitsu siemens","garmin-asus","gigabyte",\
         "gionee","google","haier","hp","htc","huawei","i-mate","i-mobile","icemobile",\
         "innostream","inq","intex","jolla","karbonn","kyocera","lava","leeco","lenovo",\
         "lg","maxon","maxwest","meizu","micromax","microsoft","mitac","mitsubishi",\
         "modu","motorola","mwg","nec","neonode","niu","nokia","nvidia","o2","oneplus",\
         "oppo","orange","palm","panasonic","pantech","parla","philips","plum","posh",\
         "prestigio","qmobile","qtek","razer","sagem","samsung","sendo","sewon",\
         "sharp","siemens","sonim","sony","sony ericsson","spice","t-molie","tel.me.",\
         "telit","thuraya","toshiba","unnecto","vertu","verykool","vivo","vk mobile",\
         "vodafone","wiko","wnd","xcute","xiaomi","xolo","yezz","yota","yu","zte"]

t = "alcatel" or "allview" or "amazon" or "amoi" or\
    "iphone" or "archos" or "asus" or "at&t" or "benefon" or\
    "benq" or "benq_siemens" or "bird" or "blackberry" or\
    "blackview" or "blu" or "bosch" or "bq" or "casio" or \
    "cat" or "celkon" or "chea" or "coolpad" or "dell" or \
    "ee" or "emporia" or "energizer" or "ericsson" or "eten" or\
    "fujitsu siemens" or "garmin-asus" or "gigabyte" or \
    "gionee" or "google" or "haier" or "hp" or "htc" or "huawei" or\
    "i-mate" or "i-mobile" or "icemobile" or "innostream" or\
    "inq" or "intex" or "jolla" or "karbonn" or "kyocera" or \
    "lava" or "leeco" or "lenovo" or "lg" or "maxon" or "maxwest" or\
    "meizu" or "micromax" or "microsoft" or "mitac" or \
    "mitsubishi" or "modu" or "motorola" or "mwg" or "nec" or \
    "neonode" or "niu" or "nokia" or "nvidia" or "o2" or "oneplus" or\
    "oppo" or "orange" or "palm" or "panasonic" or "pantech" or\
    "parla" or "philips" or "plum" or "posh" or "prestigio" or \
    "qmobile" or "qtek" or "razer" or "sagem" or "samsung" or \
    "sendo" or "sewon" or "sharp" or "siemens" or "Smartisan" or "sonim" or "sony" or\
    "sony ericsson" or "spice" or "t-molie" or "tel.me." or \
    "telit" or "thuraya" or "toshiba" or "unnecto" or "vertu" or\
    "verykool" or "vivo" or "vk mobile" or "vodafone" or "wiko" or\
    "wnd" or "xcute" or "xiaomi" or "xolo" or "yezz" or "yota" or \
    "yu" or "zte"

def search():
    f = open('100tweets.json','a')
    f.write("{\"tweets\":[\n")
    file = open ("100texts.json","a")
    file.write("{\"tweets\":[\n")
    i=0
    for tweet in tweepy.Cursor(api.search,
                               q = "phone" ,
                               lang = "en").items(100):


        all_data = tweet._json
        data = {}
        data["id"] = all_data["id"]
        data["text"] = all_data["text"]
        #data["hashtags"] = all_data["entities"]["hashtags"]

        i=i+1
        if i == 100:
            f.write(json.dumps(all_data)+"\n")
            file.write(json.dumps(data)+"\n")
        else:
            f.write(json.dumps(all_data) + ",\n")
            file.write(json.dumps(data)+",\n")
        print(json.dumps(all_data))
    print(i)
    f.write("]}")
    file.write("]}")
    f.close()
    file.close()


search()




