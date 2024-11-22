# FILE: test_main.py
import unittest
from unittest.mock import patch
import main

class TestCoffeeMachine(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['off'])
    def test_get_coin_input_off(self, mock_input):
        with self.assertRaises(SystemExit):
            main.get_coin_input("Prompt")

    @patch('builtins.input', side_effect=['5'])
    def test_get_coin_input_number(self, mock_input):
        self.assertEqual(main.get_coin_input("Prompt"), 5)

    def test_resources_sufficient(self):
        main.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        drink = main.MENU[2]  # latte
        self.assertTrue(main.resources_sufficient(drink))

        main.resources = {
            "water": 100,
            "milk": 50,
            "coffee": 10,
        }
        self.assertFalse(main.resources_sufficient(drink))

    def test_deduct_resources(self):
        main.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        drink = main.MENU[2]  # latte
        main.deduct_resources(drink)
        self.assertEqual(main.resources["water"], 100)
        self.assertEqual(main.resources["milk"], 50)
        self.assertEqual(main.resources["coffee"], 76)
        def test_resources_sufficient_propose_alternative(self):
            main.resources = {
                "water": 100,
                "milk": 50,
                "coffee": 10,
            }
            drink = main.MENU[2]  # latte
            with patch('builtins.print') as mocked_print:
                self.assertFalse(main.resources_sufficient(drink))
                mocked_print.assert_any_call("Insufficient water.")
                mocked_print.assert_any_call("Insufficient milk.")
                mocked_print.assert_any_call("Insufficient coffee.")
            
            # Propose alternative drink
            main.resources = {
                "water": 100,
                "milk": 50,
                "coffee": 20,
            }
            drink = main.MENU[2]  # latte
            with patch('builtins.print') as mocked_print:
                self.assertFalse(main.resources_sufficient(drink))
                mocked_print.assert_any_call("Insufficient water.")
                mocked_print.assert_any_call("Insufficient milk.")
                mocked_print.assert_any_call("Propose alternative drink: espresso")

            main.resources = {
                "water": 100,
                "milk": 50,
                "coffee": 20,
            }
            drink = main.MENU[1]  # espresso
            self.assertTrue(main.resources_sufficient(drink))
if __name__ == '__main__':
    unittest.main()