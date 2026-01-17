from unittest import TestCase, main
from tasks.sec_0500.task_0021_merge_two_sorted_lists import Solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        h14 = ListNode(4)
        h12 = ListNode(2, h14)
        h11 = ListNode(1, h12)

        h24 = ListNode(4)
        h23 = ListNode(3, h24)
        h21 = ListNode(1, h23)

        expected = [1, 1, 2, 3, 4, 4]
        actual = list()
        head = self.s.mergeTwoLists(h11, h21)
        while head:
            actual.append(head.val)
            head = head.next

        self.assertListEqual(actual, expected)


    def test02(self):
        expected = []
        actual = list()
        head = self.s.mergeTwoLists([], [])
        while head:
            actual.append(head.val)
            head = head.next

        self.assertListEqual(actual, expected)


    def test03(self):
        expected = [0]
        actual = list()
        head = self.s.mergeTwoLists([], ListNode())
        while head:
            actual.append(head.val)
            head = head.next

        self.assertListEqual(actual, expected)
