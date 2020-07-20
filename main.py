import time
import requests
import os
from os.path import join
from control_relay import RelayController
import json


_current_path = os.path.dirname(os.path.abspath(__file__))
config_path = join(_current_path, 'config.json')
print('config={}', config_path)

with open(config_path) as json_data_file:
    config_data = json.load(json_data_file)
print(config_data)
beach_name = config_data['BEACH_NAME']
server_url = config_data['SERVER_URL']

print('BEACH={} {}'.format(beach_name, server_url))


def make_requests():
    PARAMS = {
        'beach_name': beach_name
    }
    try:
        resp = requests.get(url=server_url, params=PARAMS)
        beach_state = resp.json()
        # print('make-request={}'.format(beach_state))
        light_state = beach_state['light_state']
        return light_state
    except:
        return None


def main_process():
    relay_controller = RelayController()
    while True:
        light_state = make_requests()
        if light_state is not None:
            print('get-request: beach={} light={} current={}'.format(beach_name, light_state, relay_controller.current_light_state))
            relay_controller.turn_relay(light_state)
        time.sleep(5)
    pass


if __name__ == '__main__':
    main_process()
    pass