import sys
import requests
import json

if len(sys.argv)==2:
    respose=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])
    data=respose.json()

    for result in data["results"]:
        print(result["trackName"])

else:
    print("Arg error")
