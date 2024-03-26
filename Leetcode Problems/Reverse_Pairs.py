class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        ans = 0 
        def merge(left_hand, right_hand):
            nonlocal ans

            #count the pairs
            left = 0
            right = 0
            while left < len(left_hand) and right < len(right_hand):
                if left_hand[left] > 2 * right_hand[right]:
                    ans += len(left_hand) - left
                    right += 1
                else:
                    left += 1

            #merge by sorting
            left = right = 0
            res = []
            while left < len(left_hand) or right < len(right_hand):
                if right == len(right_hand) or left < len(left_hand) and left_hand[left] <= right_hand[right]:
                    res.append(left_hand[left])
                    left += 1
                else:
                    res.append(right_hand[right])
                    right += 1
            
            return res


        def mergeSort(left, right, arr):
            if left >= right:
                return [arr[left]]

            mid = left + (right - left) // 2

            left_hand = mergeSort(left, mid, arr)
            right_hand = mergeSort(mid + 1, right, arr)

            return merge(left_hand, right_hand)

        temp = mergeSort(0, len(nums) - 1, nums)

        return ans
