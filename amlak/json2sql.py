import os
import sys
import json
import re

# Path to the directory containing JSON files
folder_path = "json"

def to_underscore(str):
    # Add an underscore before any capital letter preceded by a lowercase letter or a number
    underscore_string = re.sub(r'(([A-Z]*)([A-Z]))', r'\2_\3', str)    
    # Convert the string to lowercase
    underscore_string = underscore_string.lstrip('_').lower()    
    return underscore_string

# Generate the insert script
insert_script = """
CREATE TABLE IF NOT EXISTS postal_code_amlak (
    postal_code CHAR(10), 
    code INT,
    id CHAR(36),
    hc_contract_types_name VARCHAR(128),
    hc_contract_type_code INT,
    hc_estate_types_name VARCHAR(128),
    mantaghe_shahrdari INT,
    hc_usage_types_name VARCHAR(128),
    area INT,
    quota_from INT,
    quota_to INT,
    fee VARCHAR(32),
    price VARCHAR(32),
    price_per_m2 VARCHAR(32),
    floor_no INT,
    price_monthly VARCHAR(32),
    sale_sakht INT,
    hc_frame_types_name VARCHAR(128),
    apartment_floor_side_name VARCHAR(128),
    hc_frontage_type_name VARCHAR(128),
    bed_room_count INT,
    p_trace_id_date VARCHAR(16),
    unit_floor_side_name VARCHAR(128),
    tel_statuse_name VARCHAR(32),
    warehouse_status VARCHAR(32),
    parking_status VARCHAR(32),
    floors_count INT,
    unit_per_floor INT,
    elevator_status VARCHAR(32),
    subscription_status VARCHAR(128),
    area_diff INT,
    life_time_diff INT,
    d INT,
    rn INT,
    m_y VARCHAR(32)
);


"""

# Iterate over the JSON files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    # Read the JSON data from the file
    with open(file_path) as json_file:
        data = json.load(json_file)

    # Extract the "rows" array from the JSON data
    rows = data["rows"]

    for row in rows:
        column_names = []
        column_values = []
        for key, value in row.items():
            column_names.append(to_underscore(key).lower())
            if value is None:
                column_values.append("NULL")
            elif isinstance(value, str):
                column_values.append(f"'{value}'")
            elif isinstance(value, bool):
                column_values.append("1" if value else "0")
            else:
                column_values.append(str(value))

        columns = ", ".join(column_names)
        values = ", ".join(column_values)

        file_name = file_name.replace('.json', '')
        insert_script += f"INSERT INTO postal_code_amlak (postal_code, {columns}) VALUES ('{file_name}', {values});\n"

with open("insert.sql", "w") as script_file:
    script_file.write(insert_script)
print("Insert scripts generated successfully.")