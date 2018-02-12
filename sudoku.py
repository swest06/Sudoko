'''Sean West swest06.
    Sudoku solver.'''

def read_sudoku(file):
    stream = open(file)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))


def convertToSets(problem):
    for lst in problem:
        for i, x in enumerate(lst):
            if x == 0:
                lst[i] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            else:
                lst[i] = {x}

    return problem


def convertToInts(problem):
    for lst in problem:
        for i, x in enumerate(lst):
            if len(x) == 1:
                x = str(x)
                x = x.replace('{', '').replace('}', '')
                lst[i] = int(x)
            else:
                lst[i] = 0

    return problem


def getRowLocations(rowNumber):
    r = rowNumber
    lst = [(r, 0), (r, 1), (r, 2), (r, 3), (r, 4), (r, 5), (r, 6), (r, 7), (r, 8)]
    
    return lst


def getColumnLocations(columnNumber):
    c = columnNumber
    lst = [(0, c), (1, c), (2, c), (3, c), (4, c), (5, c), (6, c), (7, c), (8, c)]

    return lst


def getBoxLocations(location):
    result = []
    
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
            if e == location:
               result = lst
               
    return result


def eliminate(problem, location, listOfLocations):
    count = 0
    a = []

    if len(problem[location[0]][location[1]]) == 1:
        # Assigns set element from 'location' to num
        num = int(str(problem[location[0]][location[1]]).replace('{', '').replace('}', ''))

        # Counts number of appearances of value num using listOfLocations
        for i in listOfLocations:
            for e in problem[i[0]][i[1]]:
                if e == num:
                    a.append(i)
                    count += 1

        # 'a' contains new list of locations that contain 'num' excluding 'location'
        if location in a:
            a.remove(location)
            count -= 1

        # Removes num value from set if num appears in listOfLocations
        for x in a:
            if len(problem[x[0]][x[1]]) > 1:
                try:
                    problem[x[0]][x[1]].remove(num)
                except:
                    print("value {} not found in array location {} during 'eliminate()'.").format(num, x)

    return count


def isSolved(problem):
    #Assigns True if all sets in problem contain 1 element. Assigns False otherwise.
    result = all([len(problem[r][c]) == 1 for r in range(0, 9)
                                        for c in range(0, 9)])
                                
    return result
    

def solve(problem):
    '''Takes sudoku problem in int form and solves through iteration'''
    times = 0

    problem = convertToSets(problem)
    end = False
    while not end:
        total = 0
        for a,b in enumerate(problem):
            for x,y in enumerate(b):
                list0fLoc = []
                location = (a, x)

                row = getRowLocations(a)
                for i in row:
                    list0fLoc.append(i)
                column = getColumnLocations(x)
                for i in column:
                    if i in list0fLoc:
                        continue
                    else:
                        list0fLoc.append(i)
                box = getBoxLocations(location)
                for i in box:
                    if i in list0fLoc:
                        continue
                    else:
                        list0fLoc.append(i)

                if eliminate(problem, location, list0fLoc) > 0:
                    total += 1

        if total == 0:
            times += 1

        if times > 3:
            end = True
    result = isSolved(problem)

    return result


def print_sudoku(problem):
    '''Takes sudoku problem in its int form and prints out sudoku grid'''

    print("+-------" * 3, end= "+"), print("")
    for i, lst in enumerate(problem):

        #Prints elements in each row
        print(("| " + "{}{}{}| " * 3)
              .format(*[str(element) + " " if element > 0 else ". " for element in lst]))

        #Seperates every 3x3 grid row after every 3rd row in array(problem)
        if i % 3 > 1:
            print("+-------" * 3, end= "+"), print("")


def main():
    '''Main function'''

    finished = False

    while not finished:
        file = input("Please type/paste your file: ")
        try:
            problem = read_sudoku(file)

            #Prints unsolved problem
            print("Here is the unsolved puzzle:")
            print_sudoku(problem)
            print("")

            #Solves problem
            solve(problem)

            # Prints unsolved locations
            if not isSolved(problem):
                print("Puzzle could not be fully solved.")
                for r, lst in enumerate(problem):
                    for i, e in enumerate(lst):
                        if len(e) > 1:
                            loc = ("({}:{})").format(r, i)

                            print("Location {} may contain these possible values {}".format(loc, e))


            convertToInts(problem)
            #Prints solved problem
            print("Here is the solved puzzle")
            print_sudoku(problem)
            print("")


        except:
            print("File could not be read.")
            print("")

        #replay loop
        ask = False
        while not ask:
            reply = input("Do you want to try with another problem? Y/N: ").lower()
            print("")
            if reply[0] == "y":
                ask = True
            elif reply[0] == "n":
                ask = True
                finished = True
            else:
                print("Invalid input")
                print("")

    print("Goodbye.")


if __name__ == main():
    main()

