'''Week 7 Coding
name: Aarush Inamdar
UCINetID: inamdara

Lecture 1'''

import tkinter as tk

#creating the class for the simple calculator
class Calculator():
    #defining class variables
    __calcResult__ = 0

    #define my constructor for my calculator class
    def __init__(self) -> None:
        #initialize class variables
        self.__calcResult__ = 0
    
    def getResult(self):
        return self.__calcResult__

    #define setting/mutator method for setting the result value
    def setResult(self, result):
        self.__calcResult__ = result
    
    #defining adding numbers function
    def addNumbers(self, num1, num2):
        self.setResult(num1 + num2)
    
    #define the function that performs the subtraction
    def subNumbers(self, num1, num2):
        self.setResult(num1 - num2)
    
    #define function that multiplies numbers
    def mulNumbers(self, num1, num2):
        self.setResult(num1*num2)
    
    #define function that divides numbers
    def divNumbers(self, num1, num2):
        self.setResult(num1/num2)

    #define the method that performs the correct operation
    def checkOperation(self, operation, num1, num2):
        if (operation == '+'):
            self.addNumbers(num1,num2)
        elif (operation == '-'):
            self.subNumbers(num1,num2)
        elif (operation == '*'):
            self.mulNumbers(num1,num2)
        elif (operation == '/'):
            self.divNumbers(num1,num2)

if __name__ == '__main__':
    testCalc = Calculator()
    print(testCalc.getResult())
    
    
    testCalc.checkOperation('+', 5, 3)
    print(testCalc.getResult())

    testCalc.checkOperation('-', 5, 3)
    print(testCalc.getResult())

    testCalc.checkOperation('*', 5, 3)
    print(testCalc.getResult())

    testCalc.checkOperation('/', 5, 3)
    print(testCalc.getResult())

