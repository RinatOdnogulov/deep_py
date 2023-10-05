import time
import unittest
from dec_time import mean
import sys
import io


class TestMeanDecorator(unittest.TestCase):

    def test_mean_decorator_with_k_2(self):
        @mean(2)
        def test_func():
            time.sleep(0.1)

        self.assertAlmostEqual(TestMeanDecorator.print_value_res(test_func),
                               0.1, delta=0.01)

        self.assertAlmostEqual(TestMeanDecorator.print_value_res(test_func),
                               0.1, delta=0.01)

        self.assertAlmostEqual(TestMeanDecorator.print_value_res(test_func),
                               0.1, delta=0.01)

    def test_mean_decorator_with_k_10(self):
        @mean(10)
        def test_func():
            time.sleep(0.1)

        self.assertAlmostEqual(TestMeanDecorator.print_value_res(test_func),
                               0.1, delta=0.01)

        self.assertAlmostEqual(TestMeanDecorator.print_value_res(test_func),
                               0.1, delta=0.01)

        self.assertAlmostEqual(TestMeanDecorator.print_value_res(test_func),
                               0.1, delta=0.01)

        self.assertAlmostEqual(TestMeanDecorator.print_value_res(test_func),
                               0.1, delta=0.01)

    def test_mean_decorator_with_k_less_one(self):
        @mean(0)
        def test_func():
            time.sleep(0.1)

        self.assertAlmostEqual(TestMeanDecorator.print_value_Error(test_func),
                               "Значение k введено некорректно\n")

    def test_mean_decorator_with_k_no_int(self):
        @mean(3.5)
        def test_func():
            time.sleep(0.1)

        self.assertAlmostEqual(TestMeanDecorator.print_value_Error(test_func),
                               "Значение k введено некорректно\n")

    @staticmethod
    def print_value_res(test_func) -> float:
        output_buffer = io.StringIO()

        sys.stdout = output_buffer

        test_func()

        printed_value = output_buffer.getvalue()

        sys.stdout = sys.__stdout__

        return float(printed_value)

    @staticmethod
    def print_value_Error(test_func) -> str:
        output_buffer = io.StringIO()

        sys.stdout = output_buffer

        test_func()

        printed_value = output_buffer.getvalue()

        sys.stdout = sys.__stdout__

        return printed_value


if __name__ == '__main__':
    unittest.main()
