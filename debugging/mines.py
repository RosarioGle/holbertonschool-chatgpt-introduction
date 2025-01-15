#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        if mines >= width * height:
            raise ValueError("Too many mines for the given field size")
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.game_over = False
        self.remaining_cells = width * height - mines

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i % 10) for i in range(self.width)))  # Only show last digit for better alignment
        for y in range(self.height):
            print(f"{y % 10}", end=' ')  # Only show last digit for better alignment
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  # Skip the cell itself
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True  # Invalid move, but don't end game
        
        if self.revealed[y][x]:
            return True  # Already revealed
            
        self.revealed[y][x] = True
        
        if (y * self.width + x) in self.mines:
            return False  # Game over
            
        self.remaining_cells -= 1
        
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        return self.remaining_cells == 0

    def play(self):
        while not self.game_over:
            self.print_board()
            try:
                x = int(input("Enter x coordinate (0-9): "))
                y = int(input("Enter y coordinate (0-9): "))
                
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds! Please enter valid coordinates.")
                    continue
                    
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    self.game_over = True
                elif self.check_win():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won!")
                    self.game_over = True
                    
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    try:
        game = Minesweeper(width=10, height=10, mines=10)
        game.play()
    except ValueError as e:
        print(f"Error: {e}")
