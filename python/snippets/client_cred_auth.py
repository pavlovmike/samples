import requests
from base64 import b64encode
import json

# SET HERE YOUR url, clientId and secret
authServerTokenUrl = "https://demo.identityserver.io/connect/token"
clientId = "m2m.short"
clientSecret = "secret"

def authenticate(authUrl, username, password):
  encoded = (username + ":" + password).encode("utf-8")
  userAndPass = b64encode(encoded).decode("ascii")
  headers = { 'Authorization' : 'Basic %s' %  userAndPass }

  payload = 'grant_type=client_credentials'
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic %s' %  userAndPass,
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  response = requests.request("POST", authUrl, headers=headers, data = payload)
  data = json.loads(response.text.encode('utf8'))
  return data["access_token"]

authToken = authenticate(authServerTokenUrl, clientId, clientSecret)
print("Auth token: " + authToken)
