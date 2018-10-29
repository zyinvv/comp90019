# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("gbk")

import matplotlib.pyplot as plt
from wordcloud import WordCloud

import nltk.stem


import json
import nltk
from nltk.corpus import stopwords
import re
import nltk.stem

def process_tweets():
    brands = open("brands.txt")
    brand = brands.readline()

    while(brand):
        #string = ""
        brand = brand.rstrip("\n")
        print(brand)
        try:
            file = open("brands_tweets\\" + brand + ".json")

            tweets = file.readline()
            while(tweets):
                try:

                    tweet = tweets_sentiment(tweets)
                    f = open("internal.txt", "r")
                    ins = f.readline()
                    sum = 0
                    m  = 0
                    text = tweet["text"]
                    while (ins):

                        ins1 = ins.split(" ")
                        n = len(ins1)
                        # print(ins1[n-1])
                        # print(str(n))
                        ins = ins.rstrip("\n")
                        ins = ins.rstrip(ins1[n - 1])
                        ins = ins.rstrip(" ")
                        # print(ins)
                        if ins.lower() in text.lower():
                            print(ins.lower())
                            sum += float(ins1[n - 1])
                            m += 1
                            tweet["in_sent"] = sum / m
                        ins = f.readline()
                    if m > 0:
                        print(str(m))
                        file_sent = open("brands_tweets\\" + brand + "_in_sent.json", "a")
                        file_sent.write(json.dumps(tweet) + "\n")
                        file_sent.close()





                    #tweet1 = json.loads(tweets)
                    #text = tweet1["text"]
                    #print(text)
                    #tokens = tweets_tokens(text)
                    #string = string + " " + " ".join(tokens)

                    tweets = file.readline()

                except:
                    tweets = file.readline()
                    continue
            file_sent.close()
            file.close()
            #print(string)
            #word_cloud(string, brand)
            brand = brands.readline()
        except:
            brand = brands.readline()
            continue
    print("end")

def tweets_sentiment(tweets):
    f = open("pos_neg.txt")
    pos_neg = f.readlines()
    dict = {}
    for w in pos_neg:
        word, score = w.split()
        dict[word] = score

    tweet = json.loads(tweets)
    text = tweet["text"]
    text = process_texts(text)
    pos_score = 0
    neg_score = 0
    sent_score = 0
    pos1 = []
    neg1 = []

    s = nltk.stem.SnowballStemmer('english')

    if(text):

        tokens = nltk.word_tokenize(text)
        filtered = []
        for token in tokens:

            if not token.lower() in stopwords.words("english"):
                filtered.append(token.lower())
        for token in filtered:

            token1 = s.stem(token)
            for sent, score in dict.items():
                if sent == token1 or sent == token:
                    if score == "1" :
                        pos_score += 1
                        sent_score += 1
                        pos1.append(sent)
                    else:
                        neg_score += 1
                        sent_score += -1
                        neg1.append(sent)

                    break


    tweet["pos"] = pos_score
    tweet["neg"] = neg_score
    tweet["sentiment"] = sent_score
    tweet["pos1"] = pos1
    tweet["neg1"] = neg1


    #print(json.dumps(tweet) )

    return tweet

def process_texts(text):
    filtered = []

    if(text):
        text = text.replace("\\u"," \\u")

        text = remove_pattern(r"[RT|\"|\']", text)
        text = remove_pattern(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", text)
        #print(text)


        text = remove_pattern(r"@[\u4e00-\u9fa5\w\-]+", text)


        tokens = nltk.word_tokenize(text)


        for token in tokens:
            if not token.lower() in stopwords.words("english"):
                filtered.append(token)
        #filtered = remove_pattern(r"RT", filtered)
        #filtered = remove_pattern(r"^@", filtered)


    return text


def word_cloud(string, brand):
    wc = WordCloud(background_color = "white",
                   width = 1000,
                   height = 800,
                   margin = 10
                   ).generate(string)
    wc.to_file("brands_text\\" + brand + ".png")
    print("q")
    plt.imshow(wc)
    plt.axis('off')
    plt.show()


def remove_pattern(pattern, input_txt):
    r = re.findall(pattern, input_txt)

    for i in r:
        input_txt = re.sub(i, '', input_txt)

    return input_txt

process_tweets()

