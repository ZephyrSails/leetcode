class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []

        dials = [[' '], ['*'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        def getCombinations(dials, digits, i):
            if not digits or i == len(digits): return ['']

            rests = getCombinations(dials, digits, i+1)

            return [char + rest for rest in rests for char in dials[int(digits[i])]]

        return getCombinations(dials, digits, 0)
