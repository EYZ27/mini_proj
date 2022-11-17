from Manage import Manage
import csv

members = []

# members 리스트 구성하기
with open("members.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        members.append(row)

manage_system = Manage()

print('1. generate_introduce')
for member in members:
    print(manage_system.generate_introduce(member))
print()
print('2. compare_age')
print(manage_system.compare_age(members[0], members[4]))