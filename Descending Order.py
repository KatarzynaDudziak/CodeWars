def descending_order(num):
    numbers = [int(x) for x in str(num)]
    numbers = "".join(map(str,(sorted(numbers, reverse=True))))
    return int(numbers)
