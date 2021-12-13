from flask import Flask
from flask import Flask, request, cli, jsonify, Response
from flask_cors import CORS
import urllib3, json

import client

urllib3.disable_warnings()
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'ok'


@app.route('/valorant/join/<party_id>', methods=['POST'])
def join_party(party_id):
    json_data = request.get_json()
    region = request.args.get('region')
    payload = {}
    try:
        data = client.join_party(json_data['username'],json_data['password'],region,party_id)
        payload = data
    except:
        payload = {
            'error': 'Unable to join party.'
        }
    
    return Response(
        response=json.dumps(payload),
        status=200,
        mimetype='application/json'
    ) 

@app.route('/valorant/request/<party_id>', methods=['POST'])
def join_party(party_id):
    json_data = request.get_json()
    region = request.args.get('region')
    payload = {}
    try:
        data = client.join_party(json_data['username'],json_data['password'],region,party_id)
        payload = data
    except:
        payload = {
            'error': 'Unable to request to join party.'
        }
    
    return Response(
        response=json.dumps(payload),
        status=200,
        mimetype='application/json'
    ) 


# run the app.
if __name__ == "__main__":
    app.run()