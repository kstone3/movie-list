import csv

def printMovies():
    for row in movies:
        print("Title: " + row['title'] + "\tYear: " + row['year'])

with open('movie-list.csv') as f:
    movies = csv.DictReader(f)
    printMovies()