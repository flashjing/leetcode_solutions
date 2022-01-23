class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        n = sorted(set(nums))
        if not n:
            return None        
        if len(n) >= 3:
            return n[-3]
        else:
            return n[-1]