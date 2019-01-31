def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



#OR YOU CAN DOTHIS ALSO!!!!!



def split_and_join(line):
       x=line.split(" ") 
       x='-'.join(x)    
       return x

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)