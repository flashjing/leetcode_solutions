class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
# --------------------------- METHOD 1 ---------------------------
	# Use dictionary to keep track of how many time each number appears
	# Memory Used: 16.7 MB
	# Runtime: 132 ms

		# num_dict = {num: 0 for num in nums}
		#
		# for num in nums:
		#     num_dict[num] += 1
		#
		# for num in nums:
		#     if num_dict[num]==1:
		#         return num


# --------------------------- METHOD 2 ---------------------------
	# Use set to store numbers seen once, remove from set when seen twice. 
	# This method only works since you know you are going to see other numbers twice.
	# Memory Used: 16.7 MB
	# Runtime: 140 ms

		# seen = set()
		# for num in nums:
		#     if num in seen:
		#         seen.remove(num)
		#     else:
		#         seen.add(num)
		# return list(seen)[0]


# --------------------------- METHOD 3 ---------------------------
	# Use built-in list.count() method
	# Memory Used: 16.5 MB
	# Runtime: >5 seconds

        for num in nums:
            if nums.count(num) == 1:
                return num