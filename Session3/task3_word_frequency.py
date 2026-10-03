# Task 3: Word Frequency in WhatsApp Messages

import string


# WhatsApp messages
messages = [
    "The weather is good",
    "The food is good",
    "The service is slow",
    "Food is good and tasty"
]


# Stopwords to ignore
stopwords = {"the", "is", "at"}


# Dictionary to store word frequency
word_count = {}


# Process every message
for message in messages:

    # Convert to lowercase
    message = message.lower()

    # Remove punctuation
    message = message.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Split message into words
    words = message.split()

    # Count words
    for word in words:

        if word not in stopwords:

            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1


# Display word frequency
print("Word Frequency:")

for word, count in word_count.items():
    print(word, ":", count)