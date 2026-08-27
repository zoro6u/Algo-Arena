class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        pool = [0] * 26
        for ch in s:
            pool[ord(ch) - 97] += 1

        matched = []

        i = 0
        while i < n:
            c = ord(target[i]) - 97
            if pool[c] > 0:
                pool[c] -= 1
                matched.append(c)
                i += 1
            else:
                break

        while True:
            if i < n:
                target_c = ord(target[i]) - 97
                chosen = -1
                for c in range(target_c + 1, 26):
                    if pool[c] > 0:
                        chosen = c
                        break
                if chosen != -1:
                    pool[chosen] -= 1
                    result_prefix = [chr(97 + x) for x in matched] + [chr(97 + chosen)]
                    suffix = []
                    for c in range(26):
                        suffix.extend([chr(97 + c)] * pool[c])
                    return ''.join(result_prefix) + ''.join(suffix)

            if not matched:
                return ""
            last = matched.pop()
            pool[last] += 1
            i -= 1
            