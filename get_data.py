import os
import pandas as pd
import praw
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
user_agent = os.getenv('USER_AGENT')

# Initialize Reddit instance using the environment variables
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Create a list to store submission data
headlines = []

# Fetch submissions from the 'Investing' subreddit
for submission in reddit.subreddit('Investing').hot(limit=None):
    headlines.append({
        'title': submission.title,
        'id': submission.id,
        'author': str(submission.author),
        'score': submission.score,
        'upvote_ratio': submission.upvote_ratio,
        'url': submission.url
    })

# Create a DataFrame from the collected data
df = pd.DataFrame(headlines)

# Display the DataFrame
print(df.head())
print(df.shape)


#save the data to a csv
df.to_csv("reddit_investing_submissions_headlines.csv")