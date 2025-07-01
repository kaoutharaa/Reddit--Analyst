 
import json
import os

STATS_FILE = "C:/xampp/folder/htdocs/application_web/projet_python/stats.json"

def init_stats():
    """Initialise le fichier stats.json s'il n'existe pas"""
    if not os.path.exists(STATS_FILE):
        stats = {
            "subreddits_analyzed": 0,
            "posts_analyzed": 0,
            "comments_collected": 0,
            "sentiment_analyses_done": 0
        }
        with open(STATS_FILE, 'w') as f:
            json.dump(stats, f, indent=4)

def update_stats(subreddits=0, posts=0, comments=0, sentiments=0):
    """Met à jour les statistiques dans le fichier stats.json"""
    init_stats()  # Assure-toi que le fichier existe
    with open(STATS_FILE, 'r') as f:
        stats = json.load(f)

    # Mise à jour des statistiques
    stats["subreddits_analyzed"] += subreddits
    stats["posts_analyzed"] += posts
    stats["comments_collected"] += comments
    stats["sentiment_analyses_done"] += sentiments

    # Sauvegarde les nouvelles valeurs dans le fichier JSON
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f, indent=4)



 
