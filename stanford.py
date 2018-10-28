from stanfordcorenlp import StanfordCoreNLP
import json
from nltk.parse.stanford import StanfordParser, StanfordDependencyParser
def sent():
    nlp = StanfordCoreNLP(r'D:\\stanford-corenlp-full-2018-10-05')


    text = 'Guangdong University of Foreign Studies is located in Guangzhou. ' \
           'GDUFS is active in a full range of international cooperation and exchanges in education. '
    props = {'annotators': 'sentiment'}

    print nlp.annotate(text, properties=props)


def a():
    eng_parser = StanfordDependencyParser(r"stanfordNLTK\jar\stanford-parser.jar",
                                          r"stanfordNLTK\jar\stanford-parser-3.6.0-models.jar",
                                          r"stanfordNLTK\jar\classifiers\englishPCFG.ser.gz")

    res = list(eng_parser.parse("the quick brown fox jumps over the lazy dog".split()))
    for row in res[0].triples():
        print(row)

    nlp = StanfordCoreNLP(r'D:\\stanford-corenlp-full-2018-10-05')

    sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
    print 'Tokenize:', nlp.word_tokenize(sentence)
    print 'Part of Speech:', nlp.pos_tag(sentence)
    print 'Named Entities:', nlp.ner(sentence)
    print 'Constituency Parsing:', nlp.parse(sentence)
    print 'Dependency Parsing:', nlp.dependency_parse(sentence)

    nlp.close()
    f = open("brands_tweets\\iphone.json")
    #file = open("brands_tweets\\iphone2.json", "a")
    lines = f.readline()
    while(lines):
        line = json.loads(lines)
        text = line["text"]
        testimonial = StanfordCoreNLP(text)
        line["sent"] = testimonial.sentiment
        f1 = open("internal.txt", "r")
        ins = f1.readline()
        sum = 0
        m = 0

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
                line["in_sent"] = sum / m
            ins = f1.readline()
        if m > 0:
            print(str(m))
            file_sent = open("brands_tweets\\iphone1_in_sent.json", "a")
            file_sent.write(json.dumps(line) + "\n")
            file_sent.close()
        #file.write(json.dumps(line)+"\n")
        lines = f.readline()
    f.close()
    #file.close()

sent()