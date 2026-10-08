class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        count = Counter(nums)
        result = []
        for item, freq in count.most_common(k):
            result.append(item)
        return result

        