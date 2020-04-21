import requests
import json
from snippets.client_cred_auth import authenticate

# SET HERE YOUR url, clientId and secret
apiServerUrl = "https://<Kyivstar api base url>"
authServerTokenUrl = "https://<YOUR AUTH SERVER>/token" 
clientId = "<Your client ID>"
clientSecret = "<Your secret>"
phoneNumber = "380670000200"
activationHours = 24

authToken = authenticate(authServerTokenUrl, clientId, clientSecret)
print( f'authToken: {authToken}')

targetMethodUrl = apiServerUrl + "/msisdn/activation-check"

payload = f'{{\n\t\"msisdn\": \"{phoneNumber}\",\n\t\"activationHours\": {activationHours}\n}}'
print("Request:\n" + payload)

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer %s' % authToken
}
response = requests.request("POST", targetMethodUrl, headers=headers, data = payload)
data = json.loads(response.text.encode('utf8')) 
print("Result:\n" + json.dumps(data, indent=4, sort_keys=True))