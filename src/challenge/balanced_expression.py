def is_balanced(expression):
    """
    Determines whether an expression with parenthesis, square and curly brackets is balanced. A balanced expression
    has the same amount of opening and closing elements in the right order. This function assumes that only valid
    characters are provided, sot it is not performing any validations on the expression.

    :param expression: expression to process containing only parentheses, square and curly brackets
    :return: true if expression is correctly balanced; false otherwise
    """
    if len(expression) <= 1:
        return False

    elements = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in expression:
        if char in elements.values():
            stack.append(char)
        # stack is empty or closing does not match opening element
        elif not stack or elements[char] != stack.pop():
            return False

    return len(stack) == 0
