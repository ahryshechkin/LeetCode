from unittest import TestCase, main
from tasks.sec_0500.task_0200_number_of_islands import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        actual = self.s.numIslands(given)

        self.assertEqual(actual, 1)


    def test02(self):
        given = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        actual = self.s.numIslands(given)

        self.assertEqual(actual, 3)


if __name__ == '__main__':
    main()
