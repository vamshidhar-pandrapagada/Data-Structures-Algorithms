def is_matched(expression):
    balanced = {'{':'}', '[':']', '(':')'}
    stack = []
    for i in expression:
        if i in balanced.keys():
            stack.append(i)
        else:
            if len(stack) == 0 or balanced[stack.pop()] != i:
                return False
    return len(stack) == 0