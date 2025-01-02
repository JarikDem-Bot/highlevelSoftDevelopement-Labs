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

# itarator to return 10 first cast if it's length more that 50 chars
class CastIterator:
    def __init__(self, lst, field):
        self.lst = lst
        self.index = 0
        self.field = field

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration
        else:
            if len(self.lst[self.index][self.field]) > 50:
                self.index += 1
                return self.lst[self.index-1][self.field]
            else:
                self.index += 1
                return self.__next__()

iter = CastIterator(csv_list, headers.index("cast"))
for i, cast in enumerate(iter):
    print(f"Cast {i+1}: {cast}")
    if i == 9:
        break

# function to count adult movies
def count_adult(lst):
    adult_index = headers.index("isAdult")
    count = 0
    for i in lst:
        if i[adult_index] == '1':
            count += 1
    return count

print(f"Adult movies: {count_adult(csv_list)}")

# function to find rating of movie woth 1k+ votes
def rating_1k(lst):
    rating_index = headers.index("rating")
    votes_index = headers.index("numVotes")
    name_index = headers.index("title")
    for i in lst:
        if i[votes_index] != "" and int(float(i[votes_index])) >= 1000:
            print(f"Name: {i[name_index]} \tRating: {i[rating_index]}, \tvotes: {i[votes_index]}")

rating_1k(csv_list)

# generators to create list of titles with 10+ episodes
def episodes_10(lst):
    name_index = headers.index("title")
    episodes_index = headers.index("episodes")

    return [i[name_index] for i in lst if i[episodes_index] != "" and int(float(i[episodes_index])) >= 10]

print(episodes_10(csv_list))

# function to find movie with ratings higher than median
def rating_median(lst):
    rating_index = headers.index("rating")
    name_index = headers.index("title")

    ratings = [float(i[rating_index]) for i in lst if i[rating_index] != ""]
    median = sum(ratings) / len(ratings)

    return [i[name_index] for i in lst if i[rating_index] != "" and float(i[rating_index]) > median]

print(rating_median(csv_list))