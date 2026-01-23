class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr =[]
        for element in s:
            if element != "*":
                arr.append(element)
            else:
                arr.pop()
        
        return "".join(arr)
        