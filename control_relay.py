from smbus2 import SMBus
import sys
import time

DEVICE_BUS = 1
DEVICE_ADDR = 0x10
RELAY_GREEN = 0x01
RELAY_YELLOW = 0x02
RELAY_RED = 0x03
RELAY_OTHER = 0x04


class RelayController:
    buf = {}
    current_light_state = -1

    def __init__(self):
        self.bus = SMBus(DEVICE_BUS)
        self.current_light_state = -1
        self.turn_all_relay_off()


    def get_relay(self, light_state):
        if light_state == 0:    #Green
            return RELAY_GREEN
        if light_state == 1:
            return RELAY_YELLOW
        if light_state == 2:    # RED
            return RELAY_RED
        return RELAY_OTHER

    def turn_relay(self, light_state):
        if self.current_light_state == light_state:
            return
        off_relay = self.get_relay(self.current_light_state)
        on_relay = self.get_relay(light_state)
        self.bus.write_byte_data(DEVICE_ADDR, off_relay, 0x00)
        time.sleep(1)
        self.bus.write_byte_data(DEVICE_ADDR, on_relay, 0xFF)

    def turn_all_relay_off(self):
        self.bus.write_byte_data(DEVICE_ADDR, RELAY_GREEN, 0x00)
        time.sleep(1)
        self.bus.write_byte_data(DEVICE_ADDR, RELAY_YELLOW, 0x00)
        time.sleep(1)
        self.bus.write_byte_data(DEVICE_ADDR, RELAY_RED, 0x00)
        time.sleep(1)
        self.bus.write_byte_data(DEVICE_ADDR, RELAY_OTHER, 0x00)