#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Augmenté pour mieux correspondre à la largeur du plateau

def check_winner(board):
    # Vérification des lignes et colonnes
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":  # lignes
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":  # colonnes
            return True

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Boucle jusqu'à ce qu'un coup valide soit joué
        while True:
            try:
                print(f"Tour du joueur {player}")
                row = int(input("Entrez la ligne (0, 1, ou 2): "))
                col = int(input("Entrez la colonne (0, 1, ou 2): "))

                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Position invalide ! Les coordonnées doivent être entre 0 et 2.")
                    continue

                if board[row][col] != " ":
                    print("Cette case est déjà occupée ! Réessayez.")
                    continue

                break
            except ValueError:
                print("Entrée invalide ! Veuillez entrer un nombre.")

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Le joueur {player} gagne !")
            break

        if is_board_full(board):
            print_board(board)
            print("Match nul !")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()
