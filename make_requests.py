import urllib.request
import json, os
#import dotenv                                             
a = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?offset=1001&limit=1000'

OFFSET = 1
JSON_FILE_COUNT = 1
HEADERS = {"token": 'QNgbHQdSKePiFYmCoeFhnmySpeiddfjl'} #for request.Requests, the format of the api is a dictionary
URL = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?limit=1000&offset={OFFSET}' #+ str(OFFSET)


for i in range(1):
    req = urllib.request.Request(a, HEADERS)
    # Request is a request to access a webpage
    # headers is your token that you pass to access the api
    with urllib.request.urlopen(req) as response:
        a = response.read()
        print(type(a))
    # urlopen is like reading a file from a database
        #loaded = json.load(response, 'rb')
        #with open('locations_' + JSON_FILE_COUNT + '.json', 'w') as f:
            #json.dump(loaded, f)
    #JSON_FILE_COUNT += 1
    #OFFSET += 1000

    


