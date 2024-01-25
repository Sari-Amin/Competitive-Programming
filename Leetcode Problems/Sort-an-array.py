#https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, low, mid, right):
            temp = []
            l = low
            r = mid + 1
            while l <= mid and r <= right:
                if nums[l] <= nums[r]:
                    temp.append(nums[l])
                    l += 1
                else:
                    temp.append(nums[r])
                    r += 1
            while l <= mid:
                temp.append(nums[l])
                l += 1
            while r <= right:
                temp.append(nums[r])
                r += 1
            nums[low:right + 1] = temp

            
        def mergesort(nums, low, right):
            if low == right:
                return

            mid = (low + right)//2
            mergesort(nums, low, mid)
            mergesort(nums, mid + 1, right)
            merge(nums, low, mid, right)


        mergesort(nums, 0, len(nums) - 1)
        return nums
