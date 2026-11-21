class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        nearest = [{} for _ in range(n)]
        new_parent = [-1] * n

        def dfs(node, ancestors):
            ch = s[node]
            new_parent[node] = ancestors.get(ch, parent[node])

            old = ancestors.get(ch)
            ancestors[ch] = node

            for child in children[node]:
                dfs(child, ancestors)

            if old is None:
                ancestors.pop(ch, None)
            else:
                ancestors[ch] = old

        dfs(0, {})

        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        answer = [1] * n

        def calculate(node):
            for child in new_children[node]:
                answer[node] += calculate(child)
            return answer[node]

        calculate(0)
        return answer