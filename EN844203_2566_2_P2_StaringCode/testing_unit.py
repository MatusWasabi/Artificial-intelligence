import unittest


class TestNumber(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 2, 3)
        self.assertEqual(2 + 2, 4)
    def test_multiply(self):
        self.assertEqual(1 * 1, 1)
        self.assertEqual(1 * 2, 2)
        self.assertEqual(2 * 4, 8)


if __name__ == "__main__":
    unittest.main()