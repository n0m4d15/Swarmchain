import json

def data_dump(instruction_data):
    print("Creating JSON file...")

    file_name = "Inst"+str(instruction_data["inst_id"])
    with open(file_name, "w") as json_file:
        json.dump(instruction_data, json_file)

    print("JSON file successfully created!")