class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans= set([])
        tuple_hash = {}
        single_set = set([])

        for num in nums:
            if num in tuple_hash:
                for tup in tuple_hash[num]:
                    ans.add(tuple(sorted((tup) + (num,))))
                del tuple_hash[num]

            for key in single_set:
                if 0-num-key in tuple_hash:
                    tuple_hash[0-num-key].add((num, key))
                else:
                    tuple_hash[0-num-key] = set([(num, key)])
            single_set.add(num)#  = True

        # print ans
        return [list(i) for i in ans]
        
