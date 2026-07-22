class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()

        for i, a in enumerate(nums):
            # When the left most checker gets greater than 0 
            #since nums is sorted then anything to the left of 'a' is less than 'a'.
            #so if 'a' is greater than 0, then theres no number greater 
            #that can add to make it back to 0
            if a > 0: 
                break
            if i > 0 and a == nums[i-1]: #duplicate number
                continue

            l,r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    final.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1

        return final