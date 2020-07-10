def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    if length == 1:
        return None

    elif length == 2:
        num1 = weights[0]
        num2 = weights[1]
        if num1 + num2 == limit:
            return [1, 0]
        else:
            return None
        
    else:
        cache = {}
        answer = []

        for i in range(0, length):
            cache[weights[i]] = i

        for k, v in cache.items():
            if limit - k in cache.keys():
                answer.append(v)
        return sorted(answer, reverse=True)