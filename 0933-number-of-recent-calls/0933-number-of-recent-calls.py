class RecentCounter(object):

    def __init__(self):
        self.requests = []
        self.range = [0,0]
        self.count = 0
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)
        self.range = [t - 3000, t]
        while self.requests[0] < self.range[0]:
            del self.requests[0]

        return len(self.requests)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)