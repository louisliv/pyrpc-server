from pyrpc.decorators import safe_method

@safe_method
def print_hello():
    return "hello"

class Library():
    @safe_method
    def sum_two_numbers(self, operand1=0, operand2=0):
        """ 
        Returns the sum of two numbers. 
        Extended description of function. 

        @param operand1: Can be any float number.
        @param operand2: Can be any float number.
        @returns: operand1 + operand2. 
        """
        return operand1 + operand2

    @safe_method
    def multiply_two_numbers(self, operand1=0, operand2=0):
        """ 
        Returns the product of two numbers. 
        Extended description of function.

        @param operand1: Can be any float number.
        @param operand2: Can be any float number.
        @returns: operand1 * operand2. 
        """
        return operand1 * operand2
