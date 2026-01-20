import itertools
import math

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtype = []
        tmp_list = [n for n in range(len(nums))]
        print(tmp_list)
        for a, b in itertools.combinations(tmp_list, 2):
            if nums[a] + nums[b] == target:
                rtype.append(a)
                rtype.append(b)
        return rtype
        

        