# Task 2: Zomato Review Sentiment Classification
# Using Naive Bayes

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# Zomato reviews
reviews = [
    "The food was amazing",
    "Excellent food and great taste",
    "Loved the pizza",
    "Very delicious food",
    "Amazing restaurant",
    "Great service and tasty food",
    "The food was fantastic",
    "Really enjoyed the meal",
    "Very good experience",
    "Best food I have ever eaten",

    "The food was terrible",
    "Very bad experience",
    "Food was tasteless",
    "Service was very slow",
    "I hated the food",
    "Worst restaurant experience",
    "Food quality was poor",
    "Very disappointing food",
    "The food was awful",
    "Not worth the money"
]


# Labels
labels = [
    "positive", "positive", "positive", "positive", "positive",
    "positive", "positive", "positive", "positive", "positive",

    "negative", "negative", "negative", "negative", "negative",
    "negative", "negative", "negative", "negative", "negative"
]


# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    reviews,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)


# Convert text into numerical features
vectorizer = CountVectorizer()

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)


# Create Naive Bayes model
model = MultinomialNB()


# Train model
model.fit(X_train_vectorized, y_train)


# Predict test data
predictions = model.predict(X_test_vectorized)


# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)


print("Actual Labels:", y_test)
print("Predicted Labels:", predictions)

print("\nNaive Bayes Accuracy:", accuracy)


# Test custom reviews
custom_reviews = [
    "The food was delicious",
    "The service was horrible"
]

custom_vectorized = vectorizer.transform(custom_reviews)

custom_predictions = model.predict(custom_vectorized)

print("\nCustom Review Predictions:")

for review, prediction in zip(custom_reviews, custom_predictions):
    print(review, "->", prediction)