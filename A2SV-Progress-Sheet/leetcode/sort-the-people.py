class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp = [(names[i], heights[i]) for i in range(len(names))]
        temp = sorted(temp, reverse =True, key = lambda x : x[1])
        return [i for i,j in temp]