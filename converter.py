import re


class RegexToCFG:
    def __init__(self, regex):
        self.regex = regex
        self.position = 0
        self.grammar = []
        self.non_terminals = {}
        # self.current_symbol = 's'  # Start symbol is 's'
        self.current_status = 1

        self.special_symbols = {
            r'\s': [" ", "\\t", "\\n"],
            # r'\S': [f"{chr(i)}" for i in range(32, 127) if not (chr(i) in [' ', '\t', '\n'])],
            r'\S': "(A character that is not a whitespace character)",
            r'\d': [f"{i}" for i in range(10)],
            # r'\D': [f"{chr(i)}" for i in range(32, 127) if not ('0' <= chr(i) <= '9')],
            r'\D': "(A character that is not a digit)",
            r'\w': [f"{chr(i)}" for i in range(65, 91)] + [f"{chr(i)}" for i in range(97, 123)] +
                   [f"{i}" for i in range(10)] + ["_"],
            # r'\W': [f"{chr(i)}" for i in range(32, 48)] + [f"{chr(i)}" for i in range(58, 65)] +
            #        [f"{chr(i)}" for i in range(91, 97)] + [f"{chr(i)}" for i in range(123, 127)],
            r'\W': "(A character that is not a word character)",
        }

    def peek(self):
        if self.position < len(self.regex):
            return self.regex[self.position]
        else:
            return None

    def advance(self):
        self.position += 1

    def parse(self):
        """Parse the regex and build the CFG."""
        expr_symbol = self.regex_expr('')
        if expr_symbol != 's':
            self.add_rule('s', expr_symbol)
        return 's'

    def regex_expr(self, status):
        """Parse an expression involving alternation."""
        if self.peek() == '^':
            self.advance()  # Consume '^'
            start_anchor = f"s{self.current_status}"
            self.add_rule(start_anchor, "'^'")
            self.current_status += 1
            base_expr = self.regex_expr(status)
            return_status = f"s{self.current_status}"
            self.add_rule(return_status, f"{start_anchor} {base_expr}")
            self.current_status += 1
            return return_status
        
        term_symbol = self.regex_term(status)
        # breakpoint()
        if self.peek() == '|':
            self.advance()  # Consume '|'
            next_term = self.regex_expr(status)

            return_status = 's{}'.format(status)
            self.add_rule(return_status, term_symbol)
            self.add_rule(return_status, next_term)
            self.current_status += 1
            return return_status
        
        if self.peek() == '$':
            self.advance()  # Consume '$'
            end_anchor = f"s{self.current_status}"
            self.add_rule(end_anchor, "'$'")
            self.current_status += 1
            return_status = f"s{self.current_status}"
            self.add_rule(return_status, f"{term_symbol} {end_anchor}")
            self.current_status += 1
            return return_status
        else:
            return term_symbol

    def regex_term(self, status):
        """Parse a term involving concatenation."""
        factors = []
        while True:
            factor = self.regex_factor(status)
            # breakpoint()
            if factor:
                factors.append(factor)
            else:
                break
        if not factors:
            return None
        elif len(factors) == 1:
            return factors[0]
        else:
            return_status = 's{}'.format(status)
            self.add_rule(return_status, factors)
            return return_status

    def regex_factor(self, status):
        """Parse a factor, handling Kleene star, plus, and optional operators."""
        base, result_index = self.regex_base(status)
        
        if base:
            operator = self.peek()
            if operator == '*':
                self.advance()  # Consume '*'
                new_status = f's{self.current_status}'
                self.add_rule(new_status, [base, new_status])
                self.add_rule(new_status, ['EOF'])
                self.current_status += 1
                return new_status
            
            elif operator == '+':  # Support for the + operator
                self.advance()  # Consume '+'
                new_status = f's{self.current_status}'
                self.add_rule(new_status, [base, new_status])
                self.add_rule(new_status, [base])  # Ensures at least one occurrence
                self.current_status += 1
                return new_status
            
            elif operator == '?':  # Support for the ? operator
                self.advance()  # Consume '?'
                new_status = f's{self.current_status}'
                self.add_rule(new_status, [base])
                self.add_rule(new_status, ['EOF'])  # Allows zero occurrences
                self.current_status += 1
                return new_status

            # Handle {m}, {m,}, and {m,n} quantifiers using regex matching
            elif operator == '{':
                match = re.match(r'\{(\d+)(,)?(\d+)?\}', self.regex[self.position:])
                if match:
                    self.position += match.end()  # Move position past the matched quantifier
                    m = int(match.group(1))       # Extract minimum repetitions
                    comma = match.group(2) is not None
                    n = int(match.group(3)) if match.group(3) else None  # Extract maximum repetitions if present
                    
                    if n is None and comma:
                        # Handle {m,} (m or more repetitions)
                        start_status = f's{self.current_status}'
                        self.current_status += 1
                        new_status = start_status
                        # Add m repetitions of base
                        for _ in range(m):
                            current_status = f's{self.current_status}'
                            self.add_rule(new_status, [base, current_status])
                            new_status = current_status
                            self.current_status += 1
                        # Add remaining repetitions using Kleene star logic
                        self.add_rule(new_status, [base, new_status])
                        self.add_rule(new_status, ['EOF'])
                        return start_status
                    
                    elif n is None:
                        # Handle {m} (exactly m repetitions)
                        start_status = f's{self.current_status}'
                        new_status = start_status
                        for _ in range(m - 1):  # Add m - 1 transitions with base
                            next_status = f's{self.current_status + 1}'
                            self.add_rule(new_status, [base, next_status])
                            new_status = next_status
                            self.current_status += 1
                        # Final state transition with only the base
                        self.add_rule(new_status, [base])
                        self.current_status += 1
                        return start_status
                    
                    else:
                        # Handle {m,n} (between m and n repetitions)
                        start_status = f's{self.current_status}'
                        self.current_status += 1
                        new_status = start_status
                        # First, add exactly `m` repetitions
                        for _ in range(m):
                            current_status = f's{self.current_status}'
                            self.add_rule(new_status, [base, current_status])
                            new_status = current_status
                            self.current_status += 1
                        # Add optional repetitions up to `n`, ensuring no extra ε
                        for i in range(m, n):
                            if i < n:
                                # Add ε only up to the penultimate optional state
                                self.add_rule(new_status, ['EOF'])
                            optional_status = f's{self.current_status}'
                            self.add_rule(new_status, [base, optional_status])
                            new_status = optional_status
                            self.current_status += 1
                        # Final ε transition after optional repetitions
                        self.add_rule(new_status, ['EOF'])
                        return start_status

        return base

    def regex_base(self, status):
        """Parse a base element: literal or grouped expression."""
        char = self.peek()
        if char is None:
            return None, 0
        
        if char == '[':  # Start of a character range
            self.advance()  # Consume '['
            range_symbols = []

            while self.peek() != ']':
                range_start = self.peek()
                self.advance()  # Consume the start character
                if self.peek() == '-':
                    self.advance()  # Consume '-'
                    if self.peek() is None or self.peek() == ']':
                        raise ValueError("Mismatched square brackets")
                    range_end = self.peek()
                    self.advance()  # Consume the end character
                    range_symbols.extend([f"'{chr(i)}'" for i in range(ord(range_start), ord(range_end) + 1)])
                else:
                    range_symbols.append(f"'{range_start}'")

            if self.peek() != ']':
                raise ValueError("Mismatched square brackets")
            self.advance()  # Consume ']'

            if not range_symbols:
                raise ValueError("Empty character class")

            range_rule = f"s{self.current_status}"
            self.add_rule(range_rule, ' | '.join(range_symbols))
            self.current_status += 1
            return range_rule, 1
        
        if char == '\\':
            self.advance() # Consume '\'
            next_char = self.peek()
            if next_char and f'\\{next_char}' in self.special_symbols:
                symbol = f'\\{next_char}'
                self.advance() # Consume next character
                return_symbol = f"s{self.current_status}"
                if symbol == r'\S' or symbol == r'\D' or symbol == r'\W':
                    self.add_rule(return_symbol, self.special_symbols[symbol])
                else:
                    self.add_rule(return_symbol, ' | '.join(self.special_symbols[symbol]))
                self.current_status += 1
                return return_symbol, 1
            else:
                raise ValueError("Invalid escape sequence")
        
        elif char == '(':
            self.advance()  # Consume '('
            self.current_status += 1
            expr_symbol = self.regex_expr(str(self.current_status - 1) if status == ''
                                          else str(int(status) + self.current_status - 1))
            if self.peek() != ')':
                raise ValueError("Mismatched parentheses")
            self.advance()  # Consume ')'
            # breakpoint()
            return expr_symbol, 2
        elif char.isalnum():
            literal = f"'{char}'"
            self.advance()  # Consume character
            return literal, 1
        else:
            return None, 0

    def add_rule(self, lhs, rhs):
        """Add a production rule to the grammar."""
        rhs_str = ' '.join(rhs) if isinstance(rhs, list) else rhs
        for index, (existing_lhs, existing_rhs) in enumerate(self.grammar):
            if existing_lhs == lhs:
                self.grammar[index] = (lhs, f"{existing_rhs} | {rhs_str}")
                return
        
        self.grammar.append((lhs, rhs_str))

    def get_grammar(self):
        """Return the formatted CFG as a list of strings."""
        # Combine rules with the same LHS
        combined_rules = {}
        for lhs, rhs in self.grammar:
            if lhs not in combined_rules:
                combined_rules[lhs] = []
            if rhs not in combined_rules[lhs]:
                combined_rules[lhs].append(rhs)
        # Format the grammar
        formatted_grammar = []
        for lhs in combined_rules:
            rhs_list = combined_rules[lhs]
            if rhs_list[0] is not None:
                rhs_combined = ' | '.join(rhs_list)
                formatted_grammar.append(f"{lhs} : {rhs_combined}")
        return eliminate_redundancies(formatted_grammar)


