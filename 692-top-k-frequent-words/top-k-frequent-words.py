class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count ={}
        freq = [[] for i in range(len(words) + 1)]

        for n in words:
            count[n] = 1 + count.get(n, 0)
        
        for n,c in count.items():
            freq[c].append(n)
        
        for c in freq:
            c.sort()
            
        res = []
        
        for i in range(len(freq) - 1, 0, -1):
            for c in freq[i]:
                res.append(c)
                if len(res) == k:
                    return res
