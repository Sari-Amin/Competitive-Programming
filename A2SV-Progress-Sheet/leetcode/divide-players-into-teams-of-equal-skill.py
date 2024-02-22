class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,r=1,len(skill)-2
        team1, team2 = 0,0
        curr = skill[0] + skill[-1]
        ans = skill[0] * skill[-1]
        while l < r:
            if ans == -1:
                break
            elif curr == skill[l] + skill[r]:
                ans += (skill[l] * skill[r])
            else:
                ans = -1
            r -= 1
            l += 1
        return ans