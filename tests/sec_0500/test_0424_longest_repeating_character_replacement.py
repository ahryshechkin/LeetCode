from unittest import TestCase, main
from tasks.sec_0500.task_0424_longest_repeating_character_replacement import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.characterReplacement("ABAB", 2)
        self.assertEqual(r, 4)

    def test02(self):
        r = self.s.characterReplacement("AABABBA", 1)
        self.assertEqual(r, 4)


if __name__ == '__main__':
    main()
