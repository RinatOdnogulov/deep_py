
import sys
import io
import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    def test_add(self):
        self.assertEqual(CustomList([1, 2, 3]) + CustomList([1, 2, 3, 1]), CustomList([2, 4, 6, 1]))

    def test_sub(self):
        self.assertEqual(CustomList([1, 2, 3]) - CustomList([1, 2, 3, 0]), CustomList([0, 0, 0, 0]))

    def test_lt(self):
        self.assertEqual(CustomList([1, 2, 3]) < CustomList([1, 2, 3, 1]), True)
        self.assertEqual(CustomList([1, 2, 3]) < CustomList([1, 2, 3, -1]), False)

    def test_eq(self):
        self.assertEqual(CustomList([1, 2, 3]) == CustomList([1, 2, 3, 0]), True)
        self.assertEqual(CustomList([1, 2, 3]) == CustomList([1, 2, 4]), False)

    def test_le(self):
        self.assertEqual(CustomList([1, 2, 3]) <= CustomList([1, 2, 3, 1]), True)
        self.assertEqual(CustomList([1, 2, 3, 2]) <= CustomList([1, 2, 3, 1]), False)

    def test_ne(self):
        self.assertEqual(CustomList([1, 2, 3]) != CustomList([1, 2, 3, 0]), False)
        self.assertEqual(CustomList([1, 2, 3, 4]) != CustomList([1, 2, 3, 0]), True)

    def test_gt(self):
        self.assertEqual(CustomList([1, 2, 3]) > CustomList([1, 2, 3, -1]), True)
        self.assertEqual(CustomList([1, 2, 1]) > CustomList([1, 2, 3, -1]), False)

    def test_ge(self):
        self.assertEqual(CustomList([1, 2, 3]) >= CustomList([1, 2, 3, 1]), False)
        self.assertEqual(CustomList([8]) >= CustomList([1, 2, 3, 1]), True)

    def test_str(self):
        cust_list = CustomList([1, 2, 3])
        self.assertEqual(TestCustomList.print_custom_list(cust_list), "[1, 2, 3] summa = 6")

    @staticmethod
    def print_custom_list(cust_list: CustomList) -> str:
        output_buffer = io.StringIO()

        sys.stdout = output_buffer

        print(cust_list, end='')

        printed = output_buffer.getvalue()

        sys.stdout = sys.__stdout__

        return printed


if __name__ == '__main__':
    unittest.main()
