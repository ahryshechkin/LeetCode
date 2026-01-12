from unittest import TestCase, main
from tasks.sec_0500.task_0066_plus_one import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.plusOne([1, 2, 3])
        self.assertEqual(r, [1, 2, 4])

    def test02(self):
        r = self.s.plusOne([4, 3, 2, 1])
        self.assertListEqual(r, [4, 3, 2, 2])

    def test03(self):
        r = self.s.plusOne([9])
        self.assertListEqual(r, [1, 0])


if __name__ == '__main__':
    main()
