# Task 4: Remove Stopwords from WhatsApp Message

from nltk.corpus import stopwords


# Get English stopwords
stop_words = set(stopwords.words("english"))


def remove_stopwords(message):
    words = message.split()

    filtered_words = []

    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(word)

    return " ".join(filtered_words)


# Take WhatsApp message from user
message = input("Enter your WhatsApp message: ")

# Remove stopwords
result = remove_stopwords(message)

# Display result
print("Original Message:", message)
print("After Removing Stopwords:", result)