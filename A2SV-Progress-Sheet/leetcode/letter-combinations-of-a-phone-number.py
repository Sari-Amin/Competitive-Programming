class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        ans = []

        dic = {2:"abc", 3: "def", 4:"ghi", 5:"jkl", 6: "mno", 7:"pqrs", 8:"tuv", 9 : "wxyz"}

        def backtrack(index, path = []):
            if len(path) == len(digits) and path:
                ans.append("".join(path[:]))
                return

            for i in range(index, len(digits)):
                for j in dic[int(digits[i])]:
                    path.append(j)
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0)
        print(ans)
        return ans
                