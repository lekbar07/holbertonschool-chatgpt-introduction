#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set()
        while len(self.mines) < mines:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            self.mines.add((x, y))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(f'{i:2}' for i in range(self.width)))
        for y in range(self.height):
            print(f'{y:2} ', end='')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (x, y) in self.mines:
                        print('* ', end='')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f'{count if count > 0 else " "} ', end='')
                else:
                    print('. ', end='')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (nx, ny) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (x, y) in self.mines:
            return False
        if self.revealed[y][x]:
            return True
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < self.width) and (0 <= ny < self.height):
                        if not self.revealed[ny][nx]:
                            self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate (0-{}): ".format(self.width - 1)))
                y = int(input("Enter y coordinate (0-{}): ".format(self.height - 1)))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds.")
                    continue
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("💥 Game Over! You hit a mine.")
                    break
                # Optional: check win condition
                if self.check_win():
                    self.print_board(reveal=True)
                    print("🎉 Congratulations! You cleared the minefield.")
                    break
            except ValueError:
                print("Invalid input. Please enter integers only.")

    def check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if not self.revealed[y][x] and (x, y) not in self.mines:
                    return False
        return True

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

