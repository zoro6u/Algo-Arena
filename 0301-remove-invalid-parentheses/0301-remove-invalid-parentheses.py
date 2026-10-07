from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left_rem = right_rem = 0
        for ch in s:
            if ch == '(':
                left_rem += 1
            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        n = len(s)
        result = []
        path = []

        def dfs(i, open_count, left_rem, right_rem, prev_removed):
            if n - i < left_rem + right_rem:
                return
            if i == n:
                if left_rem == 0 and right_rem == 0 and open_count == 0:
                    result.append(''.join(path))
                return
            ch = s[i]

            if ch == '(' or ch == ')':
                can_remove = (i == 0 or s[i - 1] != ch or prev_removed)
                if can_remove:
                    if ch == '(' and left_rem > 0:
                        dfs(i + 1, open_count, left_rem - 1, right_rem, True)
                    elif ch == ')' and right_rem > 0:
                        dfs(i + 1, open_count, left_rem, right_rem - 1, True)

            if ch == '(':
                path.append(ch)
                dfs(i + 1, open_count + 1, left_rem, right_rem, False)
                path.pop()
            elif ch == ')':
                if open_count > 0:
                    path.append(ch)
                    dfs(i + 1, open_count - 1, left_rem, right_rem, False)
                    path.pop()
            else:
                path.append(ch)
                dfs(i + 1, open_count, left_rem, right_rem, False)
                path.pop()

        dfs(0, 0, left_rem, right_rem, False)
        return result