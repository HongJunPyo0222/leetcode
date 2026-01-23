class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        res = []
        # 배열 6개 택 4개 -> 3개
        res.append(sum(nums[0:k]))
        for i in range(1, len(nums) - k+ 1):
            print(i, k)
            res.append(res[-1] - nums[i - 1] + nums[i + k -1])

        print(res)
        return max(res)/(k + 0.00)

        