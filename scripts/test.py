from itertools import product
from dice_throne_probability_calculator.probability_engine.dice_probability_calculations import SimilarityProbabilityCalculator
from dice_throne_probability_calculator.utils.dice_partition import DicePartition
from dice_throne_probability_calculator.utils.combinations import SymbolCombinationThree

if __name__ == "__main__":
    print(
        SimilarityProbabilityCalculator(
            DicePartition(
                '1',
                '1',
                '2',
                '2',
                '3',
                '4'
            )
        ).calculate_probability(
            SymbolCombinationThree(
                element_1 = '1',
                element_2 = '2',
                element_3 = '3'
            ),
            5
        )
    )
    all_combinations = [comb for comb in product(range(1,7), repeat=5)]
    # print(all_combinations)
    total_count = 0
    for combination in all_combinations:
        count_1 = 0
        count_2 = 0
        count_3 = 0
        for i in combination:
            if i in {1,2}:
                count_1 += 1
            if i in {3,4}:
                count_2 += 1
            if i in {5}:
                count_3 += 1
        if count_1 >= 1 and count_2 >= 1 and count_3 >= 1:
            total_count += 1
    print(total_count / len(all_combinations))
