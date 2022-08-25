import csv
import json

files = ['ad', 'category', 'location', 'user']

def csv_to_json(file):
    with open(f'data_csv/{file}.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        if file == 'ad':
            for row in rows:
                if row.get('is_published') == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False
            
     
    with open(f'data_json/{file}.json', 'w', encoding='utf-8') as f:
        json.dump(rows, f, indent=4, ensure_ascii=False)

for file in files:    
    csv_to_json(file)
