class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in nums:
            if i % 2:
                odd.append(i)
            else:
                even.append(i)
        ans = []
        for i in range(len(nums)//2):
            ans.append(even[i])
            ans.append(odd[i])
        return ans
