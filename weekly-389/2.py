# 3084. Count Substrings Starting and Ending with Given Character
# User Accepted:16609
# User Tried:18950
# Total Accepted:17418
# Total Submissions:40856
# Difficulty:Medium
# You are given a string s and a character c. Return the total number of substrings of s that start and end with c.

 

# Example 1:

# Input: s = "abada", c = "a"

# Output: 6

# Explanation: Substrings starting and ending with "a" are: "abada", "abada", "abada", "abada", "abada", "abada".

# Example 2:

# Input: s = "zzz", c = "z"

# Output: 6

# Explanation: There are a total of 6 substrings in s and all start and end with "z".

 

# Constraints:

# 1 <= s.length <= 105
# s and c consist only of lowercase English letters.


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        pe = defaultdict(int)
        count = 0
        for i in s:
            if i == c:
                count += 1
                count += pe[i]
            pe[i] += 1
        return count 