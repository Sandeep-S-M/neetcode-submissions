class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hash_map = {}
        res = 0 
        for r in range(len(s)):
            hash_map[s[r]] = hash_map.get(s[r],0)+1

            while (r-l+1) - max(hash_map.values()) > k:
                hash_map[s[l]] -= 1 
                if hash_map[s[l]] == 0:
                    del hash_map[s[l]]
                l += 1 
            res = max(res ,r-l+1)
        return res
        


