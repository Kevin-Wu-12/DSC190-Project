# 🎓 UC Subreddit Upvote Prediction

This project analyzes Reddit posts from various **University of California subreddits** to predict how many upvotes a post will receive based on its content, metadata, and engagement features.  
It uses real Reddit data scraped from public endpoints, covering posts from **top**, **hot**, and **new** listings for each UC campus.

---

## 📘 Overview
The goal of this project is to explore what factors influence post popularity on UC subreddits and build a machine learning model to predict **upvote counts**.

Using features such as title length, post type, media presence, NSFW status, and subreddit activity levels, we aim to identify patterns that drive engagement within different UC communities.

---

## 🧠 Data Collection
Data was collected directly from Reddit’s public JSON API:

Subreddits included:
- r/UCSD  
- r/UCLA  
- r/Berkeley  
- r/UCSantaBarbara  
- r/UCI  
- r/UCDavis  
- r/UCSC  
- r/ucr  
- r/ucmerced  

Each subreddit was scraped for posts in the `top`, `hot`, and `new` listings.  
Duplicates were removed, and each UC’s data was saved separately (e.g., `UCSD.csv`, `UCLA.csv`) and combined into one master dataset `UC_subreddits_posts.csv`.

---

## 📊 Dataset Information
Each post contains the following features:

| Feature | Description |
|----------|-------------|
| `subreddit` | Name of the UC subreddit |
| `listing` | Listing type (`top`, `hot`, `new`) |
| `title` | Post title |
| `author` | Reddit username |
| `upvotes` | Total number of upvotes (target variable) |
| `upvote_ratio` | Ratio of upvotes to total votes |
| `num_comments` | Number of comments on the post |
| `over_18` | NSFW flag |
| `is_video` | Whether the post includes a video |
| `has_media` | Whether the post includes images/media |
| `score` | Reddit-calculated post score |
| `created_utc` | Timestamp of creation (UTC) |
| `author_premium` | Whether the author is a premium user |
| `link_flair_text` | Post flair category |
| `subreddit_subscribers` | Number of subscribers to that subreddit |
