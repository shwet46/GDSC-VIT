def check(list):

    if list[0] == list[-1] :
        return True
    else :
        return False
    

list1 = [1,4,5,6,1]
list2 = [1,2,3,4]

print(check(list1))
print(check(list2))
