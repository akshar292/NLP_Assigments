# Task 4: TF-IDF using TfidfVectorizer

from sklearn.feature_extraction.text import TfidfVectorizer


# Flipkart product reviews
reviews = [
    "The quality of this product is excellent",
    "I am happy with the quality",
    "The product quality is good and durable"
]


# Create TfidfVectorizer object
vectorizer = TfidfVectorizer()


# Transform reviews into TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(reviews)


# Get all feature names
feature_names = vectorizer.get_feature_names_out()


# Find the index of the word "quality"
quality_index = list(feature_names).index("quality")


# Display TF-IDF value for quality
print("TF-IDF value for 'quality':")

for i, review in enumerate(reviews):

    value = tfidf_matrix[i, quality_index]

    print(f"Review {i + 1}: {value:.4f}")