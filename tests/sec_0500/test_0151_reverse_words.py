from unittest import TestCase, main
from tasks.sec_0500.task_0151_reverse_words import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.reverseWords("the sky is blue")
        self.assertEqual(r, "blue is sky the")

    def test02(self):
        r = self.s.reverseWords("  hello world  ")
        self.assertEqual(r, "world hello")

    def test03(self):
        r = self.s.reverseWords("a good   example")
        self.assertEqual(r, "example good a")


if __name__ == '__main__':
    main()
