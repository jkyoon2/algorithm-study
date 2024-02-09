# 백준 10162

## Solution 1 

def get_change(t: int, button_list: list) -> str:
    '''
    Function returning the number of button operations
    
    args:
        t(int) : time
        button_list(list) : list of button operations

    return: 
        change: '0 1 4' / -1
    '''
    change_list = []
    for button in button_list:
        change_list.append(t // button)
        t %= button
    
    if t != 0:
        return -1
    else:
        return ' '.join(map(str, change_list))

t = int(input().strip())
button_list = [300, 60, 10]
print(get_change(t, button_list))
