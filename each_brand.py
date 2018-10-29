import json

def get_models():
    f = open("models.txt","r")
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


def each_brand():
    #f1 = open("tweets.json","r")
    f1 = open("tweets1_texts.json")
    items = get_models()
    lines = f1.readline()
    while(lines):
        print(lines)
        try:
            #lines = lines.rstrip(",\n")
            line = json.loads(lines)
            text = line["text"]
            for item in items:
                each_item = item.split()
                p = 0
                for i in each_item:
                    if i in text.lower():
                        p = p + 1
                if p == len(each_item) and item.lower() in text.lower():
                    if each_item[0] == "galaxy":
                        f = open("brands_tweets\\samsung.json", "a")
                        f.write(lines)
                        f.close()
                    elif each_item[0] == "redmi":
                        f = open("brands_tweets\\xiaomi.json", "a")
                        f.write(lines)
                        f.close()
                    elif each_item[0] == "zenfone":
                        f = open("brands_tweets\\asus.json", "a")
                        f.write(lines)
                        f.close()
                    elif each_item[0] == "moto":
                        f = open("brands_tweets\\motorola.json", "a")
                        f.write(lines)
                        f.close()
                    elif each_item[0] == "aquos":
                        f = open("brands_tweets\\sharp.json", "a")
                        f.write(lines)
                        f.close()
                    elif each_item[0] == "xperia":
                        f = open("brands_tweets\\sony.json", "a")
                        f.write(lines)
                        f.close()
                    elif each_item[0] == "nubia":
                        f = open("brands_tweets\\zte.json", "a")
                        f.write(lines)
                        f.close()
                    else:
                        f = open("brands_tweets\\" + each_item[0] + ".json", "a")
                        f.write(lines)
                        f.close()
                    break

            lines = f1.readline()
        except:
            lines = f1.readline()
            continue
    print("end")

each_brand()
