class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        count = 0
        prev = 0
        for c in s:
            count += dic[c]
            if dic[c] > prev:
                count -= prev * 2
            prev = dic[c]

        return count
            
