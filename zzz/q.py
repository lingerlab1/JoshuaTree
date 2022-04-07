# s = "()[]{}"
# stack = []

def valid_parentheses(s):
    mapping = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in s:
        if stack and char in mapping:
            last_char = stack.pop()
            if last_char != mapping[char]:
                return False
        else:
            stack.append(char)

    return not stack

s = "[)"
print(valid_parentheses(s))
