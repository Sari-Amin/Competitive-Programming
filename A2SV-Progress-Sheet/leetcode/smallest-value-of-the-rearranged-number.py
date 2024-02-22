class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num < 0:
            ans = sorted(str(num)[1:], reverse = True)
            return -int("".join(ans))
        ans = sorted(str(num))
        l = 0
        while  l < len(ans) and ans[l] == "0":
            l += 1

        ans = [ans[l]] + ans[:l] + ans[l + 1:]
        return int("".join(ans))
