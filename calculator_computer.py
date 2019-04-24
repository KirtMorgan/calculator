class Calculator():

    def __init__(self):
        self.input_1 = 0
        self.input_2 = 0
        self.total = 0
        self.operation = 'Operation'

    def get_input_1(self):
        user_input_1 = int(input('Please enter the first number'))
        self.input_1 = user_input_1

    def get_input_2(self):
        user_input_2 = int(input('Please enter the second number'))
        self.input_2 = user_input_2

    def get_operation(self):
        user_operation = input('What would you like to do with the numbers? (Add, Subtract, Multiply, Divide')
        self.operation = user_operation
    def addition(self):
        self.total = (int(self.input_1 + self.input_2))
        print(self.total)

    def subtraction(self):
        self.total = (int(self.input_1 - self.input_2))
        print(self.total)

    def multiplication(self):
        self.total = (int(self.input_1 * self.input_2))
        print(self.total)

    def division(self):
        self.total = (float(self.input_1 / self.input_2))
        print(self.total)

    def run_calculator(self):
        while True:
            print('Welcome to the Calculator')
            self.get_input_1()
            self.get_input_2()
            self.get_operation()

            if self.operation.capitalize().strip() == 'Add':
                self.addition()

            elif self.operation.capitalize().strip() == 'Subtract':
                self.subtraction()

            elif self.operation.capitalize().strip() == 'Multiply':
                self.multiplication()

            elif self.operation.capitalize().strip() == 'Divide':
                self.division()
            else:
                print('Invalid input, please type Add, Subtract, Multiply or Divide')

            player_option_input = input('Run Calculator Again? y/n')
            if player_option_input == 'n'.strip():
                print('Thank you for using this calculator')
                break

# Testing
# Stage one, Test to see if the calculator can accept and store values for input_1 & input_2
calculator = Calculator()
calculator.run_calculator()
# calculator.get_input_1()
# calculator.get_input_2()
# print(calculator.input_1)
# print(calculator.input_2)
# # Addition testing
# # Checking to see if the calculator can add two numbers
# calculator.addition()
# print('Addition result =', calculator.total)
# # Subtraction testing
# # Checking to see if the calculator can take-away two numbers
# calculator.subtraction()
# print('Subtraction result =', calculator.total)
# # Multiplication testing
# # Checking to see if the calculator can times two numbers
# calculator.multiplication()
# print('Multiplication result =', calculator.total)
# # Division testing
# # Checking to see if the calculator can divide two numbers
# calculator.division()
# print('Division result =', calculator.total)
