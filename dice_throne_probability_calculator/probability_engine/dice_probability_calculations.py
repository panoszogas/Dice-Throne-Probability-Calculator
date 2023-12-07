import math
from typing import Dict
from collections import Counter
from itertools import combinations_with_replacement
from dice_throne_probability_calculator.utils.dice_partition import DicePartition, SimpleDicePartition
from dice_throne_probability_calculator.utils.combinations import Combination

class SimilarityProbabilityCalculator:

    def __init__(
        self,
        dice_partition: DicePartition
    ) -> None:
        self.number_of_outcomes: int = len(dice_partition)
        self.symbol_frequencies: Combination = dice_partition.get_symbol_frequencies()
    
    def _calculate_probability_of_combination(
        self,
        symbol_combination: Combination,
        number_of_dice: int
    ):
        return (
            (
                math.prod(
                    map(
                        lambda x: self.symbol_frequencies[x],
                        symbol_combination.to_tuple()
                    )
                )
                * (
                    (
                        self.number_of_outcomes
                        - sum(
                            map(
                                lambda x: self.symbol_frequencies[x],
                                set(symbol_combination.to_tuple())
                            )
                        )
                    ) ** (
                        number_of_dice - len(symbol_combination.to_tuple())
                    )
                )
                * (
                    math.factorial(number_of_dice) / (
                        math.factorial(number_of_dice - len(symbol_combination.to_tuple()))
                        * math.prod(
                            map(
                                math.factorial,
                                list(
                                    (
                                        Counter(symbol_combination.to_tuple())
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

    def calculate_probability(
        self,
        symbol_combination: Combination,
        number_of_dice: int
    ):

        symbol_combination_list = symbol_combination.to_tuple()

        probability_accumulator = 0
        for number_of_n_kind in range(len(symbol_combination_list), number_of_dice + 1):
            for comb in combinations_with_replacement(
                set(symbol_combination_list),
                r=number_of_n_kind - len(symbol_combination_list)
            ):
                probability_accumulator += self._calculate_probability_of_combination(
                    symbol_combination.add_elements(
                        Combination(
                            combination = tuple(comb)
                        )
                    ),
                    number_of_dice
                )

        return probability_accumulator

class StreightProbabilityCalculator:
    def __init__(
        self
    ) -> None:
        dice_partition = SimpleDicePartition()
        self.number_of_outcomes: int = len(dice_partition)
        self.symbol_frequencies: Combination = dice_partition.get_symbol_frequencies()

    def calculate_probability(
        self,
        streight_number: int,
        number_of_dice: int
    ):
        basic_sets = [
            {j + i for j in range(streight_number)}
            for i in range(1, self.number_of_outcomes - streight_number + 2)
        ]
        prob = len(basic_sets) * SimilarityProbabilityCalculator(
            SimpleDicePartition()
        ).calculate_probability(
            Combination(
                combination = tuple([str(i) for i in range(streight_number)])
            ),
            5
        )
        for i, basic_set_i in enumerate(basic_sets):
            for basic_set_j in basic_sets[i+1:]:
                prob -= 
                print(basic_set_i | basic_set_j)

        # for streight_number_tmp in range(streight_number, number_of_dice+1):

        #     comb = Combination(
        #         combination = tuple([str(i+1) for i in range(0,streight_number_tmp)])
        #     )
        #     print(comb.to_tuple())
        #     probability_accumulator += self._calculate_probability_of_combination(
        #         comb,
        #         number_of_dice
        #     ) * (1 if streight_number_tmp == streight_number else -1)

        #     for number_of_n_kind in range(streight_number_tmp+1, self.number_of_outcomes + 1):
        #         comb = Combination(
        #             combination = comb.to_tuple()[1:] + (str(number_of_n_kind),)
        #         )
        #         print(comb.to_tuple())
        #         probability_accumulator += self._calculate_probability_of_combination(
        #             comb,
        #             number_of_dice
        #         ) * (1 if streight_number_tmp == streight_number else -1)
        # return probability_accumulator
