import json
import os

os.chdir(r'c:/users/phwh9568/sanborn_map')

inFile = open('Sanborn_Lines.geojson')

data = json.load(inFile)

inFile.close()

with open('Sanborn_Lines.geojson','w', encoding='utf-8') as outFile:
    json.dump(data,outFile,indent=4)
