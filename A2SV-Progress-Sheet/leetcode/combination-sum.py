class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(index, path = [], sm = 0):
            if sm == target:
                ans.append(path[:])
                return

            for i in range(index, len(candidates)):
                if sm + candidates[i] <= target:
                    path.append(candidates[i])
                    sm += candidates[i]
                    backtrack(i, path, sm)
                    sm -= candidates[i]
                    path.pop()

        backtrack(0)

        return ans