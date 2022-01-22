class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [elem for elem in nums if elem != val]
        return
        
#         if not nums:
#             return nums
        
#         slow = fast = 0
        
#         while fast < len(nums):
#             if nums[fast] != val:
#                 nums[slow] = nums[fast]
#                 slow += 1
#                 fast += 1
            
#             fast += 1
        
#         return nums