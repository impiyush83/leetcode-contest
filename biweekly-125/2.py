"""
3066. Minimum Operations to Exceed Threshold Value II

User Accepted:14797
User Tried:19780
Total Accepted:15662
Total Submissions:69391
Difficulty:Medium


You are given a 0-indexed integer array nums, and an integer k.

In one operation, you will:

Take the two smallest integers x and y in nums.
Remove x and y from nums.
Add min(x, y) * 2 + max(x, y) anywhere in the array.
Note that you can only apply the described operation if nums contains at least two elements.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k

"""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        import heapq 
        
        h = []

        for num in nums:
            heapq.heappush(h, num)
        
        count = 0
        while h and len(h) >= 2:
            x = heapq.heappop(h)
            y = heapq.heappop(h)
            if x >= k:
                break
            heapq.heappush(h, min(x, y) * 2 + max(x, y))
            count += 1
        return count 