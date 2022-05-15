# In the language of your choice, write a function that takes a rectangle specification 
# as input and prints the specified rectangle to standard out. A rectangle is specified 
# by a width, height, and optional fill character.
# Sample input: 6 4 "x"
# Sample output:
# +----+ 
# |xxxx|
# |xxxx|
# +----+

def rectangle(width, height, char):
    # return a 2-d matrix
    rows, cols = height, width
    # matrix = [([0] * cols) for r in range(rows)] # 4 by 6

    for r in range(rows):
        print()
        for c in range(cols):
            # four corners first
            if (r, c) in [(0, 0), (0, cols - 1), (rows - 1, 0), (rows -1, cols - 1)]:
                print('+', end='')
            # first and last row
            elif (r == 0) or (r == rows - 1):
                print('-', end='')
            # first and last col
            elif (c == 0) or (c == cols - 1):
                print('|', end='')
            else:
                print(char, end='')
    print()
    
rectangle(6, 4, 'x')
    
            
    




