class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        freq = Counter(candidates)
        unique = list(freq.keys())
        unique.sort()
        ans = []
        def backtrack(index, path = [], sm = 0):
            if sm == target:
                ans.append(path[:])
                return 

            if sm > target:
                return

            for i in range(index, len(unique)):
                if unique[i] in freq:
                    path.append(unique[i])
                    sm += unique[i]
                    freq[unique[i]] -= 1
                    if freq[unique[i]] > 0:
                        backtrack(i, path, sm)
                    else:
                        backtrack(i + 1, path, sm)
                    sm -= unique[i]
                    path.pop()
                    freq[unique[i]] += 1


        backtrack(0)
        
        return ans
