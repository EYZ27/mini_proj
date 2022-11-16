import csv
loaded_members = []

with open("members.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        loaded_members.append(row)

# 문제코드
print(loaded_members)
