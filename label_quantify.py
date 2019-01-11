"""NOTE: This was used to gather the categories that were used for the training + val set as well as determining
the total number of categories"""

import json

categories = []

f = open("bdd100k_labels_images_val.json")
data = json.load(f)
for entries in data:
    for label in entries['labels']:
        if label['category'] in categories:
            pass
        else:
            categories.append(label['category'])
    
print("categories:",categories)
print("length of categories:",len(categories))