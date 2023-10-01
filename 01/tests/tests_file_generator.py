import unittest
from file_generator import file_filter
from tempfile import NamedTemporaryFile
import os


class TestSearchInFile(unittest.TestCase):

    def setUp(self):
        self.temp_file = NamedTemporaryFile("w", delete=False, encoding='utf-8')
        self.temp_file.write("Привет\nЯ хочу отдыхать\nСегодня хороший день\n")
        self.temp_file.close()

    def test_single_words(self):
        result = list(file_filter(self.temp_file.name, ["привет"]))
        self.assertEqual(result, ["Привет\n"])

    def test_multi_words(self):
        result = list(file_filter(self.temp_file.name, ["привет", "Хочу"]))
        self.assertEqual(result, ["Привет\n", "Я хочу отдыхать\n"])

    def test_notFound_words(self):
        result = list(file_filter(self.temp_file.name, ["кто", "что"]))
        self.assertEqual(result, [])

    def file_delete(self):
        os.remove(self.temp_file.name)


if __name__ == '__main__':
    unittest.main()
