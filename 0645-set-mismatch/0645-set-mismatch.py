class Solution(object):

    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        numDict = dict()
        for num in nums:
            if num not in numDict:
                numDict[num] = 1
            else:
                numDict[num] +=1
        print(numDict)

        for k, v in numDict.items():
            if v > 1:
                duNum = k
        
        for num in range(1, len(nums)+1):
            if num not in numDict:
                missNum = num
        return [duNum, missNum]

sol = Solution()
print(sol.findErrorNums([3, 2, 2]))
    