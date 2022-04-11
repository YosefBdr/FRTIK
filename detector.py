from threading import Thread
import pytesseract
import socket
from datetime import datetime
import api

class Detector:
        def start_plate_detection():
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                api_result = api.ApiRequest.check_plate("car3.jpg");
                plate_number = api_result.get('results')[0]['plate']
                dt = datetime.now()
                date_now = dt.strftime("%d/%m/%Y")
                raw_data = {'date': date_now, 'plate_number': plate_number, 'url': 'http://www.google.com'}


                HOST = "192.168.1.17"  # The server's hostname or IP address
                PORT = 5000  # The port used by the server

                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect((HOST, PORT))
                        print(bytes(raw_data,encoding="utf-8"))
                        s.sendall(bytes(raw_data,encoding="utf-8"))
                        data = s.recv(1024)