import os
import json
from active_chain import ActiveChain


def get_difficulty() -> int:
    """
    This function return the difficulty of the blockchain based on the info from the previous block.

    Return:
    int: Return the current difficulty of the blockchain.
    """

    if not os.path.isfile(ActiveChain.WRITE_PATH):
        return 0
    else:
        with open(ActiveChain.WRITE_PATH) as old_json:
            feeds = json.load(old_json)
            diff = feeds[-1].split(',')[-1].split(':')[1].strip()[1:-2]
            return int(diff)
