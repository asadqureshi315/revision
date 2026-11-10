#Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
class StockSpanner(object):

    def __init__(self):
        self.stack=[]
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span=1
        print(price, span, self.stack)
        while self.stack and price>=self.stack[-1][1]:
            prevSpan, prevPrice=self.stack.pop()
            span+=prevSpan
            
        self.stack.append([span,price])
        return span
        
