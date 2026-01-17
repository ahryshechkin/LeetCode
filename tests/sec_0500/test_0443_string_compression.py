from unittest import TestCase, main
from tasks.sec_0500.task_0443_string_compression import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = ["a", "a", "b", "b", "c", "c", "c"]
        expected = ["a", "2", "b", "2", "c", "3"]
        k = self.s.compress(given)

        self.assertListEqual(given[:k], expected)


    def test02(self):
        given = ["a"]
        expected = ["a"]
        k = self.s.compress(given)

        self.assertListEqual(given[:k], expected)


    def test03(self):
        given = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        expected = ["a", "b", "1", "2"]
        k = self.s.compress(given)

        self.assertListEqual(given[:k], expected)


if __name__ == '__main__':
    main()
