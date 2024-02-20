class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr1) == len(arr2):
            return arr2
        dic = {}
        for i in range(len(arr2)):
            dic[arr2[i]] = i
        count = 0
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                count += 1
        arr1.sort(key= lambda x: dic.get(x, len(arr2)))
        return arr1[:-count] + sorted(arr1[-count:])