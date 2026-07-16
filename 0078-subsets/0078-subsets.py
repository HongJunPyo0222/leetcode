from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        print(nums)
        nums = list(nums)

        tmp = []
        for i in range(len(nums)+1):
            tmp+=(map(list, combinations(nums,i)))

        return tmp


