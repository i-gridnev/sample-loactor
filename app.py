import json
import os
import urllib.request

from flask import Flask
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
app = Flask(__name__)


@app.get('/')
def home():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode()
    api_url = f"http://api.ipstack.com/{external_ip}?access_key={API_KEY}&fields=latitude,longitude"
    response = urllib.request.urlopen(api_url).read().decode()
    longitude, latitude = json.loads(response).values()
    return f'Hello {external_ip}!<br>Your location:<br>{longitude=}<br>{latitude=}'
