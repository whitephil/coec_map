import json
import os

os.chdir(r'c:/users/phwh9568/sanborn_map')

file = open('Sanborn_Points.geojson')

data = json.load(file)

marker_types = []

for feature in data['features']:
    if feature['geometry']['type'] == 'Point':
        marker_type = feature['properties']['marker-symbol']
        if marker_type not in marker_types:
            marker_types.append(marker_type)

print(marker_types)

icons = ['water-blue', 'mountain', 'village-square', 'star-gold', 'attraction', 'attraction', 'horse-riding']

for feature in data['features']:
    color = feature['properties']['marker-color']
    color = '#'+color
    feature['properties']['marker-color'] = color


for i in range(len(marker_types)):
    for feature in data['features']:
        if feature['geometry']['type'] == 'Point':
            if feature['properties']['marker-symbol'] == marker_types[i]:
                feature['properties']['marker-symbol'] = icons[i]



with open('Sanborn_Icons.geojson', 'w', encoding='utf-8') as outFile:
    json.dump(data,outFile, indent=4)

file.close()
