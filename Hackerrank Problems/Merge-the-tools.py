def merge_the_tools(string, k):
    # your code goes here
    indx = 0
    while indx < len(string) - k + 1:
        ans = ""
        st = set()
        for i in string[indx:indx+k]:
            if i not in st:
                ans += i
                st.add(i)
        print(ans)
        indx += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
