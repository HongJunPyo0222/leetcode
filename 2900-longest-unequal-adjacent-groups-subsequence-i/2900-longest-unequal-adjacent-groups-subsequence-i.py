class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        가장 긴 부분 수열은 만들어야함
    
        """



        # for index, int in enumerate(groups):
        #     groups[index] = str(groups[index])
        # print(groups)
        # string = "".join(groups)
        # print(string)
        # print(string.find(1))
        ex = -1
        answer =[]
        for index, num in enumerate(groups):
            if num != ex:
                answer.append(words[index])
                #print(words[index])
                ex = num
            else:
                continue


        return answer