def putData(loaded_data):
    if loaded_data["inst_id"] != "NOID":
        print ("The Loaded Data is Listed Below:")
        print("Instruction ID : " + str(loaded_data["inst_id"]))
        print("Bot Name : " + str(loaded_data["bot_name"]))
        print("Bot ID : " + str(loaded_data["bot_id"]))
        print("Bot Configuration Code : " + str(loaded_data["bot_config"]))
        print("Bot Instruction Code : " + str(loaded_data["bot_inst_code"]))
        print("Bot Metal Sensor Value : " + str(loaded_data["bot_metal_sense"]))
        print("Bot GPS Location : " + str(loaded_data["bot_gps_val"]))
        print("Bot Timestamp: " + str(loaded_data["bot_timestamp"]))