import csv
import json


with open('data_csv/ads.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    for row in rows:
        row['is_published'] = True
 
    
with open('ads.json', 'w', encoding='utf-8') as f:
    json.dump(rows, f, indent=4, ensure_ascii=False)
    

with open('data_csv/categories.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)


with open('categories.json', 'w', encoding='utf-8') as f:
    json.dump(rows, f, indent=4, ensure_ascii=False)