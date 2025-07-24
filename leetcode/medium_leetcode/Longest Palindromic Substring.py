class Solution:
    # @return a string
    def longestPalindrome(self, s):
        center, right = 0,1
        newS = "#"+"#".join(s)+"#"
        palHalfLenCenteringHere = [1] * len(newS)
        for index in range(1, len(newS)):
            assert index <= right
            if index < right and index + palHalfLenCenteringHere[2*center-index] < right:
                palHalfLenCenteringHere[index] = palHalfLenCenteringHere[2*center-index]
            else:
                center = index
                if index < right:
                    palHalfLenCenteringHere[index] = right - center
                else:
                    palHalfLenCenteringHere[index] = 1
                    right += 1
                while right < len(newS) and 2*center-right >= 0 and newS[right] == newS[2*center-right]:
                    right += 1
                    palHalfLenCenteringHere[index] += 1
        center, halfLen = max(enumerate(palHalfLenCenteringHere), key=lambda x: x[1])
        result = newS[center - halfLen + 1: center + halfLen]
        return result.replace("#", "")

sl = Solution()
print(sl.longestPalindrome("babad"))