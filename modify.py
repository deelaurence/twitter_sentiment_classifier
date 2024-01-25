import json

# Path to the original JSON file
original_json_path = 'train.json'

# Path to the new JSON file
new_json_path = 'train_modified.json'

# Read the original JSON file
with open(original_json_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Modify sentiment values
for entry in data:
    sentiment = entry['sentiment']
    if sentiment == 'positive':
        entry['sentiment'] = 2
    elif sentiment == 'negative':
        entry['sentiment'] = 0
    elif sentiment == 'neutral':
        entry['sentiment'] = 1

# Write the modified data to a new JSON file
with open(new_json_path, 'w', encoding='utf-8') as new_json_file:
    json.dump(data, new_json_file, indent=2)

print(f'Modification completed. New JSON file saved at: {new_json_path}')
