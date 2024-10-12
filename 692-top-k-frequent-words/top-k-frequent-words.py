class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
                # Step 1: Count the frequency of each word
        count = Counter(words)
        
        # Step 2: Create buckets where index is the frequency, and each bucket contains a list of words
        max_freq = max(count.values())  # Find the maximum frequency
        buckets = [[] for _ in range(max_freq + 1)]  # Create frequency buckets
        
        for word, freq in count.items():
            buckets[freq].append(word)
        
        # Step 3: Sort the words inside each bucket lexicographically
        for i in range(len(buckets)):
            buckets[i].sort()
        
        # Step 4: Collect top k frequent words
        res = []
        for i in range(len(buckets) - 1, 0, -1):  # Start from the highest frequency
            for word in buckets[i]:
                res.append(word)
                if len(res) == k:
                    return res
        return res