class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        path = [''] * (2 * n)

        def backtrack(i, open_c, close_c):
            if i == 2 * n:
                res.append(''.join(path))
                return
            if open_c < n:
                path[i] = '('
                backtrack(i + 1, open_c + 1, close_c)
            if close_c < open_c:
                path[i] = ')'
                backtrack(i + 1, open_c, close_c + 1)

        backtrack(0, 0, 0)
        return res