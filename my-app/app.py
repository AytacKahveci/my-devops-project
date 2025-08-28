#!/usr/bin/env python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
  return jsonify({"message": "Example application"}), 200

if __name__ == '__main__':
  app.run(port=51500 ,debug=True)
