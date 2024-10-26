import chess
import chess.engine
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

#Function to generate a random board for neural network to analyze
def generate_board():
    print("Generating random board:")
    board = chess.Board()
    maxdepth = 10
    for move in board.legal_moves:
        board.push(move)
        print()
        print("Move:", move)
        print(board)
        board.pop()

#Main Function
if __name__ == "__main__":
    values = {
        "pawn" : 1,
        "bishop" : 3,
        "knight" : 3,
        "rook" : 5,
        "queen" : 9,
    }

    generate_board()

