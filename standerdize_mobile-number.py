def standardize_wrapper(func):
    def standardize(phone_number):
        return "{prefix} {left} {right}".format(prefix='+91', left=phone_number[-10:-5], right=phone_number[-5:])
    
    def wrap(phone_numbers):
        return func(map(standardize, phone_numbers))
    
    return wrap

def main():
    N = int(input())
    phone_numbers = [input() for i in range(N)]
    
    standardized_sort = standardize_wrapper(sorted)
    
    for phone_number in standardized_sort(phone_numbers):
        print(phone_number)
    
if __name__ == '__main__':
    main()
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
