from unittest import TestCase, main
from tasks.sec_1500.task_1299_replace_elements_on_right_side import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [17, 18, 5, 4, 6, 1]
        expected = [18, 6, 6, 6, 1, -1]
        actual = self.s.replaceElements(given)

        self.assertListEqual(actual, expected)


    def test02(self):
        given = [400]
        expected = [-1]
        actual = self.s.replaceElements(given)

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
