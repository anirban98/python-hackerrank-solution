import textwrap

s=input().strip()
w=int(input())
for i in range(0,len(s)+1,w):
    print(s[i:w+i])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)