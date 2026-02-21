class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        
        # j > i 인것 중이고 가격이 더 작은거에 한해서 j의 최소값
        retArr = []
        lnPrices = len(prices)
        for index, price in enumerate(prices):
            print("original price: ", price)
            flag  = 0
            for indexJ in range(index + 1, lnPrices):
                if price >= prices[indexJ]:
                    flag = 1
                    break
            print(flag)
            if flag == 1:
                retArr.append(price - prices[indexJ])
            elif flag == 0:
                retArr.append(price)

        return retArr