# This is the Main Code
# Written by N0M4D15 on 19th April 2022

from general import block_gen, data_input, data_output, json_delete, json_dump, json_load
import json
import os.path

print('''
_______________________________________________________________________________________________________
''')
print('''
Welcome to Swarmchain System. 
This is an emulation of the automated working of Swarmchain nodes when in Action.

Firstly, Create the JSON Package to be Distributed amongst other nodes. 
Note that the generation of this file is automated in Action.

Secondly, Create the first Block of the Blockchain using the First Instruction. 
Note that the naming of the file increments automatically in Action.

Thirdly, Iteratively, the data gets accumulated, stored in JSON file. 
sent to every other nodes in the network and gets appended into the blockchain during action.
''')

print('''
_______________________________________________________________________________________________________
''')

print('''
1) First Instruction Generation:
''')

print('''
_______________________________________________________________________________________________________
''')

inst_data = data_input.getData()
json_dump.data_dump(inst_data)

print('''
_______________________________________________________________________________________________________
''')

print('''
2) Set up the initial block of the Blockchain:
''')

print('''
_______________________________________________________________________________________________________
''')

mission_id = input("Enter the Mission ID : ")
inst_id = input("Enter the Instruction ID : ")
file_name = "Inst"+str(inst_id)
status = os.path.isfile(file_name)
if status == True:
    with open(file_name, "r") as json_file:
        loaded_data = str(json.load(json_file))
    init = block_gen.SwarmChainBlock(mission_id, loaded_data)
    prev_block_data = init.block_data
    prev_block_hash = init.block_hash
    print(prev_block_data)
    print(prev_block_hash)
else:
    print("This file Does NOT Exist. Initial Block Creation Failed!")
    exit()

print('''
3) The iteration starts from here, constant data accumulation and appending into the blockchain.
Note that the consensus algorithm to check for the authorization of appending the data into blockchain is pending.
''')

print('''
_______________________________________________________________________________________________________
''')

def console_disp():
    print('''
This is the JSON Dumper and Loader for Swarmchain.
Choose 1 for creation of a new JSON file
Choose 2 for loading an existing JSON file
Choose 3 for deleting an existing JSON file
Choose 0 to Exit the Program
    ''')

while True:
    print('''
_______________________________________________________________________________________________________
    ''')
    console_disp()
    choice = int(input("Enter your Choice : "))
    if choice == 1:
        instruction_data = data_input.getData()
        json_dump.data_dump(instruction_data)
        inst_id=input("Enter the Intruction ID to authenticate:")
        file_name = "Inst"+str(inst_id)
        status = os.path.isfile(file_name)
        if status == True:
            with open(file_name, "r") as json_file:
                loaded_data = str(json.load(json_file))
            init = block_gen.SwarmChainBlock(prev_block_hash, loaded_data)
            prev_block_data = init.block_data
            prev_block_hash = init.block_hash
            print(prev_block_data)
            print(prev_block_hash)
        else:
            print("This file Does NOT Exist. Initial Block Creation Failed!")
            exit()
    elif choice == 2:
        loaded_data = json_load.data_load()
        data_output.putData(loaded_data)
        print(f"The current block hash value is : {prev_block_hash}")
    elif choice == 3:
        json_delete.del_json()
    elif choice == 0:
        exit()
    else:
        print("Invalid Input, Try Again.")