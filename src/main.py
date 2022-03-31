# This is a JSON generating file

import data_input
import data_output
import json_dump
import json_load
import json_delete

#instruction_data = data_input.getData()
#json_dump.data_dump(instruction_data)
#loaded_data = json_load.data_load()
#data_output.putData(loaded_data)

def console_disp():
    print('''
This is the JSON Dumper and Loader for Swarmchain.
Choose 1 for creation of a new JSON file
Choose 2 for loading an existing JSON file
Choose 3 for deleting an existing JSON file
Choose 0 to Exit the Program
    ''')

while True:
    console_disp()
    choice = int(input("Enter your Choice : "))
    if choice == 1:
        instruction_data = data_input.getData()
        json_dump.data_dump(instruction_data)
    elif choice == 2:
        loaded_data = json_load.data_load()
        data_output.putData(loaded_data)
    elif choice == 3:
        json_delete.del_json()
    elif choice == 0:
        exit()
    else:
        print("Invalid Input, Try Again.")