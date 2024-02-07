"""Includes the Solution class to solve a problem."""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """Contains functions to solve a problem."""
    # My solution
    def solve1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add each l1 and l2 node values into a new ListNode.

        Start with an empty ListNode for keeping track. This will not be returned, the next one will.
        While l1 and l2 are not None, add them together or separtely into our result.
        Track the carry and create a new node if needed at the end.
        """
        result = ListNode()
        result_ptr = result
        carry = 0

        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                val = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next

            val += carry
            if val > 9:
                val -= 10
                carry = 1
            else:
                carry = 0

            result_ptr.next = ListNode(val=val)
            result_ptr = result_ptr.next

        if carry != 0:
            result_ptr.next = ListNode(val=carry)

        return result.next
    
    # My solution
    def solve2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Same as last solution except instead of an if statement, to deal
        with the carry, use mathematical expressions instead.
        """
        result = ListNode()
        result_ptr = result
        carry = 0

        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                val = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next

            val += carry
            carry = val // 10
            val = val % 10
            
            result_ptr.next = ListNode(val=val)
            result_ptr = result_ptr.next

        if carry != 0:
            result_ptr.next = ListNode(val=carry)

        return result.next

    # Other's solution
    def other1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """A solution posted by another user."""
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
