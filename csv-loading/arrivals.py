import csv

file = open("arrivals.csv", "r", encoding="UTF-8")
reader = csv.DictReader(file)
data = list(reader)

for flight in data:
    print(f"At {flight['arrival']} a {flight['airline']} flight arrived from the city of {flight['origin']} carrying {flight['passengers']} passengers")

file.close()
