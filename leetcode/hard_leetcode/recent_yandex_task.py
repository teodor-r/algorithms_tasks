class Solution:

    # Method to find median
    def Median(self, A, B):

        n = len(A)
        m = len(B)
        if (n > m):
            return self.Median(B, A)

        start = 0
        end = n
        realmidinmergedarray = (n + m + 1) // 2

        while (start <= end):
            mid = (start + end) // 2
            leftAsize = mid
            leftBsize = realmidinmergedarray - mid

            leftA = A[leftAsize - 1] if (leftAsize > 0) else float('-inf')
            leftB = B[leftBsize - 1] if (leftBsize > 0) else float('-inf')
            rightA = A[leftAsize] if (leftAsize < n) else float('inf')
            rightB = B[leftBsize] if (leftBsize < m) else float('inf')

            print(f"leftAsize : {leftAsize}, leftA: {leftA} , rightA: {rightA}")
            print(f"leftBsize : {leftBsize}, leftB: {leftB} , rightB: {rightB}")
            if leftA <= rightB and leftB <= rightA:
                if ((m + n) % 2 == 0):
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                return max(leftA, leftB)

            elif (leftA > rightB):
                end = mid - 1
            else:
                start = mid + 1
# Driver code
ans = Solution()
arr1 = [-5, 3, 6, 12, 15,17,25,30,41]
arr2 = [-12, -10, -6, -3, 4, 10,12,14,17]
print("Median of the two arrays is")
print(ans.Median(arr1, arr2))