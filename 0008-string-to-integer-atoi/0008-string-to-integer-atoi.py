class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX =  2**31 - 1   #  2147483647
        INT_MIN = -2**31       # -2147483648
        i, n = 0, len(s)

        # step 1 — skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # step 2 — read optional sign
        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        # step 3 — read digits with pre-multiply overflow guard
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # check BEFORE combining — can't let result temporarily exceed 32-bit
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result