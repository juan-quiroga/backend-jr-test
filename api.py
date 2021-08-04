import dataclasses

from flask import Flask, jsonify
from flask import request

from itemservice import ItemService, ItemNotFoundException

app = Flask(__name__)


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
