class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = {}
        for word in strs:
            temp = "".join(sorted(word))
            if temp in grouping:
                grouping[temp].append(word)
            else:
                grouping[temp] = [word]
        print(grouping)
        final = []
        for group in grouping.values():
            final.append(group)
        return final