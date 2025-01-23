#2674
#medium

#Given a circular linked list list of positive integers, your task is to split it into 2 circular linked lists so that the first one contains the first half of the nodes in list (exactly ceil(list.length / 2) nodes) in the same order they appeared in list, and the second one contains the rest of the nodes in list in the same order they appeared in list.

#Return an array answer of length 2 in which the first element is a circular linked list representing the first half and the second element is a circular linked list representing the second half.

#A circular linked list is a normal linked list with the only difference being that the last node's next node, is the first node.
 

#Example 1:

#Input: nums = [1,5,7]
#Output: [[1,5],[7]]
#Explanation: The initial list has 3 nodes so the first half would be the first 2 elements since ceil(3 / 2) = 2 and the rest which is 1 node is in the second half.
#Example 2:

#Input: nums = [2,6,1,5]
#Output: [[2,6],[1,5]]
#Explanation: The initial list has 4 nodes so the first half would be the first 2 elements since ceil(4 / 2) = 2 and the rest which is 2 nodes are in the second half.



#correct python3 solution (could not solve):

#this question has a weird api and is not intuitive - would reccomend avoiding

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, list: Optional[ListNode]) -> List[Optional[ListNode]]:
        slow, fast = list, list
        while fast.next != list:
            if fast.next.next == list:
                fast = fast.next
            else:
                fast = fast.next.next
                slow = slow.next
        fast.next = slow.next
        slow.next = list
        return [list, fast.next]
