class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").strip("!").strip("?").strip(".")
        s = s.replace(",", "").replace("'", "").replace(":", "")
        s = s.lower()
        for i in range((int)(len(s)/2)):
            if(s[i] != s[-i - 1]):
                return False

        return True