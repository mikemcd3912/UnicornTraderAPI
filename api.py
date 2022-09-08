#!/usr/bin/env python
# encoding: utf-8
import json, boto3
from flask import Flask, request, jsonify

app = Flask(__name__)

# client = boto3.client('dynamodb',
#   region_name='us-east-1')

@app.route('/test', methods=['GET'])
def test_route():
    return "It Works!"
    
    
@app.route('/', methods=['GET'])
def query_unicorns():
    dynamo = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamo.Table('serviceInfra-Posts868B3EAD-5N1O0N7NHVDU')
    response = table.scan()
    data = response['Items']
    return json.dumps(data)
    

if __name__ == '__main__':
    app.run(port=80, host="0.0.0.0", debug=True)