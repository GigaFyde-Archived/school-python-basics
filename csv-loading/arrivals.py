import csv

file = open("arrivals.csv", "r", encoding="UTF-8")
reader = csv.DictReader(file)
data = list(reader)
totalFlights = len(data)
totalPassengers = 0

for flight in data:
    print(f"At {flight['arrival']} a {flight['airline']} flight arrived from the city of {flight['origin']} carrying {flight['passengers']} passengers")
    totalPassengers += int(flight['passengers'])

averagePassengers = totalPassengers / totalFlights
print(f"Aantal vluchten: " + str(totalFlights))
print(f"Totaal aantal passagiers: " + str(totalPassengers))
print(f"Gemiddeld aantal passagiers per vlucht: " + str((int(averagePassengers))))
file.close()
