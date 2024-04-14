# 3097. Shortest Subarray With OR at Least K II
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an array nums of non-negative integers and an integer k.

# An array is called special if the bitwise OR of all of its elements is at least k.

# Return the length of the shortest special non-empty 
# subarray
#  of nums, or return -1 if no special subarray exists.

 

# Example 1:

# Input: nums = [1,2,3], k = 2

# Output: 1

# Explanation:

# The subarray [3] has OR value of 3. Hence, we return 1.

# Example 2:

# Input: nums = [2,1,8], k = 10

# Output: 3

# Explanation:

# The subarray [2,1,8] has OR value of 11. Hence, we return 3.

# Example 3:

# Input: nums = [1,2], k = 0

# Output: 1

# Explanation:

# The subarray [1] has OR value of 1. Hence, we return 1.

 

# Constraints:

# 1 <= nums.length <= 2 * 105
# 0 <= nums[i] <= 109
# 0 <= k <= 109


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        ans = float("inf")
        bits = [0 for i in range(32)]

        def freq_to_int(bits):
            a = ''
            for i in bits[::-1]:
                if i > 0:
                    a += '1'
                else:
                    a += '0'
            return int(''.join(a), base=2)

        for right in range(len(nums)):
            new_bit = bin(nums[right]).split('b')[1][::-1]
            for bit_index in range(len(new_bit)):
                if new_bit[bit_index] == '1':
                    bits[bit_index] += 1
            

            while left <= right and freq_to_int(bits) >= k:
                ans = min(ans, right - left + 1)
                new_bit = bin(nums[left]).split('b')[1][::-1]
                for bit_index in range(len(new_bit)):
                    if new_bit[bit_index] == '1':
                        bits[bit_index] -= 1
                left += 1
        
        return ans if ans != float("inf") else -1 
