import os
from os.path import join, dirname
import requests
from dotenv import load_dotenv

# get the .env to interact with Python
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ALIAS1 = 'tok_sandbox_rMqQ8Qgm5hYuWXP2X2RgpK'
ALIAS2 = 'tok_sandbox_azmm6dvmRXTUU1R8mpzivn'
ALIAS3 = 'tok_sandbox_bZYBz6H3WrWSV18X4zhGBA'
USERNAME = os.getenv("HTTPS_PROXY_USERNAME")
PASSWORD = os.getenv("HTTPS_PROXY_PASSWORD")
VAULTID = os.getenv("VAULT")

#the good shit
os.environ['HTTPS_PROXY'] = 'http://'+USERNAME+':'+PASSWORD+'@'+VAULTID+'.SANDBOX.verygoodproxy.com:8080'
response = requests.post('https://echo.apps.verygood.systems/post',
                         json={'card_num': ALIAS1,
                                'exp_date' : ALIAS2,
                                'cvv' : ALIAS3
                                },
                         verify='vgsapp/sandbox.pem')
print(str(response.text))



