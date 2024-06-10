import json
import os


class ActiveChain:
    # name of the blockchain file
    WRITE_PATH = 'data.json'

    """
    A class representing the active blockchain.

    Attributes:
        blockchain (Blockchain): The blockchain that is active.
    """

    def __init__(self, blockchain) -> None:
        """
        Initializes an ActiveChain object.

        Parameters:
            blockchain (Blockchain): The blockchain that is active.

        Return:
        None
        """
        self.blockchain = blockchain

    def add_to_chain(self, block) -> None:
        """
        This function check if the provided block is valid and add it to the blockchain file.

        Parameters:
            block (Block): The block that has to be added to the blockchain.

        Return:
        None
        """
        if self.blockchain.is_valid(block):

            if not os.path.isfile(self.WRITE_PATH):
                a = [str(self.blockchain.create_genesis_block())]
                with open(self.WRITE_PATH, mode='w') as f:
                    f.write(json.dumps(a))
                    self.print_in_terminal_block_validated()
                    self.print_in_terminal_block_mined()
            else:
                with open(self.WRITE_PATH) as old_json:
                    feeds = json.load(old_json)
                feeds.append(str(self.blockchain.add_block(block)))
                with open(self.WRITE_PATH, mode='w') as f:
                    f.write(json.dumps(feeds))
                self.print_in_terminal_block_validated()
                self.print_in_terminal_block_mined()

    def print_in_terminal_block_mined(self) -> None:
        print(f'Block # {len(self.blockchain.blockchain()) - 1} mined')

    def print_in_terminal_block_validated(self) -> None:
        print(f'New block with hash {self.blockchain.last_block.current_hash} successfully validated')
