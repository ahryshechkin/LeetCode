from unittest import TestCase, main
from tasks.sec_0500.task_0066_plus_one import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        expected = [1, 2, 4]
        actual = self.s.plusOne([1, 2, 3])

        self.assertEqual(actual, expected)


    def test02(self):
        expected = [4, 3, 2, 2]
        actual = self.s.plusOne([4, 3, 2, 1])

        self.assertListEqual(actual, expected)


    def test03(self):
        expected = [1, 0]
        actual = self.s.plusOne([9])

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
