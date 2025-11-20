import math

class JogoDaVelhaMinimax:
    def __init__(self):
        # O tabuleiro é uma lista de 9 espaços
        self.board = [' ' for _ in range(9)]
        self.human = 'X'
        self.ai = 'O'

    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6: print("-" * 9)
        print()

    def is_winner(self, player):
        # Todas as combinações de vitória (linhas, colunas, diagonais)
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Colunas
            (0, 4, 8), (2, 4, 6)             # Diagonais
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] == player:
                return True
        return False

    def is_draw(self):
        return ' ' not in self.board

    def minimax(self, board, depth, is_maximizing):
        # 1. Casos Base (Fim de Jogo)
        if self.is_winner(self.ai):
            return 10 - depth # IA ganha (prefere ganhar rápido)
        if self.is_winner(self.human):
            return -10 + depth # Humano ganha
        if ' ' not in board:
            return 0 # Empate

        # 2. Turno da IA (Maximizar pontuação)
        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if board[i] == ' ':
                    board[i] = self.ai
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ' ' # Desfaz o movimento (Backtracking)
                    best_score = max(score, best_score)
            return best_score

        # 3. Turno do Humano (Minimizar pontuação da IA)
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == ' ':
                    board[i] = self.human
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ' ' # Desfaz o movimento
                    best_score = min(score, best_score)
            return best_score

    # Função que chama o Minimax para decidir a jogada real
    def best_move(self):
        best_score = -math.inf
        move = -1
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = self.ai
                score = self.minimax(self.board, 0, False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
        return move

    # --- Loop do Jogo ---
    def play(self):
        print("Você é o X. A IA é o O (Invencível).\n")
        while True:
            self.print_board()
            
            # Turno do Jogador
            try:
                move = int(input("Escolha sua posição (0-8): "))
                if self.board[move] != ' ':
                    print("Posição ocupada! Tente outra.")
                    continue
            except (ValueError, IndexError):
                print("Entrada inválida.")
                continue
                
            self.board[move] = self.human

            if self.is_winner(self.human):
                self.print_board()
                print("Você venceu! (Isso não deveria acontecer...)")
                break
            if self.is_draw():
                self.print_board()
                print("Empate!")
                break

            # Turno da IA
            print("IA pensando...")
            ai_move = self.best_move()
            self.board[ai_move] = self.ai

            if self.is_winner(self.ai):
                self.print_board()
                print("A IA venceu!")
                break
            if self.is_draw():
                self.print_board()
                print("Empate!")
                break

# Rodar o jogo
if __name__ == "__main__":
    game = JogoDaVelhaMinimax()
    game.play()