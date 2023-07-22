import json

from file_parser.FileParser import FileParser

class JsonFileParser(FileParser):
    def __init__(self, file_path : str):
        super().__init__(file_path)

    def _parse(self) -> dict:
        with open(self.file_path, "r") as file:
            return json.load(file)
