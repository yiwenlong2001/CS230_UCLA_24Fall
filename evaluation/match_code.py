import sys
import os
from antlr4 import *
import importlib

def parse_line(parser, line):
    input_stream = InputStream(line)
    lexer = parser["Lexer"](input_stream)
    token_stream = CommonTokenStream(lexer)
    parser_instance = parser["Parser"](token_stream)
    try:
        tree = parser_instance.s()
        return True, tree.toStringTree(recog=parser_instance)
    except Exception:
        return False, None

def main(grammar_name, code_file):
    output_dir = f"./inter_folder/{grammar_name}/g4_folder"
    sys.path.insert(0, output_dir)

    try:
        lexer_module = f"{grammar_name}Lexer"
        parser_module = f"{grammar_name}Parser"
        Lexer = getattr(importlib.import_module(lexer_module), f"{grammar_name}Lexer")
        Parser = getattr(importlib.import_module(parser_module), f"{grammar_name}Parser")
    except ImportError as e:
        print(f"Error: Failed to import Lexer or Parser: {e}")
        sys.exit(1)

    try:
        with open(code_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Code file {code_file} not found!")
        sys.exit(1)

    parser = {"Lexer": Lexer, "Parser": Parser}
    print("Matching Results:")
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
        success, tree = parse_line(parser, line)
        if success:
            print(f"Line {i}: Matched")
            print(f"  Parse Tree: {tree}")
        else:
            print(f"Line {i}: Not Matched")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python match_code.py <grammar_name> <code_file>")
        sys.exit(1)

    grammar_name = sys.argv[1]
    code_file = sys.argv[2]
    main(grammar_name, code_file)
