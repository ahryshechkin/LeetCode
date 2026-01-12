from unittest import TestCase, main
from tasks.sec_2000.task_1653_minimum_deletions import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.minimumDeletions("aababbab")
        self.assertEqual(r, 2)

    def test02(self):
        r = self.s.minimumDeletions("bbaaaaabb")
        self.assertEqual(r, 2)


if __name__ == '__main__':
    main()
