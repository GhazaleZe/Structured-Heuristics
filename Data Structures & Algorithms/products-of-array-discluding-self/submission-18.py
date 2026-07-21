import math
from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dic = {}
        result = []
        output = 0
        for i in range(len(nums)):
            dic[i] = nums[:i] + nums[i+1:]

        for val in dic.values():
            output = math.prod(val)
            result.append(output)

        return result
