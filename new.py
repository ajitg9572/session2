def sqaure_num(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
numbers =list(range(1,11))
print(sqaure_num(numbers))
