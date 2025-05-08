class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(25)]
        # Tạo một list biểu diễn bảng 5x5

    def print_board(self):
        for i in range(5):
            print('|'.join(self.board[i*5:(i+1)*5]))
            if i < 4:
                print('-' * 9)

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def is_winner(self, symbol):
        win_conditions = [
            (0, 1, 2, 3, 4), 
            (5, 6, 7, 8, 9), 
            (10, 11, 12, 13, 14), 
            (15, 16, 17, 18, 19), 
            (20, 21, 22, 23, 24),
            (0, 5, 10, 15, 20), 
            (1, 6, 11, 16, 21), 
            (2, 7, 12, 17, 22), 
            (3, 8, 13, 18, 23), 
            (4, 9, 14, 19, 24),
            (0, 6, 12, 18, 24), 
            (4, 8, 12, 16, 20)
        ]
        for condition in win_conditions:
            if all(self.board[i] == symbol for i in condition):
                return True
        return False

    def alpha_beta(self, maximizing_player, depth, alpha, beta, max_depth=5):
      if self.is_winner('O'):
          return 10 - depth
      if self.is_winner('X'):
          return depth - 10
      if ' ' not in self.board:
          return 0
      if depth >= max_depth:  # Giới hạn độ sâu của tìm kiếm
          return 0

      if maximizing_player:
          max_eval = float('-inf')
          for move in self.available_moves():
              self.board[move] = 'O'
              eval = self.alpha_beta(False, depth + 1, alpha, beta, max_depth)
              self.board[move] = ' '
              max_eval = max(max_eval, eval)
              alpha = max(alpha, eval)
              if beta <= alpha:
                  break
          return max_eval
      else:
          min_eval = float('inf')
          for move in self.available_moves():
              self.board[move] = 'X'
              eval = self.alpha_beta(True, depth + 1, alpha, beta, max_depth)
              self.board[move] = ' '
              min_eval = min(min_eval, eval)
              beta = min(beta, eval)
              if beta <= alpha:
                  break
          return min_eval


    def find_best_move(self):
        best_move = -1
        best_eval = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        max_depth = 5  # Đặt giới hạn độ sâu để tránh treo máy

        for move in self.available_moves():
            self.board[move] = 'O'
            eval = self.alpha_beta(False, 0, alpha, beta, max_depth)
            self.board[move] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = move
        return best_move

    def get_adjacent_cells(self, index):
        """Lấy danh sách ô lân cận của một vị trí"""
        neighbors = []
        row, col = index // 5, index % 5
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                neighbors.append(nr * 5 + nc)
        return neighbors


if __name__ == "__main__":
    game = TicTacToe()
    game.print_board()
    while ' ' in game.board:
        try:
            user_move = int(input('Enter your move (0-24): '))
            if user_move not in game.available_moves():
                print('Invalid move. Try again.')
                continue
            game.board[user_move] = 'X'
        except ValueError:
            print('Please enter a valid number between 0 and 24.')
            continue

        game.print_board()
        if game.is_winner('X'):
            print('You win!')
            break
        if ' ' not in game.board:
            print('Draw!')
            break

        print('AI is making a move...')
        ai_move = game.find_best_move()
        game.board[ai_move] = 'O'
        game.print_board()
        if game.is_winner('O'):
            print('AI wins!')
            break
        if ' ' not in game.board:
            print('Draw!')
            break
