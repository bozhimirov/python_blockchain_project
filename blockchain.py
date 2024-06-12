import ast
import json
import os

from active_chain import ActiveChain
from block import Block


class Blockchain:
    """
    A class representing a blockchain.

    Attributes:
        difficulty (int): The number of starting zeroes of the hash, the number of difficulty for mining of a block.
        Default value is zero.
    """
    # A constant that shows how many block have to be mined before increasing the difficulty of the blockchain
    BLOCKS_ADJUSTMENT = 2016

    def __init__(self, difficulty=0, write_path='data.json') -> None:
        """
        Initializes a Blockchain object.

        Parameters:
            difficulty (int): The number of starting zeroes of the hash, the number of difficulty for mining of a block.
                Default value is zero.

        Return:
        None
        """
        self.difficulty = difficulty
        self.write_path = write_path
        self.last_block = None
        if not os.path.isfile(self.write_path):
            a = []
            if not os.path.isfile(self.write_path):
                a.append(str(self.create_genesis_block()))
                with open(self.write_path, mode='w') as f:
                    f.write(json.dumps(a))
                    print(f'Block # 0 mined')
                    print(f'new block with hash {self.last_block.current_hash} successfully validated')
        else:
            self.last_block = self.get_last_block()
            self.last_block = self.make_block_from_string_data()
        # function that check if there are enough blocks mined so difficulty to be increased
        self.check_for_difficulty_change()

    def get_last_block(self) -> str:
        """
        This function get the string value of the last block from the blockchain file.

        Return:
        str: Return the string representation of the last block from the blockchain file.
        """
        with open(self.write_path) as json_file:
            feeds = json.load(json_file)
            return ast.literal_eval(feeds[-1])

    def make_block_from_string_data(self) -> Block:
        """
        This function make a Block from the string representation of a block.

        Return:
        str: Return the block object with all the needed attributes.
        """
        return Block(data=self.last_block['data'], previous_hash=self.last_block['previousBlockHash'],
                     difficulty=self.last_block['difficulty'], nonce=self.last_block['nonce'],
                     timestamp=self.last_block['timestamp'], current_hash=self.last_block['currentBlockHash'])

    def create_genesis_block(self) -> dict:
        from project import make_data
        """
        This function creates the first genesis block of the blockchain with predefined data with the hash according to
        the current difficulty of the blockchain. Creates dictionary with the values for all the attributes of the
        current block. And update the last block attribute of the blockchain.

        Return:
        dict: Return all the attributes for the current block as a dictionary.
        """
        start_block = Block("Genesis Block", '0', self.difficulty)
        start_block.proof_of_work()
        data = make_data(start_block)
        self.last_block = start_block
        return data

    def add_block(self, new_block) -> dict:
        from project import make_data
        """
        This function check if the difficulty has to be increased and then creates suitable hash for the new block
        for the blockchain. Creates dictionary with the values for all the attributes of the current block. And update
        the last block attribute of the blockchain.

        Parameters:
            new_block (Block): The block that has to be added to the blockchain.

        Return:
        dict: Return all the attributes for the current block as a dictionary.
        """
        self.check_for_difficulty_change()
        new_block.proof_of_work()
        data = make_data(new_block)
        self.last_block = new_block
        return data

    def is_valid(self, block) -> bool:
        """
        This function check if there is a manipulation between the current and previous block, if there are differences
        in the hashes the validation doesn't pass.

        Parameters:
            block (Block): The block that has to be added to the blockchain.

        Return:
        bool: Return True if the info form the previous block is not manipulated and the hashes of the current block and
        the previous one are the same. If there is some difference in the hashes the function return False.
        """
        if block.current_hash != block.make_hash() and block.previous_hash != self.last_block.current_hash:
            return False
        return True

    def change_difficulty(self) -> None:
        from project import get_difficulty as get_diff
        """
        This function increases the current difficulty of the blockchain by one.

        Return:
        None
        """
        self.difficulty = get_diff(self.write_path) + 1

    def check_for_difficulty_change(self) -> None:
        from project import blockchain_as_list
        """
        This function check if there is a need for increasing the current difficulty of the blockchain by one according
        to the blocks_adjustment constant.

        Return:
        None
        """
        if len(blockchain_as_list(file=self.write_path)) % self.BLOCKS_ADJUSTMENT == 0:
            self.change_difficulty()
