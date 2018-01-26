def convertToSets(problem):
    z = set(range(1, 10))

    for lst in problem:
        for i, x in enumerate(lst):
            if x == 0:
                lst[i] = z
            else:
                lst[i] = {x}

    return problem


def convertToInts(problem):
    
    for lst in problem:
        for i, x in enumerate(lst):
            if len(x) > 1:
                lst[i] = 0
            else:
                x = str(x)
                x = x.replace('{', '').replace('}', '')
                x = int(x)
                lst[i] = x
    
    return problem
