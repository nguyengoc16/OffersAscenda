from typing import Any
import json

class Offer:
    _offer_data: dict[str, Any] = {}

    def __init__(self) -> None:
        # Specify the path to JSON file
        path = '../input.json'

        # Open the file and load the JSON data
        with open(path, 'r') as file:
            data = json.load(file)
            
        self._offer_data = data

    @property
    def offer_data(self):
        return self._offer_data
