def evaluate(expression):
    expression = expression.split()
    stack = []

    for ele in expression:

        if ele not in '*+-':
            stack.append(int(ele))
        else:
            right = stack.pop()
            left = stack.pop()

            if ele == '+':
                stack.append(left + right)

            elif ele == '-':
                stack.append(left - right)

            elif ele == '*':
                stack.append(left * right)
    return stack.pop()


string = input()
answer = evaluate(string)
print(f"{answer}")
