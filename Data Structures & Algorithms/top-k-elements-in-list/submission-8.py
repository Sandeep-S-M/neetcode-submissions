class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        sorted_counts = sorted(hashmap.values(), reverse=True)
        min_freq = sorted_counts[k-1]
        result = []
        for num in hashmap:
            if hashmap[num] >= min_freq:
                result.append(num)
        return result