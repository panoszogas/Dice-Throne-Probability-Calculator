import math
from typing import Dict
from collections import Counter
from itertools import combinations_with_replacement
from dice_throne_probability_calculator.utils.dice_partition import DicePartition
from dice_throne_probability_calculator.utils.combinations import Combination

class SimilarityProbabilityCalculator:
    def __init__(
        self,
        dice_partition: DicePartition
    ) -> None:
        self.number_of_outcomes: int = len(dice_partition)
        self.symbol_frequencies: Combination = dice_partition.get_symbol_frequencies()


    def calculate_probability(
        self,
        symbol_combination: Combination,
        number_of_dice: int
    ):

        symbol_combination_list = symbol_combination.to_list()

        probability_accumulator = 0
        for number_of_n_kind in range(len(symbol_combination_list), number_of_dice + 1):
            for comb in combinations_with_replacement(
                set(symbol_combination_list),
                r=number_of_n_kind - len(symbol_combination_list)
            ):
                probability_accumulator += (
                    (
                        math.prod(
                            map(
                                lambda x: self.symbol_frequencies[x],
                                symbol_combination_list
                            )
                        )
                        * math.prod(
                            map(
                                lambda x: self.symbol_frequencies[x],
                                comb
                            )
                        )
                        * (
                            (
                                self.number_of_outcomes
                                - sum(
                                    map(
                                        lambda x: self.symbol_frequencies[x],
                                        set(symbol_combination_list)
                                    )
                                )
                            ) ** (
                                number_of_dice - number_of_n_kind
                            )
                        )
                        * (
                            math.factorial(number_of_dice) / (
                                math.factorial(number_of_dice - number_of_n_kind)
                                * math.prod(
                                    map(
                                        math.factorial,
                                        list(
                                            (
                                                Counter(symbol_combination_list) +
                                                Counter(comb)
                                            ).values()
                                        )
                                    )
                                )
                            )
                        )
                    )
                    / (
                        self.number_of_outcomes
                        ** number_of_dice
                    )
                )
        return probability_accumulator
