import unittest
from main import isomorphic


class IsomorphicTestCase(unittest.TestCase):
    def test_positive_isomorphic(self):
        self.assertEqual(isomorphic("", ""), True)
        self.assertEqual(isomorphic(", t = ", ""), True)
        self.assertEqual(isomorphic("egg", "add"), True)
        self.assertEqual(isomorphic("paper", "title"), True)

    def test_negative_isomorphic(self):
        self.assertEqual(isomorphic("foo", "bar"), False)
        self.assertEqual(isomorphic("see", "sed"), False)


if __name__ == '__main':
    unittest.main()
