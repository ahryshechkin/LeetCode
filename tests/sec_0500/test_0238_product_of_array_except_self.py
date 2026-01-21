from unittest import TestCase, main
from tasks.sec_0500.task_0238_product_of_array_except_self import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        actual = self.s.productExceptSelf(given)

        self.assertListEqual(actual, expected)


    def test02(self):
        given = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        actual = self.s.productExceptSelf(given)

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
