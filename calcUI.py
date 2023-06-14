#import calculator function from calculator class
import calculatorclass as calc
import tkinter as tk

from tkinter import ttk

#defining a calcUI class for our User Interface
class CalcUIPacker():
    myCalc = 0
    #defining class constructor
    
    #define class variable to store my tkinter object
    master = 0
    myCalc = 0

    num1 = 0
    num2 = 0
    operation = 0
    resutl = 0

    #define my class constructor
    def __init__(self) -> None:
        #initializing class variables

        self.myCalc = calc.Calculator()
        self.canvasSetup()

        
        #initializing my calculator class variable
        self.initTKVariables()
        self.returnKeyBind()
        self.createQuitButton()

        self.createNumber1Entry()
        self.createOperationComboBox()
        self.createNumber2Entry()

        self.createResultLabel()
        
        self.createSubmitButton()
        
        self.runUI()

    def canvasSetup(self):    
        #initialize my tkinter canvas
        self.master = tk.Tk()
        self.master.title('Basic Calculator') #sets the window title
        self.master.geometry('400x400') #sets the default size of the window
        self.master.configure(background='navyblue') #sets the background color
        self.master.resizable(0,0) #sets the resizability potential

    def initTKVariables(self):
        self.num1 = tk.IntVar()
        self.num2 = tk.IntVar()
        self.operation = tk.StringVar()
        self.result = tk.IntVar()

    
    def createQuitButton(self):
        self.quitButton = tk.Button(self.master, text='Quit', command=self.master.destroy).pack()
        pass

    def createNumber1Entry(self):
        self.num1Entry = tk.Entry(self.master, textvariable=self.num1)
        self.num1Entry.pack()

    def createNumber2Entry(self):
        self.num2Entry = tk.Entry(self.master, textvariable=self.num2)
        self.num2Entry.pack()

    #define a method that creates a label for my result
    def createResultLabel(self):
        self.result.set('')
        self.resultLabel = tk.Label(self.master, textvariable=self.result, command=self.calculateResult()).pack()

    #define a method to submit button on the UI
    def createSubmitButton(self):
        self.submitButton = tk.Button(self.master,text='Submit',command=self.calculateResult).pack()
    

    #define a method that taken in the operator
    def createOperatorEntry(self):
        self.operatorEntry = tk.Entry(self.master, textvariable=self.operation)
        self.operatorEntry.pack()
    
    #define a method that triggers the calculation
    def calculateResult(self, event=None):
        self.myCalc.checkOperation(self.operation.get(), self.num1.get(), self.num2.get())
        self.result.set(self.myCalc.getResult())

    #defining a method that creates a combobox with the operation values
    def createOperationComboBox(self):
        operationValues = ['+','-', '*', '/']
        self.operation.set('Please select an operation')
        self.opCombobox = ttk.Combobox(self.master, textvariable=self.operation, values=operationValues).pack()

    #define a method that binds the return/enter key to also calculate the result
    def returnKeyBind(self):
        self.master.bind('<Return>',self.calculateResult)

    def runUI(self):
        #define a method start UI
        #starts my UI - event handler
        self.master.mainloop()


if __name__ == '__main__':
    basicCalc = CalcUIPacker()
    basicCalc.myCalc.getResult()
    #Confirming we have access to the members of the calculator object
    #print(basicCalc.myCalc.getResult())
