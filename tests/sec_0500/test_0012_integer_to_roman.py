from unittest import TestCase, main
from tasks.sec_0500.task_0012_interger_to_roman import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        self.assertEqual(self.s.intToRoman(3749), "MMMDCCXLIX")


    def test02(self):
        self.assertEqual(self.s.intToRoman(58), "LVIII")


    def test03(self):
        self.assertEqual(self.s.intToRoman(1994), "MCMXCIV")


if __name__ == '__main__':
    main()
