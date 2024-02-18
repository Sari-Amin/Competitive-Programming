class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot = 1
        zero = 0
        for i in nums:
            if i != 0:
                tot *= i
            else:
                zero += 1
        ans = []
        for i in nums:
            if i != 0:
                if zero > 0:
                    ans.append(0)
                else:
                    ans.append(tot//i)
            else:
                if zero > 1:
                    ans.append(0)
                else:
                    ans.append(tot)
        return ans 