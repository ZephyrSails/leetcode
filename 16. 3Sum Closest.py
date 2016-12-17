class Solution(object):
    # def threeSumClosest(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     # C n 3

    #     # n! / 3! * (n-3)!
    #     nums.sort()

    #     # 1,2,3,4,5,6,7,8,1000
    #     # i
    #     #   j
    #     #                  k

    #     # count = 1003
    #     # offset = 983

    #     # 20
    #     ans = float('inf')

    #     i = 0
    #     # [-3, 0, 1, 2]
    #     while i < len(nums)-2:
    #         # while i < len(nums)-2 and nums[i] == nums[i+1]: i += 1
    #         # if i != 0 and nums[i] == nums[i-1]:
    #         #     i += 1
    #         #     continue
    #         j, k = i+1, len(nums)-1
    #         # print j, k

    #         # while j < k-1 and nums[j] == nums[j-1]: j += 1
    #         # while j+1 < k and nums[k] == nums[k+1]: k -= 1

    #         # print j, k
    #         while j < k:

    #             count = nums[i] + nums[j] + nums[k]
    #             # print nums[i], nums[j], nums[k], nums, count

    #             if abs(count - target) < abs(ans - target):
    #                 ans = count
    #                 # j += 1
    #                 # k -= 1
    #                 # while j < k and nums[j] == nums[j+1]: j += 1
    #                 # while j < k and nums[k] == nums[k-1]: k -= 1

    #             if count < target:
    #                 j += 1
    #                 while j < k and nums[j] == nums[j-1]: j += 1
    #             else:
    #                 k -= 1
    #                 while j < k and nums[k] == nums[k+1]: k -= 1

    #             # if abs(count - target) < abs(ans - target):
    #             #     ans = count
    #             #     j += 1
    #             #     k -= 1
    #             #     while j < k and nums[j] == nums[j+1]: j += 1
    #             #     while j < k and nums[k] == nums[k-1]: k -= 1
    #             # moveK = abs(nums[i] + nums[j] + nums[k-1] - target)
    #             # moveJ = abs(nums[i] + nums[j+1] + nums[k] - target)

    #             # elif abs(nums[i+1] + nums[j] + nums[k] - target) < min(moveK, moveJ):
    #             #     break

    #             # elif moveK < moveJ:
    #             #     k -= 1
    #             #     while j < k and nums[k] == nums[k-1]: k -= 1
    #             # else:
    #             #     j += 1
    #             #     while j < k and nums[j] == nums[j+1]: j += 1

    #         i += 1
    #         #while i < len(nums)-2 and nums[i] == nums[i+1]: i += 1
    #     return ans

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        minDiff, minS = sys.maxint, None
        nums.sort()
        keys = nums
        for i in xrange(len(keys) - 2):
            if i != 0 and keys[i] == keys[i-1]:
                continue
            n1 = keys[i]
            j, k = i + 1, len(keys) - 1
            while j < k:
                n2, n3 = keys[j], keys[k]
                s = n1 + n2 + n3
                d = abs(s - target)
                if d == 0:
                    return s
                if minDiff > d:
                    minDiff = d
                    minS = s
                if s < target:
                    j += 1
                    while j < k and keys[j] == keys[j-1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and keys[k] == keys[k+1]:
                        k -= 1
        return minS

                
