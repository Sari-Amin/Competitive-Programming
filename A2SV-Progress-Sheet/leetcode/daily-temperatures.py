class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for i in range(len(temperatures))]
        st = []
        for i in range(len(temperatures) - 1, -1, -1):
            while len(st) > 0 and temperatures[i] >= st[-1][1]:
                st.pop()
            if len(st) != 0:
                ans[i] = st[-1][0] - i
            st.append((i, temperatures[i]))
        return ans