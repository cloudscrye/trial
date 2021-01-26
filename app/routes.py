from app import app
from flask import render_template, request, jsonify
import requests
import os
from os.path import join, dirname
import json
from dotenv import load_dotenv

# Main page of web application
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# After data entry on main page, returns token aliases
@app.route('/add_message', methods=['POST'])
def add_message():
        cardnum = request.form['cardnum']
        expir = request.form['expir']
        last3 = request.form['last3']
        response = requests.post("https://tnt45d7vas7.SANDBOX.verygoodproxy.com/post",
                          json={'card_num': cardnum,
                                'exp_date' : expir,
                                'cvv' : last3})

        # Logic to parse/read return data from POST request in web app                        
        parse = response.json()
        cardtoken = (parse['json']['card_num'])
        extoken = (parse['json']['exp_date'])
        l3token = (parse['json']['cvv'])
        print(parse)
        return render_template(
                'message.html',  
                cardnum=cardnum,
                expir=expir,
                last3=last3,
                cardtoken=cardtoken,
                extoken=extoken,
                l3token=l3token
                )

# return card data utilizing tokens page
@app.route("/forward", methods=['POST'])
def forward():

    # get the .env to interact with Python
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    
    #.env variable connections
    USERNAME = os.getenv("HTTPS_PROXY_USERNAME")
    PASSWORD = os.getenv("HTTPS_PROXY_PASSWORD")
    VAULTID = os.getenv("VAULT") 

    #logic for sending token aliases and retrieving sensitive data from VGS
    cardnum = request.form['cardnum']
    expir = request.form['expir']
    last3 = request.form['last3']
    os.environ['HTTPS_PROXY'] = 'http://'+USERNAME+':'+PASSWORD+'@'+VAULTID+'.SANDBOX.verygoodproxy.com:8080'
    res = requests.post('https://echo.apps.verygood.systems/post',
                         json={'card_num': cardnum,
                                'exp_date' : expir,
                                'cvv' : last3
                                },
                         verify='/vgsapp/sandbox.pem')

    parse = res.json()
    cardreturn = (parse['json']['card_num'])
    exreturn = (parse['json']['exp_date'])
    l3return = (parse['json']['cvv'])
    print(parse)
    return render_template(
            'forward.html', 
            cardnum=cardnum,
            expir=expir,
            last3=last3,
            cardreturn=cardreturn,
            exreturn=exreturn,
            l3return=l3return            
            )
