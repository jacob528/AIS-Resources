from pathlib import Path
from matplotlib import pyplot
import numpy as np
import requests
import pickle
import torch
import gzip
import math

print("Beginning program:")
print()
 
# Function to apply the logarithm to the softmax output
def log_softmax(x):
    return x - x.exp().sum(-1).log().unsqueeze(-1)

# Calculate softmax with weights and biases (@ stands for the matrix multiplication operation)
def model(xb):
    return log_softmax(xb @ weights + bias)

# Calculate the negative log likelihood (loss/cost function)
def nll(input, target):
    return -input[range(target.shape[0]), target].mean()

def accuracy(out, yb):
    preds = torch.argmax(out, dim=1)
    return (preds == yb).float().mean()

DATA_PATH = Path("data")
PATH = DATA_PATH / "mnist"

PATH.mkdir(parents=True, exist_ok=True)

URL = "https://github.com/pytorch/tutorials/raw/main/_static/"
FILENAME = "mnist.pkl.gz"

if not (PATH / FILENAME).exists():
    content = requests.get(URL + FILENAME).content
    (PATH / FILENAME).open("wb").write(content)
    print("Opened File")

with gzip.open((PATH / FILENAME).as_posix(), "rb") as f:
    ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(f, encoding="latin-1")


pyplot.imshow(x_train[0].reshape((28, 28)), cmap="gray")
# ``pyplot.show()`` only if not on Colab

"""
try:
    import google.colab
except ImportError:
    pyplot.show()
"""



#Print shape
print("Shape of training array:")
print(x_train.shape)
print()

x_train, y_train, x_valid, y_valid = map(torch.tensor, (x_train, y_train, x_valid, y_valid))

n, c = x_train.shape

print(x_train, y_train)
print(x_train.shape)

print("Y training min/max:")
print(y_train.min(), y_train.max())
print()

# Declare weights and biases (use requires gradient because we dont want the step included in the gradient)
weights = torch.randn(784, 10) / math.sqrt(784)
weights.requires_grad_()
bias = torch.zeros(10, requires_grad=True)

bs = 64  # batch size

xb = x_train[0:bs]  # a mini-batch from x
preds = model(xb)  # predictions
preds[0], preds.shape
print()
print("Predictions (Log Probabilities for digits (0-9)):")
print(preds[0], preds.shape)
print()

# Convert log probabilities to actual probabilities using torch.exp()
probs = torch.exp(preds[0])  # Exponentiate the log probabilities for the first image

# Display actual probabilities
print("\nActual probabilities (for digits 0-9):")
print(probs)

print()
# To confirm they sum to 1 (since they are probabilities)
print("\nSum of probabilities (should be close to 1):")
print(probs.sum())

loss_func = nll

print()
print("Cost/Loss Function Predictions:")
yb = y_train[0:bs]
print(loss_func(preds, yb))

print()
print("Accuracy of Model:") 
print(accuracy(preds, yb))