from unittest import TestCase, main
from tasks.sec_0500.task_0007_reverse_integer import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        self.assertEqual(self.s.reverse(123), 321)


    def test02(self):
        self.assertEqual(self.s.reverse(-123), -321)


    def test03(self):
        self.assertEqual(self.s.reverse(120), 21)


    def test04(self):
        self.assertEqual(self.s.reverse(1534236469), 0)


    def test05(self):
        self.assertEqual(self.s.reverse(-2147483412), -2143847412)


if __name__ == '__main__':
    main()
