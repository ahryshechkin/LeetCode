from unittest import TestCase, main
from tasks.sec_0500.task_0027_remove_element import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [3, 2, 2, 3]
        expected = [2, 2, 3, 3]

        actual = self.s.removeElement(given, 3)

        self.assertEqual(r, 2)
        self.assertListEqual(given, expected)


    def test02(self):
        given = [0, 1, 2, 2, 3, 0, 4, 2]
        expected = [0, 1, 4, 0, 3, 2, 2, 2]

        actual = self.s.removeElement(given, 2)

        self.assertEqual(r, 5)
        self.assertListEqual(given, expected)


if __name__ == '__main__':
    main()
