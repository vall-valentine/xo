import tkinter as tk


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()  # Создание окна
        self.root.title("Tic-Tac-Toe")
        self.canvas = tk.Canvas(self.root, width=300, height=400)
        self.canvas.pack()
        self.draw_board()
        self.board = [["" for _ in range(3)] for _ in range(3)]  # Инициализация поля
        self.turn = "X"  # Установка начального хода

    def draw_board(self):
        for i in range(1, 3):
            self.canvas.create_line(100 * i, 0, 100 * i, 300)  # Отрисовка  линий
            self.canvas.create_line(0, 100 * i, 300, 100 * i)
        self.canvas.create_line(0, 100 * 3, 300, 100 * 3)

    def on_click(self, event):  # Oбрабатывает клики мыши
        row = event.y // 100
        col = event.x // 100
        if self.board[row][col] == "":
            self.board[row][col] = self.turn
            self.draw_move(row, col)
            winner = self.check_winner()
            if winner:
                self.show_winner(winner)
            elif all(self.board[i][j] != "" for i in range(3) for j in range(3)):
                self.show_draw()
            else:
                self.turn = "O" if self.turn == "X" else "X"  # Смена хода

    def draw_move(self, row, col):
        x = col * 100 + 50
        y = row * 100 + 50
        self.canvas.create_text(x, y, text=self.turn, font=("Arial", 50))

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]
        return None

    def restart(self):
        self.root.destroy()
        self.root = tk.Tk()  # Создание окна
        self.root.title("Tic-Tac-Toe")
        self.canvas = tk.Canvas(self.root, width=300, height=400)
        self.canvas.pack()
        self.draw_board()
        self.board = [["" for _ in range(3)] for _ in range(3)]  # Инициализация поля
        self.turn = "X"  # Установка начального хода
        self.root.bind("<Button-1>", game.on_click)
        self.root.mainloop()

    def show_winner(self, winner):
        self.canvas.create_text(70, 350, text=f"{winner} wins!", font=("Arial", 30))
        btn = tk.Button(text="Restart", command=self.restart, height=2, width=7)
        btn.place(x=200, y=330)

    def show_draw(self):
        self.canvas.create_text(120, 350, text="It's a draw!", font=("Arial", 30))
        btn = tk.Button(text="Restart", command=self.restart, height=2, width=7)
        btn.place(x=215, y=330)

    # запуск главного цикла обработки событий


game = TicTacToe()
game.root.bind("<Button-1>", game.on_click)  # Привязка обработчика события клика мыши к методу
game.root.mainloop()  # Запуск игрового цикла
