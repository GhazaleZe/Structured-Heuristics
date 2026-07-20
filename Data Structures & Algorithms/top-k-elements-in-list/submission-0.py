class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        out = []
        mc = c.most_common(k)
        for i in range(k):
            out.append(mc[i][0])

        return out
        