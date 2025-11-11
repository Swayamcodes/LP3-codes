class NQBacktracking:
    def __init__(self, x_, y_):
        """Initialize helper arrays and first queen position"""
        self.ld = [0] * 30   # left diagonal
        self.rd = [0] * 30   # right diagonal
        self.cl = [0] * 30   # columns
        self.x = x_          # row of first queen
        self.y = y_          # column of first queen

    def printSolution(self, board):
        """Print the final board solution"""
        print(
            "\nN Queen Backtracking Solution:",
            f"\nGiven initial position of 1st queen at row: {self.x}, column: {self.y}\n",
        )
        for line in board:
            print(" ".join(map(str, line)))

    def solveNQUtil(self, board, col, N):
        """Recursive utility function to solve N-Queen problem"""
        if col >= N:
            return True

        # Skip the column where the first queen is already placed
        if col == self.y:
            return self.solveNQUtil(board, col + 1, N)

        for i in range(N):
            if i == self.x:  # Skip row of first queen
                continue

            # Check if queen can be placed
            if (self.ld[i - col + N - 1] != 1 and
                self.rd[i + col] != 1 and
                self.cl[i] != 1):

                # Place queen
                board[i][col] = 1
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 1

                # Recur to place rest of the queens
                if self.solveNQUtil(board, col + 1, N):
                    return True

                # Backtrack
                board[i][col] = 0
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 0

        return False

    def solveNQ(self, N):
        """Main function to set up the board and solve"""
        board = [[0 for _ in range(N)] for _ in range(N)]
        board[self.x][self.y] = 1  # Place first queen

        self.ld[self.x - self.y + N - 1] = self.rd[self.x + self.y] = self.cl[self.x] = 1

        if not self.solveNQUtil(board, 0, N):
            print("\nSolution does not exist for the given position.")
            return False
        self.printSolution(board)
        return True


# ---------------------------
# USER INPUT SECTION
# ---------------------------
if __name__ == "__main__":
    N = int(input("Enter the size of the chessboard (N): "))
    x = int(input("Enter the row of the first queen (0-indexed): "))
    y = int(input("Enter the column of the first queen (0-indexed): "))

    if x >= N or y >= N or x < 0 or y < 0:
        print("Invalid position! Row and column must be between 0 and N-1.")
    else:
        NQBt = NQBacktracking(x, y)
        NQBt.solveNQ(N)





# import time

# def solveNqueens(n:int,first_queen_col:int):
#     col=set()
#     posDiag=set()
#     negDiag=set()

#     res=[]
#     board=[['.']* n for _ in range(n)]
    
#     def backtrack(r):
#         if(r==n):
#             res.append([''.join(row) for row in board])
#             return
#         for c in range(n):
#             if c in col or (r+c) in posDiag or (r-c) in negDiag:
#                 continue
#             col.add(c)
#             posDiag.add(r+c)
#             negDiag.add(r-c)
#             board[r][c]="Q"

#             backtrack(r+1)
#             col.remove(c)
#             posDiag.remove(r+c)
#             negDiag.remove(r-c)
#             board[r][c]="."
#     col.add(first_queen_col)
#     posDiag.add(0+first_queen_col)
#     negDiag.add(0-first_queen_col)
#     board[0][first_queen_col]="Q"

#     backtrack(1)
#     return res

# if __name__=="__main__":
#     n=8
#     print('=' * 50) 
#     print("8-Queens Problem Using Backtracking") 
#     print('=' * 50) 
     
#     first_queen_col = int(input("\nEnter the column position (0–7) for the first queen: ")) 
#     print('-' * 50) 
     
#     if first_queen_col < 0 or first_queen_col >= n: 
#         print("\nInvalid column position. Please enter a value between 0 and 7.\n") 
#         exit(1) 
         
#     print(f"\nSolving {n}-Queens problem with first queen at column {first_queen_col} :\n") 
     
#     start_time = time.time() 
 
#     solutions = solveNqueens(n, first_queen_col) 
     
#     end_time = time.time() 
 
#     if not solutions: 
#         print("No valid solutions found for this initial queen position.") 
#     else: 
#         print("All Possible Solutions:\n") 
#         for idx, board in enumerate(solutions, 1): 
#             print(f"Solution {idx}:") 
#             for row in board: 
#                 print(" ".join(row)) 
#             print() 
 
#         print("Total Solutions Found:", len(solutions)) 
#         print(f"Execution Time: {end_time - start_time:.16f} seconds\n\n") 