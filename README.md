# Postal Code JSON Fetcher

**crawler.py** script fetches JSON data for postal codes from a specified API endpoint and saves the results to individual JSON files.
**json2sql.py** script generates an SQL insert script for loading postal code data from JSON files into a MySQL table.

## Prerequisites

- Python 3.x
- `requests` library

## Usage

1. Install the `requests` library if not already installed:
   ```
   $ pip install requests
   ```

2. Prepare a CSV file named postal_code.csv with the list of postal codes to fetch JSON data for.

3. Run the script with the following command:

   ```
   $ python crawler.py <API_URL> <AUTH_TOKEN>
   ```

   Replace <API_URL> with the URL of the API endpoint and <AUTH_TOKEN> with the authorization token required for the API.

   Example:

   ```
   $ python crawler.py "https://api.example.com/endpoint" "abcdef123456"
   ```

4. The script will send parallel requests to fetch JSON data for each postal code in the CSV file. The JSON data will be saved in individual files under the json/ directory.

5. The script will display progress messages for each postal code indicating if the request was successful or encountered an error.

6. Run the json2sql.py script using the following command:

   ```
   $ python json2sql.py
   ```

7. The script will read the JSON files in the json directory and generate an SQL insert script.

8. Use the generated insert.sql script to insert the postal code data into the table in your MySQL database.

## Customization

If you need to modify the table schema, update the CREATE TABLE statement in the script before running it.

If your JSON files have different field names or structure, you may need to adjust the code accordingly.

## License

This project is licensed under the [MIT License](https://chat.openai.com/LICENSE).