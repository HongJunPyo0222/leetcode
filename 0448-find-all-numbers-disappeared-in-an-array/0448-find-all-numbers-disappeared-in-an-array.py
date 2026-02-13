class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ln = len(nums)
        tmpset =set(i for i in range(1,ln + 1))
        
        return list(tmpset - set(nums))