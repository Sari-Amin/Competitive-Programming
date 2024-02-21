class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        wall = set()
        guard = set()
        visit = set()
        for i in range(len(walls)):
            wall.add((walls[i][0], walls[i][1]))
        for i in range(len(guards)):
            guard.add((guards[i][0], guards[i][1]))
        for i in range(len(guards)):
            r = guards[i][0]
            c = guards[i][1]

            # north
            rr = r
            cc = c
            while rr > 0 and (rr - 1, cc) not in wall and (rr - 1, cc) not in guard:
                if (rr - 1, cc) not in visit:
                    visit.add((rr - 1,cc))
                rr -= 1
            # south
            rr = r
            cc = c
            while rr < m - 1 and (rr + 1, cc) not in wall and (rr + 1, cc) not in guard:
                if (rr + 1, cc) not in visit:
                    visit.add((rr + 1,cc))
                rr += 1
            # east
            rr = r
            cc = c
            while cc < n - 1 and (rr, cc + 1) not in wall and (rr, cc + 1) not in guard:
                if (rr, cc + 1) not in visit:
                    visit.add((rr,cc + 1))
                cc += 1
            # west
            rr = r
            cc = c
            while cc > 0 and (rr, cc - 1) not in wall and (rr, cc - 1) not in guard:
                if (rr, cc - 1) not in visit:
                    visit.add((rr,cc - 1))
                cc -= 1


        return m * n - len(visit) - len(guard) - len(wall)
