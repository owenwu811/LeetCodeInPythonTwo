


#2689
#easy

#You are given the root of a binary tree and an integer k. Besides the left and right children, every node of this tree has two other properties, a string node.val containing only lowercase English letters (possibly empty) and a non-negative integer node.len. There are two types of nodes in this tree:

#Leaf: These nodes have no children, node.len = 0, and node.val is some non-empty string.
#Internal: These nodes have at least one child (also at most two children), node.len > 0, and node.val is an empty string.
#The tree described above is called a Rope binary tree. Now we define S[node] recursively as follows:

#If node is some leaf node, S[node] = node.val,
#Otherwise if node is some internal node, S[node] = concat(S[node.left], S[node.right]) and S[node].length = node.len.
#Return k-th character of the string S[root].

#Note: If s and p are two strings, concat(s, p) is a string obtained by concatenating p to s. For example, concat("ab", "zz") = "abzz".

 

#Example 1:

#Input: root = [10,4,"abcpoe","g","rta"], k = 6
#Output: "b"
#Explanation: In the picture below, we put an integer on internal nodes that represents node.len, and a string on leaf nodes that represents node.val.
#You can see that S[root] = concat(concat("g", "rta"), "abcpoe") = "grtaabcpoe". So S[root][5], which represents 6th character of it, is equal to "b".


#my own solution using python3:

#encode only the strings using dfs, and get the kth character from the left

# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        self.cur = ""
        def f(root):
            if not root:
                return 
            print(root.val)
            if type(root.val) == str:
                self.cur += root.val
            f(root.left)
            f(root.right)



        f(root)
        print(self.cur)
        return self.cur[k - 1]
