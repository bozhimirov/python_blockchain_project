import os

import pytest

from ..block import Block
from ..active_chain import ActiveChain
from ..blockchain import Blockchain


def test_block():
    start_block = Block("Genesis Block", '0', 0)
    assert start_block.current_hash == start_block.make_hash()
    assert str(start_block) == f'{start_block.nonce}, {start_block.timestamp}, Genesis Block, 0,' \
                               f' {start_block.make_hash()}'


def test_block_with_difficulty():
    start_block = Block("Genesis Block", '0', 3)
    start_block.proof_of_work()
    print(start_block.current_hash)
    assert start_block.current_hash[:3] == '000'


def test_blockchain_creation():
    file = ActiveChain.WRITE_PATH
    assert os.path.isfile(file) == False
    test_chain = Blockchain()
    assert os.path.isfile(file) == True
    assert test_chain.last_block.data == 'Genesis Block'
    os.remove(file)


def test_blockchain_add_block():
    file = ActiveChain.WRITE_PATH
    test_chain = Blockchain()
    active = ActiveChain(test_chain)
    assert len(active.blockchain.blockchain()) == 1
    block = Block('a', active.blockchain.last_block.current_hash, active.blockchain.difficulty)
    active.blockchain.add_block(block)
    assert len(active.blockchain.blockchain()) == 2
    assert test_chain.last_block.data == 'a'
    os.remove(file)


# test = Blockchain()
# chain = ActiveChain(test)
# data = 'asd'
# if data:
#     chain.add_to_chain(
#         Block(data, chain.blockchain.last_block.current_hash, chain.blockchain.difficulty))
# all_chain = chain.blockchain.blockchain()


