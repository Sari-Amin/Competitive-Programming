class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = nums.count(1)
        zeros = len(nums) - ones
        lsum = 0
        res = []

        for i in range(len(nums)):
            res.append((ones + lsum, i))
            if nums[i] == 0:
                lsum += 1
            else:
                ones -= 1
        res.append((ones + lsum, i + 1))
        res.sort(reverse = True)
        
        ans = [res[0][1]]
        for i in range(1,len(res)):
            if res[0][0] == res[i][0]:
                ans.append(res[i][1])
            else:
                break

        return ans