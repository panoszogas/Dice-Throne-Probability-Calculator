from itertools import product
from dice_throne_probability_calculator.probability_engine.dice_probability_calculations import NOfAKind

if __name__ == "__main__":
    print(NOfAKind(5,3,3,6).calculate_probability())
    all_combinations = [comb for comb in product(range(1,7), repeat=5)]
    # print(all_combinations)
    total_count = 0
    for combination in all_combinations:
        count = 0
        for i in combination:
            if i in {1,2,3}:
                count += 1
        if count >= 3:
            total_count += 1
    print(total_count / len(all_combinations))