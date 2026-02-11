class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # 숫자의 각 출현이 다 다르면 True
        # 1: 3 
        intMap = dict()

        # 문자의 출현 횟수를 딕셔너리 형태로 표시
        for num in arr:
            if num not in intMap:
                intMap[num] = 1
            else:
                intMap[num] +=1
        
        # 딕셔너리의 크기와 set(values)의 크기가 같으면 True
        setInt =set(intMap.values())

        print(setInt)

        if len(intMap) == len(setInt):
            return True
        else:
            return False
