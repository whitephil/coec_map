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

icons = ['circle-11', 'village-11', 'mountain-11', 'star-11', 'attraction-11', 'attraction-11', 'circle-stroked-11']

for i in range(len(marker_types)):
    for feature in data['features']:
        if feature['geometry']['type'] == 'Point':
            if feature['properties']['marker-symbol'] == marker_types[i]:
                feature['properties']['marker-symbol'] = icons[i]



with open('Sanborn_icons.geojson', 'w', encoding='utf-8') as outFile:
    json.dump(data,outFile, indent=4)

file.close()
