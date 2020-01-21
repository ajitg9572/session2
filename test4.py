def filter_num(l):
    filter =[]
    filter1=[]
    for i in l:
        if i %2==0:
            filter.append(i)
        else:
            filter1.append(i)
    output =[filter,filter1]
    return output
num =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(filter_num(num))
