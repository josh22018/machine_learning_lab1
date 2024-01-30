# intersecting two lists.
list1=[1,3,4,5,6,7]
list2=[2,4,5,6,7,8,0]
def intersec(list1,list2):
    list3=[]
    for v in list1:
        if v in list2:
            list3.append(v)
    return list3
print(intersec(list1,list2))
