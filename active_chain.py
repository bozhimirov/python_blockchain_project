import json
import os


class ActiveChain:
    """
    A class representing the active blockchain.

    Attributes:
        blockchain (Blockchain): The blockchain that is active.
        write_path: name of the blockchain file
    """

    def __init__(self, blockchain, write_path='data.json') -> None:
        """
        Initializes an ActiveChain object.

        Parameters:
            blockchain (Blockchain): The blockchain that is active.
            write_path(str): name of the blockchain file

        Return:
        None
        """
        self.blockchain = blockchain
        self.write_path = write_path

    def add_to_chain(self, block) -> None:
        """
        This function check if the provided block is valid and add it to the blockchain file.

        Parameters:
            block (Block): The block that has to be added to the blockchain.

        Return:
        None
        """
        if self.blockchain.is_valid(block):
            if not os.path.isfile(self.write_path):
                a = [str(self.blockchain.create_genesis_block())]
                with open(self.write_path, mode='w') as f:
                    f.write(json.dumps(a))
                    self.print_in_terminal_block_validated()
                    self.print_in_terminal_block_mined()
            else:
                with open(self.write_path) as old_json:
                    feeds = json.load(old_json)
                feeds.append(str(self.blockchain.add_block(block)))
                with open(self.write_path, mode='w') as f:
                    f.write(json.dumps(feeds))
                self.print_in_terminal_block_validated()
                self.print_in_terminal_block_mined()

    def print_in_terminal_block_mined(self) -> None:
        from project import blockchain_as_list
        print(f'Block # {len(blockchain_as_list(file=self.write_path)) - 1} mined')

    def print_in_terminal_block_validated(self) -> None:
        print(f'New block with hash {self.blockchain.last_block.current_hash} successfully validated')
