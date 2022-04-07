# index of each cell in a 3*3 matrix
# (0, 0), (0, 1), (0, 2)
# (1, 0), (1, 1), (1, 2)
# (2, 0), (2, 1), (2, 2)

# (1) check valid board
# 0 <= x_count - o_count <= 1
# (2) check winner
# each row or col or diag or anti_diag == player

class TicTacToe:
    def __init__(self, n):
        self.n = n # n * n board
        self.rows = [0] * n # count in each row
        self.cols = [0] * n # count in each col
        self.diag = 0 # count in diagnol
        self.anti_diag = 0 # count in anti-diagnol
        self.total_moves = 0 # track total moves

    def move(self, row, col, player):
        # assign score 1 to player 1 and score -1 to player 2
        score = 1 if player == 1 else -1

        # update the count in row, col
        self.rows[row] += score
        self.cols[col] += score

        # update the count in diag and anti-diag
        if row == col:
            self.diag += score
        if row + col + 1 == self.n:
            self.anti_diag += score

        # update the total moves
        self.total_moves += 1

        # check whether there is winner
        if (self.n * score) in [self.rows[row], self.cols[col], self.diag, self.anti_diag]:
            return f'The winner is {player}.'

        # check if it is draw
        if self.total_moves == (self.n * self.n):
            return 'Draw'

        else:
            return 'Pending'

test = TicTacToe(3)
print(test.move(0, 0, 1))
print(test.move(0, 1, 2))
print(test.move(0, 2, 1))
print(test.move(1, 0, 2))
print(test.move(1, 1, 1))
print(test.move(2, 0, 2))
print(test.move(2, 1, 1))
print(test.move(2, 2, 2))
print(test.move(1, 2, 1))



         
