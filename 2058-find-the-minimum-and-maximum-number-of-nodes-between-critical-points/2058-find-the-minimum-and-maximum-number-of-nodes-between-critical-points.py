from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_idx = -1
        prev_idx = -1
        prev_val = head.val
        node = head.next
        idx = 1

        min_dist = float('inf')
        max_dist = -1

        while node.next:
            is_max = node.val > prev_val and node.val > node.next.val
            is_min = node.val < prev_val and node.val < node.next.val
            if is_max or is_min:
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - prev_idx)
                if prev_idx != -1:
                    max_dist = max(max_dist, idx - first_idx)
                prev_idx = idx
            prev_val = node.val
            node = node.next
            idx += 1

        if prev_idx == first_idx:
            return [-1, -1]

        return [min_dist, max_dist]