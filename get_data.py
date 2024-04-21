import requests
import json

class JustEatAPI:
    def __init__(self, postcode):
        self.postcode = postcode
        self.url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }

    def fetch_data(self):
        """
        Fetches data from the Just Eat API based on the provided postcode.
        Returns:
            dict: JSON response data
        """
        try:
            result = requests.get(self.url, headers=self.headers)
            result.raise_for_status()  # Raise an exception for HTTP errors
            content_json = result.json()
            return content_json
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def save_to_json(self, filename):
        """
        Saves fetched data to a JSON file.
        Args:
            filename (str): Name of the JSON file to save.
        """
        data = self.fetch_data()
        if data:
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
                print(f"Data saved to {filename}")
        else:
            print("No data to save.")

