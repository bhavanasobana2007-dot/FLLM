# Simple Tokenization

text = "I love learning AI"

tokens = text.split()

print("Original Text:", text)
print("Tokens:", tokens)

# Simple Embedding

embedding = {
    "I": [0.1, 0.2],
    "love": [0.8, 0.6],
    "learning": [0.4, 0.9],
    "AI": [0.7, 0.3]
}

word = "AI"

print("Word:", word)
print("Embedding:", embedding[word])


import numpy as np

# Embedding Matrix
matrix = np.array([
    [0.1, 0.2],
    [0.8, 0.6],
    [0.4, 0.9],
    [0.7, 0.3]
])

print("Embedding Matrix:")
print(matrix)

# Simple Attention

words = ["I", "love", "AI"]

attention_scores = [0.2, 0.3, 0.5]

print("Attention Scores")

for word, score in zip(words, attention_scores):
    print(word, "->", score)
