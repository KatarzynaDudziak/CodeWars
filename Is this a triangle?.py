def is_triangle(a, b, c):
    list = [a,b,c]
    sorted_list = sorted(list)
    
    if (sorted_list[0] + sorted_list[1]) > sorted_list[2]:
        return True
    return False
