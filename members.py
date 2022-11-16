import csv
import manage.team_information as team_information

print(team_information.members)

columns = ["성", "이름", "소속", "국적", "나이"]

with open("members.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    writer.writerows(team_information.members)
