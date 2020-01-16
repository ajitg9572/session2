def reverse_num(l):
    r_list = []
    for i in range(len(l)):
        popped_list = l.pop()
        r_list.append(popped_list)
    return r_list
numbers = [1,2,3,4,5]
print(reverse_num(numbers))