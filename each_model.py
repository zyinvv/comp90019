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


def each_models():
    #f1 = open("tweets.json","r")

    brands = get_brands()
    models = get_models()
    for brand in brands:
        try:
            f1 = open("top10\\"+ brand+"_sent.json")
            lines = f1.readline()
            while (lines):
                line = json.loads(lines)
                text = line["text"]
                for model in models:
                    model = model.rstrip("\n")
                    if model.lower() in text.lower():
                        each_item = model.split()
                        string = "_".join(each_item)
                        f = open("models\\" + string + ".json", "a")
                        f.write(lines)
                        f.close()
                        break
                lines = f1.readline()
        except:
            continue
    print("end")




each_models()
