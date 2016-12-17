class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        groups = collections.defaultdict(set)

        for x, y in points:
            groups[y].add(x)

        median = None
        for y in groups.keys():
            group = list(groups[y])
            group.sort()

            i, j = 0, len(group) - 1

            while i <= j:
                m = (group[i] + group[j]) / 2.0
                if median == None:
                    median = m
                elif median != m:
                    return False
                i += 1
                j -= 1

        return True
        
