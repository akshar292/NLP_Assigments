# Task 1: Load IPL Tweets Dataset

import pandas as pd


# Load IPL tweets CSV file
df = pd.read_csv("ipl_tweets.csv")


# Display first 10 tweets
print("First 10 IPL Tweets:")
print(df.head(10))