class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        k = str(k)
        ans = []
        i,j = len(num)-1,len(k)-1
        while i >= 0 or j >= 0 or carry != 0:
            if i >= 0 :
                carry += num[i]
                i -= 1
            if j >= 0 :
                carry += int(k[j])
                j -= 1
            ans.append(carry % 10)
            carry //= 10
        return ans[::-1]