def eliminate_redundancies(grammar):
    """
    Eliminates redundant rules from the CFG by:
    - Removing unnecessary self-referencing or indirect recursive rules.
    - Removing unused non-terminals.
    """
    # Step 1: Parse the grammar into a dictionary format
    parsed_grammar = {}
    for rule in grammar:
        lhs, rhs = rule.split(" : ")
        rhs_alternatives = rhs.split(" | ")
        if lhs not in parsed_grammar:
            parsed_grammar[lhs] = set(rhs_alternatives)
        else:
            parsed_grammar[lhs].update(rhs_alternatives)

    # Step 2: Remove self-referencing and indirect recursive rules
    def remove_self_references(parsed_grammar):
        to_remove = set()
        for lhs in list(parsed_grammar.keys()):
            rhs_set = parsed_grammar[lhs]
            # Remove direct self-references
            if lhs in rhs_set:
                rhs_set.discard(lhs)
            # Remove indirect recursive rules (e.g., `s : s2` and `s2 : s`)
            for rhs in rhs_set:
                if rhs in parsed_grammar and lhs in parsed_grammar[rhs]:
                    to_remove.add((lhs, rhs))

        # Remove detected recursive pairs
        for lhs, rhs in to_remove:
            parsed_grammar[lhs].discard(rhs)
            if not parsed_grammar[lhs]:
                del parsed_grammar[lhs]

    remove_self_references(parsed_grammar)
    # Step 3: Remove unused non-terminals
    reachable_non_terminals = {'s'}
    added = True
    while added:
        added = False
        for nt in list(reachable_non_terminals):
            for production in parsed_grammar.get(nt, []):
                for symbol in production.split():
                    if symbol in parsed_grammar and symbol not in reachable_non_terminals:
                        reachable_non_terminals.add(symbol)
                        added = True
    # Keep only reachable non-terminals
    parsed_grammar = {nt: prods for nt, prods in parsed_grammar.items() if nt in reachable_non_terminals}

    # Step 4: Consolidate the grammar back to list format
    consolidated_grammar = []
    for lhs, rhs_set in parsed_grammar.items():
        rhs_combined = " | ".join(sorted(rhs_set))
        consolidated_grammar.append(f"{lhs} : {rhs_combined}")

    return consolidated_grammar


