from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)
port = '5000'

@app.route('/', methods=['POST'])
def index():
  data = json.loads(request.get_data())

  # FETCH THE CRYPTO NAME
  crypto_name = data['conversation']['memory']['crypto']['value']

  # FETCH BTC/USD/EUR PRICES
  r = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsym="+crypto_name+"&tsyms=BTC,USD,EUR&api_key=9e456f965f6da5c50073be6f1f1f53d24243b5acffc6bcffdc1f4c27d90ee993")


  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'The price of %s is %f BTC and %f USD %f EUR' % (crypto_name, r.json()['BTC'], r.json()['USD'], r.json()['EUR'])
    }]
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port)
