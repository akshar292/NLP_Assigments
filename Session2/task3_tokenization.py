# Task 3: Tokenization of a Zomato Food Description


# Take food description from user
food_description = input("Enter your Zomato food description: ")

# Split sentence into individual words
tokens = food_description.split()

# Display tokens
print("Original Description:", food_description)
print("Tokens:", tokens)