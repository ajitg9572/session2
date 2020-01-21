def odd_even(l):
    odd_num =[]
    even_num=[]
    for i in l:
        if i %2==0:
            even_num.append(i)
        else:
            even_num.append(i)
        output =[odd_num,even_num]
        return output
num =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(odd_even(num))
        