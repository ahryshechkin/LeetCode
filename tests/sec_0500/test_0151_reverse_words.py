from unittest import TestCase, main
from tasks.sec_0500.task_0151_reverse_words import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = "the sky is blue"
        expected = "blue is sky the"
        actual = self.s.reverseWords(given)

        self.assertEqual(actual, expected)


    def test02(self):
        given = "  hello world  "
        expected = "world hello"
        actual = self.s.reverseWords(given)

        self.assertEqual(actual, expected)


    def test03(self):
        given = "a good   example"
        expected = "example good a"
        actual = self.s.reverseWords(given)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    main()
