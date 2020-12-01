"""

Runtime: 32 ms, faster than 61.01% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 14.2 MB, less than 48.16% of Python3 online submissions for Spiral Matrix II.

"""

def generateMatrix(self, n: int) -> List[List[int]]:
    l, r, t, b = 0, n - 1, 0, n - 1
    mat = [[0 for _ in range(n)] for _ in range(n)]
    num, tar = 1, n * n
    while num <= tar:
        for i in range(l, r + 1): # left to right
            mat[t][i] = num
            num += 1
        t += 1
        for i in range(t, b + 1): # top to bottom
            mat[i][r] = num
            num += 1
        r -= 1
        for i in range(r, l - 1, -1): # right to left
            mat[b][i] = num
            num += 1
        b -= 1
        for i in range(b, t - 1, -1): # bottom to top
            mat[i][l] = num
            num += 1
        l += 1
    return mat
