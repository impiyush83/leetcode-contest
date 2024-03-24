class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        class TrieNode:
            def __init__(self):
                self.keys = {}
                self.items = []
        
        trie = TrieNode() 
        all_items = []
        for i in range(len(wordsContainer)):
            index = i 
            leni = len(wordsContainer[index])
            item = (leni, index)
            all_items.append(item)
            word = wordsContainer[i][::-1]
            t = trie
            for ch in word:
                if ch not in t.keys:
                    t.keys[ch] = TrieNode()
                t = t.keys[ch]
                t.items.append(item)
        
        t = trie
       
        ans = []
        for i in range(len(wordsQuery)):
            t = trie
            word = wordsQuery[i]
            for ch in word[::-1]:
                if ch in t.keys:
                    t = t.keys[ch]
                else:
                    break
                    
            items = t.items
            if not items:
                items = sorted(all_items, key = lambda x: x[0])
            else:
                items = sorted(items, key = lambda x: x[0])
            ans.append(items[0][1])
        return ans 