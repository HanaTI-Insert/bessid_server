#!/usr/bin/python
#-*- coding: utf-8 -*-
from flask import Flask, request
import time
app = Flask(__name__)
@app.route("/index.php", methods=['POST'])
def main():
    with open(time.strftime(time.localtime()), 'wb') as f : f.write(request.get_data())
    return 'Hello World'
app.run(host='0.0.0.0', port=80, debug=True)

