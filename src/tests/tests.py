import unittest
from ..calculator import modules


class ConversionTests(unittest.TestCase):

    def test_simple_expression(self):
        exp = '1 + 12 * 4 / 2'
        obj = modules.Conversion(len(exp))
        self.assertListEqual(obj.infixToPostfix(exp), ['1', '12', '4', '*', '2', '/', '+'])

    def test_medium_expression(self):
        exp = '( 3 * 5 ) ^ 2 + 10 / 5'
        obj = modules.Conversion(len(exp))
        self.assertListEqual(obj.infixToPostfix(exp), ['3', '5', '*', '2', '^', '10', '5', '/', '+'])

    def test_hard_expression(self):
        exp = '15 + 6 * ( 2 ^ 5 - 2 ) ^ ( 1 + 345 * 0 ) - 69'
        obj = modules.Conversion(len(exp))
        self.assertListEqual(obj.infixToPostfix(exp),
                    ['15', '6', '2', '5', '^', '2', '-', '1', '345', '0', '*', '+', '^', '*', '+', '69', '-'])

