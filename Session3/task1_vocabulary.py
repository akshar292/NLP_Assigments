# Task 1: Create Vocabulary from Instagram Captions

import string


# Three Instagram captions
captions = [
    "I love traveling and exploring new places!",
    "Traveling with friends makes life beautiful.",
    "Exploring new places and trying new food."
]


# Create an empty set for unique words
vocabulary = set()


# Process each caption
for caption in captions:

    # Convert to lowercase
    caption = caption.lower()

    # Remove punctuation
    caption = caption.translate(str.maketrans("", "", string.punctuation))

    # Split into words
    words = caption.split()

    # Add words to vocabulary
    vocabulary.update(words)


# Convert set to sorted list
vocabulary = sorted(vocabulary)


# Display vocabulary
print("Vocabulary:")
print(vocabulary)

print("\nTotal Unique Words:", len(vocabulary))