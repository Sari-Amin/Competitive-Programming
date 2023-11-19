class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        total = sum(nums)
        for j in range(len(queries)):
            lsum = 0
            temp = 0
            if queries[j] >= total:
                ans.append(len(nums))
                continue
            if queries[j] < nums[0]:
                ans.append(0)
                continue
            for i in range(len(nums)):
                lsum += nums[i]
                if lsum  <= queries[j]:
                    temp = max(temp,i+1)
            ans.append(temp)
        return ans
                
