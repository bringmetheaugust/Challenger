import os
import requests, json

MAIN_SERVER_URL: str = os.getenv('MAIN_SERVER_URL')

def errorReport(err) -> None:
    try:
        requests.post(url = MAIN_SERVER_URL + '/api/report/error?source=telegram', data = json.load(err))

        print(f'ERROR: {err}.\n')
        print('Success report sent.\n')
    except:
        print('Fail to send error report.')
