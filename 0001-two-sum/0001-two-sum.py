class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i in range (len(nums)):
            sum = target - nums[i]
            if sum in hash_map :
                return (hash_map[sum] , i)
            else :
                hash_map[nums[i]] = i