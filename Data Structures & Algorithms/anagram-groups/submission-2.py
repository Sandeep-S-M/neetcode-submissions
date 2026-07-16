class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            alpha = [0]*26
            for char in s:
                alpha[ord(char) - ord('a')] += 1
            result[tuple(alpha)].append(s)
        return list(result.values())

   

        #groups = defaultdict(list)
        #for s in strs:
        #    key = ''.join(sorted(s))
        #    groups[key].append(s)
        #return list(groups.values())
  