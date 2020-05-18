import money
from pair import Pair

class Bank():
    _rates = {}

    def reduce(self, source, to: str):
        return source.reduce(self, to)

    def addRate(self, fr: str, to: str, rate: int):
        pair: Pair = Pair(fr, to)
        self._rates[pair] = rate

    def rate(self, fr: str, to: str) -> int:
        if fr == to: return 1
        pair: Pair = Pair(fr, to)
        return self._rates[pair]
 