for i in range(11, 79+1):
    if (i % 3 == 0) and (i % 5 == 0): print('$$@@')
    elif i % 3 == 0: print('$$')
    elif i % 5 == 0: print('@@')