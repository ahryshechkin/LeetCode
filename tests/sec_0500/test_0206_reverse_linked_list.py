from unittest import TestCase, main
from tasks.sec_0500.task_0206_reverse_linked_list import Solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        expected = [5, 4, 3, 2, 1]
        actual = list()

        cuactual = self.s.reverseList(head)
        while cur:
            actual.append(cur.val)
            cuactual = cur.next

        self.assertListEqual(actual, expected)


    def test02(self):
        head = ListNode(1)
        head.next = ListNode(2)

        expected = [2, 1]
        actual = list()

        cuactual = self.s.reverseList(head)
        while cur:
            actual.append(cur.val)
            cuactual = cur.next

        self.assertListEqual(actual, expected)


    def test03(self):
        head = None

        expected = []
        actual = list()

        cuactual = self.s.reverseList(head)
        while cur:
            actual.append(cur.val)
            cuactual = cur.next

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
