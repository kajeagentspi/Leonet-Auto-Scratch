import requests
import json

session = requests.Session()
keys = {}

def getAccessKey():
    global keys
    headers = {
        'accept': 'application/json, text/plain, */*',
        'x-sitecode': 'LeoApp_lRoom',
        'x-password': 'n4cMDaG5xSni4rkS',
        'Host': 'app.leo-net.jp',
        'User-Agent': 'okhttp/3.12.1',
    }
    response = session.post('https://app.leo-net.jp/api/certify/site', headers=headers)
    data = json.loads(response.text)
    keys['x-accesskey'] =data["responseData"]['accessKey']

def login():
    global keys
    headers = {
        'accept': 'application/json, text/plain, */*',
        'Host': 'app.leo-net.jp',
        'User-Agent': 'okhttp/3.12.1',
    }
    headers = {**headers, **keys}
    with open('credentials.json', 'r') as f:
        data = json.load(f)
    response = requests.post('https://app.leo-net.jp/api/certify/login', headers=headers, data=data)
    data = json.loads(response.text)
    keys['x-token'] =data["responseData"]['token']
    keys['x-uuid'] =data["responseData"]['uuid']

def scratch():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'cache-control': 'max-age=0',
        'Host': 'app.leo-net.jp',
        'User-Agent': 'okhttp/3.12.1',
    }
    headers = {**headers, **keys}
    data = {
        'clientType': 'AndroidSmartphone'
    }
    response = requests.post('https://app.leo-net.jp/api/scratch/lottery/', headers=headers, data=data)
    data = json.loads(response.text)
    print("Gained points: {}".format(data["responseData"]["scratchResult"]))
    print("Total points: {}".format(data["responseData"]["winInfo"]["restPoint"]))
    print("Scratches left till W chance: {} ".format(data["responseData"]["wChanceEntryInfo"]["wChanceRestCount"]))

getAccessKey()
login()
scratch()