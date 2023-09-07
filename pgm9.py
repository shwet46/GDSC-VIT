list1 = [23,56,87,45,36,66,54]
list2 = [65,34,78,67,16,89,49]

list3 = []

for i in list1 :
    if i % 2 != 0 :
        list3.append(i)

for i in list2 :
    if i % 2 == 0 :
        list3.append(i) 

print(list3)     