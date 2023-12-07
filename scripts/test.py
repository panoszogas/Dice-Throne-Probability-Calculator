from itertools import product
from dice_throne_probability_calculator.probability_engine.dice_probability_calculations import SimilarityProbabilityCalculator, StreightProbabilityCalculator
from dice_throne_probability_calculator.utils.dice_partition import DicePartition, SimpleDicePartition
from dice_throne_probability_calculator.utils.combinations import SymbolCombination

if __name__ == "__main__":
    # print(
    #     SimilarityProbabilityCalculator(
    #         # DicePartition(
    #         #     '1',
    #         #     '1',
    #         #     '2',
    #         #     '2',
    #         #     '3',
    #         #     '4'
    #         # )
    #         SimpleDicePartition()
    #     ).calculate_probability(
    #         SymbolCombination(
    #             combination = ('1','2','3','3','3')
    #         ),
    #         5
    #     )
    # )
    print(
        SimilarityProbabilityCalculator(
            SimpleDicePartition()
        ).calculate_probability(
            SymbolCombination(
                combination = ('1','2','3')
            ),
            5
        ),
        SimilarityProbabilityCalculator(
            SimpleDicePartition()
        ).calculate_probability(
            SymbolCombination(
                combination = ('1','2','3')
            ),
            5
        )*6**5
    )
    print(
        StreightProbabilityCalculator(
        ).calculate_probability(
            2,
            5
        )
    )
    all_combinations = [comb for comb in product(range(1,7), repeat=5)]
    total_count = 0
    for combination in all_combinations:
        norm_combination = sorted(list(set(combination)))
        cum_sum = 0
        for i, n_i in zip(norm_combination[:-1],norm_combination[1:]):
            if i+1 == n_i:
                cum_sum += 1
        if cum_sum >= 2:
            total_count += 1
    print(total_count / len(all_combinations))
    print(total_count,len(all_combinations))
