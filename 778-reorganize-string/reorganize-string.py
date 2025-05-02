class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, chr] for chr, cnt in count.items()]

        heapq.heapify(maxHeap)

        prev = None
        res = ""

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, chr = heapq.heappop(maxHeap)
            res += chr
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, chr]
            
        return res