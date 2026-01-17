from unittest import TestCase, main
from tasks.sec_1500.task_1248_count_number_nice_subarrays import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [1, 1, 2, 1, 1]
        actual = self.s.numberOfSubarrays(given, 3)

        self.assertEqual(actual, 2)


    def test02(self):
        given = [2, 4, 6]
        actual = self.s.numberOfSubarrays(given, 1)

        self.assertEqual(actual, 0)


    def test03(self):
        given = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
        actual = self.s.numberOfSubarrays(given, 2)

        self.assertEqual(actual, 16)


if __name__ == '__main__':
    main()
