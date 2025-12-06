def vaild_parenttheses(s):
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        if stack: 
            if c == ')':
                char = stack[-1]
                if char == '(':
                    stack.pop()
                else:
                    return False
            if c == '}':
                char = stack[-1]
                if char == '{':
                    stack.pop()
                else:
                    return False
            if c == ']':
                char = stack[-1]
                if char == '[':
                    stack.pop()
                else:
                    return False
    if len(stack) == 0:
        return True
    return False
            

print(vaild_parenttheses(")("))
print(vaild_parenttheses("([]}"))
print(vaild_parenttheses("{()[]}"))
print(vaild_parenttheses("(([{})])"))
print(vaild_parenttheses("[[{}]]()"))
print(vaild_parenttheses("(({[]}()[[]]))"))
