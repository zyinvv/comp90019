from textblob import TextBlob
import json

def get_brands():
    f = open("brands.txt")
    brands = []
    brand = f.readline()
    while(brand):
        brands.append(brand.rstrip("\n"))
        brand = f.readline()
    return brands

def sent1():

    for brand in ["samsung"]:
        try:
            f = open("top10\\" + brand + ".json")
            lines = f.readline()
            while (lines):
                line = json.loads(lines)
                text = line["text"]
                testimonial = TextBlob(text)
                line["sent"] = testimonial.sentiment
                file = open("top10\\" + brand + "_sent.json","a")
                file.write(json.dumps(line)+"\n")
                file.close()
                lines = f.readline()
        except:
            print(brand)
            continue
    print("end")



def sent():
    for brand in get_brands():
        f = open("brands_tweets\\" + brand + ".json")
        lines = f.readline()
        while (lines):
            line = json.loads(lines)
            text = line["text"]
            testimonial = TextBlob(text)
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
            # file.write(json.dumps(line)+"\n")
            lines = f.readline()
        f.close()
        # file.close()

sent1()