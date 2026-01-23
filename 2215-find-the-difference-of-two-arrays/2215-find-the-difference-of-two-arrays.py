class Solution(object):
    def findDifference(self, nums1, nums2):
        resNums1 = []
        resNums2 =[]
        for element in nums1:
            if element not in nums2:
                if element not in resNums1:
                    resNums1.append(element)

        for element in nums2:
            if element not in nums1:
                if element not in resNums2:
                    resNums2.append(element)
            
        return resNums1, resNums2
        