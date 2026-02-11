class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = -1

        for index in range(len(nums)):
            sum1 = sum(nums[:index + 1])
            sum2 = sum(nums[index:])

            if sum1 == sum2:
                answer = index
                return index
        return answer