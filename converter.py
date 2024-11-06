class RegexToCFG:
    def __init__(self, regex):
        self.regex = regex
        self.position = 0
        self.grammar = []
        self.non_terminals = {}
        self.current_symbol = 'S'  # Start symbol is 'S'

    def peek(self):
        if self.position < len(self.regex):
            return self.regex[self.position]
        else:
            return None

    def advance(self):
        self.position += 1

    def parse(self):
        """Parse the regex and build the CFG."""
        expr_symbol = self.regex_expr()
        if expr_symbol != 'S':
            self.add_rule('S', expr_symbol)
        return 'S'

    def regex_expr(self):
        """Parse an expression involving alternation."""
        term_symbol = self.regex_term()
        if self.peek() == '|':
            self.advance()  # Consume '|'
            next_term = self.regex_expr()
            # Use predefined non-terminal 'S2' for alternation
            self.add_rule('S2', term_symbol)
            self.add_rule('S2', next_term)
            return 'S2'
        else:
            return term_symbol

    def regex_term(self):
        """Parse a term involving concatenation."""
        factors = []
        while True:
            factor = self.regex_factor()
            if factor:
                factors.append(factor)
            else:
                break
        if not factors:
            return None
        elif len(factors) == 1:
            return factors[0]
        else:
            # Combine factors directly if possible
            if self.current_symbol == 'S':
                self.add_rule('S', factors)
                return 'S'
            else:
                # Create a unique symbol for concatenation
                symbol = self.next_symbol()
                self.add_rule(symbol, factors)
                return symbol

    def regex_factor(self):
        """Parse a factor, handling Kleene star."""
        base = self.regex_base()
        if base and self.peek() == '*':
            self.advance()  # Consume '*'
            # Use predefined non-terminal 'S1' for Kleene star
            if base == 'S2':
                self.add_rule('S1', [base, 'S1'])
                self.add_rule('S1', ['ε'])
                return 'S1'
            else:
                symbol = 'S1'
                self.add_rule(symbol, [base, symbol])
                self.add_rule(symbol, ['ε'])
                return symbol
        else:
            return base

    def regex_base(self):
        """Parse a base element: literal or grouped expression."""
        char = self.peek()
        if char is None:
            return None
        if char == '(':
            self.advance()  # Consume '('
            expr_symbol = self.regex_expr()
            if self.peek() != ')':
                raise ValueError("Mismatched parentheses")
            self.advance()  # Consume ')'
            return expr_symbol
        elif char.isalnum():
            literal = f"'{char}'"
            self.advance()  # Consume character
            return literal
        else:
            return None

    def add_rule(self, lhs, rhs):
        """Add a production rule to the grammar."""
        if isinstance(rhs, list):
            rhs_str = ' '.join(rhs)
        else:
            rhs_str = rhs
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
                formatted_grammar.append(f"{lhs} → {rhs_combined}")
        return formatted_grammar

if __name__ == "__main__":
    regex = ""
    converter = RegexToCFG(regex)
    try:
        converter.parse()
        grammar = converter.get_grammar()
        grammar.sort()
        print(f"\nContext-Free Grammar for {regex}:")
        for rule in grammar:
            print(rule)
    except ValueError as e:
        print(f"Error: {e}")
