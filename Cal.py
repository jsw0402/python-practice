class CalFour:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def div(self):
        result=self.first/self.second
        return result

a=CalFour(5,6)
print(a.add())

class MoreCal(CalFour):
    pas
b=MoresCal(4,6)
print(b.mul())