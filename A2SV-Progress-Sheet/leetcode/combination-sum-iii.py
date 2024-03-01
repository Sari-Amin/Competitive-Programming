class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def combination(num, path = [], sum_ = 0):
            if len(path) > k:
                return
            if sum_ == n and len(path) == k:
                ans.append(path[:])
                return
            
            for i in range(num, min(n + 1, 10)):
                path.append(i)
                sum_ += i
                combination(i+1, path, sum_)
                path.pop()
                sum_ -= i
        combination(1)
        return ans