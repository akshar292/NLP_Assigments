# Task 2: Remove Punctuation from a Product Review

import string


def remove_punctuation(review):
    cleaned_text = ""

    for char in review:
        if char not in string.punctuation:
            cleaned_text += char

    return cleaned_text


# Take product review from user
review = input("Enter your Flipkart product review: ")

# Remove punctuation
result = remove_punctuation(review)

# Display result
print("Original Review:", review)
print("Cleaned Review:", result)