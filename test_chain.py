import os

import pytest

from block import Block
from active_chain import ActiveChain
from blockchain import Blockchain
from get_diff import get_difficulty


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
    active.add_to_chain(block)
    assert len(active.blockchain.blockchain()) == 2
    assert test_chain.last_block.data == 'a'
    os.remove(file)


def test_make_block_from_chain():
    file = ActiveChain.WRITE_PATH
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
    os.remove(file)


def test_block_valid():
    file = ActiveChain.WRITE_PATH
    test_chain = Blockchain()
    active = ActiveChain(test_chain)
    block = Block('a', active.blockchain.last_block.current_hash, active.blockchain.difficulty)
    active.add_to_chain(block)
    active.blockchain.last_block = active.blockchain.get_last_block()
    active.blockchain.make_block_from_string_data()
    assert active.blockchain.is_valid(block) == True
    active.blockchain.add_block(block)
    t_block = active.blockchain.last_block
    print(type(t_block))
    t_block.current_hash = '123'
    assert active.blockchain.is_valid(t_block) == False
    os.remove(file)


def test_change_difficulty():
    file = ActiveChain.WRITE_PATH
    test_chain = Blockchain()
    active = ActiveChain(test_chain)
    active.blockchain.BLOCKS_ADJUSTMENT = 2
    assert active.blockchain.difficulty == 0
    block = Block('a', active.blockchain.last_block.current_hash, active.blockchain.difficulty)
    active.add_to_chain(block)
    block = Block('a', active.blockchain.last_block.current_hash, active.blockchain.difficulty)
    active.add_to_chain(block)
    assert active.blockchain.difficulty == 1
    os.remove(file)


def test_get_diff():
    file = ActiveChain.WRITE_PATH
    test_chain = Blockchain()
    active = ActiveChain(test_chain)
    assert active.blockchain.difficulty == 0
    assert active.blockchain.difficulty == get_difficulty(file)




