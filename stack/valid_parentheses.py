def vaild_parenttheses(s):
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        if stack:
            char = stack[-1] 
            if c == ')':
                if char == '(':
                    stack.pop()
                else:
                    return False
            if c == '}':
                if char == '{':
                    stack.pop()
                else:
                    return False
            if c == ']':
                if char == '[':
                    stack.pop()
                else:
                    return False
                
    return True if len(stack) == 0 else False
            

print(vaild_parenttheses(")("))
print(vaild_parenttheses("([]}"))
print(vaild_parenttheses("{()[]}"))
print(vaild_parenttheses("(([{})])"))
print(vaild_parenttheses("[[{}]]()"))
print(vaild_parenttheses("(({[]}()[[]]))"))
