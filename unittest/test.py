import unittest
import fizzbuzz
class TestStringMethods(unittest.TestCase):

    def test_3(self):
        self.assertEqual(get_fizzbuzz(3), 'fizz')
    def test_5(self):
        self.assertEqual(get_fizzbuzz(5), 'buzz')
    def test_both(self):
        self.assertEqual(get_fizzbuzz(15), 'fizzbuzz')

if __name__ == '__main__':
    unittest.main()
