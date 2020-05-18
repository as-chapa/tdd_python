from dataclasses import dataclass

@dataclass
class Pair():
    _fr: str
    _to: str
    def __eq__(self, pair):
        return self._fr == pair._fr and self._to == pair._to

    def __hash__(self):
        return hash((self._fr, self._to))

    def equals(self, fr: str , to: str) -> bool:
        return self._fr == fr and self._to == to