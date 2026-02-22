def monotonic_array(array):
    n = len(array)
    first = array[0]
    last = array [n-1]

    if first > last:
        for i in range(n-1):
            if array[i] < array[i+1]:return False

    elif first == last:
        for i in range(n-1):
            if array[i] != array[i+1]:return False
    else:
        for i in range(n-1):
            if array[i] > array[i+1]:return False
    return True

print (monotonic_array([1,2,3,4,4,5,6]))

