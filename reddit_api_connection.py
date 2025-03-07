import praw
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT


class RedditAPI:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT
        )

    def get_posts(self, subreddit_name, limit=10):
        subreddit = self.reddit.subreddit(subreddit_name)
        return [submission.title + " " + submission.selftext for submission in subreddit.hot(limit=limit)]

