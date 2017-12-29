def convertToSets(problem):
    z = set(range(1, 10))

    for lst in problem:
        for i, x in enumerate(lst):
            if x == 0:
                lst[i] = z
            else:
                lst[i] = {x}

    return problem

