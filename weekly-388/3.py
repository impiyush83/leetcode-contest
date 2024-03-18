# 3076. Shortest Uncommon Substring in an Array
# User Accepted:7958
# User Tried:9941
# Total Accepted:8504
# Total Submissions:21402
# Difficulty:Medium
# You are given an array arr of size n consisting of non-empty strings.

# Find a string array answer of size n such that:

# answer[i] is the shortest substring of arr[i] that does not occur as a substring in any other string in arr. If multiple such substrings exist, answer[i] should be the lexicographically smallest. And if no such substring exists, answer[i] should be an empty string.
# Return the array answer.

 

# Example 1:

# Input: arr = ["cab","ad","bad","c"]
# Output: ["ab","","ba",""]
# Explanation: We have the following:
# - For the string "cab", the shortest substring that does not occur in any other string is either "ca" or "ab", we choose the lexicographically smaller substring, which is "ab".
# - For the string "ad", there is no substring that does not occur in any other string.
# - For the string "bad", the shortest substring that does not occur in any other string is "ba".
# - For the string "c", there is no substring that does not occur in any other string.
# Example 2:

# Input: arr = ["abc","bcd","abcd"]
# Output: ["","","abcd"]
# Explanation: We have the following:
# - For the string "abc", there is no substring that does not occur in any other string.
# - For the string "bcd", there is no substring that does not occur in any other string.
# - For the string "abcd", the shortest substring that does not occur in any other string is "abcd".
 

# Constraints:

# n == arr.length
# 2 <= n <= 100
# 1 <= arr[i].length <= 20
# arr[i] consists only of lowercase English letters.


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        x = {}
       
        for i in range(len(arr)):     
            y = {}
            for j in range(len(arr[i])):
                for k in range(j + 1, len(arr[i]) + 1):
                    if (k - j) in y:
                        y[k - j].append(arr[i][j:k])
                    else:
                        y[k - j] = [arr[i][j:k]]
                        
            if not y:
                continue
            maxi = max(y.keys())
            merged = []
            for j in range(1, maxi + 1):
                merged.extend(sorted(y[j]))
            x[i] = merged
        
        ans = []
        
        
        
        for i in range(len(arr)):
            default = ""
       
            for substring in x[i]:
                present = False
                for j in range(len(arr)):
                    if j != i:
                        
                        if substring in arr[j]:
                            present = True
                            break

                if not present:
                    default = substring 
                    break

            ans.append(default)
        return ans 
                    
                           
                