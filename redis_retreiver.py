#Create a flask app to get redis key value based on function name pattern

from flask import Flask, request, jsonify
import os
import redis
import json
from datetime import datetime

app = Flask(__name__)

password = os.environ.get('password')
host = os.environ.get('host')
port = os.environ.get('port')
redis_client = redis.Redis(host=host, port=port, password=password, db=0)

@app.route('/get_result', methods=['GET'])
def get_result():
    function_name = request.args.get('function_name')
    function_name = function_name if function_name else ''
    keys = redis_client.keys(f"{function_name}*")
    print(keys)
    for key in keys:
        print(redis_client.get(key))

    response = {}
    for key in keys:
        response[key.decode()] = redis_client.get(key).decode()
    print(response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)