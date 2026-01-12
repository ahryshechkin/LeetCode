from unittest import TestCase, main
from tasks.sec_0500.task_0412_fizz_buzz import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        expected = ["1", "2", "Fizz"]
        self.assertListEqual(self.s.fizzBuzz(3), expected)

    def test02(self):
        expected = ["1", "2", "Fizz", "4", "Buzz"]
        self.assertListEqual(self.s.fizzBuzz(5), expected)

    def test03(self):
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
        self.assertListEqual(self.s.fizzBuzz(15), expected)


if __name__ == '__main__':
    main()
