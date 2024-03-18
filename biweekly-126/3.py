# 3081. Replace Question Marks in String to Minimize Its Value
# User Accepted:3460
# User Tried:9071
# Total Accepted:3602
# Total Submissions:25216
# Difficulty:Medium
# You are given a string s. s[i] is either a lowercase English letter or '?'.

# For a string t having length m containing only lowercase English letters, we define the function cost(i) for an index i as the number of characters equal to t[i] that appeared before it, i.e. in the range [0, i - 1].

# The value of t is the sum of cost(i) for all indices i.

# For example, for the string t = "aab":

# cost(0) = 0
# cost(1) = 1
# cost(2) = 0
# Hence, the value of "aab" is 0 + 1 + 0 = 1.
# Your task is to replace all occurrences of '?' in s with any lowercase English letter so that the value of s is minimized.

# Return a string denoting the modified string with replaced occurrences of '?'. If there are multiple strings resulting in the minimum value, return the lexicographically smallest one.

 

# Example 1:

# Input:  s = "???" 

# Output:  "abc" 

# Explanation: In this example, we can replace the occurrences of '?' to make s equal to "abc".

# For "abc", cost(0) = 0, cost(1) = 0, and cost(2) = 0.

# The value of "abc" is 0.

# Some other modifications of s that have a value of 0 are "cba", "abz", and, "hey".

# Among all of them, we choose the lexicographically smallest.

# Example 2:

# Input: s = "a?a?"

# Output: "abac"

# Explanation: In this example, the occurrences of '?' can be replaced to make s equal to "abac".

# For "abac", cost(0) = 0, cost(1) = 0, cost(2) = 1, and cost(3) = 0.

# The value of "abac" is 1.

 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either a lowercase English letter or '?'.

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        from string import ascii_lowercase
        
        freq = defaultdict(int)
        h = []
        
        for c in s:
            if c != '?':
                freq[c] += 1
        
        z = [i for i in s]
        
        counter = Counter(s)
        q = [[counter[chr(ord('a')+i)], chr(ord('a')+i)] for i in range(26)]

        for c in ascii_lowercase:
            heapq.heappush(h, (freq[c], ord(c)))
        
        
        q = []
        
        for i in range(len(z)):
            if z[i] == '?':
                _, replacement = heapq.heappop(h)
              
                heapq.heappush(h, (_ + 1, replacement))
                q.append(chr(replacement))
        
        q.sort()
        index = 0
        for i in range(len(z)):
            if z[i] == '?':
                z[i] = q[index]
                index += 1
       
        return ''.join(z)
