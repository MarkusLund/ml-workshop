import requests
import json

def postScore(name, loss, acc):
    headers = {
        'Authorization': 'Bearer TOKEN',
        'Content-Type': 'application/json',
    }

    data = {
        "fields": {
            "Navn": name,
            "Accuracy": acc,
            "Loss": loss
        }
    }

    response = requests.post('https://api.airtable.com/v0/appcZ7ggxFxKCdj7e/Table%201', headers=headers, data=json.dumps(data))
    print("Bra jobba!")
