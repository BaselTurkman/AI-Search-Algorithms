from collections import deque
from queue import PriorityQueue
class Grid:
    def __init__(self, board):
        self.grid = board  
        self.parentState = (None,"")

    def get(self, i, j):
        return self.grid[i][j]
    def set(self, i, j, val):
        self.grid[i][j] = val
    def printGrid(self):
        print(self.grid)
    def getGrid(self):
        return self.grid
        

class ChessBoard:
    def __init__(self):
        self.chessBoards = deque() 
        self.buffer = deque() 
        self.visited = set()
        self.pqueue = PriorityQueue()
    # Helper functions for BFS and A* Algorithms    
    def printChessboard(self,grid):
        WHITE = '\033[0m'
        BLACK = '\033[40m'
        GREY = '\033[47m'
        RED = '\033[31m'   
        for i in range(len(grid)):
            print()
            for j in range(len(grid[i])):
                cell = grid[i][j]
                if (i + j) % 2 == 0:
                    bg_color = WHITE
                else:
                    bg_color = GREY
                if cell:
                    print(f'{bg_color}{RED}{cell:^7}{WHITE}|', end="")
                else:
                    print(f'{bg_color}{"":^7}{WHITE}|', end="")
        print("")
    def findFirstLetter(self,state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j]!="":
                    return (i,j)
        return (0,0)
    
    def isValidMove(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def knightsMoves(self,grid):
        position = self.findFirstLetter(grid.getGrid())
        #All possible move for a knight
        steps = [(2,1),(1,2),(-1,2),(2,-1),(-2,1),(1,-2),(-1,-2),(-2,-1)]
        seen = set()
        seen.add(grid.get(position[0],position[1]))
        queue = deque()
        queue.append((position[0],position[1]))
        while queue:
            x, y = queue.popleft()
            for step in steps:
                nx, ny = x + step[0], y + step[1]
                if self.isValidMove(nx, ny) and grid.get(nx,ny) not in seen and grid.get(nx,ny)!="":
                    seen.add(grid.get(nx,ny))
                    queue.append((nx, ny))
            if len(seen) == 6:
                return len(seen)
        return len(seen)
    #===============================================================================================================================================

    #BFS Solution===================================================================================================================================
    def rearrangeLettersUsingBFS(self,state):
        self.printChessboard(state.getGrid())
        print()
        print("----------------------------------------------------------------")
        self.chessBoards.append(state)
        self.buffer.append(state)
        numberOfExpandedStates = 1
        while True:
            while self.chessBoards:
                board = self.chessBoards.popleft()
                board_hash = tuple(map(tuple, board.getGrid()))
                if board_hash in self.visited:
                    continue
                self.visited.add(board_hash)    
                if self.knightsMoves(board)==6:
                    print("One of the Vaild Solutions Using BFS Algorithm")
                    self.printChessboard(board.getGrid())
                    print("Solution moves is :")
                    self.printBFSSolution(board)
                    return numberOfExpandedStates
                numberOfExpandedStates += 1
            self.generateChessboard(self.buffer.popleft())
            
    def generateChessboard(self, board):
        parent = board
        board = board.getGrid()
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(8):
            for j in range(8):
                if board[i][j] != "":
                    letter = board[i][j]
                    board[i][j] = ""
                    for step in steps:
                        nx, ny = i + step[0], j + step[1]
                        if self.isValidMove(nx, ny) and board[nx][ny] == "":
                            new_board = [row[:] for row in board]  
                            new_board[nx][ny] = letter
                            new_chessboard = Grid(new_board)
                            new_chessboard.parentState = (parent,f"move {letter} to down") if step == (1, 0) else (parent,f"move {letter} to up") if step == (-1, 0) else (parent,f"move {letter} to right") if step == (0,1) else (parent,f"move {letter} to left") if step==(0,-1) else None
                            self.chessBoards.append(new_chessboard)  
                            self.buffer.append(new_chessboard)
                    board[i][j] = letter
    def printBFSSolution(self, state):
        arr = []
        move = state.parentState[1]
        while move != "":
            arr.append(move)
            state = state.parentState[0]
            move = state.parentState[1]
        for move in arr[::-1]:
            print(move)


    #===============================================================================================================================================
    #A* Solution====================================================================================================================================
    def rearrangeLettersUsingAStar(self,state):
        self.printChessboard(state.getGrid())
        print()
        print("----------------------------------------------------------------")
        self.pqueue.put((6-self.knightsMoves(state),state.getGrid()))
        numberOfExpandedStates = 1
        while not self.pqueue.empty():
            dist,state = self.pqueue.get()
            board_hash = tuple(map(tuple, state))
            if board_hash in self.visited:
                continue
            self.visited.add(board_hash)    
            if dist == 0:
                print("One of the Vaild Solutions Using A* Algorithm")
                self.printChessboard(state)
                print("Solution moves is :")
                self.printAStarSolution(self.buffer[0])
                return numberOfExpandedStates
            numberOfExpandedStates+=1
            self.generateChessboardWithKinghtMoves(Grid(state))
        return -1
                
            
    def generateChessboardWithKinghtMoves(self, board):
        parent = board
        board = board.getGrid()
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(8):
            for j in range(8):
                if board[i][j] != "":
                    letter = board[i][j]
                    board[i][j] = ""
                    for step in steps:
                        nx, ny = i + step[0], j + step[1]
                        if self.isValidMove(nx, ny) and board[nx][ny] == "":
                            new_board = [row[:] for row in board]
                            new_board[nx][ny] = letter
                            new_chessboard = Grid(new_board)
                            new_chessboard.parentState = (parent,f"move {letter} to down") if step == (1, 0) else (parent,f"move {letter} to up") if step == (-1, 0) else (parent,f"move {letter} to right") if step == (0,1) else (parent,f"move {letter} to left") if step==(0,-1) else None
                            self.buffer.append(new_chessboard)
                            self.pqueue.put((6-self.knightsMoves(new_chessboard),new_board))
                    board[i][j] = letter

    def printAStarSolution(self,state):
        s = set()
        for state in self.buffer:
            board_hash = tuple(map(tuple, state.getGrid()))
            if board_hash in self.visited and board_hash not in s:
                s.add(board_hash)
                print(state.parentState[1])
            if len(s)==len(self.visited):
                return
            
            
    #===============================================================================================================================================
#Test-case1
# arr = [
#     ["", "", "", "", "", "", "", ""],
#     ["", "B", "", "", "", "", "", ""],
#     ["", "", "A", "", "S", "", "", ""],
#     ["", "", "", "", "", "", "", ""],
#     ["", "T", "", "", "", "", "", ""],
#     ["", "", "", "", "U", "", "", ""],
#     ["", "", "", "", "", "", "", "R"],
#     ["", "", "", "", "", "", "", ""],
# ]

#Test-case2
arr = [
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "B", "", "", "", ""],
    ["", "", "A", "", "", "", "", ""],
    ["", "R", "", "", "", "", "", ""],
    ["", "", "T", "", "", "", "", ""],
    ["", "", "", "", "U", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "S", "", "", "", ""],
]


#Test-case3
# arr = [
#     ["", "", "", "", "", "", "", ""],
#     ["", "", "", "B", "", "", "", ""],
#     ["", "", "A", "", "", "", "", ""],
#     ["", "", "", "", "", "", "", ""],
#     ["", "", "", "", "", "S", "", ""],
#     ["", "", "", "", "U", "", "", ""],
#     ["T", "", "", "", "", "", "", "R"],
#     ["", "", "", "", "", "", "", ""],
# ]

board = Grid(arr)
chessboard = ChessBoard()
print("Name: Basel Turkman")
print("First six unique letters are: B,A,S,T,U,R")
print("initial State is :")
#BFS Algorithm:
# print("Number of Expanded State:",chessboard.rearrangeLettersUsingBFS(board))

#A* Algorithm:
print("Number of Expanded State:",chessboard.rearrangeLettersUsingAStar(board))