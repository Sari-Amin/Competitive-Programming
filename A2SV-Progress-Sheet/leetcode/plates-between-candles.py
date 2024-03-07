class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles  = []
        for i,v in enumerate(s):
            if v == "|":
                candles.append(i)
        ans = []
      
        for l,r in queries:
            x = bisect_left(candles,l)
            y = bisect_right(candles,r)-1
            if x<=y:
                ans.append(candles[y] - candles[x] - 1 - (y - x -1))
            else:
                ans.append(0)

        return ans