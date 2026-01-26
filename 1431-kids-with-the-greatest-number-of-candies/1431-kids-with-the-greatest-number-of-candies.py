class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        returnArr = [False for _ in range(len(candies))]
        print(returnArr)
        for index in range(len(candies)):
            nowCandies = candies[index] + extraCandies
            if nowCandies >= max(candies):
                returnArr[index] = True
        
        return returnArr
        