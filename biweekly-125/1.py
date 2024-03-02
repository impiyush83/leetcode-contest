"""
3065. Minimum Operations to Exceed Threshold Value I

User Accepted:22485
User Tried:23044
Total Accepted:24663
Total Submissions:30016
Difficulty:Easy


You are given a 0-indexed integer array nums, and an integer k.

In one operation, you can remove one occurrence of the smallest element of nums.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.

"""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        import heapq 
        
        h = []

        for num in nums:
            heapq.heappush(h, num)
        
        count = 0
        while h:
            if h[0] < k:
                heapq.heappop(h)
                count += 1
            else:
                break
                
        return count 