from unittest import TestCase, main
from tasks.sec_0500.task_0020_valid_parantheses import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertTrue(self.s.isValid("()"))

    def test02(self):
        self.assertTrue(self.s.isValid("()[]{}"))

    def test03(self):
        self.assertFalse(self.s.isValid("(]"))

    def test04(self):
        self.assertTrue(self.s.isValid("([])"))

    def test05(self):
        self.assertFalse(self.s.isValid("([)]"))

    def test06(self):
        self.assertFalse(self.s.isValid("("))

    def test07(self):
        self.assertFalse(self.s.isValid(")"))


if __name__ == '__main__':
    main()
