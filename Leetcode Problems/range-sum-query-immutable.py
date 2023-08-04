class NumArray:
    def __init__(self, nums: List[int]):
        self.presum = [0]
        self.presum.append(nums[0])
        for i in range(2,len(nums)+1):
            self.presum.append(self.presum[i-1] + nums[i-1])
        print(self.presum)
    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right+1] - self.presum[left]
