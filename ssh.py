authtoken = ("2BKoFAIlkRcOOuhw6GVRIkf3zem_7H9HsByW5gp8VqaVNGTWX")
get_ipython().system_raw('./ngrok authtoken $authtoken && ./ngrok tcp 22 &')
sleep 3

import requests
from re import sub
r = requests.get('http://localhost:4040/api/tunnels')
str_ssh = r.json()['tunnels'][0]['public_url']
str_ssh = sub("tcp://", "", str_ssh)
str_ssh = sub(":", " -p ", str_ssh)
str_ssh = "ssh root@" + str_ssh
print(str_ssh)
