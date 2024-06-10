import ast
import os

import pytest

from block import Block
from active_chain import ActiveChain
from blockchain import Blockchain
from project import get_difficulty, blockchain_as_list, make_data

file = 'data.json'
# file = 'demo.json'


def remove_file():
    if os.path.isfile(file):
        os.remove(file)


def test_block():
    remove_file()
    start_block = Block("Genesis Block", '0', 0)
    assert start_block.current_hash == start_block.make_hash()
    assert str(start_block) == f'{start_block.nonce}, {start_block.timestamp}, Genesis Block, 0,' \
                               f' {start_block.make_hash()}'
    remove_file()


def test_block_with_difficulty():
    remove_file()
    start_block = Block("Genesis Block", '0', 3)
    start_block.proof_of_work()
    print(start_block.current_hash)
    assert start_block.current_hash[:3] == '000'
    remove_file()


def test_blockchain_creation():
    remove_file()
    assert os.path.isfile(file) == False
    test_chain = Blockchain()
    assert os.path.isfile(file) == True
    assert test_chain.last_block.data == 'Genesis Block'
    remove_file()


def test_blockchain_add_block():
    remove_file()
    test_chain = Blockchain()
    active = ActiveChain(test_chain)
    assert len(blockchain_as_list()) == 1
    block = Block('a', active.blockchain.last_block.current_hash, active.blockchain.difficulty)
    active.add_to_chain(block)
    assert len(blockchain_as_list()) == 2
    assert test_chain.last_block.data == 'a'
    remove_file()


def test_make_block_from_chain():
    remove_file()
    test_chain = Blockchain()
    active = ActiveChain(test_chain)
    block = Block('a', active.blockchain.last_block.current_hash, active.blockchain.difficulty)
    active.add_to_chain(block)
    active.blockchain.last_block = None
    assert active.blockchain.last_block == None
    active.blockchain.last_block = active.blockchain.get_last_block()
    last_block = active.blockchain.make_block_from_string_data()
    assert block.data == last_block.data
    assert block.previous_hash == last_block.previous_hash
    assert str(block.timestamp) == last_block.timestamp
    assert block.current_hash == last_block.current_hash
    assert str(block.nonce) == last_block.nonce
    assert str(block.difficulty) == last_block.difficulty
    remove_file()


def test_block_valid():
    remove_file()
    test_chain = Blockchain()
    active = ActiveChain(test_chain)
    block = Block('a', active.blockchain.last_block.current_hash, active.blockchain.difficulty)
    active.add_to_chain(block)
    active.blockchain.last_block = active.blockchain.get_last_block()
    active.blockchain.make_block_from_string_data()
    assert active.blockchain.is_valid(block) == True
    active.blockchain.add_block(block)
    t_block = active.blockchain.last_block
    t_block.current_hash = '123'
    assert active.blockchain.is_valid(t_block) == False
    remove_file()


def test_change_difficulty():
    remove_file()
    test_chain = Blockchain()
    active = ActiveChain(test_chain)
    active.blockchain.BLOCKS_ADJUSTMENT = 2
    assert active.blockchain.difficulty == 0
    block = Block('a', active.blockchain.last_block.current_hash, active.blockchain.difficulty)
    active.add_to_chain(block)
    block = Block('a', active.blockchain.last_block.current_hash, active.blockchain.difficulty)
    active.add_to_chain(block)
    assert active.blockchain.difficulty == 1
    remove_file()


def test_get_difficulty():
    remove_file()
    test_chain = Blockchain()
    active = ActiveChain(test_chain)
    assert active.blockchain.difficulty == 0
    assert active.blockchain.difficulty == get_difficulty(file)
    remove_file()


def test_blockchain_as_list():
    remove_file()
    test_chain = Blockchain()
    active = ActiveChain(test_chain)
    assert len(blockchain_as_list(file)) == 1
    block = Block('a', active.blockchain.last_block.current_hash, active.blockchain.difficulty)
    active.add_to_chain(block)
    active.blockchain.add_block(block)
    assert len(blockchain_as_list(file)) == 2
    res = ast.literal_eval(blockchain_as_list(file)[-1])
    assert res == active.blockchain.get_last_block()
    remove_file()


def test_make_data():
    remove_file()
    test_chain = Blockchain()
    active = ActiveChain(test_chain)
    block = Block('a', active.blockchain.last_block.current_hash, active.blockchain.difficulty)
    block_data_dict = make_data(block)
    assert block_data_dict['timestamp'] == str(block.timestamp)
    assert block_data_dict['data'] == str(block.data)
    assert block_data_dict['data'] == 'a'
    assert block_data_dict['currentBlockHash'] == str(block.current_hash)
    assert block_data_dict['previousBlockHash'] == str(block.previous_hash)
    assert block_data_dict['previousBlockHash'] == str(active.blockchain.last_block.current_hash)
    assert block_data_dict['nonce'] == str(block.nonce)
    assert block_data_dict['difficulty'] == str(block.difficulty)
    assert block_data_dict['difficulty'] == str(active.blockchain.difficulty)

    remove_file()
