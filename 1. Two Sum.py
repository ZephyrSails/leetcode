class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_buff = {}
        for i in range(len(nums)):
            if target-nums[i] in hash_buff:
                return [hash_buff[target-nums[i]], i]
            else:
                hash_buff[nums[i]] = i
