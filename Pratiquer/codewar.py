#Finish Guess the Number Game

class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
        
    def guess(self,n):
        if self.lives < 1:
            raise "Error"
        if n == self.number:
            return True
        else:
            self.lives -= 1  
        return False

#Refactored Greeting https://www.codewars.com/kata/5121303128ef4b495f000001/train/python

class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self, your_name):
        return f"Hello {your_name}, my name is {self.name}"

