import unittest
from Convert import convert


def get_xrates():
    # perform some actions to be used globally in testing
    lines = {}
    x_rates = {}
    with open('test_data.txt', 'r') as t:
        lines = t.readlines()
        for line in lines:
            key, value = line.split(",")
            x_rates[key] = value.rstrip('\n')
    t.close()
    return x_rates


class MyTestCase(unittest.TestCase):

    def test_us_to_euro(self):
        expected = 0.950667
        actual = convert('US Dollar', 'Euro', get_xrates(), 1)
        self.assertEqual(expected, actual)

    def test_euro_to_franc(self):
        expected = 0.979581 / 0.950667
        actual = convert('Euro', 'Swiss Franc', get_xrates(), 1)
        self.assertEqual(expected, actual)

    def test_ringgit_to_canadian(self):
        expected = 1.282904 / 4.353672
        actual = convert('Malaysian Ringgit', 'Canadian Dollar', get_xrates(), 1)
        self.assertEqual(expected, actual)

    def test_us_to_yen(self):
        expected = 130.1502
        actual = convert('US Dollar', 'Japanese Yen', get_xrates(), 1)
        self.assertEqual(expected, actual)

    def test_rupee_to_euro(self):
        expected = 0.950667 / 76.421118
        actual = convert('Indian Rupee', 'Euro', get_xrates(), 1)
        self.assertEqual(expected, actual)

    def test_pound_to_us(self):
        expected = 1 / 0.800801
        actual = convert('British Pound', 'US Dollar', get_xrates(), 1)
        self.assertEqual(expected, actual)

    def test_us_to_yuan(self):
        expected = 6.607945 / 1
        actual = convert('US Dollar', 'Chinese Yuan Renminbi', get_xrates(), 1)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
