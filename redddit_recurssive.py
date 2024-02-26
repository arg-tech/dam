import praw
import pandas as pd

# Define a recursive function to fetch replies
def get_replies(comment):
    replies = []
    for reply in comment.replies:
        replies.append(reply.body)
        replies.extend(get_replies(reply))  # Fetch replies recursively
    return replies

# Initialize the Reddit API connection
reddit = praw.Reddit(client_id='hzaiE_jdx19eNm_itx1MTQ',
                     client_secret='yQaPXC-fu7c5zVzY88mim8xd4ktGpg',
                     user_agent='arg_tech_llm')

# Specify the subreddit (use 'all' for the entire Reddit)
subreddit = reddit.subreddit('all')

# Create an empty list to store post data
all_data = []

# Fetch posts iteratively
for submission in subreddit.top(time_filter='all', limit=None):
    data = {
        "Title": submission.title,
        "Post Text": submission.selftext,
        "ID": submission.id,
        "Score": submission.score,
        "Total Comments": submission.num_comments,
        "Post URL": submission.url,
        "Subreddit": submission.subreddit.display_name,
        "Created UTC": pd.to_datetime(submission.created_utc, unit='s'),
        "Comments": []  # Initialize an empty list to store comments
    }
    print(data['Title'])
    # Force the loading of the comment forest
    submission.comments.replace_more(limit=None)
    
    # Fetch and flatten comments, handling MoreComments
    comments = []
    for comment in praw.models.flatten_tree(submission.comments.list()):
        if isinstance(comment, praw.models.MoreComments):
            continue
        comments.append(comment.body)
        comments.extend(get_replies(comment))  # Fetch replies recursively
        print(comments)
    
    data["Comments"] = comments

    # Append data to the list
    all_data.append(data)

# Create a pandas DataFrame
all_data_df = pd.DataFrame(all_data)

# Saving the data to a CSV file
all_data_df.to_csv('reddit_data_all_recursive.csv', index=False)

# Display the DataFrame
print(all_data_df)
