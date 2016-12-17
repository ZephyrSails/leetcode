class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1 and not edges: return [0]

        neighbour = {i: set() for i in xrange(n)}

        for v, w in edges:
            neighbour[v].add(w)
            neighbour[w].add(v)

        queue = collections.deque()

        for v in xrange(n):
            if len(neighbour[v]) == 1:
                queue.append((v, 0))

        curDepth = 0
        depthDel = []
        while queue:
            v, depth = queue.popleft()
            if depth != curDepth:
                curDepth = depth
                depthDel = []

            if len(neighbour[v]) == 1:
                w = neighbour[v].pop()
                neighbour[w].remove(v)
                if len(neighbour[w]) == 1:
                    queue.append((w, depth + 1))

            del neighbour[v]
            depthDel.append(v)

        return depthDel

    #     8
    #     |
    #     0 9
    #     |/
    #     1
    #   / \
    #   2   3
    #  / \  |\
    # 4   5 6 7

    #     |
    #     0
    #     |/
    #     1
    #   / \
    #   2   3
    #  / \  |\

    #     |
    #     1
    #   / \
    #   2   3
    #  / \  |\

         
