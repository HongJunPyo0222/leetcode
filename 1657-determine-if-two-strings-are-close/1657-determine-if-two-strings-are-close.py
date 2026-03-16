class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        dict1 = dict()
        dict2 = dict()
        
        for char in word1:
            if char not in dict1:
                dict1[char] = 1
            else:
                dict1[char] +=1
        
        
        for char in word2:
            if char not in dict2:
                dict2[char] = 1
            else:
                dict2[char] +=1


        print(dict1, dict2)

        print(sorted(dict1.values()))
        set1 = set()
        for k, v in dict1.items():
            set1.add(k)

        print(set1)

        set2 = set()
        for k, v in dict2.items():
            set2.add(k)

        if sorted(dict1.values()) == sorted(dict2.values()) and set1 == set2:
            return True
        else:
            return False
        