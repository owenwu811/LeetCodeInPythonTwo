
#1586
#medium

#Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

#BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
#boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
#int next() Moves the pointer to the right, then returns the number at the pointer.
#boolean hasPrev() Returns true if there exists a number in the traversal to the left of the pointer, otherwise returns false.
#int prev() Moves the pointer to the left, then returns the number at the pointer.
#Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

#You may assume that next() and prev() calls will always be valid. That is, there will be at least a next/previous number in the in-order traversal when next()/prev() is called.


#my own solution using python3:

#do the inorder traversal in the constructor and then copy the picture exactly, starting the pointer at index -1 instead of 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.ptr = -1
        self.cur = deque()
        def f(root):
            if not root:
                return None
            f(root.left)
            self.cur.append(root.val)
            f(root.right)
        f(root)

    def hasNext(self) -> bool:
        return len(self.cur) > 0 and self.ptr < len(self.cur) - 1
        
    def next(self) -> int:
        #print("next", self.cur, self.ptr)
        self.ptr += 1
        #print("next", self.cur, self.ptr)
        ans = self.cur[self.ptr]
        return ans
        
    def hasPrev(self) -> bool:
        return self.ptr > 0
        
    def prev(self) -> int:
        self.ptr = self.ptr - 1
        #print("prev", self.cur, self.ptr)
        ans = self.cur[self.ptr]
        return ans

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()
