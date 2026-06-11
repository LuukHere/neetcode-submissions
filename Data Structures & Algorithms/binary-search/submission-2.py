class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l<=r:
            half = (r+l)//2 #The first l acts as a starting point 
            print(l, r, half, nums[half], target)
            if nums[half] == target:
                return half
            elif nums[half] > target:
                r = half - 1
            else:
                l = half + 1
            print(l, r, half, nums[half], target)
            print("/-----/")
        return -1
                