# Example usage
if __name__ == "__main__":
    regexs = ["(a|b)c*", "ab|cd", "a*d", "a(b|c)*d", "a", "", "(a(b|c))*", "a+", "b?", "(ab)+", "a(bc)?", "a*b+c?", r"\s", r"\w*", r"a\d", r"\S", r"\D", r"\W", r"\d+", r"\w+\s*", "^abc$", "^a(b|c)*d$", "^\d+\s*$", "a|^b$"]
    # regexs.extend(["a{3}","b{2,}","c{1,3}","(ab){2,4}", "a{1}b{2,5}c{3,}" ])
    #regexs = ["(a(b|c))*"]
    # regexs = ["[a-z]", "[A-Z]", "[0-9]", "[a-zA-Z]", "[a-f0-5]", "[a-cx-z]", "[0-3A-D]", "[-a-z]", "[a-z-]", "[a-z]*", "[0-9]+", "[A-Za-z]{3,5}", "[a-]"]

    for regex in regexs:
        converter = RegexToCFG(regex)
        print(f"\nSimplified Context-Free Grammar for '{regex}':")
        try:
            converter.parse()
            grammar = converter.get_grammar()
            simplified_grammar = eliminate_redundancies(grammar)
            simplified_grammar.sort()
            grammar.sort()
            # print(f"\nSimplified Context-Free Grammar for '{regex}':")
            with open("cfg.g4", "w") as f:
                f.write("grammar cfg;\n")
                for rule in grammar:
                    f.write(rule+";\n")
                    print(rule)
        except ValueError as e:
            print(f"Error: {e}")
