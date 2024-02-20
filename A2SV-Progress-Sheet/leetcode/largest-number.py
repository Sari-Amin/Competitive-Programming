class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key = lambda x: x // 10 ** (len(str(x)) - 1), reverse = True)
        for i in range(len(nums) - 1):
            for j in range(i + 1,len(nums)):
                if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        

        return str(int("".join(map(str,nums))))