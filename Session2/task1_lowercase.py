# Task 1: Convert Instagram Bio to Lowercase

def convert_to_lowercase(bio):
    return bio.lower()


# Take Instagram bio from user
bio = input("Enter your Instagram bio: ")

# Convert bio to lowercase
result = convert_to_lowercase(bio)

# Display result
print("Original Bio:", bio)
print("Lowercase Bio:", result)