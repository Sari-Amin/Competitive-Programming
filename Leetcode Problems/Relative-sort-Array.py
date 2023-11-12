class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for i in arr2:
            ans += [i] * arr1.count(i)
        ans1 = []
        for i in arr1:
            if i not in arr2:
                ans1.append(i)
        return ans + sorted(ans1)
