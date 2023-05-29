import os
import sys
import csv
import requests
import json
import concurrent.futures


csv_file = "postal_code.csv"
url = sys.argv[1]

def fetch_json(postal_code):
    file_name = 'json/' + postal_code + '.json'
    if os.path.isfile(file_name):
        return
    data = {
        'PostalCode': postal_code,
        'page': "1",
        'rows': "20",
        'recaptchaToken': sys.argv[2],
        'filterRules[0][field]': "HCEstateTypesName",
        'filterRules[0][operator]': "equal",
        'filterRules[0][valuetype]': "string",
        'filterRules[1][field]': "HCUsageTypesName",
        'filterRules[1][operator]': "equal",
        'filterRules[1][valuetype]': "string",
    }
    response = requests.post(url, data=data,)
    if response.status_code == 200:
        json_data = response.json()
        # save to file
        with open(file_name, 'w') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=2)
        print(postal_code, " OK")
    else:
        json_data = {}
        print(postal_code, " Error")
    
    return json_data

# Load numbers from CSV file
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    postal_codes = [row[0] for row in csv_reader]

# Send requests in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(fetch_json, postal_codes)