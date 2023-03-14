# First make a class
class Calc():

    def __init__(self):
        self.rentalincome = 0 
        self.new_income = 0 
        self.totalexpenses = 0 
        self.cash_Flow = 0 
    
    #Write first method for income 

    def getIncome(self):
        self.rentalincome= input("Enter the price of the rental: ")
        print(f"You've entered {self.rentalincome}")
        additional_income = input("Do you have any additional income?")
        if additional_income == "yes":
            income_ = int(input("Enter additional income."))
            self.new_income = int(self.rentalincome) + int(income_)
            print(f'Your rental income is {self.new_income}.')
        else: 
            print(f'Your rental income is: {self.rentalincome}.')
    
    #Write second method for expenses 

    def getExpenses(self):
        num_of_expenses = int(input("Enter number of expenses: "))
        self.totalexpenses = 0
        for i in range(num_of_expenses): 
            num = float(input("Enter number "+ str(i+1) + ": "))
            self.totalexpenses += num 
        print(f'Your total expenses are: {self.totalexpenses}')
    
    #Write a third function for cashFlow 

    def cashFlow(self):
        input1= int(input("Enter your income: "))
        input2= int(input("Enter your expenses: "))
        self.cash_Flow = input1 - input2 
        print(f'Your cash flow is: {self.cash_Flow}.')
        return self.cash_Flow
    
    #Write a fourth function for ROI

    def ROI_(self):
        annual_cashFlow = self.cash_Flow * 12 
        input3 = int(input("Enter what you spent on the property:"))
        investment_return = (annual_cashFlow/input3) * 100 
        print (f'Your ROI is: {investment_return}')
    
    #Function to exit program

    def exit_(self): 
        quit()

#Make object real 

a_rental_calc = Calc() 

print("Welcome! This is the rental property calculator.")
print("Type 'enter' to begin.")
print("Type 'exit' to exit.")

def run():
    while True:
        an_input = input("What would you like to do?")

        if an_input == "enter": 
            a_rental_calc.getIncome()
            a_rental_calc.getExpenses()
            a_rental_calc.cashFlow()
            a_rental_calc.ROI_() 
            a_rental_calc.exit_() 
        elif an_input == "exit":
            a_rental_calc.exit_()
        else:
            print("That's not a valid option.")

run() 