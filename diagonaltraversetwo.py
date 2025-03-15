#1424
#medium

#Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

#Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,4,2,7,5,3,8,6,9]


#my own solution using python3:

#make some careful observations

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        #[0, 0] [1, 0], [0, 1] [2, 0], [1, 1], [0, 2], [2, 1], [1, 2], [2, 2]


        #{0: [[0, 0]], 1: [[0, 1], [1, 0]], 2: [[0, 2], [1, 1], [2, 0]], 3: [[1, 2], [2, 1]], 4: [[2, 2]]})

        d = defaultdict(deque)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                cursum = i + j
                d[cursum].appendleft([i, j])
        
        print(d)
        res = []
        for k in d:
            for a in d[k]:
                #print(a)
                x, y = a[0], a[1]
                if x < len(nums) and y < len(nums[x]):
                    res.append(nums[x][y])
                #print(x, y)
        return res
