import csv

file_name = "netflix_list.csv"

# Read csv to list
headers = []
csv_list = []
with open(file_name, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')

    headers = next(f).split(',')

    for row in csv_reader:
        csv_list.append(row)

# Rating > 7.5 comprehension
rating_index = headers.index("rating")
rating_75_list = [x for x in csv_list if x[rating_index] != "" and float(x[rating_index]) > 7.5]

for i in rating_75_list: # list preview (name and rating only)
    print(f"{i[1]}, {i[rating_index]}")

# Only first 5 columns
only_5_columns = [x[:5] for x in csv_list]

for i in only_5_columns:
    print(i)

# Generator english only
def only_eng_generator(lst):
    lang_index = headers.index('language')
    for i in lst:
        if i[lang_index] == 'English':
            yield i

for row in only_eng_generator(csv_list):
    print(f"{row[1]} - {row[10]}")

# Generator only ended after 2015
def only_ended_15_generator(lst):
    end_index = headers.index('endYear')
    for i in lst:
        if i[end_index] != '' and int(i[end_index]) >= 2015:
            yield i

for row in only_ended_15_generator(csv_list):
    print(f"{row[1]} - {row[5]}")