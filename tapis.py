def creation_tapis(tapis): 
    print('+' + '-' * (tapis - 1) + '+')
    for i in reversed(range(- 1, tapis - 2)):
        row = ''
        for j in range(- 1, tapis - 2):
            if i == j:
                row += ' '
            else:
                row += '#'       
        print('|' + row + '|')
    print('+' + '-' * (tapis - 1) + '+')    
creation_tapis(10)    