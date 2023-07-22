from os import path
from typing import Optional

from file_parser.FileParser import FileParser
from file_parser.JsonFileParser import JsonFileParser
from file_parser.YamlFileParser import YamlFileParser


class ParserFactory:
    def __init__(self):
        pass

    def create(self, file_path : str) -> FileParser:
        extension = path.basename(file_path).split(".")[-1]

        if extension == "yaml":
            return YamlFileParser(file_path)
        elif extension == "json":
            return JsonFileParser(file_path)
        else:
            raise ValueError(f"Unsupported file extension: {extension}")
