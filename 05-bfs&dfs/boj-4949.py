line_input = input()[:-1].split(".")[:-1]

for line in line_input:
    brackets_list = []
    for i in line:
        if i in ['(',')','[',']']:
            brackets_list.append(i)

    bracket_types = ['(',')','[',']']
    stack = []
    for i in brackets_list:
        stack.append(i)
        try:
            if stack[-2] in ['('] and stack[-1] in [')']:
                stack.pop()
                stack.pop()
            elif stack[-2] in ['['] and stack[-1] in [']']:
                stack.pop()
                stack.pop()
        except:
            pass

    if stack==[]:
        print("yes")
    else:
        print("no")