from unittest import TestCase, main
from tasks.sec_0500.task_0008_string_to_integer import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertEqual(self.s.myAtoi("42"), 42)

    def test02(self):
        self.assertEqual(self.s.myAtoi("  -42"), -42)

    def test03(self):
        self.assertEqual(self.s.myAtoi("1337c0d3"), 1337)

    def test04(self):
        self.assertEqual(self.s.myAtoi("0-1"), 0)

    def test05(self):
        self.assertEqual(self.s.myAtoi("words and 987"), 0)


if __name__ == '__main__':
    main()
