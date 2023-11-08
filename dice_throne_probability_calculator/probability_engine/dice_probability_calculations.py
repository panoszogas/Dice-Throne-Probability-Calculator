import math
from 

class SymbolCombination:
    def __init__(
        self,
        number_of_dice,
        n_similar,
        n_of_a_kind,
        number_of_outcomes
    ) -> None:
        self.number_of_dice = number_of_dice
        self.n_similar = n_similar
        self.n_of_a_kind = n_of_a_kind
        self.number_of_outcomes = number_of_outcomes

    def calculate_probability(self):
        probability_accumulator = 0
        for number_of_n_kind in range(self.n_of_a_kind,self.number_of_dice+1):
            probability_accumulator += (
                (
                    (
                        self.n_similar**number_of_n_kind
                    ) * (
                        (
                            self.number_of_outcomes-self.n_similar
                        ) ** (
                            self.number_of_dice-number_of_n_kind
                        )
                    ) * (
                        math.factorial(self.number_of_dice) / (
                            math.factorial(number_of_n_kind)
                            * math.factorial(self.number_of_dice-number_of_n_kind)
                        )
                    )
                ) / (
                    self.number_of_outcomes**self.number_of_dice
                )
            )
        return probability_accumulator
  
if __name__ == "__main__":
    print(NOfAKind(5,3,3,6).calculate_probability())
