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
    if result.get('cache', 0) is not 1:
        return {}, 500

    return {}, 200


@app.route("/items", methods=['POST'])
def create_item():
    # Write code

    # Fix next line
    status_code = 100
    return jsonify(dataclasses.asdict(item)), status_code


@app.route("/items", methods=['GET'])
def list_items():
    # Write code

    # Fix next line
    status_code = 100
    return jsonify([dataclasses.asdict(item) for item in items]), status_code


@app.route("/items/<item_id>", methods=['GET'])
def get_item(item_id):
    try:
        # Write code
        pass
    except ItemNotFoundException:
        # Fix next line
        status_code = 100
        return jsonify({'error_code': 'ITEM_NOT_FOUND'}), status_code

    # Fix next line
    status_code = 100
    return jsonify(dataclasses.asdict(item)), status_code


@app.route("/items/<item_id>", methods=['PUT'])
def increment_item(item_id):
    # Write code
    if increment:
        # Write code

        # Fix next lines
        status_code = 100
        return jsonify(dataclasses.asdict(item)), status_code
    else:
        # Fix next lines
        status_code = 100
        return {}, status_code
