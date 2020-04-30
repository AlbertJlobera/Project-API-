
# Import Json data from json file.
import requests
import json
with open('../quotes-100-en.json') as file:
    data = json.load(file)


# Filter data.



print(len(data))
