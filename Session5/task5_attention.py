# Task 5: Basic Attention Mechanism Example

import math


def attention_scores(query, keys):
    """
    Calculate simple attention scores using dot product.
    """

    scores = []

    for key in keys:

        # Dot product
        score = sum(q * k for q, k in zip(query, key))

        scores.append(score)

    # Convert scores into attention weights using softmax
    exp_scores = [math.exp(score) for score in scores]

    total = sum(exp_scores)

    attention_weights = [
        score / total for score in exp_scores
    ]

    return scores, attention_weights


# Three short sentences represented by simple vectors
sentences = [
    "I love pizza",
    "Pizza is delicious",
    "The weather is good"
]


# Simple numerical representations
keys = [
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 0]
]


# Query representing the word/context we are interested in
query = [1, 1, 1]


# Calculate attention
scores, weights = attention_scores(query, keys)


# Display results
print("Attention Scores:")
print()

for sentence, score, weight in zip(sentences, scores, weights):

    print("Sentence:", sentence)
    print("Raw Score:", score)
    print("Attention Weight:", round(weight, 4))
    print()