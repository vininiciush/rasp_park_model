#!/usr/bin/env python
import time
import serial
import json
import requests

HOST = 'http://localhost:8085'
PATH = '/v1/sensors/receive'
PORTS = ['/dev/ttyACM0', '/dev/ttyUSB0']
BAUDRATE = 9600

serialInputs = []

for PORT in PORTS:
        ser = serial.Serial(
                port=PORT,
                baudrate = BAUDRATE,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1)

        serialInputs.append(ser)

def sendDataToApi(body):
        response = requests.post(HOST + PATH, json = body)

def convertMessageToJson(message):
        try:
                json_message = json.loads(message)
                return json_message
        except:
                return None

def startReading():
        while 1:
                for serial in serialInputs:
                        message = serial.readline()
                        json_message = convertMessageToJson(message)

                        if(json_message != None):
                                print(json_message)
                                sendDataToApi(json_message)

startReading()
