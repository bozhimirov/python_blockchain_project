import ast
import json
import os

from active_chain import ActiveChain
from block import Block
from get_diff import get_difficulty


class Blockchain:
    """
    A class representing a blockchain.

    Attributes:
        difficulty (int): The number of starting zeroes of the hash, the number of difficulty for mining of a block.
        Default value is zero.
    """
    # A constant that shows how many block have to be mined before increasing the difficulty of the blockchain
    BLOCKS_ADJUSTMENT = 2016

    def __init__(self, difficulty=0) -> None:
        """
        Initializes a Blockchain object.

        Parameters:
            difficulty (int): The number of starting zeroes of the hash, the number of difficulty for mining of a block.
                Default value is zero.

        Return:
        None
        """
        self.difficulty = difficulty
        self.last_block = None
        if not os.path.isfile(ActiveChain.WRITE_PATH):
            a = []
            if not os.path.isfile(ActiveChain.WRITE_PATH):
                a.append(str(self.create_genesis_block()))
                with open(ActiveChain.WRITE_PATH, mode='w') as f:
                    f.write(json.dumps(a))
                    print(f'Block # 0 mined')
                    print(f'new block with hash {self.last_block.current_hash} successfully validated')
        else:
            self.last_block = self.get_last_block()
            self.last_block = self.make_block_from_string_data()
        # function that check if there are enough blocks mined so difficulty to be increased
        self.check_for_difficulty_change()

    @staticmethod
    def get_last_block() -> str:
        """
        This function get the string value of the last block from the blockchain file.

        Return:
        str: Return the string representation of the last block from the blockchain file.
        """
        with open(ActiveChain.WRITE_PATH) as json_file:
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

    @staticmethod
    def blockchain(file=ActiveChain.WRITE_PATH) -> list:
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

    def create_genesis_block(self) -> dict:
        """
        This function creates the first genesis block of the blockchain with predefined data with the hash according to
        the current difficulty of the blockchain. Creates dictionary with the values for all the attributes of the
        current block. And update the last block attribute of the blockchain.

        Return:
        dict: Return all the attributes for the current block as a dictionary.
        """
        start_block = Block("Genesis Block", '0', self.difficulty)
        start_block.proof_of_work()
        data = self.make_data(start_block)
        self.last_block = start_block
        return data

    def add_block(self, new_block) -> dict:
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
        data = self.make_data(new_block)
        self.last_block = new_block
        return data

    @staticmethod
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
        """
        This function increases the current difficulty of the blockchain by one.

        Return:
        None
        """
        self.difficulty = get_difficulty(ActiveChain.WRITE_PATH) + 1

    def check_for_difficulty_change(self) -> None:
        """
        This function check if there is a need for increasing the current difficulty of the blockchain by one according
        to the blocks_adjustment constant.

        Return:
        None
        """
        if len(self.blockchain()) % self.BLOCKS_ADJUSTMENT == 0:
            self.change_difficulty()

