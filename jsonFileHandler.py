import json

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except:
        print("El archivo no fue encontrado ")
    return data
        

