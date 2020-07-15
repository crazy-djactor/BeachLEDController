import time
import requests
import config
from control_relay import RelayController


def make_requests():
    PARAMS = {
        'beach_name': config.BEACH_NAME
    }
    try:
        resp = requests.get(url=config.SERVER_URL, params=PARAMS)
        beach_state = resp.json()
        light_state = beach_state['light_state']
        return light_state
    except:
        return None


def main_process():
    relay_controller = RelayController()
    while True:
        light_state = make_requests()
        if light_state is not None:
            relay_controller.turn_relay(light_state)
        time.sleep(5)
    pass


if __name__ == '__main__':
    main_process()
    pass