class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for index in range(0, len(nums)):
            complement = target - nums[index]
            if complement in dict :
                return ({index, dict.get(complement)})
            else:
                dict[nums[index]] = index
            
