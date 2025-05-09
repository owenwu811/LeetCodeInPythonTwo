
#2095
#medium

#You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

#The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

#For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

#Input: head = [1,3,4,7,1,2,6]
#Output: [1,3,4,1,2,6]
#Explanation:
#The above figure represents the given linked list. The indices of the nodes are written below.
#Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
#We return the new list after removing this node. 


#my own solution using python3 on 3/13/25 (originally solved in July of 2024 but forgot to upload the file):

#as always, turn the linked list into an integer array, manipulate the integer array, and then turn the integer array back into a linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = []
        while head:
            cur.append(head.val)
            head = head.next
        if len(cur) % 2 == 0:
            mid = len(cur) // 2 
        else:
            mid = len(cur) // 2
        cur.pop(mid)
        dummy = ListNode()
        now = dummy
        for c in cur:
            now.next = ListNode(c)
            now = now.next
        return dummy.next
