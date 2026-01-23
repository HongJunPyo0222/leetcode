class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        currentAltitude = [0]
        for index, gain in enumerate(gain):
            currentAltitude.append(currentAltitude[index] + gain)
        
        return max(currentAltitude)