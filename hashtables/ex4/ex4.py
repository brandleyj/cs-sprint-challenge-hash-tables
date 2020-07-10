import math

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}

    pos_num = [i**2 for i in a]

    for num in pos_num:
        if num in cache:
            cache[num] += 1
        else:
            cache[num] = 1
    
    result = []

    for k, v in cache.items():
        if v == 2:
            result.append(int(math.sqrt(k)))
   
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
