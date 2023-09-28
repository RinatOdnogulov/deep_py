import unittest
from unittest.mock import patch
from tabel_massage import predict_message_mood


class TestString(unittest.TestCase):

    def test_bad_rating(self):
        with patch('tabel_massage.SomeModel') as mock_predict:
            mock_predict.predict.return_value = 0.2
        result = predict_message_mood("Daniel", mock_predict)
        self.assertEqual(result, "неуд")

    def test_good_rating(self):
        with patch('tabel_massage.SomeModel') as mock_predict:
            mock_predict.predict.return_value = 0.9
        result = predict_message_mood("Daniel", mock_predict)
        self.assertEqual(result, "отл")

    def test_neutral_rating(self):
        with patch('tabel_massage.SomeModel') as mock_predict:
            mock_predict.predict.return_value = 0.5
        result = predict_message_mood("Daniel", mock_predict)
        self.assertEqual(result, "норм")


if __name__ == '__main__':
    unittest.main()
