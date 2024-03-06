"""

3072. Distribute Elements Into Two Arrays II
User Accepted:1869
User Tried:6356
Total Accepted:2017
Total Submissions:16078
Difficulty:Hard
You are given a 1-indexed array of integers nums of length n.

We define a function greaterCount such that greaterCount(arr, val) returns the number of elements in arr that are strictly greater than val.

You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums[1] to arr1. In the second operation, append nums[2] to arr2. Afterwards, in the ith operation:

If greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i]), append nums[i] to arr1.
If greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i]), append nums[i] to arr2.
If greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i]), append nums[i] to the array with a lesser number of elements.
If there is still a tie, append nums[i] to arr1.
The array result is formed by concatenating the arrays arr1 and arr2. For example, if arr1 == [1,2,3] and arr2 == [4,5,6], then result = [1,2,3,4,5,6].

Return the integer array result.

 

Example 1:

Input: nums = [2,1,3,3]
Output: [2,3,1,3]
Explanation: After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3rd operation, the number of elements greater than 3 is zero in both arrays. Also, the lengths are equal, hence, append nums[3] to arr1.
In the 4th operation, the number of elements greater than 3 is zero in both arrays. As the length of arr2 is lesser, hence, append nums[4] to arr2.
After 4 operations, arr1 = [2,3] and arr2 = [1,3].
Hence, the array result formed by concatenation is [2,3,1,3].


"""

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        from sortedcontainers import SortedList
        
        a = [nums[0]]
        b = [nums[1]]
        
        asort = SortedList()
        asort.add(nums[0])
        bsort = SortedList()
        bsort.add(nums[1])
        
        def greaterCount(arr, val):
            index = arr.bisect_right(val)
            return len(arr) - index
       
        
        for i in range(2, len(nums)):
            if  greaterCount(asort, nums[i]) > greaterCount(bsort, nums[i]):
                a.append(nums[i])
                asort.add(nums[i])
            elif greaterCount(asort, nums[i]) < greaterCount(bsort, nums[i]):
                b.append(nums[i])
                bsort.add(nums[i])
            elif len(a) > len(b):
                b.append(nums[i])
                bsort.add(nums[i])
            else:
                a.append(nums[i])
                asort.add(nums[i])
        a.extend(b) 
        return a 