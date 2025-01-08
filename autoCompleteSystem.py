# Time:
# Space:
# Leetcode: No
# Issues: Prirority queue logic for max heap issue

from collections import defaultdict
import heapq
class AutocompleteSystem:

    class TrieNode:

        def __init__(self):
            self.children = {}
            self.startsWith = []  

    def __init__(self, sentences: List[str], times: List[int]):
        self.hmap = defaultdict(int)
        self.search = ""
        self.root = self.TrieNode()
        
        for i in range(len(sentences)):
            sentence = sentences[i]
            time = times[i]
            self.hmap[sentence] += time
            self.insert(sentence)
        
    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = self.TrieNode()
            curr = curr.children[c]
            curr.startsWith.append(word)

    def searchPrefix(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return []
            curr = curr.children[c]
        return curr.startsWith                
    

    def input(self, c: str) -> List[str]:
        if c == '#':
            if self.search not in self.hmap:
                self.insert(self.search)
      
            self.hmap[self.search] += 1
            self.search = ""
            # return []

            self.search += c
            lst = self.searchPrefix(self.search)              # list of candidates
            
            
            pq = []
            for sentence in lst:
                heapq.heappush(pq, sentence) #issue here
                if len(pq) >3:
                    heapq.heappop(pq)

            result = []
            while pq:
                result.append(heapq.heappop(pq))
            return result[::-1]

