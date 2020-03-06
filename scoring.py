import requests
import json

def postScore(name, loss, acc, params):
    headers = {
        'Authorization': 'Bearer keyKUg4iQiVVtCOmF',
        'Content-Type': 'application/json',
    }

    data = {
        "fields": {
            "Navn": name,
            "Accuracy": acc,
            "Loss": loss,
            "Params": params
        }
    }

    response = requests.post('https://api.airtable.com/v0/appcZ7ggxFxKCdj7e/Table%201', headers=headers, data=json.dumps(data))
    print("Bra jobba!")
