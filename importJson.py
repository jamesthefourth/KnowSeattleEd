# This script imports the json file and
# uses the data to return schools within
# a given radius of a given lat lon.



import json

with open('sampleSchool.json') as json_data:
    d = json.load(json_data)
    print("Testing import of json")
    print("lat:" + d["school"][0]["lat"])
    print("lon:" + d["school"][0]["lon"])



latitude = 47.6992
longitude = -122.3334
distance = 1.0


for school in d["school"]:
	d = ( ( (float(school["lat"]) - latitude) * (float(school["lat"]) - latitude) ) + ( ( float(school["lon"]) - longitude) * (float(school["lon"]) - longitude) ) )**0.5 #square root
	if (d < distance):
		print(school["name"] + " " + "latitude: " + school["lat"] + " " + "longitude: " + school["lon"])