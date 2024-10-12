class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        freq = [[] for i in range(len(words) + 1)]

        for c in words:
            count[c] = 1 + count.get(c, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        for c in freq:
            c.sort()

        res = []

        for i in range(len(freq) -1, 0, -1):
            for word in freq[i]:
                res.append(word)
                if len(res) == k:
                    return res
        
