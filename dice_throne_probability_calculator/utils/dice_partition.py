from dataclasses import dataclass

@dataclass(frozen = True)
class DicePartition:
    side_1: str
    side_2: str
    side_3: str
    side_4: str
    side_5: str
    side_6: str