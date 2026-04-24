class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """

        """

        L, R, _로 구성된 스트링 , 이 스트링은 당신의 움직임을 나타냄 0 에서 시작

        i 번째 움직임에서  moves[i] = l 혹은 _이면 l로 이동
        origin에서 가장 먼 거리를 가야함
        """


       
        count_ = 0
        cur = 0

        for char in moves:
            if char == "L":
                cur -=1
            elif(char == "R"):
                cur +=1
            else:
                count_ +=1

        
        if cur < 0:
            return abs(cur - count_)
        else :
            return cur + count_
