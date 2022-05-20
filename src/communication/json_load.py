import json
import os.path

def data_load():
    inst_id = input("Provide the Instruction ID : ")
    file_name = "Inst"+str(inst_id)
    status = os.path.isfile(file_name)
    loaded_data = {"inst_id":"NOID", "bot_name":"", "bot_id":"", "bot_config":"", "bot_inst_code":"", "bot_metal_sense":"", "bot_gps_val":"","bot_timestamp":""}
    if status == True:
        with open(file_name, "r") as json_file:
            loaded_data = json.load(json_file)
        return loaded_data
    else:
        print("This file Does NOT Exist.")
        return loaded_data
