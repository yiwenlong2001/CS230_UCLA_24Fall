# Generated by Grammarinator 23.7

import itertools

from math import inf
from grammarinator.runtime import *

class cfg9Generator(Generator):


    def EOF(self, parent=None):
        pass
    EOF.min_depth = 0

    def s(self, parent=None):
        with RuleContext(self, UnparserRule(name='s', parent=parent)) as current:
            UnlexerRule(src='a', parent=current)
            self.s2(parent=current)
            return current
    s.min_depth = 1

    def s1(self, parent=None):
        with RuleContext(self, UnparserRule(name='s1', parent=parent)) as current:
            UnlexerRule(src='b', parent=current)
            UnlexerRule(src='c', parent=current)
            return current
    s1.min_depth = 0

    def s2(self, parent=None):
        with RuleContext(self, UnparserRule(name='s2', parent=parent)) as current:
            with AlternationContext(self, [0, 1], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    pass
                elif choice0 == 1:
                    self.s1(parent=current)
            return current
    s2.min_depth = 0

    def WS(self, parent=None):
        with RuleContext(self, UnlexerRule(name='WS', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[1]), parent=current)
            return current
    WS.min_depth = 0

    _default_rule = s

    _charsets = {
        0: list(itertools.chain.from_iterable([range(32, 127)])),
        1: list(itertools.chain.from_iterable([range(9, 10), range(10, 11), range(13, 14), range(32, 33)])),
    }
