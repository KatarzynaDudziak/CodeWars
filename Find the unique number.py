def find_uniq(arr):

    list_arr = list(set(arr))
    
    counter = 0
    
    for i in arr:
        if list_arr[0] == i:
            counter += 1
            if counter > 1:
                return list_arr[1]
    return list_arr[0]
