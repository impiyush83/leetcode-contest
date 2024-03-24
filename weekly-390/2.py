class Solution:
    def minOperations(self, temp: int) -> int:
        if temp == 1:
            return 0
        k = temp
        ans = float("inf")
        while k > 1:
            multiple = temp / k
            intmultiple = int(multiple)
            remmultiple = multiple - intmultiple
            if remmultiple:
                intmultiple += 1
           
            ans = min(ans, k - 1 + intmultiple - 1)
            k -= 1
        return ans 