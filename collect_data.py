import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    # utc_timestamp = datetime.datetime.utcnow().replace(
    #     tzinfo=datetime.timezone.utc).isoformat()
    
    import urllib.request as urllib2
    import json
    import pyrebase

    config = {
        "apiKey": "AAaaAaAaAA-AAaaaaaAaaAa0AAAAaaaAAaaA0A0",
        "authDomain": "name-aa0aa.firebaseapp.com",
        "databaseURL": "https://name-aa0aa-default-rtdb.europe-west1.firebasedatabase.app",
        "projectId": "name-aa0aa",
        "storageBucket": "name-aa0aa.appspot.com",
        "messagingSenderId": "00000000000",
        "appId": "1:00000000000:web:000aaa000aa0a000aaa000",
        "measurementId": "G-A0A00A000A"
    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    def loader(url):
        temp = urllib2.urlopen(url).read()
        temp = json.loads(temp)
        temp = json.loads(json.dumps(temp['mainEntity']['itemListElement']))
        dict1 = dict()
        for i in temp:
            u = i['currency']
            dict1[u] = i['currentExchangeRate']['price']
        # time_stamp = "deneme"
        time_stamp = datetime.datetime.now()
        time_stamp = time_stamp.strftime("%m%d%Y%H%M%S")
        db.child(f'data/{time_stamp}').set(dict1)
        
    borsaURL = "https://canlidoviz.com/borsa.jsonld"

    loader(borsaURL)

    # if mytimer.past_due:
    #     logging.info('The timer is past due!')

    # logging.info('Python timer trigger function ran at %s', utc_timestamp)
