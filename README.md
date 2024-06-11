# python_blockchain_project

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

## Description

#### **static/css**
In styles.css are all the formatting of the html template

#### **templates**
index.html contains the structure of the UI

#### **active_chain.py**
Contains the ActiveChain class with functions that manage blocks and help with information in the terminal. A list of
all functions of the class:

- add_to_chain
- print_in_terminal_block_mined
- print_in_terminal_block_validated

#### **block.py**
block.py contains Block class that makes a block that can be added to the blockchain.  A list of all functions of the 
class:

- make_hash
- proof_of_work
- __str__

#### **blockchain.py**
blockchain.py contains Blockchain class that makes a blockchain.  A list of all functions of the class:

- get_last_block
- make_block_from_string_data
- create_genesis_block
- add_block
- is_valid
- change_difficulty
- check_for_difficulty_change

#### **requirements.txt**
In this file there are the requirements that have to be installed for the program to work properly


#### **test_project.py**
In test_project.py file there are some tests of the main functionality of the program. A list of all functions:

- remove_file
- test_block
- test_block_with_difficulty
- test_blockchain_creation
- test_blockchain_add_block
- test_make_block_from_chain
- test_block_valid
- test_change_difficulty
- test_get_difficulty
- test_blockchain_as_list
- test_make_data


### **project.py**
This is the main file of the project. A list of all functions:

- main
- get_difficulty
- blockchain_as_list
- make_data
