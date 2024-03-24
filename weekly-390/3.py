class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        import heapq 

        h = []
        ans = []
        x = defaultdict(int)
        
        for i in range(len(nums)):
            identity = nums[i]
            count = freq[i]
            
            x[identity] += count
            
            while h:
                if x[h[0][1]] != - h[0][0]:
                    heapq.heappop(h)
                else:
                    break
            
            heapq.heappush(h, (-x[identity], identity))
            
            z = 0
            if h:
                z = - h[0][0]
           
            ans.append(z)
        return ans 