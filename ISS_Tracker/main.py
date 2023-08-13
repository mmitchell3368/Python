# import statements
import json, turtle, urllib.request, time, webbrowser, geocoder

# NASA URL & Result
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

# Create file and write to it
file = open("iss.txt", "w")
file.write("There are currently " + str(result["number"]) + " astronauts on the ISS: \n\n")

people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")

# Print long and lat
g = geocoder.ip('me')
file.write("\n Your current lat / long is: " + str(g.latlng))
file.close()

# open the txt file
webbrowser.open("iss.txt")

# Setup the world map in the turtle module 
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# Load the world map image
screen.bgpic("Images/map.gif")

# Load the iss image
screen.register_shape("Images/iss.gif")
iss = turtle.Turtle()
iss.shape("Images/iss.gif")
iss.setheading(45)
iss.penup()

while True:
    # Load the current status of the ISS in real-time
    # NASA URL & Result
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Extract the ISS location
    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]

    # Output latitude and longitude to the terminal
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # Update the ISS location on the map
    iss.goto(lon, lat)

    # Refresh each 5 seconds
    time.sleep(5)