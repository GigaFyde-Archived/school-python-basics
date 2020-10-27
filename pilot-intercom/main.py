pilotName = input("Enter Pilot name\n")
planeName = input("Enter Plane name\n")
currentFlightHeightinFoot = input("Enter current flight height in foot\n")
desiredFlightHeightInFoot = input("Enter desired flight height in foot\n")
isTurbulenceExpected = input("Is Turbulence expected? Yes/No\n")
flightDuration = input("What is the expected duration of the flight? Please enter in full\n")
arrivalDestination = input("What is the destination of arrival?\n")
arrivalTime = input("What is the arrival time?\n")
pointOfInterest = input("What is the point of interest?\n")
weatherCircumstances = input("What are the weather circumstances\n")
clearSkies = input("Are the skies clear for flight? Yes/No\n")
weatherCircumstancesDestination = input("What is the weather at the place of destination\n")
degreesTemperature = input("Please enter the temperature\n")

if isTurbulenceExpected:
    turbulenceText = "bumpy ride"
else:
    turbulenceText = "smooth ride"

if clearSkies:
    clearSkiesText = "clear skies, which will give us a chance to point out some specific landmarks."
else:
    clearSkiesText = "cloudy, so we will not get to see much of the specific landmarks."

altitudeDifference = int(desiredFlightHeightInFoot) - int(currentFlightHeightinFoot)

print(
    "Good evening Ladies & gentlemen. This is " + pilotName + ", your captain for this flight. Here is some information about the flight progress. Our " + planeName +
    " is presently climbing through " + currentFlightHeightinFoot + " feet and is en route to our cruising altitude of " + desiredFlightHeightInFoot +
    " feet so we expect a climb of " + str(altitudeDifference) + "  feet. We are expecting a " + turbulenceText +
    " and our flight plan shows an en route time of two hours and " + flightDuration +
    ". We expect to arrive in " + arrivalDestination + " at " + arrivalTime + " Local time . Our route today will take us over " + pointOfInterest + " , visible on the left-hand side of the aircraft. The en route weather is " + clearSkiesText +
    " The " + arrivalDestination + " weather is " + weatherCircumstancesDestination + " and about " + degreesTemperature + " degrees Celsius. Please enjoy your flight.")
