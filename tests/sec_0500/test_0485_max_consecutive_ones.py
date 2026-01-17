from unittest import TestCase, main
from tasks.sec_0500.task_0485_max_consecutive_ones import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [1, 1, 0, 1, 1, 1]
        actual = self.s.findMaxConsecutiveOnes(given)

        self.assertEqual(actual, 3)


    def test02(self):
        given = [1, 0, 1, 1, 0, 1]
        actual = self.s.findMaxConsecutiveOnes(given)

        self.assertEqual(actual, 2)


if __name__ == '__main__':
    main()
