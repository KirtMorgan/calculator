class Calculator():
    def __init__(self):
        self.input_1 = 0
        self.input_2 = 0
        self.total = 0
    def get_input_1(self):
        user_input_1 = int(input('Please enter the first number'))
        self.input_1 = user_input_1
    def get_input_2(self):
        user_input_2 = int(input('Please enter the second number'))
        self.input_2 = user_input_2
    def addition(self):
        self.total = (int(self.input_1 + self.input_2))
    def subtraction(self):
        self.total = (int(self.input_1 - self.input_2))
    def multiplication(self):
        self.total = (int(self.input_1 * self.input_2))
    def division(self):
        self.total = (float(self.input_1 / self.input_2))
    def run_calculator(self):
        while True:
            print('Welcome to the Calculator')
            self.get_input_1()
            self.get_input_2()
            self.addition()
            print('Addition result =', calculator.total)
            self.subtraction()
            print('Subtraction result =', calculator.total)
            self.multiplication()
            print('Multiplication result =', calculator.total)
            self.division()
            print('Division result =', calculator.total)

            player_option_input = input('Run Calculator Again? y/n')
            if player_option_input == 'n'.strip():
                break

# Testing
# Stage one, Test to see if the calculator can accept and store values for input_1 & input_2
calculator = Calculator()
calculator.run_calculator()
# calculator.get_input_1()
# calculator.get_input_2()
# # print(calculator.input_1)
# # print(calculator.input_2)
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
