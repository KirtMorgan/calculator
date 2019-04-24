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
        return self.total

    def subtraction(self):
        self.total = (int(self.input_1 - self.input_2))
        print(self.total)
        return self.total

    def multiplication(self):
        self.total = (int(self.input_1 * self.input_2))
        print(self.total)
        return self.total

    def division(self):
        self.total = (float(self.input_1 / self.input_2))
        print(self.total)
        return self.total

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

calculator = Calculator()
# calculator.run_calculator() # Uncomment this line to run the calculator