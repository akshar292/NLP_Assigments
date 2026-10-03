# Task 5: Stemming using PorterStemmer

from nltk.stem import PorterStemmer


# Create PorterStemmer object
stemmer = PorterStemmer()


# List of trending hashtags
hashtags = ["#playing", "#dancing", "#eating"]


print("Original\tStemmed")
print("------------------------")


# Stem each hashtag
for hashtag in hashtags:

    # Remove # symbol
    word = hashtag.replace("#", "")

    # Apply stemming
    stemmed_word = stemmer.stem(word)

    # Display original and stemmed word
    print(hashtag, "\t\t", stemmed_word)