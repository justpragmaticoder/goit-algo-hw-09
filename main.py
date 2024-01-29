from utils import get_fastest_alg, determine_overal_champion

# Test on small amounts (1.13 EUR)
small_amount_to_return = 113
small_amount_test_result = get_fastest_alg("Small amount", small_amount_to_return)

# Test on big amounts (99999.99 EUR)
big_amount_to_return = 99999
big_amount_test_result = get_fastest_alg("Big amount", big_amount_to_return)

# Test on very big amounts (12193.99 EUR)
biggest_amount_to_return = 1219399
bigest_amount_test_result = get_fastest_alg("Biggest amount", biggest_amount_to_return)

overal_test_champion = determine_overal_champion(
    [small_amount_test_result, big_amount_test_result, bigest_amount_test_result]
)

print("Conclusion: ")
print(
    f"The champion in handling of small amounts is: {small_amount_test_result[0]}, with result: {small_amount_test_result[1]}"
)
print(
    f"The champion in handling of big amounts is: {big_amount_test_result[0]}, with result: {big_amount_test_result[1]}"
)
print(
    f"The champion in handling of biggest amounts is: {bigest_amount_test_result[0]}, with result: {bigest_amount_test_result[1]}"
)
print(f"The champion in handling of different amounts is: {overal_test_champion}")
