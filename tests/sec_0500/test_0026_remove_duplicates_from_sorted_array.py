from unittest import TestCase, main
from tasks.sec_0500.task_0026_remove_duplicates_from_sorted_array import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [1, 1, 2]
        expected = [1, 2, 2]
        actual = self.s.removeDuplicates(given)

        self.assertEqual(actual, 2)
        self.assertListEqual(given, expected)


    def test02(self):
        given = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
        actual = self.s.removeDuplicates(given)

        self.assertEqual(actual, 5)
        self.assertListEqual(given, expected)


if __name__ == '__main__':
    main()
