# From smallest to biggest
COIN_DENOMINATIONS = [1, 2, 5, 10, 25, 50]


def get_last_used_coins_list(amount):
    min_coins = [float("inf")] * (amount + 1)
    min_coins[0] = 0

    last_used_coins = [-1] * (amount + 1)

    for current_amount in range(1, amount + 1):
        for coin in COIN_DENOMINATIONS:
            if (
                current_amount >= coin
                and min_coins[current_amount - coin] + 1 < min_coins[current_amount]
            ):
                min_coins[current_amount] = min_coins[current_amount - coin] + 1
                last_used_coins[current_amount] = coin

    return last_used_coins


def get_coin_counters(last_used_coins, amount):
    coin_counters = {}
    current_amount = amount

    while current_amount > 0:
        coin_used = last_used_coins[current_amount]
        if coin_used in coin_counters:
            coin_counters[coin_used] += 1
        else:
            coin_counters[coin_used] = 1
        current_amount -= coin_used

    return coin_counters


def find_min_coins(amount):
    last_used_coins = get_last_used_coins_list(amount)

    return get_coin_counters(last_used_coins, amount)
