#725
#medium


#Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

#The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

#The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

#Return an array of the k parts.



#my own solution using python3:


#messy but working after lots of trial and error

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        tmp = deque()
        while head:
            tmp.append(head.val)
            head = head.next
        print(len(tmp), k)
        if len(tmp) < k:
            res = []
            for t in tmp:
                res.append(ListNode(t))
            diff = k - len(tmp)
            while diff > 0:
                res.append(None)
                diff -= 1
            return res
            
        elif len(tmp) > k:
            res = []
            leftover = len(tmp) % k
            sizes = []
            if leftover > 0:
                parts = len(tmp) // k 
                while leftover > 0:
                    sizes.append(parts + 1)
                    leftover -= 1
                diff = len(tmp) - (parts + 1)
                while diff > 0:
                    sizes.append(parts)
                    diff -= k
                if sum(sizes) < len(tmp):
                    diff = len(tmp) - sum(sizes)
                    while diff > 0:
                        sizes.append(1)
                        diff -= 1
                for s in sizes:
                    dummy = ListNode()
                    curpart = dummy
                    while tmp and s > 0:
                        curpart.next = ListNode(tmp.popleft())
                        curpart = curpart.next
                        s -= 1
                    res.append(dummy.next)
                while res and res[-1] == None:
                    res.pop()
                return res
            else:
                res = []
                parts = len(tmp) // k
                sizes = []
                diff = len(tmp) // parts
                while diff > 0:
                    sizes.append(parts)
                    diff -= 1
                for s in sizes:
                    dummy = ListNode()
                    curpart = dummy
                    while tmp and s > 0:
                        curpart.next = ListNode(tmp.popleft())
                        curpart = curpart.next
                        s -= 1
                    res.append(dummy.next)
                while res[-1] == [None]:
                    res.pop()
                return res
        else:
            res = []
            leftover = len(tmp) % k
            sizes = []
            if leftover >= 1:
                parts = len(tmp) // k
                while leftover > 0:
                    sizes.append(parts + 1)
                    leftover -= 1
                diff = len(tmp) - parts
                while diff > 0:
                    sizes.append(parts)
                    diff -= k
                if sum(sizes) < len(tmp):
                    diff = len(tmp) - sum(sizes)
                    while diff > 0:
                        sizes.append(1)
                        diff -= 1
                print(sum(sizes), len(tmp))
                for s in sizes:
                    dummy = ListNode()
                    curpart = dummy
                    while tmp and s > 0:
                        curpart.next = ListNode(tmp.popleft())
                        curpart = curpart.next
                        s -= 1
                    res.append(dummy.next)
                return res
            else:
                res = []
                parts = len(tmp) // k
                sizes = []
                diff = len(tmp) // parts
                while diff > 0:
                    sizes.append(parts)
                    diff -= 1
                for s in sizes:
                    dummy = ListNode()
                    curpart = dummy
                    while tmp and s > 0:
                        curpart.next = ListNode(tmp.popleft())
                        curpart = curpart.next
                        s -= 1
                    res.append(dummy.next)
                return res
