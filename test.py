import unittest
from ReverseInteger import Solution


class ReverseIntegerTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.value = 123
        self.assertEqual(temp.reverse(self.value), 321)

    def test_value_zero(self):
        temp = Solution()
        self.value = 0
        self.assertEqual(temp.reverse(self.value), 0)

    def test_negative_value(self):
        temp = Solution()
        self.value = -123456
        self.assertEqual(temp.reverse(self.value), -654321)

    def test_positive_maximum_value(self):
        temp = Solution()
        self.value = 8463847412
        self.assertEqual(temp.reverse(self.value), 0)

    def test_negative_maximum_value(self):
        temp = Solution()
        self.value = -8463847412
        self.assertEqual(temp.reverse(self.value), 0)
        
    def test_none_int_input(self):
        temp = Solution()
        self.value = ""
        self.assertEqual(temp.reverse(self.value), None)
    

if __name__ == "__main__":
    unittest.main()
