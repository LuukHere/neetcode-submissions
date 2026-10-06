class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #piles[i] = num bananas
        #i = pile number
        #h = number of hours to eat bananas
        #k = bananas per hour
        L, R = 1, max(piles)
        result = R
        while L <= R:
            k = (L + R) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                result = min(result, k)
                R = k - 1
            else:
                L = k + 1
        return result
