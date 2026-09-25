from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = [[[], {''}]]  # [union_parts, concat_set]

        for ch in expression:
            if ch == '{':
                stack.append([[], {''}])
            elif ch == '}':
                union_parts, concat_set = stack.pop()
                union_parts.append(concat_set)
                group_value = set()
                for part in union_parts:
                    group_value |= part
                stack[-1][1] = {a + b for a in stack[-1][1] for b in group_value}
            elif ch == ',':
                union_parts, concat_set = stack[-1]
                union_parts.append(concat_set)
                stack[-1][1] = {''}
            else:
                stack[-1][1] = {a + ch for a in stack[-1][1]}

        union_parts, concat_set = stack[-1]
        union_parts.append(concat_set)
        final_set = set()
        for part in union_parts:
            final_set |= part

        return sorted(final_set)