import csv

# csv header
fieldnames = ['date', 'mood', 'journal-entry']

# csv data - we would get this from javascript
rows = [
    {'date': 'Jan. 15, 2023',
    'mood': 'happy',
    'journal-entry': 'I was feeling very happy today :))'},
    {'date': 'Jan. 16, 2023',
     'mood': 'sad',
     'journal-entry': 'It did not go well. I am sad'},
    {'date': 'Jan. 17, 2023',
     'mood': 'disappointed',
     'journal-entry': 'WHy am I here? What is the meaning of life?'}
]

# each row is a dictionary (set of 2 key-value pairs)
# each dictionary contains:
#      mood - string representation of emoji
#      journal entry - a paragraph of text

with open('data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)