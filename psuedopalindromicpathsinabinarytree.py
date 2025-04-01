#1457
#medium

#Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

#Return the number of pseudo-palindromic paths going from the root node to leaf nodes.


#my own solution using python3:

#use a dictionary to keep track of palindromes 

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.c = Counter()
        self.paths = []
        def f(root):
            if not root:
                return None
            self.paths.append(root.val)
            self.c[root.val] += 1
            if not root.left and not root.right:
                flag = False
                cnt = 0
                for a, b in self.c.items():
                    if b % 2 != 0:
                        cnt += 1
                    if cnt >= 2:
                        flag = False
                        break
                else:
                    flag = True
                if flag:
                    self.res += 1
            f(root.left)
            f(root.right)
            a = self.paths.pop()
            self.c[a] -= 1
            if self.c[a] == 0:
                del self.c[a]
            #self.paths.pop()
        f(root)
        return self.res
