from unittest import TestCase, main
from tasks.sec_0500.task_0049_group_anagrams import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
        r = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        self.assertListEqual(self.s.groupAnagrams(arr), r)


    def test02(self):
        arr = [""]
        r = [[""]]
        self.assertListEqual(self.s.groupAnagrams(arr), r)


    def test03(self):
        arr = ["a"]
        r = [["a"]]
        self.assertListEqual(self.s.groupAnagrams(arr), r)


if __name__ == '__main__':
    main()
