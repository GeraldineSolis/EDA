def change_to_postfix(expression):
    rules = {'+':1, '-':1, '*':2, '/':2, '(':0}
    box = []
    result = []
    parts = expression.split()

    for thing in parts:
        if thing.isdigit():
            result.append(thing)
        elif thing == '(':
            box.append(thing)
        elif thing == ')':
            take = box.pop()
            while take != '(':
                result.append(take)
                take = box.pop()
        else:
            while box and rules[box[-1]] >= rules[thing]:
                result.append(box.pop())
            box.append(thing)

    while box:
        result.append(box.pop())

    return result

def solve_postfix(postfix_list):
    stack = []

    for thing in postfix_list:
        if thing.isdigit():
            stack.append(int(thing))
        else:
            num2 = stack.pop()
            num1 = stack.pop()

            if thing == '+':
                stack.append(num1 + num2)
            elif thing == '-':
                stack.append(num1 - num2)
            elif thing == '*':
                stack.append(num1 * num2)
            elif thing == '/':
                stack.append(num1 / num2)

    return stack[0]
def solve_expression(expression):
    postfix = change_to_postfix(expression)
    answer = solve_postfix(postfix)
    return answer

my_math = "( 3 + 4 ) * 2"
print("The answer is:", solve_expression(my_math))
