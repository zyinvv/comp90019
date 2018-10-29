from stanfordcorenlp import StanfordCoreNLP
import json
import nltk


def sent1():
    print(features)
    text = 'the phone has good camera. '
    score = 0
    nlp = StanfordCoreNLP(r'D:\\stanford-corenlp-full-2018-10-05')

    tokens = nlp.word_tokenize(text)
    print(tokens)

    dep = nlp.dependency_parse(text)
    print(dep)

    for d in dep:
        try:
            if d[0].lower() != "root":
                #(a,b,c) = d
                string= d[0] +", "+ tokens[d[1]].lower() +", "+ tokens[d[2]].lower()
                print(string)
                if tokens[d[1]].lower() in features and tokens[d[2]].lower() in sent_words.keys():
                    if sent_words[tokens[d[2]].lower()] == "-1":
                        score += -1
                    else:
                        score += 1
                elif tokens[d[2]].lower() in features and tokens[d[1]].lower() in sent_words.keys():
                    if sent_words[tokens[d[1]].lower()] == "-1":
                        score += -1
                    else:
                        score += 1
                print "o"
        except:
            continue


    print score
    nlp.close()


def get_features():
    feature = []
    file = open("camera.txt", "r")
    f = file.readline()
    while(f):
        f = f.rstrip("\n")
        feature.append(f.lower())
        f = file.readline()
    return feature

def get_sents():
    sents = {}
    file = open("pos_neg.txt", "r")
    s = file.readlines()
    for w in s:
        word, score = w.split()
        sents[word.lower()] = score
    return sents

features = get_features()
sent_words = get_sents()

def stan(text):

    score = 0
    nlp = StanfordCoreNLP(r'D:\\stanford-corenlp-full-2018-10-05')

    tokens = nlp.word_tokenize(text)

    print(tokens)

    dep = nlp.dependency_parse(text)
    print(dep)
    for d in dep:
        try:
            if d[0] != "root":
                if tokens[d[1]].lower() in features and tokens[d[2]].lower() in sent_words.keys():
                    if sent_words[tokens[d[2]].lower()] == "-1":
                        score += -1
                    else:
                        score += 1
                elif tokens[d[2]].lower() in features and tokens[d[1]].lower() in sent_words.keys():
                    if sent_words[tokens[d[1]].lower()] == "-1":
                        score += -1
                    else:
                        score += 1
                print score
        except:
            continue


    nlp.close()
    return score

def get_brands():
    f = open("brands.txt")
    brands = []
    brand = f.readline()
    while (brand):
        brands.append(brand.rstrip("\n"))
        brand = f.readline()
    return brands

def get_sent():
    for brand in get_brands():
        try:
            brand = brand.rstrip("\n")
            file = open("brands_tweets\\" + brand + ".json")
            print(brand)
            tweets = file.readline()
            while (tweets):
                tweet = json.loads(tweets)
                text = tweet["text"]

                for feature in features:
                    if feature.lower() in text.lower():
                        print(text)

                        score = stan(text)
                        tweet["sent"] = score


                        file_sent = open("brands_tweets\\" + brand + "_in_sent.json", "a")
                        file_sent.write(json.dumps(tweet) + "\n")
                        file_sent.close()
                        break

                tweets = file.readline()
            file.close()
        except:
            continue




    print("end")






sent1()

#get_sent()