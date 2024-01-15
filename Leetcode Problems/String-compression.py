class Solution:
    def compress(self, chars: List[str]) -> int:
        temp = []
        cnt = 1 
        curr = chars[0]
        ans = 0
        for i in range(1,len(chars)):
            if curr == chars[i]:
                cnt += 1
            else:
                if cnt == 1:
                    temp.append(curr)
                    ans += 1
                else:
                    temp.append(curr)
                    ans += 1
                    if cnt >= 10:
                        temp.extend(list(str(cnt)))
                        ans += len(str(cnt))
                    else:
                        temp.append(str(cnt))
                        ans += 1
                cnt = 1
                curr = chars[i]
        if cnt == 1:
            temp.append(curr)
            ans += 1
        else:
            temp.append(curr)
            ans += 1
            if cnt >= 10:
                temp.extend(list(str(cnt)))
                ans += len(str(cnt))
            else:
                temp.append(str(cnt))
                ans += 1
        chars[:] = temp
        return ans
