class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        ans = 0 
        for i in dic:
            if dic[i] % 3 == 0:
                ans += dic[i] // 3
            elif dic[i] != 1 and (dic[i] % 3) % 2 == 1:
                ans += dic[i] // 3
                ans -= 1
                ans += (dic[i] % 3 + 3) // 2
            elif (dic[i] % 3) % 2 == 0:
                ans += dic[i] // 3
                ans += (dic[i] % 3) // 2
            else:
                return -1
        return ans
