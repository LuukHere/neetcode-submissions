class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for char in s:
            if char.isalnum():
                newS += char
        newS = newS.lower()
        print(newS)
        for i in range((int)(len(newS)/2)):
            if(newS[i] != newS[-i - 1]):
                return False

        return True