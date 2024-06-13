def reversed_string(string):

    stack = []

    for char in string:
        stack.append(char)

    reversed = ""
    while stack:
        reversed += stack.pop()
    return reversed
print(reversed_string("eric"))