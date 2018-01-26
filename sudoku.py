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
                x = str(x.replace('{', '').replace('}', ''))
                lst[i] = int(x)
    
    return problem


def getRowLocations(rowNumber):
    r = rowNumber
    lst =  [(r, 0), (r, 1), (r, 2), (r, 3), (r, 4), (r, 5), (r, 6), (r, 7), (r, 8)]
    
    return lst


def getColumnLocations(columnNumber):
    c = columnNumber
    lst = [(0, c), (1, c), (2, c), (3, c), (4, c), (5, c), (6, c), (7, c), (8, c)]

    return lst


def def getBoxLocations(location):
