def print_formatted(number):
    # your code goes here
    w = len(f"{number:b}")
    for i in range(1,number+1):
        print(f"{i:>{w}} {i:>{w}o} {i:>{w}X} {i : >{w}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
