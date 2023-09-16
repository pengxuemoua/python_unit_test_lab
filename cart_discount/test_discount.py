import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    # TODO more unit tests here. Each test should test one scenario
    def test_list_of_four_or_five_prices(self):
        expected_discount = 4
        self.assertEqual(expected_discount, discount([10, 4, 20, 75])) # 4 prices
        self.assertEqual(expected_discount, discount([10, 4, 20, 75, 90])) # 5 prices
    
    def test_list_for_one_or_two_prices(self):

        self.assertIsNone(discount([10])) # 1 price
        self.assertIsNone(discount([10,4])) # 2 prices
        
    def test_list_of_zero_price(self):
        self.assertIsNone(discount([0]))
    
    def test_list_of_empty_prices(self):
        self.assertIsNone(discount([]))

    def test_list_of_negative_prices(self):
        with self.assertRaises(ValueError):
            discount([-8.25, -96.85, -101, -8578])

    def test_list_of_three_duplicate_prices(self):
        expected_discount = 3
        self.assertEqual(expected_discount, discount([3, 3, 3]))

    def test_string_entry_prices(self):
        self.assertIsNone(discount(['Hello', 'Sup', 'Howdy']))

if __name__ == '__main__':
    unittest.main()