from flask import Flask, request
import requests
import os
import logging
application = Flask(__name__)


@application.route('/hello')
def hello():
    return 'Hello there'


@application.route('/jobs', methods=['POST'])
def jobs():
    token = request.headers['Authorization']
    data = {"token": token}
    result = requests.post(os.environ['AUTH_SERVICE'], data=data).text
    if result == "density":
        return 'Jobs:\nTitle: Devops\nDescription: Awesome\n'
    else:
        return 'fail'


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
