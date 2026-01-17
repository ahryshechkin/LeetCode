from unittest import TestCase, main
from tasks.sec_0500.task_0141_linked_list_cycle import Solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        n4 = ListNode(-4)
        n3 = ListNode(0, n4)
        n2 = ListNode(2, n3)
        n1 = ListNode(3, n2)
        n4.next = n2

        self.assertTrue(self.s.hasCycle(n1))


    def test02(self):
        n1 = ListNode(1)
        n2 = ListNode(2, n1)
        n1.next = n2

        self.assertTrue(self.s.hasCycle(n1))


    def test03(self):
        n1 = ListNode(1)

        self.assertFalse(self.s.hasCycle(n1))


    def test04(self):
        self.assertFalse(self.s.hasCycle([]))


    def test05(self):
        n2 = ListNode(2)
        n1 = ListNode(1, n2)

        self.assertFalse(self.s.hasCycle(n1))


if __name__ == '__main__':
    main()
