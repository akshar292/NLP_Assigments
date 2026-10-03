# Task 3: Sentiment Analysis using Hugging Face

from transformers import pipeline


# Create sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")


# Three food delivery app reviews
reviews = [
    "The food was delicious and delivery was very fast.",
    "The food was cold and the delivery was very late.",
    "Amazing taste and excellent service!"
]


# Analyze each review
for review in reviews:

    result = sentiment_analyzer(review)

    print("Review:", review)
    print("Sentiment:", result[0]["label"])
    print("Score:", round(result[0]["score"], 4))
    print()