# coding: utf-8
# four culation.py
"""A class for four arithmetic calculations"""

class FourCalculation: # class는 함수와 달리 첫번째 글자가 모두 대문자로 사작해야 한다.
    """A class for four arithmetic calculation"""
    
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
        if second == 0:
            raise ValueError('the number must NOT be zero')

    def add(self):
        return self.first + self.second
    
    def mul(self):
        return self.first * self.second
    
    def sub(self):
        return self.first - self.second
    
    def div(self):
        return self.first / self.second
