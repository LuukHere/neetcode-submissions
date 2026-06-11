class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in stringSet:
                stringSet.remove(s[left])
                left += 1
            stringSet.add(s[right])
            print(result, right, left)
            result = max(result, right - left + 1)
        return result
