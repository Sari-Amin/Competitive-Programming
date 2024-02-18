class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        increasing, decreasing, n = 0, len(arr) - 1, len(arr)
        while increasing + 1 < n and arr[increasing] < arr[increasing + 1]:
            increasing += 1
        while decreasing > 0 and arr[decreasing - 1] > arr[decreasing]: 
            decreasing -= 1
        return  0 < increasing == decreasing < n - 1