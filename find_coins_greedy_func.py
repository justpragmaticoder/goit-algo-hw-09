# From biggest to smallest
COIN_DENOMINATIONS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    coin_counters = {}
    amount_left = amount

    for coin in COIN_DENOMINATIONS:
        coins_qty = amount_left // coin

        if coins_qty > 0:
            coin_counters[coin] = coins_qty

        amount_left = amount_left % coin

    return coin_counters
