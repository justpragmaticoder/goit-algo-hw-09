import unittest
from find_coins_greedy_func import find_coins_greedy
from find_min_coins_func import find_min_coins


class Test(unittest.TestCase):
    def test_find_coins_greedy_on_small_amount(self):
        # 1.13 EUR
        amount_to_return = 113

        result = find_coins_greedy(amount_to_return)

        self.assertEqual(result, {50: 2, 10: 1, 2: 1, 1: 1})

    def test_find_coins_greedy_on_big_amount(self):
        # 12193.99 EUR
        amount_to_return = 1219399

        result = find_coins_greedy(amount_to_return)

        self.assertEqual(result, {50: 24387, 25: 1, 10: 2, 2: 2})

    def test_find_min_coins_on_small_amount(self):
        # 1.13 EUR
        amount_to_return = 113

        result = find_min_coins(amount_to_return)

        self.assertEqual(result, {1: 1, 2: 1, 10: 1, 50: 2})

    def test_find_min_coins_on_big_amount(self):
        # 12193.99 EUR
        amount_to_return = 1219399

        result = find_min_coins(amount_to_return)

        self.assertEqual(result, {2: 2, 10: 2, 25: 1, 50: 24387})
