import csv
import json

# Specify the paths for your CSV and JSON files
csv_file_path = 'train.csv'
json_file_path = 'train.json'

# Read the CSV file and convert the selected fields to a list of dictionaries
csv_data = []
with open(csv_file_path, 'r', encoding='latin-1') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Extract only the desired fields
        selected_fields = {
            'text': row['text'],
            'selected_text': row['selected_text'],
            'sentiment': row['sentiment']
        }
        csv_data.append(selected_fields)

# Write the list of dictionaries to a JSON file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(csv_data, json_file, indent=2)

print(f'Conversion completed. JSON file saved at: {json_file_path}')
