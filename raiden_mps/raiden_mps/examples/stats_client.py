import requests
import json
import time
import sys

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def nice_print(key, val, val_prev):
    if val > val_prev:
        color = bcolors.GREEN
    elif val < val_prev:
        color = bcolors.RED
    else:
        color = bcolors.ENDC
    print(bcolors.BOLD+key+"\t\t"+color+str(val)+bcolors.ENDC)

def run():
    json_prev = None
    try:
        while True:
            response = requests.get("http://localhost:5000/api/1/stats")
            json_response = json.loads(response.text)
            if json_prev is None:
                json_prev = json_response
            print('\033[H\033[J')
            nice_print("balance", json_response['balance_sum'], json_prev['balance_sum'])
            nice_print("open", json_response['open_channels'], json_prev['open_channels'])
            nice_print("pending", json_response['pending_channels'], json_prev['pending_channels'])
            nice_print("senders", json_response['unique_senders'], json_prev['unique_senders'])
            nice_print("liquid", json_response['liquid_balance'], json_prev['liquid_balance'])
            nice_print("deposit", json_response['deposit_sum'], json_prev['deposit_sum'])
            json_prev = json_response
            time.sleep(2)
    except KeyboardInterrupt:
        sys.exit(1)



if __name__ == '__main__':
    run()
