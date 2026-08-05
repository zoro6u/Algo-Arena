class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # phase 1: adjacency list of outgoing calls
        graph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)

        # phase 2: iterative DFS from k (recursion would overflow at n = 1e5)
        suspicious = [False] * n
        suspicious[k] = True
        stack = [k]
        while stack:
            node = stack.pop()
            for nxt in graph[node]:
                if not suspicious[nxt]:       # mark on push => never queued twice
                    suspicious[nxt] = True
                    stack.append(nxt)

        # phase 3: any clean method calling into the group makes removal illegal
        for a, b in invocations:
            if not suspicious[a] and suspicious[b]:
                return list(range(n))         # all-or-nothing => keep everything

        return [i for i in range(n) if not suspicious[i]]