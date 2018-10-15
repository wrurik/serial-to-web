#!/usr/bin/env python

from dotenv import load_dotenv
load_dotenv()

import serial
import os
import requests

port = serial.Serial(
        port=os.getenv("SERIAL_PORT"),
        baudrate=os.getenv("SERIAL_BAUDRATE"),
        parity=serial.PARITY_NONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
       );

counter=0
message = ''

while True:
    x=port.readline()
    decodedLine = x.decode('utf-8')

    if decodedLine.rstrip() == os.getenv("MESSAGE_START"):
        message = ''
        counter = 0

    message = message + decodedLine

    counter += 1

    if int(counter) == int(os.getenv("MESSAGE_LINES")):
        requests.post(os.getenv("URL"), message)
