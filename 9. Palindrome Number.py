import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        if x < 100:
            return True if x/10 == x%10 else False
        if x % 10 == 0:
            return False

        i = x % 10
        x = x / 10
        while i < x:
            i = i*10 + x%10
            x /= 10

        if i > x:
            i /= 10

        return True if i == x else False
