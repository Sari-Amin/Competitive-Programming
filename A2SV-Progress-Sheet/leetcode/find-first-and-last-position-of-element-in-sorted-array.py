class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(leftBias, left = 0, right = len(nums) - 1):
            index = -1
            while left <= right:
                 
                mid = left + (right - left) // 2
              
                if nums[mid] == target:
                    index = mid
                    if leftBias:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return index

        return [binarySearch(True), binarySearch(False)]
 