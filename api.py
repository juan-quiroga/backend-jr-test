import dataclasses

from flask import Flask, jsonify
from flask import request

from db import DB
from itemservice import ItemService, ItemNotFoundException

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
    #############################
    #### WRITE YOUR CODE HERE ###
    #############################

    #############################
    return jsonify(dataclasses.asdict(item)), status_code


@app.route("/items", methods=['GET'])
def list_items():
    #############################
    #### WRITE YOUR CODE HERE ###
    #############################

    #############################
    return jsonify([dataclasses.asdict(item) for item in items]), status_code


@app.route("/items/<item_id>", methods=['GET'])
def get_item(item_id):
    try:
        #############################
        #### WRITE YOUR CODE HERE ###
        #############################

        #############################
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
    # Write code
    if increment:
        #############################
        #### WRITE YOUR CODE HERE ###
        #############################

        #############################
        return jsonify(dataclasses.asdict(item)), status_code
    else:
        return {}, 200
