import ast
import json
import os

from flask import Flask, render_template, request
from flask_restful import Api

from active_chain import ActiveChain
from block import Block
from blockchain import Blockchain

app = Flask(__name__)
api = Api(app)

INDEX = "index.html"


@app.route("/", methods=["GET", "POST"])
def main():
    diff = get_difficulty()
    test_blockchain = Blockchain(diff)
    chain = ActiveChain(test_blockchain)
    all_chain = blockchain_as_list()
    if request.method == "POST":
        data = request.form.get("new-data")
        data = data.replace(', ', ',; ')
        if data:
            chain.add_to_chain(
                Block(data, chain.blockchain.last_block.current_hash, chain.blockchain.difficulty))
        all_chain = blockchain_as_list()
        return render_template(INDEX, all_chain=all_chain)
    return render_template(INDEX, all_chain=all_chain)


def get_difficulty(file=ActiveChain.WRITE_PATH) -> int:
    """
    This function return the difficulty of the blockchain based on the info from the previous block.

    Return:
    int: Return the current difficulty of the blockchain.
    """

    if not os.path.isfile(file):
        return 0
    else:
        with open(file) as old_json:
            feeds = json.load(old_json)
            diff = feeds[-1].split(',')[-1].split(':')[1].strip()[1:-2]
            return int(diff)


def blockchain_as_list(file=ActiveChain.WRITE_PATH) -> list:
    """
    This function check if there is a file used as a blockchain and if there is such a file extracts the block's
    data and save each block data in a list.

    Parameters:
        file (file): The file used as blockchain.

    Return:
    list: Return list of string representations of the blocks in the blockchain file.
    """
    blockchain_list = []
    if os.path.isfile(file):
        with open(file, 'r') as f:
            jsonData = json.load(f)
            for line in jsonData:
                blockchain_list.append(line)
    return blockchain_list


def make_data(block) -> dict:
    """
    This function creates dictionary with the values for all the attributes of the current block.

    Parameters:
        block (Block): The block that has to be added to the blockchain.

    Return:
    dict: Return all the attributes for the current block as a dictionary.
    """
    data = {
        "timestamp": str(block.timestamp),
        "data": str(block.data),
        "currentBlockHash": str(block.current_hash),
        "previousBlockHash": str(block.previous_hash),
        "nonce": str(block.nonce),
        "difficulty": str(block.difficulty),
    }
    return data


if __name__ == '__main__':
    app.run(debug=True)
