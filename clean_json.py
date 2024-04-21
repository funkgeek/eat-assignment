import json
import sqlite3
from get_data import JustEatAPI

class RestaurantDataProcessor:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path

    def load_data_from_json(self):
        """
        Load data from a JSON file.
        Returns:
            dict: Loaded JSON data.
        """
        with open(self.json_file_path, 'r', encoding='utf-8') as load_f:
            return json.load(load_f)

    def clean_data(self, data):
        """
        Clean the JSON data to keep only selected fields.
        Args:
            data (dict): JSON data to clean.
        Returns:
            list: Cleaned records.
        """
        clean_records = []
        for restaurant in data['restaurants'][:10]:
            clean_record = {}
            for key, value in restaurant.items():
                if key == 'id':
                    clean_record['id'] = value
                elif key == 'cuisines':
                    cuisines = '|'.join(cuisine['name'] for cuisine in value)
                    clean_record['cuisines'] = cuisines
                elif key == 'address':
                    clean_record['address'] = f"{value['firstLine']}, {value['city']}, {value['postalCode']}"
                elif key == 'rating':
                    clean_record['rating'] = value['starRating']
                elif key in ['name']:
                    clean_record[key] = value
            clean_records.append(clean_record)
        return clean_records

    def create_database(self, db_file):
        """
        Create an SQLite database and table to store restaurant data.
        Args:
            db_file (str): Path to the SQLite database file.
        """
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS restaurant(
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        cuisines TEXT,
                        rating REAL,
                        address TEXT
                    )''')
        conn.commit()
        conn.close()

    def insert_data_into_database(self, db_file, clean_records):
        """
        Insert cleaned data into the SQLite database.
        Args:
            db_file (str): Path to the SQLite database file.
            clean_records (list): List of cleaned records.
        """
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        for record in clean_records:
            cur.execute('INSERT INTO restaurant (name, cuisines, rating, address) VALUES (?, ?, ?, ?)', 
                        (record['name'], record['cuisines'], record['rating'], record['address']))
        conn.commit()
        conn.close()


    def print_database_contents(self, db_file):
        """
        Print the contents of the SQLite database.
        Args:
            db_file (str): Path to the SQLite database file.
        """
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM restaurant")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        conn.close()

def main():
    # Fetch data using JustEatAPI
    postcode = "G38AG"
    api = JustEatAPI(postcode)
    api.save_to_json("all_data.json")

    # Process data
    processor = RestaurantDataProcessor("all_data.json")
    data = processor.load_data_from_json()
    clean_records = processor.clean_data(data)

    # Create and populate database
    db_file = "eat_task.db"
    processor.create_database(db_file)
    processor.insert_data_into_database(db_file, clean_records)

    # Print database contents
    processor.print_database_contents(db_file)

if __name__ == "__main__":
    main()
