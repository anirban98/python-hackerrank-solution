L = []

N = int(input())

for i in range(0, N):
    tokns = input().split()

    if tokns[0] == 'insert':
        L.insert(int(tokns[1]), int(tokns[2]))
    elif tokns[0] == 'print':
        print (L)
    elif tokns[0] == 'remove':
        L.remove(int(tokns[1]))
    elif tokns[0] == 'append':
        L.append(int(tokns[1]))
    elif tokns[0] == 'sort':
        L.sort()
    elif tokns[0] == 'pop':
        L.pop()
    elif tokns[0] == 'reverse':
        L.reverse()