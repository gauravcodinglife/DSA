def sorted_array(array):
    n= len(array)
    i,j=0,n-1
    res= [0]*n
    for k in reversed(range(n)):
        if array[i]**2 > array[j]**2:
            res[k]= array[i]**2
            i+=1
        else:
            res[k]= array[j]**2
            j-=1
    return res

print(sorted_array([-10, -5, 0, 2, 3]))




