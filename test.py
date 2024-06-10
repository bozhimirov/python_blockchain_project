
import pytest

from blockchain import Blockchain
from block import Block
from active_chain import ActiveChain

test = Blockchain()
chain = ActiveChain(test)
data = 'asd'
if data:
    chain.add_to_chain(
        Block(data, chain.blockchain.last_block.current_hash, chain.blockchain.difficulty))
all_chain = chain.blockchain.blockchain()


