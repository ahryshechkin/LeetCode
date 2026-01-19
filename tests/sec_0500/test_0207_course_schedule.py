from unittest import TestCase, main
from tasks.sec_0500.task_0207_course_schedule import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [[1, 0]]
        self.assertTrue(self.s.canFinish(2, given))


    def test02(self):
        given = [[1, 0], [0, 1]]
        self.assertFalse(self.s.canFinish(2, given))


if __name__ == '__main__':
    main()
