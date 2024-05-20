class Solution(object):
    def groupAnagrams(self, strs):
        map = collections.defaultdict(list) #map chat count of each string(key) to list of anagrams (ensures that default value is 0 edge case if it doesnt exist)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord("a")] += 1
                
            map[tuple(count)].append(s) #for this count append string s
        return map.values()


        