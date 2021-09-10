import praw

#create the reddit instance
reddit = praw.Reddit(
    client_id = "client_id",
    client_secret = "client_secret",
    password = "password",
    user_agent = "user_agent",
    username = "username")