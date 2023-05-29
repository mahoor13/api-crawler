import os
import json

# Path to the directory containing JSON files
folder_path = "json"

# Generate the CREATE TABLE statement
insert_script = """
CREATE TABLE IF NOT EXISTS postal_code_kilid (
    postal_code CHAR(10),
    age INT,
    floor_area DECIMAL(10, 2),
    location TEXT,
    stats_kind INT,
    stats_kind_phrase VARCHAR(128),
    value INT,
    order_id INT,
    symbol VARCHAR(16),
    description TEXT,
    fixed_period BOOL
);


"""

# Iterate over the JSON files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    # Read the JSON data from the file
    with open(file_path) as json_file:
        data = json.load(json_file)

    # Extract the data from the JSON
    attributes = data["attributes"]
    value = data["value"]

    if attributes is None and value is None:
        continue
    
    # Extract the values from attributes
    if attributes is not None:
        age = attributes.get("age") if attributes.get("age") else "NULL"
        floor_area = attributes.get("floorArea") if attributes.get("floorArea") else "NULL"
        location = attributes.get("location", "")

    if value is not None:
        # Extract the values from value
        stats_kind = value.get("statsKind") if value.get("statsKind") else "NULL"
        stats_kind_phrase = value.get("statsKindPhrase", "")
        value_value = round(value.get("value") if value.get("value") else 0)
        order_id = value.get("orderId") if value.get("orderId") else "NULL"
        symbol = value.get("symbol", "")
        description = value.get("description") if value.get("description") else "NULL"
        fixed_period = 1 if value.get("fixedPeriod") else 0

    file_name = file_name.replace('.json', '')
    # Generate the INSERT INTO statement
    insert_statement = f"INSERT INTO postal_code_kilid VALUES ('{file_name}', {age}, {floor_area}, '{location}', {stats_kind}, '{stats_kind_phrase}', {value_value}, {order_id}, '{symbol}', {description}, {fixed_period});\n"

    insert_script += insert_statement

# Write the CREATE TABLE and INSERT INTO scripts to a file
with open("insert.sql", "w") as output_file:
    output_file.write(insert_script)

print(f"MySQL script generated successfully. Output file: insert.sql")
