import argparse
from typing import Optional

class KeyValueAction(argparse.Action):
    def __call__(self, parser, namespace, values : list, option_string=None):
        setattr(namespace, self.dest, dict())
        for value in values:
            key, value = value.split("=")
            getattr(namespace, self.dest)[key] = value

class Arguments():
    def __init__(self, **kwargs):
        self.input_file : str = kwargs["input_file"]
        self.output_file : str = kwargs["output_file"]
        self.variable_file : Optional[str] = kwargs["variable_file"]
        self.variables : dict = kwargs["variables"]

    def __str__(self):
        return f"Arguments(input_file={self.input_file}, output_file={self.output_file}, variable_file={self.variable_file}, variables={self.variables})"

    def __repr__(self):
        return self.__str__()

class ArgumentParser:
    def __init__(self):
        self.application_name = "render_markdown"

    def __setup(self):
        parser = argparse.ArgumentParser(prog=self.application_name)
        parser.add_argument("input_file", help="The file to render")
        parser.add_argument("output_file" , help="The output file")
        parser.add_argument("-v", "--variable-file", help="The template file")
        parser.add_argument("variables", nargs="*", action=KeyValueAction, help="The variables file")
        return parser

    def parse(self) -> Arguments:
        parser = self.__setup()
        args = parser.parse_args()
        return Arguments(**vars(args))
