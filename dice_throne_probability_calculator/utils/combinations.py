from dataclasses import dataclass
from typing import List, Optional

@dataclass(frozen = True, kw_only = True)
class Combination:
    combination_type: Optional[str] = None

    def to_list(self) -> List[str]:
        return []

@dataclass(frozen = True, kw_only = True)
class CombinationOne(Combination):
    element_1: str

    def to_list(self) -> List[str]:
        return [
            self.element_1,
        ]

@dataclass(frozen = True, kw_only = True)
class CombinationTwo(CombinationOne):
    element_2: str

    def to_list(self) -> List[str]:
        return [
            self.element_1,
            self.element_2,
        ]

@dataclass(frozen = True, kw_only = True)
class CombinationThree(CombinationTwo):
    element_3: str

    def to_list(self) -> List[str]:
        return [
            self.element_1,
            self.element_2,
            self.element_3,
        ]

@dataclass(frozen = True, kw_only = True)
class CombinationFour(CombinationThree):
    element_4: str

    def to_list(self) -> List[str]:
        return [
            self.element_1,
            self.element_2,
            self.element_3,
            self.element_4,
        ]

@dataclass(frozen = True, kw_only = True)
class CombinationFive(CombinationFour):
    element_5: str

    def to_list(self) -> List[str]:
        return [
            self.element_1,
            self.element_2,
            self.element_3,
            self.element_4,
            self.element_5,
        ]

@dataclass(frozen = True, kw_only = True)
class SymbolCombinationOne(CombinationOne):
    combination_type: str = 'symbol'

@dataclass(frozen = True, kw_only = True)
class SymbolCombinationTwo(CombinationTwo):
    combination_type: str = 'symbol'

@dataclass(frozen = True, kw_only = True)
class SymbolCombinationThree(CombinationThree):
    combination_type: str = 'symbol'

@dataclass(frozen = True, kw_only = True)
class SymbolCombinationFour(CombinationFour):
    combination_type: str = 'symbol'

@dataclass(frozen = True, kw_only = True)
class SymbolCombinationFive(CombinationFive):
    combination_type: str = 'symbol'

@dataclass(frozen = True, kw_only = True)
class DigitCombinationOne(CombinationOne):
    combination_type: str = 'digit'

@dataclass(frozen = True, kw_only = True)
class DigitCombinationTwo(CombinationTwo):
    combination_type: str = 'digit'

@dataclass(frozen = True, kw_only = True)
class DigitCombinationThree(CombinationThree):
    combination_type: str = 'digit'

@dataclass(frozen = True, kw_only = True)
class DigitCombinationFour(CombinationFour):
    combination_type: str = 'digit'

@dataclass(frozen = True, kw_only = True)
class DigitCombinationFive(CombinationFive):
    combination_type: str = 'digit'
