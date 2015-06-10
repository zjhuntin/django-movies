import csv
import chardet

print("Converting users...")
with open("data/ml-1m/users.dat") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    with open("data/ml-1m/users.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        for row in reader:
            writer.writerow(row[::2])

print("Converting movies...")
with open("data/ml-1m/movies.dat", encoding="windows-1252") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    with open("data/ml-1m/movies.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        for row in reader:
            writer.writerow(row[0:2])

print("Converting ratings...")
with open("data/ml-1m/ratings.dat") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    with open("data/ml-1m/ratings.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        for row in reader:
            writer.writerow(row)
