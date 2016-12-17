class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()

        # if len(nums) % 2:
        half = len(nums[::2]) - 1
        # else:
        # half = len(nums[::2])

        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
