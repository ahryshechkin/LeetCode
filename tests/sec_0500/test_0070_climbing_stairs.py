from unittest import TestCase, main
from tasks.sec_0500.task_0070_climbing_stairs import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        self.assertEqual(self.s.climbStairs(2), 2)


    def test02(self):
        self.assertEqual(self.s.climbStairs(3), 3)


if __name__ == '__main__':
    main()
