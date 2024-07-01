class TicTacToe:
    def __init__(self):
        self.board = {
            'top-l': ' ', 'top-c': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-c': ' ', 'mid-r': ' ',
            'bot-l': ' ', 'bot-c': ' ', 'bot-r': ' ',
        }
        self.turn = 'X'
        self.move_count = 0

    def print_board(self):
        print(self.board['top-l'] + ' | ' + self.board['top-c'] + ' | ' + self.board['top-r'])
        print('--+---+--')
        print(self.board['mid-l'] + ' | ' + self.board['mid-c'] + ' | ' + self.board['mid-r'])
        print('--+---+--')
        print(self.board['bot-l'] + ' | ' + self.board['bot-c'] + ' | ' + self.board['bot-r'])

    def check_win(self):
        win_conditions = [
            ['top-l', 'top-c', 'top-r'],
            ['mid-l', 'mid-c', 'mid-r'],
            ['bot-l', 'bot-c', 'bot-r'],
            ['top-l', 'mid-l', 'bot-l'],
            ['top-c', 'mid-c', 'bot-c'],
            ['top-r', 'mid-r', 'bot-r'],
            ['top-l', 'mid-c', 'bot-r'],
            ['top-r', 'mid-c', 'bot-l'],
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                print("Congratulations! " + self.board[condition[0]] + " won!")
                return True
        if ' ' not in self.board.values():
            print("Draw!")
            return True
        return False

    def play(self):
        while self.move_count < 9:
            self.print_board()
            print(f"Turn for {self.turn}. Move to which space? (top-l, top-c, top-r, mid-l, mid-c, mid-r, bot-l, bot-c, bot-r)")
            move = input()
            if self.board.get(move) == ' ':
                self.board[move] = self.turn
                self.move_count += 1
            else:
                print("Space already taken. Try again.")
                continue
            if self.check_win():
                self.print_board()
                break
            self.turn = 'O' if self.turn == 'X' else 'X'
        else:
            print("It's a draw!")
            self.print_board()
