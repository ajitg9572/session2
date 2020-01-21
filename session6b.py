def filter_num(l):
    filter =[]
    filter1=[]
    for i in l:
        if i >=200:
            filter.append(i)
        else:
            filter1.append(i)
    output =[filter,filter1]
    return output
num =[1,2,3,2000,20,200,300,500,45,55]
print(filter_num(num))
