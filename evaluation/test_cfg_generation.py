import os
import re
import subprocess
import unittest

# Paths
G4_FOLDER = "/Users/XiaojieZhou/UCLA/CS230/CS230_UCLA_24Fall/evaluation/g4_folder"
OUTPUT_FOLDER = "/Users/XiaojieZhou/UCLA/CS230/CS230_UCLA_24Fall/evaluation/grammarinator_test_strings"
REGEX_MAP = {
    "cfg0.g4" : r"(a|b)c*",  # Alternation with repetition: matches 'a' or 'b' followed by zero or more 'c's
    "cfg1.g4" : r"ab|cd",  # Simple alternation: matches 'ab' or 'cd'
    "cfg2.g4" : r"a*d",  # Kleene star: matches zero or more 'a's followed by 'd'
    "cfg3.g4" : r"a(b|c)*d",  # Alternation within repetition: matches 'a', zero or more 'b' or 'c', and 'd'
    "cfg4.g4" : r"a",  # Single literal: matches only 'a'
    "cfg5.g4" : r"(a(b|c))*",  # Nested grouping: matches zero or more occurrences of 'a' followed by 'b' or 'c'
    "cfg6.g4" : r"a+",  # One or more repetition: matches one or more 'a's
    "cfg7.g4" : r"b?",  # Optional character: matches zero or one 'b'
    "cfg8.g4" : r"(ab)+",  # Group repetition: matches one or more 'ab's
    "cfg9.g4" : r"a(bc)?",  # Optional group: matches 'a' followed by zero or one 'bc'
    "cfg10.g4" : r"a*b+c?",  # Combination of *, +, ?: matches zero or more 'a's, one or more 'b's, and zero or one 'c'
    "cfg11.g4" : r"a{3}",  # Exact repetition: matches exactly three 'a's
    "cfg12.g4" : r"b{2,}",  # At least repetition: matches two or more 'b's
    "cfg13.g4" : r"c{1,3}",  # Range repetition: matches one to three 'c's
    "cfg14.g4" : r"(ab){2,4}",  # Group repetition with range: matches two to four 'ab's
    "cfg15.g4" : r"a{1}b{2,5}c{3,}",  # Mixed repetition constraints: matches one 'a', two to five 'b's, and three or more 'c's
    "cfg16.g4" : r"[0-9]{2,4}",  # Digit repetition range: matches two to four digits
    "cfg17.g4" : r"a(bc|de)*f",  # Alternation in repetition with suffix: matches 'a', zero or more 'bc' or 'de', and 'f'
    "cfg18.g4" : r"a(b|c)+d",  # Alternation in repetition with suffix: matches 'a', one or more 'b' or 'c', and 'd'
    "cfg19.g4" : r"a{1,2}(b|c){3}",  # Mixed repetition with alternation: matches one to two 'a's followed by three 'b's or 'c's
    "cfg20.g4" : r"(1|2|3)+",  # Alternation with one or more repetition: matches one or more of '1', '2', or '3'
    "cfg21.g4" : r"(ab|cd){2,}",  # Group repetition with minimum constraint: matches two or more 'ab' or 'cd'
    "cfg22.g4" : r"(a(b(c|d)))",  # Nested groups: matches 'a' followed by 'b', and then 'c' or 'd'
    "cfg23.g4" : r"[a-d0-3]",  # Combined range: matches 'a', 'b', 'c', 'd', '0', '1', '2', or '3'
    "cfg24.g4" : r"(ab){3,5}"  # Group repetition with range: matches three to five 'ab's
}

# Commands for processing and generating
PROCESS_CMD = (
    "grammarinator-process {g4_file} -o {output_dir} --no-actions"
)
GENERATE_CMD = (
    "export PYTHONPATH=$PYTHONPATH:/Users/XiaojieZhou/UCLA/CS230/CS230_UCLA_24Fall/evaluation/g4_folder\n"
    "grammarinator-generate {generator} -n 10 -d 50  -o {output_dir}/{grammar_name}_test%d.txt "
)


def process_and_generate():
    """
    Process .g4 files and generate test strings directly.
    """
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for g4_file in os.listdir(G4_FOLDER):
        if not g4_file.endswith(".g4"):
            continue

        g4_path = os.path.join(G4_FOLDER, g4_file)
        grammar_name = g4_file.replace(".g4", "")
        process_output_dir = os.path.join(G4_FOLDER, grammar_name)

        # Ensure the output directory exists
        os.makedirs(process_output_dir, exist_ok=True)

        # Step 1: Process the .g4 file
        process_cmd = PROCESS_CMD.format(
            g4_file=g4_path,
            output_dir=process_output_dir
        )
        try:
            subprocess.run(process_cmd, shell=True, check=True)
            print(f"Processed {g4_file}.")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {g4_file}: {e}")
            continue

        # Step 2: Generate
        generator = f"{g4_file[:-3]}.{g4_file[:-3]}Generator.{g4_file[:-3]}Generator"
        # if not os.path.exists(generator):
        #     print(f"Generate file not found for {g4_file}, skipping generation.")
        #     continue

        generate_cmd = GENERATE_CMD.format(
            generator=generator,
            output_dir=OUTPUT_FOLDER,
            grammar_name=grammar_name
        )
        try:
            subprocess.run(generate_cmd, shell=True, check=True)
            print(f"Generated test strings for {grammar_name}.")
        except subprocess.CalledProcessError as e:
            print(f"Error generating test strings for {grammar_name}: {e}")


# def validate_generated_strings():
#     """
#     Validate generated strings against the original regex.
#     """
#     results = []
#     for grammar_name, regex in REGEX_MAP.items():
#         for i in range(10):
#             test_file_path = os.path.join(OUTPUT_FOLDER, f"{grammar_name[:-3]}_test{i}.txt")
#
#             if not os.path.exists(test_file_path):
#                 print(f"Test file for {grammar_name} not found, skipping.")
#                 continue
#
#             with open(test_file_path, 'r') as f:
#                 test_strings = f.readlines()
#
#             for string in test_strings:
#                 string = string.strip()
#                 if re.fullmatch(regex, string):
#                     results.append((grammar_name, string, "PASS"))
#                 else:
#                     results.append((grammar_name, string, "FAIL"))
#
#     return results

class TestGrammarGeneration(unittest.TestCase):
    """
    Unit tests to validate grammar-generated strings against the expected regex.
    """

    @classmethod
    def setUpClass(cls):
        print("Processing .g4 files and generating test strings...")
        process_and_generate()

    def test_generated_strings(self):
        """
        Validate generated strings against their corresponding regex.
        """
        for grammar_name, regex in REGEX_MAP.items():
            for i in range(10):
                test_file_path = os.path.join(
                    OUTPUT_FOLDER, f"{grammar_name[:-3]}_tests.txt"
                )

                # Skip if the test file does not exist
                if not os.path.exists(test_file_path):
                    self.fail(f"Test file for {grammar_name} not found.")

                with open(test_file_path, "r") as f:
                    test_strings = f.readlines()

                # Check each string
                for string in test_strings:
                    string = string.strip()
                    with self.subTest(grammar=grammar_name, string=string):
                        self.assertRegex(
                            string, regex,
                            msg=f"String '{string}' does not match regex for {grammar_name}."
                        )


if __name__ == "__main__":
    # print("Processing .g4 files and generating test strings...")
    # process_and_generate()
    # print("Validating test strings...")
    # results = validate_generated_strings()
    #
    # print("\nValidation Results:")
    # for grammar_name, string, status in results:
    #     print(f"[{status}] Grammar: {grammar_name}, String: {string}")
    unittest.main()