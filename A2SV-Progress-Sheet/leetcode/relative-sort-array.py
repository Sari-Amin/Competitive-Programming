class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        for i in range(len(arr2)):
            dic[arr2[i]] = i

        arr1.sort(key= lambda x: dic.get(x, x + len(arr2)))
        
        return arr1