
#1669
#medium

#You are given two linked lists: list1 and list2 of sizes n and m respectively.

#Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

#Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
#Output: [10,1,13,1000000,1000001,1000002,5]
#Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.



#my own solution using python3 on 3/13/25 (originally solved in August of 2024 but forgot to add the file):

#just turn the linked list into an array, subsitute the portion of one between a and b with two, and turn one back into a linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        first = []
        while list1:
            first.append(list1.val)
            list1 = list1.next
        second = []
        while list2:
            second.append(list2.val)
            list2 = list2.next
        first[a:b + 1] = second
        dummy = ListNode()
        cur = dummy
        for f in first:
            cur.next = ListNode(f)
            cur = cur.next
        return dummy.next
