import json
import os

def update_analysis_data(subreddit_name, post_path, file_name="reddit_stock.json"):
 
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {
            "analyzed_subreddits": [],
            "post_paths": []
        }

    
    if subreddit_name not in data["analyzed_subreddits"]:
        data["analyzed_subreddits"].append(subreddit_name)

    if post_path not in data["post_paths"]:
        data["post_paths"].append(post_path)
 
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Added {subreddit_name} and {post_path} to {file_name}")
 