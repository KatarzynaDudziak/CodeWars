def count_positives_sum_negatives(arr):
    
    positive = []
    negative = []
    
    for element in arr:
        if element > 0:
            positive.append(element)
        if element < 0:
            negative.append(element)
 
    if len(arr) == 0:
        return []
    
    if len(positive) == 0 and len(negative) == 0:
        return [0, 0]

    return [len(positive), sum(negative)]
