import json
from threading import Thread
import pytesseract
import socket
from datetime import datetime
import api

def openSocketWithFiras(data_to_send):
        HOST = "192.168.1.17"  # The server's hostname or IP address
        PORT = 5000  # The port used by the server

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                print(bytes(data_to_send,encoding="utf-8"))
                s.sendall(bytes(data_to_send,encoding="utf-8"))
                data = s.recv(1024)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

api_result = api.ApiRequest.check_plate("./violations/output1.jpg");
if len(api_result.get('results')) > 0:
        plate_number = api_result.get('results')[0]['plate']
        dt = datetime.now()
        date_now = dt.strftime("%d/%m/%Y")
        raw_data = {'date': date_now, 'plate_number': plate_number, 'url': 'https://drive.google.com/file/d/1wqMM2ankspzy4_HCmrk4uqMJ8AJN1Koj/view?usp=sharing'}
        raw_data = json.dumps(raw_data)

        openSocketWithFiras(raw_data)