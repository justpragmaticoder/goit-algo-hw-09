import timeit

from find_coins_greedy_func import find_coins_greedy
from find_min_coins_func import find_min_coins

EXECUTION_QTY = 20


def get_fastest_alg(test_name: str, amount_to_return, executionQty=EXECUTION_QTY):
    results = {
        "Greedy": timeit.timeit(
            lambda: find_coins_greedy(amount_to_return), number=executionQty
        ),
        "Dynamic programming": timeit.timeit(
            lambda: find_min_coins(amount_to_return), number=executionQty
        ),
    }

    print(f"{test_name} test: ".upper())

    for algorithm, execution_time in results.items():
        print(f"Algorithm: {algorithm}, Execution Time: {execution_time}")

    min_time_algorithm, min_time = min(results.items(), key=lambda x: x[1])

    print(f"Fastest algorithm is {min_time_algorithm} with result: {min_time}\n")

    return min_time_algorithm, min_time


def determine_overal_champion(champions):
    champion_counts = {}
    for champion, _ in champions:
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return max(champion_counts, key=champion_counts.get)
