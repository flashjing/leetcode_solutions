class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        X = sum([row.count('X') for row in board])
        O = sum([row.count('O') for row in board])
        
        def win(char):
            target = char * 3
            for row in board:
                if row == target: return True
            for j in range(3):
                col = "".join(board[i][j] for i in range(3))
                if col == target: return True
            diag = "".join(board[i][i] for i in range(3))
            anti_diag = "".join(board[i][2-i] for i in range(3))
            
            return target in [diag, anti_diag]
        
        winX = win('X')
        winO = win('O')
        
        if winX and winO:       return False # case 1: if X won and O won
        if winX and X - O != 1: return False # case 2: if X won, then there must be one more X than O
        if winO and X - O != 0: return False # case 3: if O won, then there must be the same amount of X and O
        return X - O in [0, 1]               # case 4: if no winner, then there must be the same amount of X and O xor one more X than O