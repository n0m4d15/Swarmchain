import os

def del_json():
    inst_id = input("Enter the Instruction ID : ")
    file_name = "Inst" + str(inst_id)
    if os.path.isfile(file_name) == True:
        os.remove(file_name)
        print(str(file_name) + " is Successfully Deleted")
    else:
        print("This file does not exist")