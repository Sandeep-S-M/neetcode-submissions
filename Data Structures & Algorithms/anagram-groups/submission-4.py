class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            pre_data = [0]*26
            for ch in s:
                pre_data[ord(ch) - ord('a')] += 1 
            result[tuple(pre_data)].append(s)
        return list(result.values())
            

