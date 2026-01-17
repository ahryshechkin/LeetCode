from unittest import TestCase, main
from tasks.sec_1500.task_1346_check_if_n_and_its_double_exist import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [10, 2, 5, 3]
        self.assertTrue(self.s.checkIfExist(given))


    def test02(self):
        given = [3, 1, 7, 11]
        self.assertFalse(self.s.checkIfExist(given))


    def test03(self):
        given = [7, 1, 14, 11]
        self.assertTrue(self.s.checkIfExist(given))


if __name__ == '__main__':
    main()
