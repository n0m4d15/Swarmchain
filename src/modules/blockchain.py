# This is the Blockchain Append Code
# Written by N0M4D15 on 26th Dec 2021

import block_gen
import json
import os.path

print('''
This is the Initial Block of the Blockchain.
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

while True:
    print('''
The appending of blocks can now begin.
Choose 1 to append data into Blockchain
Choose 2 to view previous block data and block hash values
Choose 0 to Exit
    ''')
    choice = int(input("Enter your choice here : "))
    if choice == 1:
        inst_id = input("Enter the Instruction ID : ")
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
    elif choice == 2:
        print(prev_block_data)
        print(prev_block_hash)
    elif choice == 0:
        exit()
    else:
        print("Invalid Input. Try Again.")
