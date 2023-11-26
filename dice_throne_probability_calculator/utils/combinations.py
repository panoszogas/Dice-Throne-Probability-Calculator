from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass(frozen = True, kw_only = True)
class Combination:
    combination: Tuple[str, ...] = ()
    combination_type: Optional[str] = None

    def to_tuple(self) -> Tuple[str, ...]:
        return self.combination

    def add_elements(self, new_comb: 'Combination') -> 'Combination':
        return Combination(
            combination = self.to_tuple() + new_comb.to_tuple()
        )

@dataclass(frozen = True, kw_only = True)
class SymbolCombination(Combination):
    combination_type: str = 'symbol'
@dataclass(frozen = True, kw_only = True)
class DigitCombination(Combination):
    combination_type: str = 'digit'
