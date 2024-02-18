class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        number_of_zeros = 0
        for num in nums:
            if num == 0:
                number_of_zeros += 1
            else:
                total_product *= num

        if number_of_zeros > 1:
            return [0] * len(nums)
        ans = []
        for i in range(len(nums)):
            if nums[i] == 0:
                ans.append(total_product)
            else:
                if number_of_zeros:
                    ans.append(0)
                else:
                    ans.append(total_product // nums[i])
        
        return ans
