from unittest import TestCase, main
from tasks.sec_0500.task_0387_first_unique_character_in_a_string import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        self.assertEqual(self.s.firstUniqChar("leetcode"), 0)


    def test02(self):
        self.assertEqual(self.s.firstUniqChar("loveleetcode"), 2)


    def test03(self):
        self.assertEqual(self.s.firstUniqChar("aabb"), -1)


if __name__ == '__main__':
    main()
