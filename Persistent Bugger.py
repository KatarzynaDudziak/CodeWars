def get_product(n):
    n = list(map(int, str(n)))
    l = 1
    
    for element in n:
        l = l * element
    return l

def persistence(n):
    count = 0
    
    while n >= 10:
        count += 1
        n = get_product(n)
    return count
