from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

from constants import brandList

app = Flask(__name__)

@app.route('/api/params/brands', methods = ['GET'])
def getBrandList():
    return jsonify(brandList)

@app.route('/api/report/error', methods = ['POST'])
def errorReport():
    print("LOL")
