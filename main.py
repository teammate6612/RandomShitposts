import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id="aPee9PV4m46RnXhZy2OFIg",
                               client_secret="GfpuhUwyQM2Ll2j3CmKumCyvD34x_A",
                               user_agent="RandomShitposts")

subreddit = reddit_read_only.subreddit("shitposts")

# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)

# Display the title of the Subreddit
print("Title:", subreddit.title)

# Display the description of the Subreddit
print("Description:", subreddit.description)

posts = subreddit.top(time_filter="month")
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [], "Post URL": []}

for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)

    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)

    # URL of each post
    posts_dict["Post URL"].append(post.url)

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
print(top_posts)
import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id="aPee9PV4m46RnXhZy2OFIg",
                               client_secret="GfpuhUwyQM2Ll2j3CmKumCyvD34x_A",
                               user_agent="RandomShitposts")

subreddit = reddit_read_only.subreddit("shitposts")

# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)

# Display the title of the Subreddit
print("Title:", subreddit.title)

# Display the description of the Subreddit
print("Description:", subreddit.description)

posts = subreddit.top(time_filter="month")
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [], "Post URL": []}

for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)

    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)

    # URL of each post
    posts_dict["Post URL"].append(post.url)

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
print(top_posts)
