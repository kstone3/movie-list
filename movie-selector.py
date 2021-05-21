import csv
import random

def select_movie(f):
    reader = csv.reader(f)
    chosen_row = random.choice(list(reader))
    print(chosen_row)

with open('movie-list.csv') as f:
    movies = csv.DictReader(f)
    # for row in movies:
    #     print(row['title'])
    select_movie(f)

