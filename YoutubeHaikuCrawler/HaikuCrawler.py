import praw
import configs

if configs.client_id == "" or configs.client_secret == "" or configs.user_agent == "":
    SystemExit()

reddit = praw.Reddit(client_id = configs.client_id, client_secret = configs.client_secret, user_agent = configs.user_agent, redirect_uri = "http://localhost:8080")

youtubeLinks = []

for i in reddit.get("/r/youtubehaiku/hot", {"limit": 100}):
    if "reddit.com/r/youtubehaiku" in i.url:
        continue
    youtubeLinks.append(i.url)

print(youtubeLinks)