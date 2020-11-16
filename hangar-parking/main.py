#Gegevens
hangars = [
  {'num': 10, 'occupied': False},
  {'num': 11, 'occupied': False},
  {'num': 12, 'occupied': True},
  {'num': 13, 'occupied': False},
  {'num': 14, 'occupied': False},
  {'num': 15, 'occupied': True},
  {'num': 16, 'occupied': True},
  {'num': 17, 'occupied': False},
  {'num': 18, 'occupied': False},
  {'num': 19, 'occupied': True},
]
planesLanded = [
  {
    'code': 'ACV1',
    'type': 'Airbus A123',
    'capacity': 853,
    'hangar': 0
  },
  {
    'code': 'GOR7',
    'type': 'Boeing 909',
    'capacity': 110,
    'hangar': 0
  },
  {
    'code': 'QEN4',
    'type': 'Fokker X888',
    'capacity': 530,
    'hangar': 0
  },
  {
    'code': 'TOV2',
    'type': 'Airbus X303',
    'capacity': 495,
    'hangar': 0
  },
]

#Start program
print("Welkom bij HangarParkeerder3000\n")
running = True

def getNonParkedPlanes():
  for plane in planesLanded:
    if plane["hangar"] == 0:
      print(plane["code"] + " (type: " + plane["type"] + ")")

def getFreeHangars():
  print("Momenteel vrije hangaars:")
  for hangar in hangars:
    if hangar["occupied"] == False:
      print(hangar["num"])

while running:
  print("Deze vliegtuigen wachten om geparkeerd te worden:")
  getNonParkedPlanes()
  print("-------------------------------------------------")
  getFreeHangars()
  print("-------------------------------------------------")
  planeCode = input("Voer vliegtuigcode in: ")
  selectedHangar = input("Voer het hangaar nummer in: ")
  
  for plane in planesLanded:
    if plane["code"] == planeCode:
      plane["hangar"] = int(selectedHangar)

  for hangar in hangars:
    if hangar["num"] == int(selectedHangar):
      hangar["occupied"] = True

  print("Vliegtuig " + plane["code"] + " wordt geparkeerd in Hangaar " + selectedHangar) 
  print("-------------------------------------------------")