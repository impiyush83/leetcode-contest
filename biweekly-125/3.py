"""
3067. Count Pairs of Connectable Servers in a Weighted Tree Network

User Accepted:3746
User Tried:4864
Total Accepted:3965
Total Submissions:7834
Difficulty:Medium

You are given an unrooted weighted tree with n vertices representing servers numbered from 0 to n - 1, an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional edge between vertices ai and bi of weight weighti. You are also given an integer signalSpeed.

Two servers a and b are connectable through a server c if:

a < b, a != c and b != c.
The distance from c to a is divisible by signalSpeed.
The distance from c to b is divisible by signalSpeed.
The path from c to b and the path from c to a do not share any edges.
Return an integer array count of length n where count[i] is the number of server pairs that are connectable through the server i.

"""
from collections import defaultdict

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], ss:int) -> List[int]:

        
        graph = defaultdict(list)
        for edge in edges:
            u, v, w = edge
            graph[u].append((v, w))
            graph[v].append((u, w))

        n = len(edges) + 1
        
        x = defaultdict(list)
        
        def recurse(node):
            count = 0
            
            def recurse1(n1,parent, sumi):
               
                nonlocal count 
                if sumi % ss == 0:
                    count += 1
                for e, w in graph[n1]:
                    if e != parent:
                        recurse1(e, n1, sumi + w)

            
            ans = []
            # precompute all subtrees for i node

            f = 0
            for e, w in graph[node]:
                count = 0 
                recurse1(e, node, w)
                ans.append(count)
                
            current = 0
            # accumulation
            for a in ans:
                f += current * a 
                current += a
            return f 

        for i in range(n):
            yield recurse(i)