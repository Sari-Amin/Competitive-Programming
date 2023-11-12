class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in nums:
            if i % 2:
                odd.append(i)
            else:
                even.append(i)
        turn = True
        o,e=0,0
        for i in range(len(nums)):
            if turn:
                nums[i] = even[e]
                e += 1
            else:
                nums[i] = odd[o]
                o += 1
            turn = not turn
        return nums
