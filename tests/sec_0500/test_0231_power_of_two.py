from unittest import TestCase, main
from tasks.sec_0500.task_0231_power_of_two import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        self.assertTrue(self.s.isPowerOfTwo(1))


    def test02(self):
        self.assertTrue(self.s.isPowerOfTwo(16))


    def test03(self):
        self.assertFalse(self.s.isPowerOfTwo(3))


    def test04(self):
        self.assertFalse(self.s.isPowerOfTwo(0))


if __name__ == '__main__':
    main()
