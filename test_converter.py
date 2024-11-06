import unittest

from converter import RegexToCFG

class TestRegexToCFG(unittest.TestCase):

    def run_cfg_test(self, regex_input, expected_output):
        converter = RegexToCFG(regex_input)
        try:
            converter.parse()
            grammar = converter.get_grammar()
            grammar.sort()
            expected_output.sort()
            self.assertEqual(expected_output, grammar)
        except Exception as e:
            self.fail(f"Exception raised for regex '{regex_input}': {e}")

    def test_1(self):
        regex_input = "a(b|c)*d"
        expected_output = [
            "S → 'a' S1 'd'",
            "S1 → S2 S1 | ε",
            "S2 → 'b' | 'c'"
        ]
        self.run_cfg_test(regex_input, expected_output)

    def test_2(self):
        regex_input = "a*d"
        expected_output = [
            "S → S1 'd'",
            "S1 → 'a' S1 | ε"
        ]
        self.run_cfg_test(regex_input, expected_output)

    def test_3(self):
        regex_input = "ab|cd"
        expected_output = [
            "S → 'a' 'b' | 'c' 'd'"
        ]
        self.run_cfg_test(regex_input, expected_output)

    def test_4(self):
        regex_input = "(a|b)c*"
        expected_output2 = [
            "S → 'a' S1 | 'b' S1",
            "S1 → 'c' S1 | ε"
        ]
        expected_output = ['S → S2 S1',
                  "S1 → 'c' S1 | ε",
                  "S2 → 'a' | 'b'"]
        self.run_cfg_test(regex_input, expected_output)

    def test_5(self):
        regex_input = "a"
        expected_output = [
            "S → 'a'"
        ]
        self.run_cfg_test(regex_input, expected_output)

    def test_empty_regex(self):
        regex_input = ""
        expected_output = []
        self.run_cfg_test(regex_input, expected_output)

    def test_nested_groups(self):
        regex_input = "(a(b|c))*"
        expected_output = [
            "S → S1 S | ε",
            "S1 → 'a' S2",
            "S2 → 'b' | 'c'"
        ]
        self.run_cfg_test(regex_input, expected_output)

    # def test_complex_regex(self):
    #     regex_input = "a(b|c)d*e+"
    #     with self.assertRaises(ValueError):
    #         self.run_cfg_test(regex_input, [])

if __name__ == "__main__":
    unittest.main()