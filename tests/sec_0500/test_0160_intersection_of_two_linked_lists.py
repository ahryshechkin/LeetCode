from unittest import TestCase, main
from tasks.sec_0500.task_0160_intersection_of_two_linked_lists import Solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        n5 = ListNode(5)
        n4 = ListNode(4, n5)
        n8 = ListNode(8, n4)

        n11 = ListNode(1, n8)
        headA = ListNode(4, n11)

        n21 = ListNode(1, n8)
        n26 = ListNode(6, n21)
        headB = ListNode(5, n26)

        actual = self.s.getIntersectionNode(headA, headB)
        self.assertEqual(r, n8)


    def test02(self):
        n4 = ListNode(4)
        n2 = ListNode(2, n4)

        n11 = ListNode(1, n2)
        n19 = ListNode(9, n11)
        headA = ListNode(1, n19)

        headB = ListNode(3, n2)

        actual = self.s.getIntersectionNode(headA, headB)
        self.assertEqual(r, n2)


if __name__ == '__main__':
    main()
