import json
import os
import pprint


os.chdir(r'C:\Users\phwh9568\Sanborn_Map')

file = open('Staff_Map.json')

inData = json.load(file)

print(inData['features'][0])

outPoints = dict(type='FeatureCollection',features=[])
outLines = dict(type='FeatureCollection',features=[])
#print(outData)

for feature in inData['features']:
    if feature['geometry']['type'] == 'Point':
        outPoints['features'].append(feature)
    if feature['geometry']['type'] == 'LineString':
        outLines['features'].append(feature)


#pprint.pprint(outData['features'])

with open('Sanborn_Points.geojson', 'w') as outFile:
    json.dump(outPoints,outFile, indent=4)
with open('Sanborn_Lines.geojson', 'w') as outFile:
    json.dump(outLines,outFile,indent=4)

file.close()
#outData['features'].append('x')
