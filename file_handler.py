import json
import os


class FileHandler:

    @staticmethod
    def save_data(filename, data):
        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print("Error saving data:", e)

    @staticmethod
    def load_data(filename):
        try:
            if not os.path.exists(filename):
                return []

            with open(filename, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            print("Invalid JSON file.")
            return []

        except Exception as e:
            print("Error loading data:", e)
            return []