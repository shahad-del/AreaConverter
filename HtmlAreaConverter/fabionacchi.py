
fibonacci

# fib = []
# fib.append(0)
# fib.append(1)
# for i in range(2,len(lst)):
#     try:
#         fib.append( (fib[i-2]) + (fib[i - 1]))
#     except:
#         print("error")
#     print(i)

# print(fib)

lst = []
lst.append(0)
lst.append(1)
n = int(input('Enter n:'))

if(n > 2):
    for i in range(n-2):
        listLength = len(lst)
        lastElement = lst[listLength-1]
        secondLastElement = lst[listLength-2]
        lst.append(lastElement + secondLastElement)

print(lst)

