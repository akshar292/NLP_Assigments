# Task 4: Compare Naive Bayes and Logistic Regression

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
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
    "negative", "negative", "negative", "negative"
]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    reviews,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)


# Convert text into TF-IDF features
vectorizer = TfidfVectorizer()

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)


# -------------------------
# Naive Bayes
# -------------------------

nb_model = MultinomialNB()

nb_model.fit(X_train_vectorized, y_train)

nb_predictions = nb_model.predict(X_test_vectorized)

nb_accuracy = accuracy_score(y_test, nb_predictions)


# -------------------------
# Logistic Regression
# -------------------------

lr_model = LogisticRegression()

lr_model.fit(X_train_vectorized, y_train)

lr_predictions = lr_model.predict(X_test_vectorized)

lr_accuracy = accuracy_score(y_test, lr_predictions)


# Display results
print("Naive Bayes Accuracy:", nb_accuracy)
print("Logistic Regression Accuracy:", lr_accuracy)


# Compare the models
if nb_accuracy > lr_accuracy:
    print("\nNaive Bayes has higher accuracy on this test split.")

elif lr_accuracy > nb_accuracy:
    print("\nLogistic Regression has higher accuracy on this test split.")

else:
    print("\nBoth models have the same accuracy on this test split.")