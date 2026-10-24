class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = [0]
        for d in days:
            prefix.append(prefix[-1] + d)          # days before each month

        def day_of_year(s: str) -> int:
            return prefix[int(s[:2]) - 1] + int(s[3:])

        start = max(day_of_year(arriveAlice), day_of_year(arriveBob))
        end = min(day_of_year(leaveAlice), day_of_year(leaveBob))
        return max(0, end - start + 1)