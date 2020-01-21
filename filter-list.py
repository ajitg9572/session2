def filter(l):
    after_f=[]
    normal =[]
    for i in l:
        if i >=2000:
            after_f.append(i)
        else:
            normal.append(i)
    output =[after_f,normal]
    return output
    num =[2000,5000,1,23,445,700,9999,6778,4,5666]
    print(filter(num))