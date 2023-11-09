from dataclasses import dataclass
from typing import Dict
from collections import Counter

@dataclass(frozen = True)
class DicePartition:
    side_1: str
    side_2: str
    side_3: str
    side_4: str
    side_5: str
    side_6: str

    def to_dict(self) -> Dict[str, str]:
        return {
            '1': self.side_1,
            '2': self.side_2,
            '3': self.side_3,
            '4': self.side_4,
            '5': self.side_5,
            '6': self.side_6
        }

    def get_symbol_frequencies(self) -> Dict[str, int]:
        symbol_dict = self.to_dict()
        return Counter(symbol_dict.values())

    def __len__(self) -> int:
        return 6
