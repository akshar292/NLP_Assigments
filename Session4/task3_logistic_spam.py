# Task 3: WhatsApp Spam Detector
# Using Logistic Regression

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# WhatsApp-style messages
messages = [
    "Congratulations you won a free prize",
    "Click this link to win free money",
    "You have won a lottery prize",
    "Get free recharge now",
    "Claim your free gift today",
    "Win a free smartphone",
    "Congratulations claim your reward",
    "You are selected for a free offer",

    "Hey, are you coming to college today",
    "Please send me the notes",
    "Let's meet tomorrow",
    "What time is the class",
    "Can you call me later",
    "I am going to the market",
    "Please send the project file",
    "Are you free for lunch"
]


# Labels
labels = [
    "spam", "spam", "spam", "spam",
    "spam", "spam", "spam", "spam",

    "not spam", "not spam", "not spam", "not spam",
    "not spam", "not spam", "not spam", "not spam"
]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    messages,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels
)


# Convert text into TF-IDF features
vectorizer = TfidfVectorizer()

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)


# Create Logistic Regression model
model = LogisticRegression()


# Train model
model.fit(X_train_vectorized, y_train)


# Test data prediction
predictions = model.predict(X_test_vectorized)


# Display test predictions
print("Test Predictions:")
print(predictions)


# Three new custom messages
new_messages = [
    "You won a free mobile phone",
    "Please send me your college notes",
    "Click here to claim your free prize"
]


# Convert new messages
new_vectorized = vectorizer.transform(new_messages)


# Predict
new_predictions = model.predict(new_vectorized)


print("\nCustom Message Predictions:")

for message, prediction in zip(new_messages, new_predictions):
    print(message)
    print("Prediction:", prediction)
    print()