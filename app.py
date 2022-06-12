import json
import os
import urllib.request

from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
app = Flask(__name__)


@app.get('/')
def home():
    # For local testing IP is local host, so external api is used
    # external_ip = urllib.request.urlopen('https://ident.me').read().decode()
    external_ip = request.remote_addr

    api_url = f"http://api.ipstack.com/{external_ip}?access_key={API_KEY}&fields=latitude,longitude"
    response = urllib.request.urlopen(api_url).read().decode()
    longitude, latitude = json.loads(response).values()
    return f'Hello {external_ip}!<br>Your location:<br>{longitude=}<br>{latitude=}'
