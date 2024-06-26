import unittest
from ..calculator import modules


class ConversionTests(unittest.TestCase):

    def test_simple_expression(self):
        exp = '1 + 12 * 4 / 2'
        obj = modules.Conversion()
        result = obj.infix_to_postfix(exp)
        self.assertListEqual(result, ['1', '12', '4', '*', '2', '/', '+'])

    def test_medium_expression(self):
        exp = '( 3 * 5 ) ^ 2 + 10 / 5'
        obj = modules.Conversion()
        result = obj.infix_to_postfix(exp)
        self.assertListEqual(result, ['3', '5', '*', '2', '^', '10', '5', '/', '+'])

    def test_hard_expression(self):
        exp = '15 + 6 * ( 2 ^ 5 - 2 ) ^ ( 1 + 345 * 0 ) - 69'
        obj = modules.Conversion()
        result = obj.infix_to_postfix(exp)
        self.assertListEqual(result,
                             ['15', '6', '2', '5', '^', '2', '-', '1', '345', '0', '*', '+', '^', '*', '+', '69', '-'])

    def test_negative_numbers(self):
        exp = '-100 * 55 / 25 + 21'
        obj = modules.Conversion()
        result = obj.infix_to_postfix(exp)
        self.assertListEqual(result, ['-100', '55', '*', '25', '/', '21', '+'])


class TestPush(unittest.TestCase):

    def test_positive(self):
        exp = "42"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 42, "Не удалось запушить положительное целое число.")

    def test_negative(self):
        exp = "-13"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, -13, "Не удалось запушить отрицательное целое число.")

    def test_excessive_spaces(self):
        exp = "       69       "
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 69, "Не удалось запушить целое число с чрезмерным количеством пробелов.")

    def test_extra_on_stack(self):
        exp = "42 69"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        self.assertRaises(ValueError, modules.calculate_postfix, postfix)

    def test_empty(self):
        exp = ""
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        self.assertRaises(ValueError, modules.calculate_postfix, postfix)

    def test_nonnum_push(self):
        exp = " рофель "
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        self.assertRaises(ValueError, modules.calculate_postfix, postfix)


class TestAddition(unittest.TestCase):

    def test_add_positives(self):
        exp = "27 + 42"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 69, "Не удалось сложить два положительных целых числа.")

    def test_add_negatives(self):
        exp = "-56 + -13"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, -69, "Не удалось сложить два отрицательных целых числа.")

    def test_add_pos_neg(self):
        exp = "100 + -31"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 69, "Не удалось добавить отрицательное число к положительному целому числу.")

    def test_add_neg_pos(self):
        exp = "-42 + 111"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 69, "Не удалось сложить положительное число с отрицательным.")

    def test_add_excessive_spaces(self):
        exp = " 228 +    192    "
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 420, "Не удалось добавить целые числа с чрезмерными пробелами.")

    def test_add_not_enough_nums(self):
        exp = "42 +"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        self.assertRaises(ValueError, modules.calculate_postfix, postfix)

    def test_add_extra_nums(self):
        exp = "228 + 69 42"
        exp = "42 69"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        self.assertRaises(ValueError, modules.calculate_postfix, postfix)


class TestSubtraction(unittest.TestCase):

    def test_sub_positives(self):
        exp = "69 - 27"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 42, "Не удалось вычесть два положительных целых числа.")

    def test_sub_negatives(self):
        exp = "-111 - -69"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, -42, "Не удалось вычесть два отрицательных целых числа.")

    def test_sub_pos_neg(self):
        exp = "56 - -13"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 69, "Не удалось вычесть отрицательное число из положительного целого числа.")

    def test_sub_neg_pos(self):
        exp = "-42 - 27"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, -69, "Не удалось вычесть положительное число из отрицательного целого числа.")

    def test_sub_excessive_spaces(self):
        exp = " 420 - 192  "
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 228, "Не удалось вычесть целые числа с лишними пробелами.")

    def test_sub_not_enough_nums(self):
        exp = "42 -"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        self.assertRaises(ValueError, modules.calculate_postfix, postfix)

    def test_sub_extra_nums(self):
        exp = "228 69 - 42"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        self.assertRaises(ValueError, modules.calculate_postfix, postfix)


class TestMultiplication(unittest.TestCase):

    def test_mul_positives(self):
        exp = "23 * 3"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 69, "Не удалось перемножить два положительных целых числа.")

    def test_mul_negatives(self):
        exp = "-21 * -2"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 42, "Не удалось перемножить два отрицательных целых числа.")

    def test_mul_pos_neg(self):
        exp = "57 * -4"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, -228, "Не удалось умножить отрицательное и положительное целое число.")

    def test_mul_neg_pos(self):
        exp = "-42 * 10"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, -420, "Не удалось умножить положительное и отрицательное целое число.")

    def test_mul_excessive_spaces(self):
        exp = " 191 *     7 "
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 1337, "Не удалось умножить целые числа с лишними пробелами.")

    def test_mul_not_enough_nums(self):
        exp = "42 *"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        self.assertRaises(ValueError, modules.calculate_postfix, postfix)

    def test_mul_extra_nums(self):
        exp = "228 69 * 42"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        self.assertRaises(ValueError, modules.calculate_postfix, postfix)


class TestDivision(unittest.TestCase):

    def test_div_positives(self):
        exp = "207 / 3"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 69, "Не удалось разделить два положительных целых числа.")

    def test_div_negatives(self):
        exp = "-294 / -7"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 42, "Не удалось разделить два отрицательных целых числа.")

    def test_div_pos_neg(self):
        exp = "228 / -4"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, -57, "Не удалось разделить положительное целое число на отрицательное.")

    def test_div_neg_pos(self):
        exp = "-420 / 60"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, -7, "Не удалось разделить отрицательное число на положительное целое число.")

    def test_div_excessive_spaces(self):
        exp = " 621 /    9"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 69, "Не удалось разделить целые числа с лишними пробелами.")

    def test_div_not_enough_nums(self):
        exp = "42 //"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        self.assertRaises(ValueError, modules.calculate_postfix, postfix)

    def test_div_extra_nums(self):
        exp = "228 69 42 //"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        self.assertRaises(ValueError, modules.calculate_postfix, postfix)


class TestInfixCalculator(unittest.TestCase):

    def test_no_space(self):
        exp = "3 + 6 * ( 3 - 2 )"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, eval(exp))

    def test_with_space(self):
        exp = "5 * 3 + 2 ^ 4"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 31)

    def test_1(self):
        exp = "6 * ( 3 - 5 ) ^ 2"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, 24)

    def test_2(self):
        exp = "36 / 12"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, eval(exp))

    def test_3(self):
        exp = "5 * 3 / ( 6 - 1 )"
        obj = modules.Conversion()
        postfix = obj.infix_to_postfix(exp)
        result = modules.calculate_postfix(postfix)
        self.assertEqual(result, eval(exp))


if __name__ == '__main__':
    unittest.main()
