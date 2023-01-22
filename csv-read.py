import csv

with open('data.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            print(f'On {row[0]}, you were feeling {row[1]}. You wrote: {row[2]}')




# row[0] - date
# row[1] - mood
# row[2] - journal entry