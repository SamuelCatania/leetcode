class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left = 0
        right = sum(nums)

        for p in range(len(nums)):
            right -= nums[p]
            
            if left == right:
                return p
                
            left += nums[p]

        return -1
