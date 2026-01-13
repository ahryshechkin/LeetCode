from unittest import TestCase, main
from tasks.sec_0500.task_0011_container_with_most_water import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(self.s.maxArea(height), 49)


    def test02(self):
        height = [1, 1]
        self.assertEqual(self.s.maxArea(height), 1)


if __name__ == '__main__':
    main()