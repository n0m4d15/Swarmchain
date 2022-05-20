from datetime import datetime

def getData():
    input_data = {"inst_id":"", "bot_name":"", "bot_id":"", "bot_config":"", "bot_inst_code":"", "bot_metal_sense":"", "bot_gps_val":"", "bot_timestamp":""}
    print ('''
Welcome to Swarmchain Terminal for JSON file generation.

Enter the Data to be Appended into the JSON file for Parsing:
    ''')

    # Every Instruction Requires its own Instruction ID so that it can be saved in a chronological manner 
    inst_id=input("Enter the Intruction ID:")
    input_data["inst_id"]=inst_id

    # Bot Name denotes the name of the UGV assigned to it
    bot_name=input("Enter the Bot Name:")
    input_data["bot_name"]=bot_name

    # Bot ID is the Identification number associated with the UGV
    bot_id=input("Enter the Bot Identification Number:")
    input_data["bot_id"]=bot_id

    # Bot Config code is necessary as it can be used to determine the operational mode of the UGV
    # 000 - Start UP
    # 001 - Mission Process
    # 002 - Mission Completion
    # 003 - Mission Abort
    # 004 - Error
    bot_config=input("Enter the Bot Configuration Code:")
    input_data["bot_config"]=bot_config

    # An instruction code refers to the potential algorithms that the bots must commit to in a synchronous manner
    bot_inst_code=input("Enter the Bot Instruction Code:")
    input_data["bot_inst_code"]=bot_inst_code

    bot_metal_sense=input("Gathering Metal Sensor OP:")
    input_data["bot_metal_sense"]=bot_metal_sense

    bot_gps_val=input("Gathering Bot GPS Location:")
    input_data["bot_gps_val"]=bot_gps_val

    dt=datetime.now()
    input_data["bot_timestamp"]=str(dt)

    return input_data
    