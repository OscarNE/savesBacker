import json
import os

# Load a single file in json format to a python object
def loadJson(path):
    # Opening JSON file
    f = open(path)
    
    # returns JSON object as a dictionary
    data = json.load(f)
    
    # Closing file
    f.close()

    return data

#Load all files in a directory ina  python object
def loadAllConfigFiles():
    data = []
    for filename in os.listdir(os.getcwd()):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            data.append(loadJson(f))
    return data