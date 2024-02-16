class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dic = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        for i in s:
            if i in "([{":
                st.append(i)
            elif len(st) > 0:
                if dic[st[-1]] == i:
                    st.pop()
                else:
                    return False
            else:
                return False

        if len(st) == 0:
            return True
        else:
            return False