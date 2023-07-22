import re

from dynamic_markdown.ArgumentParser import ArgumentParser
from file_parser import ParserFactory

def main():
    args = ArgumentParser().parse()
    variables = args.variables

    if args.variable_file:
        parser = ParserFactory().create(args.variable_file)
        variables.update(parser.parse())

    with open(args.input_file, "r") as input_file:
        with open(args.output_file, "w") as output_file:
            while line := input_file.readline(): 
                matches = re.findall(r"\{\{(.*)\}\}", line)
                for match in matches:
                    if match not in variables:
                        raise Exception(f"Variable {match} not found")

                    line = line.replace("{{%s}}" % match, str(variables[match]))
                output_file.write(line)

if __name__ == "__main__":
    main()
