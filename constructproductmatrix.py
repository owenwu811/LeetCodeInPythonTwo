
#2906
#medium

#fuck this question 

#my "too slow" solution apparently:

class Solution:
    sys.set_int_max_str_digits(10000)
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        tot = 1
        cur = []
        for g in grid:
            cur.extend(g)
            tot *= math.prod(g)
        p = 1
        for i in range(len(cur)):
            p *= cur[i]
            cur[i] = (tot // cur[i]) % MOD
        size = len(grid[0])
        new = []
        for i in range(0, len(cur), size):
            new.append(cur[i: i + size])
        return new

#chatgpt solution (could not solve) - dumbest solution requiring tricks:

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        
        # Flatten the grid
        cur = [num for row in grid for num in row]
        n = len(cur)
        
        # Prefix and Suffix products
        prefix = [1] * n
        suffix = [1] * n

        # Compute prefix product
        for i in range(1, n):
            prefix[i] = (prefix[i - 1] * cur[i - 1]) % MOD

        # Compute suffix product
        for i in range(n - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * cur[i + 1]) % MOD
        
        # Compute result using prefix and suffix
        for i in range(n):
            cur[i] = (prefix[i] * suffix[i]) % MOD
        
        # Reshape to match the original grid size
        size = len(grid[0])
        return [cur[i:i + size] for i in range(0, n, size)]

        
