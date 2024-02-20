class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(s1,s2):
            if (s1 + s2) < (s2 + s1):
                return -1
            elif (s1 + s2) == (s2 + s1):
                return 0
            else:
                return 1
        return str(int("".join(sorted(map(str,nums), key = cmp_to_key(compare), reverse = True))))