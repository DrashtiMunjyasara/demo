def remove_duplicate(lst):
    unique=[]
    
    for i in lst:
        if i not in unique:
            unique.append(i)
        
    return unique


l1=[1,1,2,5,6,5,6,8]
print(remove_duplicate(l1))
#to remove duplicates from a list and creating a new list.