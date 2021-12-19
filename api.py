import dataclasses

from flask import Flask, jsonify
from flask import request

from db import DB
from itemservice import ItemService, ItemNotFoundException

import requests

app = Flask(__name__)


@app.route("/status", methods=['GET'])
def status():
    db = DB()
    connection = db.get_connection()
    connection.execute('SELECT 1 cache')
    results = connection.fetchall()
    if not results:
        return {}, 500

    result = results[0]
    if result.get('cache', 0) != 1:
        return {}, 500

    return {}, 200


@app.route("/items", methods=['POST'])
def create_item():

    item_id = request.args.get('item_id')
    description = request.args.get('description')
    available_amount = request.args.get('available_amount')
    item = ItemService
    item.create(description)
    status_code = requests.get("http://localhost:8000/items").status_code
    return jsonify(dataclasses.asdict(item)), status_code


@app.route("/items", methods=['GET'])
def list_items():
    '''
    suponiendo que tenemos un form en html
    '''
    items = []
    for key,val in request.form.items():
        items.append(key+" :"+val)
    status_code = requests.get("http://localhost:8000/items").status_code
    return jsonify([dataclasses.asdict(item) for item in items]), status_code


@app.route("/items/<item_id>", methods=['GET'])
def get_item(item_id):
    try:
        item_id = request.form.get('item_id')
        item = ItemService()
        item.find_by_id(item_id)
        pass
    except ItemNotFoundException:
        #############################
        #### WRITE YOUR CODE HERE ###
        #############################

        #############################
        return jsonify({'error_code': 'ITEM_NOT_FOUND'}), status_code

    #############################
    #### WRITE YOUR CODE HERE ###
    #############################

    #############################
    return jsonify(dataclasses.asdict(item)), status_code


@app.route("/items/<item_id>", methods=['PUT'])
def increment_item(item_id):
    #############################
    #### WRITE YOUR CODE HERE ###
    #############################

    #############################
    if increment:
        #############################
        #### WRITE YOUR CODE HERE ###
        #############################

        #############################
        return jsonify(dataclasses.asdict(item)), status_code
    else:
        return {}, 200
