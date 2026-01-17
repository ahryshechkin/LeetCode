from unittest import TestCase, main
from tasks.sec_0500.task_0155_min_stack import MinStack


class TestSolution(TestCase):
    def test01(self):
        s = MinStack()
        s.push(-2)
        s.push(0)
        s.push(-3)
        self.assertEqual(s.getMin(), -3)
        s.pop()
        self.assertEqual(s.top(), 0)
        self.assertEqual(s.getMin(), -2)


    def test02(self):
        s = MinStack()
        s.push(-1)
        self.assertEqual(s.top(), -1)
        self.assertEqual(s.getMin(), -1)


    def test03(self):
        s = MinStack()
        s.push(0)
        s.push(1)
        s.push(0)
        self.assertEqual(s.getMin(), 0)
        s.pop()
        self.assertEqual(s.getMin(), 0)
        s.pop()
        self.assertEqual(s.getMin(), 0)
        s.pop()
        s.push(-2)
        s.push(-1)
        s.push(-2)
        self.assertEqual(s.getMin(), -2)
        s.pop()
        self.assertEqual(s.top(), -1)
        self.assertEqual(s.getMin(), -2)
        s.pop()
        self.assertEqual(s.getMin(), -2)
        s.pop()


if __name__ == '__main__':
    main()
