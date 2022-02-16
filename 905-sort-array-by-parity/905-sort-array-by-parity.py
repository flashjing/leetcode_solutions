class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # two pass
        return ([x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1])
    
    
    
        # nums.sort(key = lambda x: x%2)
        # return nums
    

    
    
    
#         n = len(nums)
#         i, j = 0, n - 1
        
#         while i < j:
#             while nums[i] % 2 == 0:
#                 i += 1
#             while nums[j] % 2 == 1:
#                 j -= 1
#             if i > j:
#                 break
#             else:
                