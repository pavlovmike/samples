import requests
from base64 import b64encode
import json

def authenticate(authUrl, username, password):
  encoded = (username + ":" + password).encode("utf-8")
  userAndPass = b64encode(encoded).decode("ascii")
  headers = { 'Authorization' : 'Basic %s' %  userAndPass }

  payload = 'grant_type=client_credentials'
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic %s' %  userAndPass,
  }
  response = requests.request("POST", authUrl, headers=headers, data = payload)
  data = json.loads(response.text.encode('utf8'))
  return data["access_token"]
