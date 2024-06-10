from flask import Flask, render_template, request
from flask_restful import Api

from active_chain import ActiveChain
from block import Block
from blockchain import Blockchain
from get_diff import get_difficulty

app = Flask(__name__)
api = Api(app)

INDEX = "index.html"


@app.route("/", methods=["GET", "POST"])
def main():
    diff = get_difficulty()
    test_blockchain = Blockchain(diff)
    chain = ActiveChain(test_blockchain)
    all_chain = chain.blockchain.blockchain()
    if request.method == "POST":
        data = request.form.get("new-data")
        data = data.replace(', ', ',; ')
        if data:
            chain.add_to_chain(
                Block(data, chain.blockchain.last_block.current_hash, chain.blockchain.difficulty))
        all_chain = chain.blockchain.blockchain()
        return render_template(INDEX, all_chain=all_chain)
    return render_template(INDEX, all_chain=all_chain)


if __name__ == '__main__':
    app.run()
