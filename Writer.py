import json
import os
import csv
import logging


class Writer:
    def __init__(self, json_file, csv_file):
        self.json_file = json_file
        self.csv_file = csv_file

    def write_to_json(self, data):
        if not isinstance(data, dict):
            raise ValueError('Data must be a dictionary.')

        required_keys = {'round_no', 'wolf_pos', 'sheep_pos'}
        if not required_keys.issubset(data.keys()):
            raise ValueError(f"Data must contain keys: {required_keys}")

        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as file:
                try:
                    existing_data = json.load(file)
                    if not isinstance(existing_data, list):
                        raise ValueError(
                            "Existing file content is not a list."
                        )
                except json.JSONDecodeError:
                    existing_data = []
        else:
            existing_data = []

        existing_data.append(data)

        with open(self.json_file, 'w') as file:
            json.dump(existing_data, file, indent=4)
        logging.debug("Information was saved to pos.json file")

    def write_to_csv(self, round_number, number_of_alive_sheeps):
        if not isinstance(round_number, int):
            raise ValueError('Round number must be an integer.')

        if not isinstance(number_of_alive_sheeps, int):
            raise ValueError('Number of alive sheeps must be an integer.')

        headers = ['round_number', 'number_of_alive_sheeps']
        row = [round_number, number_of_alive_sheeps]

        file_exists = os.path.exists(self.csv_file)

        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(headers)

            writer.writerow(row)
        logging.debug("Information was saved to alive.csv file")

    def erase_file_content(self):
        with open(self.csv_file, 'w'):
            pass
        with open(self.json_file, 'w'):
            pass