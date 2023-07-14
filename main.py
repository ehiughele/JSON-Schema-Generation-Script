import json
import os

def sniff_json_schema(json_data):
    schema = {}
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == "message":
                if isinstance(value, dict):
                    for msg_key, msg_value in value.items():
                        schema[msg_key] = generate_schema(msg_value)
    return schema

def generate_schema(data):
    if isinstance(data, dict):
        schema = {}
        for key, value in data.items():
            if isinstance(value, dict):
                schema[key] = generate_schema(value)
            elif isinstance(value, list) and value:
                if isinstance(value[0], dict):
                    schema[key] = {
                        "type": "array",
                        "tag": "",
                        "description": "",
                        "required": False,
                        "items": generate_schema(value[0])
                    }
                else:
                    schema[key] = {
                        "type": "enum",
                        "tag": "",
                        "description": "",
                        "required": False,
                        "values": [type(item).__name__ for item in value]
                    }
            else:
                schema[key] = {
                    "type": type(value).__name__,
                    "tag": "",
                    "description": "",
                    "required": False
                }
        return schema

# Specify the paths
input_file = 'C:/Users/HP/OneDrive/Desktop/Data_science/Python_engineer_assessment/python_engineer_experienced_professional/data/data_1.json'
output_file = 'C:/Users/HP/OneDrive/Desktop/Data_science/Python_engineer_assessment/python_engineer_experienced_professional/schema/schema_1.json'

# Read the JSON file
with open(input_file, 'r') as file:
    json_data = json.load(file)

# Sniff the JSON schema
schema = sniff_json_schema(json_data)

# Dump the schema to a different location
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, 'w') as file:
    json.dump(schema, file, indent=4)

print("Schema has been successfully dumped to", output_file)