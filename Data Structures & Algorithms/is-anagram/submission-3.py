class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        if len(s) != len(t):
            return False
        for char in s:
            sdict[char] = sdict.get(char, 0) + 1
        for char in t:
            tdict[char] = tdict.get(char, 0) + 1
        
        return sdict == tdict
            