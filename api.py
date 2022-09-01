#!/usr/bin/env python
# encoding: utf-8
import json, boto3
from flask import Flask, request, jsonify

app = Flask(__name__)

client = boto3.client('dynamodb',
  aws_access_key_id='yyyy',
  aws_secret_access_key='xxxx',
  region_name='us-east-1')

@app.route('/test', methods=['GET'])
def test_route():
    return "It Works!"
    
    
@app.route('/getAll', methods=['GET'])
def query_unicorns():
    dynamo = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamo.Table('Posts')
    response = table.scan()
    data = response['Items']
    return json.dumps(data)
    

@app.route('/', methods=['PUT'])
def create_post():
    record = json.loads(request.data)
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_post():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
    
# @app.route('/', methods=['DELETE'])
# def delte_record():
#     record = json.loads(request.data)
#     new_records = []
#     with open('/tmp/data.txt', 'r') as f:
#         data = f.read()
#         records = json.loads(data)
#         for r in records:
#             if r['name'] == record['name']:
#                 continue
#             new_records.append(r)
#     with open('/tmp/data.txt', 'w') as f:
#         f.write(json.dumps(new_records, indent=2))
#     return jsonify(record)

if __name__ == '__main__':
    app.run(port=80, host="0.0.0.0", debug=True)