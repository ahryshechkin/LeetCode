from unittest import TestCase, main
from tasks.sec_1000.task_0849_maximize_distance_to_clesest_person import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [1, 0, 0, 0, 1, 0, 1]
        actual = self.s.maxDistToClosest(given)

        self.assertEqual(actual, 2)


    def test02(self):
        given = [1, 0, 0, 0]
        actual = self.s.maxDistToClosest(given)

        self.assertEqual(actual, 3)


    def test03(self):
        given = [0, 1]
        actual = self.s.maxDistToClosest(given)

        self.assertEqual(actual, 1)


    def test04(self):
        given = [0, 0, 1]
        actual = self.s.maxDistToClosest(given)

        self.assertEqual(actual, 2)


    def test05(self):
        given = [0, 1, 0, 0, 0, 0]
        actual = self.s.maxDistToClosest(given)

        self.assertEqual(actual, 4)


if __name__ == '__main__':
    main()
