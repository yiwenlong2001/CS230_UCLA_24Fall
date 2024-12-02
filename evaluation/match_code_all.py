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
    output_dir = f"./inter_folder/{grammar_name}"
    sys.path.insert(0, output_dir)

    try:
        lexer_module = f"{grammar_name}Lexer"
        parser_module = f"{grammar_name}Parser"
        Lexer = getattr(importlib.import_module(lexer_module), f"{grammar_name}Lexer")
        Parser = getattr(importlib.import_module(parser_module), f"{grammar_name}Parser")
    except ImportError as e:
        print(f"Error: Failed to import Lexer or Parser for {grammar_name}: {e}")
        sys.exit(1)

    try:
        with open(code_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Code file {code_file} not found!")
        sys.exit(1)

    unmatched_lines = []
    parser = {"Lexer": Lexer, "Parser": Parser}
    print(f"Matching Results for grammar: {grammar_name}")
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
        success, tree = parse_line(parser, line)
        if success:
            print(f"Line {i}: Matched by {grammar_name}")
            print(f"  Parse Tree: {tree}")
        else:
            unmatched_lines.append((i, line))

    if unmatched_lines:
        print(f"Unmatched lines for grammar {grammar_name}:")
        for line_num, content in unmatched_lines:
            print(f"  Line {line_num}: {content}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python match_code.py <grammar_name> <code_file>")
        sys.exit(1)

    grammar_name = sys.argv[1]
    code_file = sys.argv[2]
    main(grammar_name, code_file)
