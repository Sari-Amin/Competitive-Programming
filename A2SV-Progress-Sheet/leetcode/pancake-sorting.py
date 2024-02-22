class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        sortedarr = sorted(arr)
        if arr == sortedarr:
            return ans
        r = len(arr)
        while arr != sortedarr:
            temp = arr.index(max(arr[:r])) + 1
            ans.append(temp)
            arr[:temp] = arr[:temp][::-1]
            arr[:r] = arr[:r][::-1]
            ans.append(r)
            r -= 1
        return ans