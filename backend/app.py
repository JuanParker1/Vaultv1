from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin
from binance.client import Client
from firebase import firebase
from binance.exceptions import BinanceAPIException


app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'
firebase=firebase.FirebaseApplication('https://crypto-d33e5-default-rtdb.asia-southeast1.firebasedatabase.app/', None)

@app.route("/dataentry", methods=["POST","GET"])
def submitData():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        data = {
        'amount' :post_data.get('amount'),
        'coin':post_data.get('coin')
        }
        # name        = post_data.get('amount'),
        # department  = post_data.get('coin')
        firebase.post('/crypto-d33e5/withdraw/',data )
        client = Client(post_data.get('api_key'), post_data.get('seceret_key'))
    try:
        client.withdraw(
        coin='MATIC',
        address='0x7aa2a5f3592963fe9e35bf419565a8a483dffe75',
        amount=post_data.get('amount'),
        name='Withdraw')
    except BinanceAPIException as e:
        print(e)
    else:
        print("Success")
       
        
        response_object['message'] ='Data added!'
        return jsonify(response_object)


if __name__ == '__main__':
    app.run(debug=True)