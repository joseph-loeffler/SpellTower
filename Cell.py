class Cell:
    def __init__(self, char: str, min: int, row: int, col: int):
        self._char = char
        self._min = min
        self._row = row
        self._col = col

    def __str__(self):
        return f"({self.row}, {self.col}): {self.value} (adjChecked={self.adjChecked})"

    def markVisited(self):
        self.visited = True

    def isVisited(self):
        return self._visited
    
    def getChar(self):
        return self._char
    
    def getRow(self):
        return self._row
    
    def getCol(self):
        return self._col
    
    def getMin(self):
        return self._min