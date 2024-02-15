class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        st = []
        for i in s:
            if i == ")":
                if len(st) > 0:
                    st.pop()
                else:
                    ans += 1
            else:
                st.append(i)
                
        return ans + len(st)