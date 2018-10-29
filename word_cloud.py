# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("gbk")

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

import json
import nltk
from nltk.corpus import stopwords
import re
import nltk.stem




def process_tweets():
    brands = open("brands.txt")
    brand = brands.readline()

    while(brand):

        string = ""
        string1 = ""
        brand = brand.rstrip("\n")
        try:
            file = open("top10\\" + brand + ".json")
            tweets = file.readline()

            while(tweets):
                try:
                    tweet = json.loads(tweets)
                    text = tweet["text"]
                    tokens = process_texts(text)
                    #print("1"+tokens)
                    #string = string + " " + " ".join(tokens)
                    #tokens = text.split(" ")
                    for token in tokens:
                        dicts = open("dic.txt","r")
                        dict = dicts.readline()
                        #dict = dict.rstrip("\n")
                        #print(token)

                        while(dict):
                            #print("1"+dict)
                            dict = dict.rstrip("\n")

                            if dict.lower() in token.lower():

                                string = string + " " + token.lower()
                                print("2"+token)
                                break

                            dict = dicts.readline()

                        dicts.close()

                    tweets = file.readline()

                except:
                    tweets = file.readline()
                    continue
            file.close()
            """
            file1 = open("brands_text\\" + brand + "_no_RT.json")
            tweets1 = file1.readline()

            print(string)
            while (tweets1):

                try:
                    tweet = json.loads(tweets1)
                    text = tweet["text"]
                    tokens = process_texts(text)

                    # string = string + " " + " ".join(tokens)
                    #tokens = text.split(" ")
                    for token in tokens:
                        dicts = open("dic.txt","r")
                        dict = dicts.readline()
                        #dict = dict.rstrip("\n")
                        #print(token)

                        while(dict):
                            #print("1"+dict)
                            dict = dict.rstrip("\n")

                            if dict.lower() in token.lower():

                                string1 = string1 + " " + token.lower()
                                print("1 1"+token)
                                break

                            dict = dicts.readline()

                        dicts.close()

                except:
                    tweets1 = file1.readline()
                    continue

            file.close()
            """
            word_cloud(string, brand, 0)
            #word_cloud(string1, brand, 1)

            brand = brands.readline()
        except:
            brand = brands.readline()
            continue


    print("end")

def process_features():
    brands = open("brands.txt")
    brand = brands.readline()

    while(brand):

        string = ""
        brand = brand.rstrip("\n")
        try:
            file = open("top10\\" + brand + ".json")
            tweets = file.readline()

            while(tweets):
                tweet = json.loads(tweets)
                text = tweet["text"]
                tokens = process_texts(text)

                string = string + " ".join(tokens)


                tweets = file.readline()

            file.close()

            word_cloud(string, brand, 0)
            #word_cloud(string1, brand, 1)

            brand = brands.readline()
        except:
            brand = brands.readline()
            continue


    print("end")

def process_texts(text):
    filtered = []

    if(text):
        text = text.replace("\\u"," \\u")

        text = remove_pattern(r"[RT]", text)
        text = remove_pattern(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", text)



        text = remove_pattern(r"@[\u4e00-\u9fa5\w\-]+", text)


        tokens = nltk.word_tokenize(text)


        for token in tokens:
            if not token.lower() in stopwords.words("english"):
                filtered.append(token)
        #filtered = remove_pattern(r"RT", filtered)
        #filtered = remove_pattern(r"^@", filtered)


    return filtered


def word_cloud(string, brand, n):
    print(brand)
    wc = WordCloud(background_color = "white",
                   width = 1000,
                   height = 800,
                   margin = 10
                   ).generate(string)
    if n == 0 :
        wc.to_file("top10\\" + brand + ".png")
    else:
        wc.to_file("top10\\" + brand + "_no_RT.png")
    print("q")
    plt.imshow(wc)
    plt.axis('off')
    plt.show()


def remove_pattern(pattern, input_txt):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)

    return input_txt

process_features()
#process_tweets()
#word_cloud(, "aa", 0)

