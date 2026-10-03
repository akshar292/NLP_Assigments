# Task 2: Bag of Words using CountVectorizer

from sklearn.feature_extraction.text import CountVectorizer


# Zomato food reviews
reviews = [
    "Loved the pizza",
    "Service was slow",
    "Great ambience"
]


# Create CountVectorizer object
vectorizer = CountVectorizer()


# Convert reviews into Bag of Words matrix
bow_matrix = vectorizer.fit_transform(reviews)


# Display vocabulary
print("Vocabulary:")
print(vectorizer.get_feature_names_out())


# Display Bag of Words matrix
print("\nBag of Words Matrix:")
print(bow_matrix.toarray())