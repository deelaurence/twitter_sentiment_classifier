import json

# Path to the original JSON file
original_json_path = 'train_modified.json'


# Read the original JSON file

positive=[]
negative=[]
neutral=[]


with open(original_json_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Modify sentiment values
for entry in data:
    sentiment = entry['sentiment']
    if sentiment == 2:
        positive.append(entry)
    elif sentiment == 0:
        negative.append(entry)
    elif sentiment == 1:
        neutral.append(entry)


print(f"positive is {len(positive)}")
print(f"negative is {len(negative)}")
print(f"neutral is {len(neutral)}")