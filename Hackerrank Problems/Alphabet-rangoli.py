def print_rangoli(size):
    # your code goes here
    al = "abcdefghijklmnopqrstuvwxyz"
    #number of rows
    n = 2 * size - 1
    #number of columns
    m = 2 * n - 1
    #to keep the first half row after get the row string
    ls  = []
    space = m//2
    for i in range(n//2 + 1):
        curr = "-" * (space)
        indx = size - 1
        turn = True
        for j in range(space,m//2 + 1):
            if indx >= 0 and turn:
                curr += al[indx]
                turn = not turn
                indx -= 1
            else:
                curr += "-"
                turn = not turn
        curr = curr + curr[:-1][::-1]
        ls.append(curr)
        space -= 2
    #print the first n//2 + 1 rows
    for i in range(len(ls)):
        print(ls[i])
    #print the last n // 2 rows
    for i in ls[:-1][::-1]:
        print(i)
            
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
