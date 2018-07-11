# Problem 20
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


open_close_bracket_mapping = {
    '(' : ')',
    '{' : '}',
    '[' : ']'
}

def isValid(s):
    stack = []
    
    for bracket in s:
        if bracket in open_close_bracket_mapping.keys():
            stack.append(bracket)
        else:
            matching = stack.pop()
            if open_close_bracket_mapping[matching] != bracket:
                return False

    return True

if __name__ == "__main__":
    s1 = "{(){}[]}"
    s2 = "{{{}}]"
    print(isValid(s1))
    print(isValid(s2))

