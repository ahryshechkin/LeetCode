from unittest import TestCase, main
from tasks.sec_0500.task_0049_group_anagrams import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

        self.assertListEqual(self.s.groupAnagrams(given), expected)


    def test02(self):
        given = [""]
        expected = [[""]]

        self.assertListEqual(self.s.groupAnagrams(given), expected)


    def test03(self):
        given = ["a"]
        expected = [["a"]]

        self.assertListEqual(self.s.groupAnagrams(given), expected)


if __name__ == '__main__':
    main()
