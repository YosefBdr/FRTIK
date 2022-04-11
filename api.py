import requests

class ApiRequest:
    def check_plate(img):
        regions = ['mx', 'us-ca', 'il'] # Change to your country
        with open(img, 'rb') as fp:
            response = requests.post(
                'https://api.platerecognizer.com/v1/plate-reader/',
                data=dict(regions=regions),  # Optional
                files=dict(upload=fp),
                headers={'Authorization': 'Token 46308d8b076e4157ea9132a65e4a4e129211cf27'})
        return response.json()