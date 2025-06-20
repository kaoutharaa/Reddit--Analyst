
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import csv
import os
from tkinter import scrolledtext, messagebox, filedialog
import tkinter.font as font
from model_function import resultat
from visualisation import visualisation_fct
from state_manager import update_stats
from state2_manager import update_analysis_data
import praw
import re
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import os
from PIL import Image, ImageTk   
import sys
sys.stdout.reconfigure(encoding='utf-8')


 
reddit = praw.Reddit(
    client_id="_XSiH1rREA1oRh7SyRXXNA",
    client_secret="fo9sZoMq8jXiq13e8tUm7xKWEqT2Yg",
    user_agent="test_api",
    username="Ok-Cicada-6705",
    password="pookie123"
)

 
import re

def remove_bot_messages(comments):
    pattern = re.compile(r"I am a bot, and this action was performed automatically\..*contact the moderators of this subreddit.*", re.IGNORECASE)
    return [comment for comment in comments if not pattern.search(comment)]

def fetch_comments(subreddit_name, n):
    comments = []
    try:
        subreddit = reddit.subreddit(subreddit_name)
        _ = subreddit.id  
        for comment in subreddit.comments(limit=n):
            comments.append(comment.body)
        comments = remove_bot_messages(comments)
    except Exception as e:
        print(f"❌ Erreur lors de la récupération des commentaires : {e}")
        
    return comments


 
def reddit_comments(subreddit, n):
    filename = 'C:/xampp/folder/htdocs/application_web/projet_python/web_data_comment.csv'
    
    try:
        n = int(n)
        if n <= 0:
            print("❌ Le nombre de commentaires doit être supérieur à zéro.")
            return None
    except ValueError:
        print("❌ Valeur invalide pour le nombre de commentaires.")
        return None

    comments = fetch_comments(subreddit, n)
     
 

 
    if not comments:
        print("❌ Aucun commentaire trouvé ou une erreur est survenue.")
        return None
 
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for comment in comments:
            writer.writerow([comment])
    
    
    print("✅ Commentaires récupérés et sauvegardés !")
    print(f"🔍 {len(comments)} commentaires enregistrés.")
    
    image_path = visualisation_fct(filename, subreddit)
    
    if image_path:
        print(f"✅ Image générée : {image_path}")
    else:
        print("❌ Image non générée dans visualisation_fct()")
        
    return image_path
 


def fct(file_path):
    try:
        
        data = pd.read_csv(file_path, encoding="ISO-8859-1")  

        
        if data.shape[1] == 1:
            print("✅ Dataset chargé avec succès !")
            return data
        else:
            messagebox.showwarning("Erreur", "⚠️ Le fichier doit contenir UNE SEULE colonne ! Réessayez.")
            return None   
    except Exception as e:
        messagebox.showerror("Erreur", f"❌ Erreur lors du chargement du fichier : {e}. Réessayez.")
        return None  

 
    
def clean_column(text):
       text = re.sub(r"http\S+|www\S+", "", text)
       text = re.sub(r"@\w+", "", text)
       text = re.sub(r"#\w+", "", text)
       text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
       text = re.sub(r"\s+", " ", text).strip()
       return text
   
 
 

def visualisation_fct(path, subreddit):
    data = fct(path)
    if data is None:
        return None   

    data.columns = ['texte']
    data.dropna(inplace=True)
    data['texte'] = data['texte'].apply(clean_column)
    print(data.head())
    texts = data['texte'].tolist()

   
    model_path = "C:/xampp/folder/htdocs/application_web/projet_python/model.ipynb/Logistic_Regression.pkl"
    vectorizer_path = "C:/xampp/folder/htdocs/application_web/projet_python/model.ipynb/vectorizer.pkl"
    loaded_model = joblib.load(model_path)
    loaded_vectorizer = joblib.load(vectorizer_path)

    X_new = loaded_vectorizer.transform(texts)
    predictions = loaded_model.predict(X_new)
    unique, counts = np.unique(predictions, return_counts=True)

 
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
 
    df_plot = pd.DataFrame({
        "Sentiment": ["Négatif", "Positif"],
        "Count": counts
    })
 
    sns.barplot(data=df_plot, x="Sentiment", y="Count", hue="Sentiment", palette=["red", "green"], legend=False, ax=axs[0])

    axs[0].set_xlabel("Sentiment")
    axs[0].set_ylabel("Nombre de commentaires")
    axs[0].set_title("Répartition des sentiments")

    axs[1].pie(counts, labels=["Négatif", "Positif"], autopct='%1.1f%%', colors=["red", "#06da9b"])
    axs[1].set_title("Pourcentage des sentiments")

    positive_texts = " ".join(np.array(texts)[predictions == 1])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(positive_texts)
    axs[2].imshow(wordcloud, interpolation="bilinear")
    axs[2].axis("off")
    axs[2].set_title("Nuage de mots des commentaires positifs")
 
    output_path = f"C:/xampp/folder/htdocs/application_web/projet_python/visualiation_web.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

   
    plt.savefig(output_path)
    print(f"✅ Image sauvegardée à : {output_path}")
    

 
    return output_path
print(r"C:\xampp\htdocs\application_web\projet_python\visualiation_web.png")
 
 
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        subreddit_arg = sys.argv[1]
        try:
            n = int(sys.argv[2])   
            image_path = reddit_comments(subreddit_arg, n)
            if image_path:
                print(image_path)
            else:
                print("❌ Erreur: Aucun chemin d’image retourné.")
        except ValueError:
            print("❌ Erreur : le deuxième argument doit être un nombre entier.")
        except Exception as e:
            print(f"❌ Exception capturée : {e}")
    else:
        print("❌ Arguments insuffisants. Utilisation : python script.py <subreddit> <nombre_commentaires>")


 
 