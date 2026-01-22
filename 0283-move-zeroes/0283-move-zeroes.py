class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        res = []
        zeroIndex = []
        for index in range(len(nums)- 1, -1, -1):
            if nums[index] == 0:
                zeroIndex.append(index)

        for index in zeroIndex:
            del nums[index]
            nums.append(0)