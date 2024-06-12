# Python Blockchain Project

#### Video Demo:  <URL HERE>

#### Description:
Demo of a blockchain written in python with local data.json file that stores the blockchain info. Each block has a data,
timestamp, previous hash, difficulty, nonce and current hash. After initiation automatically is generated genesis block 
and a data file is created to store the blocks. After that from the UI users can add data to blockchain. Each block, 
once created, cannot be deleted from the data file. Each time the project is run the data is added to the already 
created blockchain. If the data.json file is deleted, after the project is run new blockchain is created with new 
genesis block.
Enjoy!

## Getting started
- Download Python 3
- Create folder for the project e.g. C:\Users\youruser\Desktop\python_blockchain_project
- Navigate to folder from your terminal and create virtual environment with following command:
```
python -m venv myenv
```
- Activate environment by navigating to myenv/Scripts and execute following command:
```
activate.bat
```
- Clone the repository
```
git clone https://github.com/bozhimirov/python_blockchain_project
```
- Install requirements.txt with following command:
```
pip install -r requirements.txt
```
- Run the tests before first initialization or after any changes in the code are made
```
pytest test_project.py
```
- Run the project
```
python project.py
```
- Navigate to
```
http://localhost:5000
```

## python_blockchain_project

#### **static/css**
In styles.css are all the formatting of the html template

#### **templates**
index.html contains the structure of the UI

#### **active_chain.py**
Contains the ActiveChain class with functions that manage blocks and help with information in the terminal. A list of
all functions of the class:

- add_to_chain - this function check if the block is valid and add it to the blockchain file
- print_in_terminal_block_mined - print in the terminal the number of the block that is mined
- print_in_terminal_block_validated - print in the terminal if the block is validated successfully

#### **block.py**
block.py contains Block class that makes a block that can be added to the blockchain.  A list of all functions of the 
class:

- make_hash - this function calculates the hash of the block, based of the provided parameters
- proof_of_work -this function try to calculate the hash of the block to match the current difficulty of the blockchain.
If the hash doesn't fit the requirements the function changes the value of the nonce and calculate the hash again. When
the requirements are fulfilled, the nonce used for the calculations is assigned to the block and the current hash is 
assigned to the block
- __str__ - this is a string representation of the block's data

#### **blockchain.py**
blockchain.py contains Blockchain class that makes a blockchain.  A list of all functions of the class:

- get_last_block - this function return the string representation of the last block from the blockchain file
- make_block_from_string_data - this function makes a block from hte string representation of the block
- create_genesis_block - generates genesis block if there is no blockchain file and return data of the genesis block as 
dictionary
- add_block - create valid block and return data of the block as dictionary
- is_valid - check if the block is valid based on the current and previous hash
- change_difficulty - increases the current difficulty of the blockchain by one
- check_for_difficulty_change - this function check if there is a need of increasing the current difficulty of the 
blockchain

#### **requirements.txt**
In this file there are the requirements that have to be installed for the program to work properly


#### **test_project.py**
In test_project.py file there are some tests of the main functionality of the program. A list of all functions:

- remove_file - helper function to remove the temporary blockchain file created for testing
- test_block - test block creation
- test_block_with_difficulty - test block creation with increased difficulty
- test_blockchain_creation - test blockchain creation
- test_blockchain_add_block - test adding block to the blockchain
- test_make_block_from_chain - test making block from string data
- test_block_valid - test if block is valid
- test_change_difficulty - test if difficulty is changed if needed
- test_get_difficulty - test get_difficulty function from the project.py 
- test_blockchain_as_list - test blockchain_as_list function from the project.py
- test_make_data - test make_data function from the project.py


#### **project.py**
This is the main file of the project. A list of all functions:

- main - main function that interact with the browser's interface
- get_difficulty - this function return the difficulty of the blockchain based on the info from the previous block in 
the blockchain file
- blockchain_as_list - this function check if there is a file used as a blockchain and if there is such a file extracts 
the block's data and save each block data in a list
- make_data - this function creates dictionary with the values for all the attributes of the current block

