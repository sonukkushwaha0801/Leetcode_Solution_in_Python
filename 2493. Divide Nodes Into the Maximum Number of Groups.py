# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Create the graph
        map = defaultdict(list)
        for a, b in edges:
            map[a].append(b)
            map[b].append(a)

        groups = {}
        group_count = 0
        result = defaultdict(int)

        level = [0] * (n + 1)
        
        for node in range(1, n + 1):
            new_group = node not in groups
            group_count += new_group
            res = 0
            q = deque([node])
            visited = { node }
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    if new_group:
                        level[cur] = res
                        groups[cur] = group_count

                    for nxt in map[cur]:
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)
                        elif new_group and level[cur] - level[nxt] == 0:
                            return -1
                res += 1
            result[groups[node]] = max(result[groups[node]], res)
        return sum(result.values())