def common(l1,l2):
    com_num =[]
    for i in l1:
        if i in l2:
            com_num.append(i)
            return com_num
print(common([1,2,3,4,5],[1,2,3,6,7]))