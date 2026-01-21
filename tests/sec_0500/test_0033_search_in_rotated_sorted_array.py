from unittest import TestCase, main
from tasks.sec_0500.task_0033_search_in_rotated_sorted_array import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(self.s.search(given, 0), 4)


    def test02(self):
        given = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(self.s.search(given, 3), -1)


    def test03(self):
        given = [1]
        self.assertEqual(self.s.search(given, 0), -1)


    def test04(self):
        given = [5, 1, 3]
        self.assertEqual(self.s.search(given, 3), 2)


if __name__ == '__main__':
    main()
