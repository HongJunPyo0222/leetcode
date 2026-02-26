class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmp = []
        for index, num in enumerate(nums):
            if index == 0:
                tmp.append(num)
            else:    
                if num == tmp[-1]:
                    pass
                else:
                    tmp.append(num)

        ln = len(tmp)
        print(tmp)
        if len(set(tmp)) < 3:
            return False
        if len(tmp) < 3:
            return False
        for a in range(ln):
            for b in range(a + 1, ln):
                if tmp[b] <= tmp[a]:
                    break
                for c in range(b + 1, ln):
                    if tmp[c] > tmp[b]:
                        return True
        return False
        
k = Solution()
print(k.increasingTriplet([1, 2, 3, 4, 5]))