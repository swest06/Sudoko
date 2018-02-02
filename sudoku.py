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


def getBoxLocations(location):
    
    result = []
    l = location
    
    ary = [[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
        [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
        [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
        [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
        [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
        [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
        [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
        [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
        [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]]

    #Finds relevant list in ary that contains location tuple
    for lst in ary:
        for i, e in enumerate(lst):
            if e == l:
               result = lst
               
    return result



def eliminate(problem, location, listOfLocations):
    ll = listOfLocations
    count = 0
    a = []
    
    #Creates index from location argument
    in_1 = location[0]
    in_2 = location[1]
    num = int(str(problem[in_1][in_2]).replace('{', '').replace('}', ''))
    
    #Counts number of apperances of value num using listOfLocations
    for tup in ll: 
        for i in problem[tup[0]][tup[1]]:
            if i == num:
                a.append(tup)
                count = count + 1
    
    #Removes num value from array if num appears in listOfLocations            
    for tup in a:
        problem[tup[0]][tup[1]].remove(num)
        
    return count


