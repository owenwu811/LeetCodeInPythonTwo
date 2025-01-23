#1522
#medium

#Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

#The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

#(Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)

#Input: root = [1,null,3,2,4,null,5,6]
#Output: 3
#Explanation: Diameter is shown in red color.



#correct python3 solution (could not solve):

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int


        """
        self.res = 0
        def f(root):
            if not root.children:
                return 0
            l1, l2 = 0, 0
            for a in root.children:
                depth = 1 + f(a)
                print(depth)
                if depth >= l1:
                    ph = l1
                    l2 = ph
                    l1 = depth
                elif depth >= l2:
                    l2 = depth
            self.res = max(self.res, l1 + l2) 
            return l1
        f(root)
        return self.res
