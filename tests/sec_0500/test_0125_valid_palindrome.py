from unittest import TestCase, main
from tasks.sec_0500.task_0125_valid_palindrome import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = "A man, a plan, a canal: Panama"
        self.assertTrue(self.s.isPalindrome(given))


    def test02(self):
        given = "race a car"
        self.assertFalse(self.s.isPalindrome(given))


    def test03(self):
        given = " "
        self.assertTrue(self.s.isPalindrome(given))


if __name__ == '__main__':
    main()
