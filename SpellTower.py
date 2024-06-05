from Cell import Cell


def createCellMatrix(matrix):
    cellMatrix = []

    for i in range(len(matrix)):
        cellMatrix.append([None for _ in matrix[0]])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            regCell = matrix[i][j]
            if len(regCell) > 1:   
                cellMatrix[i][j] = Cell(regCell[0], int(regCell[1]), i, j)
            else:
                cellMatrix[i][j] = Cell(regCell, 0, i, j)

    return cellMatrix


def getAllWords(matrix):
    cmatrix = createCellMatrix(matrix)
    engDict = createDictList()
    prefixes = getPrefs(engDict)
    wordDict = {}
    for i in range(len(cmatrix)):
        for j in range(len(cmatrix[0])):
            # print(f"{(i,j)}: start")
            wordDict[(i,j)] = set(searchWords(cmatrix, i, j, prefixes, engDict))
            # print(f"{(i,j)}: end")
    return wordDict


def createDictList():
    with open("dictionary.txt") as file:
        ret = file.read().split()
        for i in range(len(ret)):
            ret[i] = ret[i].upper()
        return ret


def getPrefs(strList):
    prefSet = set([])
    for word in strList:
        wordPrefs = [word[:i + 1] for i in range(len(word))]
        for w in wordPrefs:
            prefSet.add(w)
    prefSet.add("")
    return prefSet


def searchWords(cmatrix, i, j, prefixes, engDict):

    crawler = [
        [1, 1, 0, -1, -1, -1,  0,  1],
        [0, 1, 1,  1,  0, -1, -1, -1]
        ]

    wordSet = set([])
    stack = []

    currBuild = []
    stack.append(cmatrix[i][j])
    currCell = None

    while len(stack) > 0:
        cell = stack.pop()
        if cell == currCell:
            currBuild.pop()
            if len(currBuild) > 0:
                currCell = currBuild[-1]
            else:
                currCell = None
            continue
        currBuild.append(cell)

        if "".join([x.getChar() for x in currBuild]) in prefixes:
            currCell = cell
            stack.append(cell)
            for k in range(len(crawler[0])):
                ai = cell.getRow() + crawler[0][k]
                aj = cell.getCol() + crawler[1][k]
                if inRange(cmatrix, ai, aj):
                    adjCell = cmatrix[ai][aj]
                    if (not adjCell in currBuild) and (adjCell.getChar() != "_") and (adjCell.getChar() != "@"):
                        stack.append((adjCell))
        else:
            currBuild.pop()
            currPrefix = "".join([x.getChar() for x in currBuild])
            if (maxMin(currBuild) < len(currPrefix)) and (currPrefix in engDict):
                wordSet.add(currPrefix)

    return wordSet


def maxMin(cellList):
    max_min = 0

    for cell in cellList:
        min = cell.getMin()
        if min > max_min:
            max_min = min
    
    return max_min


def inRange(matrix, i, j):
    if (i < 0) or (j < 0) or (i >= len(matrix)) or (j >= len(matrix[1])):
        return False
    else:
        return True



if __name__ == "__main__":
    matrix = [
        ["H", "N" ,"O" ,"I" ,"F" ,"N", "N" ,"D" ,"T" ],
        ["W", "P" ,"V" ,"I" ,"T" ,"F", "O" ,"G" ,"L" ],
        ["L", "K" ,"A" ,"T" ,"R" ,"I", "E" ,"A" ,"S" ],
        ["M", "H" ,"@" ,"Q" ,"X" ,"N", "H" ,"E" ,"A" ],
        ["R", "C" ,"E" ,"I" ,"O" ,"L", "R" ,"O" ,"B" ],
        ["E", "S" ,"G" ,"C" ,"@" ,"T", "E" ,"Y" ,"G" ],
        ["O", "N" ,"S" ,"I" ,"P" ,"A", "S" ,"R" ,"Z" ],
        ["S", "@" ,"L" ,"N" ,"R" ,"M", "A" ,"M" ,"Y" ],
        ["T", "I" ,"P" ,"L" ,"D" ,"S", "A" ,"I" ,"A" ],
        ["S", "O" ,"E" ,"E" ,"E" ,"T", "J" ,"S" ,"C" ],
        ["P", "@" ,"I" ,"E" ,"U" ,"O", "E" ,"E" ,"S" ],
        ["R", "B" ,"L" ,"N" ,"S" ,"A", "D" ,"U" ,"R" ],
        ["I", "C" ,"E" ,"T" ,"U" ,"C", "U" ,"D" ,"I" ],
        
    ]

    d = getAllWords(matrix)

    for key in d:
        d[key] = [w for w in d[key] if (len(w) >= 8)]
    print(d)