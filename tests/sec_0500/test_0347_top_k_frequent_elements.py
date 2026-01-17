from unittest import TestCase, main
from tasks.sec_0500.task_0347_top_k_frequent_elements import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [1, 1, 1, 2, 2, 3]
        expected = [1, 2]
        actual = self.s.topKFrequent(given, 2)

        self.assertListEqual(actual, expected)


    def test02(self):
        given = [1]
        expected = [1]
        actual = self.s.topKFrequent(given, 1)

        self.assertListEqual(actual, expected)


    def test03(self):
        given = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
        expected = [1, 2]
        actual = self.s.topKFrequent(given, 2)

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
