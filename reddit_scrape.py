import requests
import pandas as pd
import time




headers = {"User-Agent": "Mozilla/5.0"}

# --- Collect post data ---
posts = []
uc_subreddits = [
    "Berkeley",
    "ucla",
    "UCSD",
    "UCSantaBarbara",
    "UCI",
    "UCDavis",
    "UCSC",
    "ucr",
    "ucmerced",
]


import requests, time, pandas as pd

headers = {"User-Agent": "script:ucsd-scraper:v1.0 (by u/war1ock970)"}

posts = []
seen_ids = set()  # <-- store unique Reddit post 
for uc in uc_subreddits:
    for listing in ["top", "hot", "new"]:  # cycle through listing types
        time.sleep(1)  # avoid rate limit
        url = f"https://www.reddit.com/r/{uc}/{listing}/.json?limit=100"
        response = requests.get(url, headers=headers)
        data = response.json()

        # Skip if subreddit returned error or empty
        if "data" not in data or "children" not in data["data"]:
            continue

        for post in data["data"]["children"]:
            post_data = post["data"]
            post_id = post_data.get("id")

            if post_id in seen_ids:
                continue
            seen_ids.add(post_id)
            post_data = post["data"]

            posts.append({
                "subreddit": uc,
                "listing": listing,
                "title": post_data.get("title"),
                "author": post_data.get("author"),
                "upvotes": post_data.get("ups"),
                "post_text": post_data.get("selftext"),
                "upvote_ratio": post_data.get("upvote_ratio"),
                "total_awards_received": post_data.get("total_awards_received"),
                "score": post_data.get("score"),
                "edited": post_data.get("edited"),
                "num_comments": post_data.get("num_comments"),
                "is_self": post_data.get("is_self"),
                "is_video": post_data.get("is_video"),
                "over_18": post_data.get("over_18"),
                "domain": post_data.get("domain"),
                "link_flair_text": post_data.get("link_flair_text"),
                "created_utc": post_data.get("created_utc"),
                "subreddit_subscribers": post_data.get("subreddit_subscribers"),
                "author_premium": post_data.get("author_premium"),
                "stickied": post_data.get("stickied"),
                "has_media": "preview" in post_data,
                "permalink": "https://www.reddit.com" + post_data.get("permalink", ""),
                "url": post_data.get("url")
            })
    df = pd.DataFrame(posts)        
    df.to_csv(f"{uc}.csv", index=False)
    print(uc)

