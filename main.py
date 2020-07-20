import time
import requests
import os
from dotenv import load_dotenv
from os.path import join, dirname
from control_relay import RelayController

dotenv_path = join(dirname(__file__), '.env')
print('env_path={}', dotenv_path)
load_dotenv(dotenv_path)

beach_name = os.getenv('BEACH_NAME')
beach01 = os.environ.get('BEACH_NAME')
server_url = os.getenv('SERVER_URL')
print('BEACH={} {} {}'.format(beach_name, server_url, beach01))

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