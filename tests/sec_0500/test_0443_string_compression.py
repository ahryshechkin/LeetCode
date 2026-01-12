from unittest import TestCase, main
from tasks.sec_0500.task_0443_string_compression import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        a = ["a", "a", "b", "b", "c", "c", "c"]
        k = self.s.compress(a)
        self.assertListEqual(a[:k], ["a", "2", "b", "2", "c", "3"])

    def test02(self):
        a = ["a"]
        k = self.s.compress(a)
        self.assertListEqual(a[:k], ["a"])

    def test03(self):
        a = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        k = self.s.compress(a)
        self.assertListEqual(a[:k], ["a", "b", "1", "2"])


if __name__ == '__main__':
    main()
