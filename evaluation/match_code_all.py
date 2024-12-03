import sys
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
import importlib

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append((line, column, msg))


def parse_line(parser, line):
    input_stream = InputStream(line)
    lexer = parser["Lexer"](input_stream)
    token_stream = CommonTokenStream(lexer)
    parser_instance = parser["Parser"](token_stream)

    error_listener = CustomErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    parser_instance.removeErrorListeners()
    parser_instance.addErrorListener(error_listener)

    try:
        tree = parser_instance.s()
        # Check if there were syntax errors
        if error_listener.errors:
            return False, None, error_listener.errors
        return True, tree.toStringTree(recog=parser_instance), None
    except Exception as e:
        # Handle unexpected exceptions (e.g., runtime errors in the parser)
        return False, None, [str(e)]

def main(grammar_name, code_file):
    scoreboard = {'grammer_name': grammar_name, 'total_lines':0, 'unmatched_lines':0}

    output_dir = f"./inter_folder/{grammar_name}/g4_folder"
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

    parser = {"Lexer": Lexer, "Parser": Parser}
    print(f"Matching Results for grammar: {grammar_name}")
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
        scoreboard['total_lines']+=1
        success, tree, err = parse_line(parser, line)
        if success:
            print(f"Line {i}: Matched by {grammar_name}")
            print(f"  Parse Tree: {tree}")
        else:
            print(f"Unmatched Line {i} for {grammar_name}")
            print(f"ERROR: {err}")
            scoreboard['unmatched_lines']+=1
    
    return scoreboard


if __name__ == "__main__":
    args = sys.argv[1:]

    # Split the arguments into two lists using the delimiter
    delimiter_index = args.index("DELIMITER")
    grammar_name_list = args[:delimiter_index]
    code_file_list = args[delimiter_index + 1:]

    scoreboards=[]
    for grammar_name, code_file in zip(grammar_name_list, code_file_list):
        scoreboard = main(grammar_name, code_file)
        scoreboards.append(scoreboard)
    
    
with open("scoreboard.txt", "w") as file:
    for scoreboard in scoreboards:
        total_lines = scoreboard['total_lines']
        unmatched_lines = scoreboard['unmatched_lines']
        correct_rate = 1 - unmatched_lines/total_lines if total_lines!=0 else 0
        formatted_correct_rate = f"{correct_rate:.2%}"
        file.writelines(f"{scoreboard['grammer_name']}: Number of string tested: {total_lines}, Number of Error: {unmatched_lines}, Correct Rate: {formatted_correct_rate} \n")