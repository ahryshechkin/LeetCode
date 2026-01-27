from unittest import TestCase, main
from tasks.sec_0500.task_0242_valid_anagram import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        self.assertTrue(self.s.isAnagram("anagram", "nagaram"))


    def test02(self):
        self.assertFalse(self.s.isAnagram("rat", "car"))


if __name__ == '__main__':
    main()
