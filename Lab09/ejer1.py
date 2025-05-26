def infix_to_postfix(tokens):
    # Define precedence levels of operators
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    # Stack to hold operators and parentheses
    operator_stack = []
    
    # Output list for the postfix expression
    output = []

    # Iterate through each token in the input list
    for token in tokens:
        if token.isnumeric():
            # If token is a number, append it to output
            output.append(token)
        elif token in precedence:
            # If token is an operator, process stack precedence
            while (operator_stack and operator_stack[-1] != '(' and
                   precedence.get(operator_stack[-1], 0) >= precedence[token]):
                # Pop from stack to output while precedence is higher or equal
                output.append(operator_stack.pop())
            # Push the current operator to the stack
            operator_stack.append(token)
        elif token == '(':
            # Push opening parenthesis to the stack
            operator_stack.append(token)
        elif token == ')':
            # Pop everything until the matching '('
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()  # Pop the '(' itself
    
    # Pop any remaining operators from the stack
    while operator_stack:
        output.append(operator_stack.pop())

    # Return the final postfix expression
    return output

#       Test Cases
def test_infix_to_postfix():
    """Test the infix_to_postfix function. 📝"""
    
    test1_input = ['2', '+', '3']
    test1_expected = ['2', '3', '+']
    assert infix_to_postfix(test1_input) == test1_expected, "Test Case 1 Failed"
    
    test2_input = ['2', '+', '3', '*', '4']
    test2_expected = ['2', '3', '4', '*', '+']
    assert infix_to_postfix(test2_input) == test2_expected, "Test Case 2 Failed"
    
    test3_input = ['(', '2', '+', '3', ')', '*', '4']
    test3_expected = ['2', '3', '+', '4', '*']
    assert infix_to_postfix(test3_input) == test3_expected, "Test Case 3 Failed"
    
    test4_input = ['(', '5', '+', '3', ')', '*', '(', '10', '-', '8', ')']
    test4_expected = ['5', '3', '+', '10', '8', '-', '*']
    assert infix_to_postfix(test4_input) == test4_expected, "Test Case 4 Failed"
    
    test5_input = ['(', '(', '2', '+', '3', ')', '*', '4', ')', '-', '5']
    test5_expected = ['2', '3', '+', '4', '*', '5', '-']
    assert infix_to_postfix(test5_input) == test5_expected, "Test Case 5 Failed"
    
    print("✅ All test cases passed!")

# Run the tests
test_infix_to_postfix()
