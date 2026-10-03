# Task 5: Flipkart Review Classification
# Using TF-IDF and Logistic Regression

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Flipkart product reviews
reviews = [
    "Excellent product and amazing quality",
    "Very good product",
    "I loved this product",
    "Great quality and useful product",
    "Product is amazing",
    "Very happy with my purchase",
    
    "Very bad product",
    "Poor quality product",
    "I hated this product",
    "Worst product ever",
    "Product stopped working",
    "Very disappointing purchase"
]


# Labels
labels = [
    "positive",
    "positive",
    "positive",
    "positive",
    "positive",
    "positive",
    
    "negative",
    "negative",
    "negative",
    "negative",
    "negative",
    "negative"
]


# Create TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(reviews)


# Create Logistic Regression model
model = LogisticRegression()

# Train model
model.fit(X, labels)


# Two sample reviews
test_reviews = [
    "The product quality is excellent",
    "Very poor product and bad quality"
]


# Convert test reviews
test_vectors = vectorizer.transform(test_reviews)


# Predict sentiment
predictions = model.predict(test_vectors)


# Display results
print("Flipkart Review Predictions:")
print()

for review, prediction in zip(test_reviews, predictions):
    print("Review:", review)
    print("Sentiment:", prediction)
    print()