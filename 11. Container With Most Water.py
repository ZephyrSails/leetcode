class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        ans = j * min([height[i], height[j]])
        print ans
        hi = height[i]
        hj = height[j]
        while i <= j:
            if height[i] < height[j]:
                while height[i] <= hi and i <= j:
                    i += 1
                ans = max([ans, min([height[i], height[j]]) * (j-i)])
                hi = height[i]
                # print i, j, height[i], height[j], ans
            else:
                while height[j] <= hj and i <= j:
                    j -= 1
                ans = max([ans, min([height[i], height[j]]) * (j-i)])
                hj = height[j]
                # print i, j, height[i], height[j], ans
        return ans
        # le = len(height)
        # ans = 0
        # i = 0
        # j = le - 1
        # ans = (j - i)*min(height[i], height[j])

        # recordi = height[i]
        # recordj = height[j]
        # while i < j:
        #     if recordi < recordj:
        #         while i < j and height[i] <= recordi:
        #             i = i + 1

        #         anst = (j - i)*min(height[i], height[j])
        #         recordi = height[i]
        #         if ans < anst:
        #             ans = anst
        #     else:
        #         while i < j and height[j] <= recordj:
        #             j = j - 1

        #         anst = (j - i)*min(height[i], height[j])
        #         recordj = height[j]
        #         if ans < anst:
        #             ans = anst

        # return ans

    # def getArea(self, i, j, height):
    #     return (j - i) * min([height[i], height[j]])
