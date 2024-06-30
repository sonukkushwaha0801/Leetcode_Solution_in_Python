# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        def find(x, parent):
            if parent[x] != x:
                parent[x] = find(parent[x], parent)
            return parent[x]

        def union(x, y, parent):
            parent[find(x, parent)] = find(y, parent)

        dsu1 = list(range(n + 1))
        dsu2 = list(range(n + 1))
        count = 0
        edges.sort(key=lambda x: x[0], reverse=True)

        for edge in edges:
            if edge[0] == 3:
                if find(edge[1], dsu1) == find(edge[2], dsu1) and find(edge[1], dsu2) == find(edge[2], dsu2):
                    count += 1
                    continue

                union(edge[1], edge[2], dsu1)
                union(edge[1], edge[2], dsu2)
            elif edge[0] == 1:
                if find(edge[1], dsu1) == find(edge[2], dsu1):
                    count += 1

                union(edge[1], edge[2], dsu1)
            else:
                if find(edge[1], dsu2) == find(edge[2], dsu2):
                    count += 1

                union(edge[1], edge[2], dsu2)

        for i in range(1, n + 1):
            find(i, dsu1)
            find(i, dsu2)

        for i in range(2, n + 1):
            if dsu1[i] != dsu1[1] or dsu2[i] != dsu2[1]:
                return -1

        return count