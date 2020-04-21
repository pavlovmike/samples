# samples

Collection of code snippets and libraries for Kyivstar Open Telecom project

# Endpoint snippet structure

Snippets for endpoints started with parameters you should set for your environment and sample before run, for example:
/python/snippets/msisdn_activation_check.py
...
``` python
apiServerUrl = "https://<Kyivstar api base url>"
authServerTokenUrl = "https://<YOUR AUTH SERVER>/token" 
clientId = "<Your client ID>"
clientSecret = "<Your secret>"
phoneNumber = "380670000200"
activationHours = 24
```
