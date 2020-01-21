def odd_even(p):
    odd_num =[]
    even_num =[]
    for i in p:
        if i %2==0:
            even_num.append(i)
        else:
            odd_num.append(i)
    output =[even_num,odd_num]
    return output
num =[1,2,3,4,5,6,7,8,9,10,11,12,21]
print(odd_even(num))