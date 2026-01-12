from unittest import TestCase, main
from tasks.sec_0500.task_0049_group_anagrams import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        r = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        self.assertListEqual(r, self.s.groupAnagrams(strs))


if __name__ == '__main__':
    main()
