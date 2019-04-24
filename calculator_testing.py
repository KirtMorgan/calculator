from calculator_computer import *

# Testing
# Testing self.inputs, setting and checking the value
calculator.input_1 = 50
calculator.input_2 = 20
print('Input 1 is 20, testing value 20', calculator.input_1 == 20)
print('Input 1 is 20, testing value 25', calculator.input_1 == 25)

# Testing the addition method
print('Testing addition, total should be 70, test set to equal 70', calculator.addition() == 70)
# Testing subtraction method
print('Testing subtraction, total should be 30, test set to equal 30', calculator.subtraction() == 30)



