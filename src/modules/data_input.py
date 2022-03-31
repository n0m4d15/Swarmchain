def getData():
    input_data = {"inst_id":"", "bot_name":"", "bot_id":"", "bot_config":"", "bot_inst_code":""}
    print ('''
Welcome to Swarmchain Terminal for JSON file generation.

Enter the Data to be Appended into the JSON file for Parsing:
    ''')

    inst_id=input("Enter the Intruction ID:")
    input_data["inst_id"]=inst_id

    bot_name=input("Enter the Bot Name:")
    input_data["bot_name"]=bot_name
    
    bot_id=input("Enter the Bot Identification Number:")
    input_data["bot_id"]=bot_id

    bot_config=input("Enter the Bot Configuration Code:")
    input_data["bot_config"]=bot_config

    bot_inst_code=input("Enter the Bot Intrustion Code:")
    input_data["bot_inst_code"]=bot_inst_code

    return input_data
    