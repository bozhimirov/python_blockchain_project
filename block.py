import hashlib
from datetime import datetime


class Block:
    """
    A class representing a block from a blockchain.

    Attributes:
        data (str): The data to be written in the blockchain.
        previous_hash (str): The hash of the previous block, if there is no previous block, the hash is zero.
        difficulty (int): The number of starting zeroes of the hash, the number of difficulty for mining of a block.
        nonce (int): The numerical value used in a trial-and-error process to have a block added to the blockchain.
        timestamp (float): The exact moment the block is created, represented in Unix Time Representation.
        current_hash (str): The hash of the current block.
    """
    def __init__(self, data, previous_hash, difficulty, nonce=0, timestamp=datetime.utcnow().timestamp(),
                 current_hash='') -> None:
        """
        Initializes a Block object.

        Parameters:
            data (str): The data to be written in the blockchain.
            previous_hash (str): The hash of the previous block, if there is no previous block, the hash is zero.
            difficulty (int): The number of starting zeroes of the hash, the number of difficulty for mining of a block.
            nonce (int): The numerical value used in a trial-and-error process to have a block added to the blockchain.
            timestamp (float): The exact moment the block is created, represented in Unix Time Representation.
            current_hash (str): The hash of the current block.
        Return:
        None
        """
        self.data = data
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonce = nonce
        self.timestamp = timestamp
        if not current_hash:
            self.current_hash = self.make_hash()
        else:
            self.current_hash = current_hash

    def make_hash(self) -> str:
        """
        This function calculates the hash of the block, based of the provided parameters.

        Return:
        str: Return the new calculated hash of the block as string.
        """
        hash_string = str(self.previous_hash) + str(self.timestamp) + str(self.data) + str(self.nonce) + str(self.
                                                                                                             difficulty)
        return hashlib.sha256(hash_string.encode()).hexdigest()

    def proof_of_work(self) -> None:
        """
        This function try to calculate the hash of the block to match the current difficulty of the blockchain. If the
        hash doesn't fit the requirements the function changes the value of the nonce and calculate the hash again. When
        the requirements are fulfilled, the nonce used for the calculations is assigned to the block and the current
        hash is assigned to the block.

        Return:
        None: The function directly modify the class attributes.
        """
        while not str(self.current_hash[0:self.difficulty]).startswith("0"*self.difficulty):
            self.nonce += 1
            self.current_hash = self.make_hash()

    def __str__(self) -> str:
        """
        This function concatenates the attributes of the block in a single string.

        Return:
        str: A concatenated string with all the attributes of the block.
        """
        return f'{self.nonce}, {self.timestamp}, {self.data}, {self.previous_hash}, {self.current_hash}'


