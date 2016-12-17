class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''

        longestPrefix = strs[0]

        def longestCommonPrefix(s1, s2):
            if len(s1) > len(s2):
                s1, s2 = s2, s1

            for i in xrange(len(s1)):
                if s1[i] != s2[i]:
                    return s1[:i]

            return s1


        for s in strs[1:]:
            if longestPrefix != s[:len(longestPrefix)]:
                longestPrefix = longestCommonPrefix(s, longestPrefix)

        return longestPrefix
