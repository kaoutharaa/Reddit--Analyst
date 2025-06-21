
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import csv
import os
import tkinter as tk
import os
from tkinter import ttk
from tkinter import scrolledtext
import tkinter.font as font
from tkinter import filedialog
from model_function import resultat
from visualisation import visualisation_fct
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from wordcloud import WordCloud
from tkinter import messagebox
from PIL import Image, ImageTk
from state_manager import update_stats
from state2_manager import update_analysis_data
import praw

reddit = praw.Reddit(
    client_id="",  
    client_secret="",   
    user_agent="test_api",  
    username="",   
    password=""  
)
 
REDDIT_BG_COLOR = "#DAE0E6"
REDDIT_HEADER_BG = "#FF4500"
REDDIT_TEXT_COLOR = "#222222"
REDDIT_BUTTON_BG = "#FF8C00"
REDDIT_BUTTON_FG = "white"
REDDIT_BUTTON_HOVER_BG = "#FF6347"
REDDIT_BUTTON_ACTIVE_BG = "#E64A19"
REDDIT_FONT_HEADER = ("Segoe UI", 18, "bold")
REDDIT_FONT_NORMAL = ("Segoe UI", 12, "bold")


def fetch_comments(subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    comments = []

     
    for comment in subreddit.comments(limit=limit):
        comments.append(comment.body)

    return comments

 
image_label = None


def reddit_comments(subreddit, parent_window):
    """Displays Reddit comments and a visualization button."""

    filename = 'C://xampp//folder//htdocs//application_web//projet_python//reddit_data_comments.csv'
    comments = fetch_comments(subreddit, 100)
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for comment in comments:
            writer.writerow([comment])

    frame = tk.Frame(parent_window, bg=REDDIT_BG_COLOR)
    frame.pack(fill="both", expand=True)

    result_text = tk.Text(frame, wrap="word", width=80, height=10, bg="white", fg=REDDIT_TEXT_COLOR,
                           font=REDDIT_FONT_NORMAL) # Réduction de la hauteur du texte
    result_text.pack(pady=10, padx=10, fill="x")

    if comments:
        result_text.delete("1.0", tk.END)
        for i, comment in enumerate(comments, 1):
            result_text.insert(tk.END, f"{i}. {comment}\n\n")
    else:
        result_text.insert(tk.END, "No comments found or an error occurred.", fg="red")

    def show_visualisation():
        global image_label
        image_path = visualisation_fct(
            "C:/xampp/folder/htdocs/application_web/projet_python/reddit_data_comments.csv", subreddit)

        if image_path and os.path.exists(image_path):
            try:
                with open(image_path, 'rb') as f:
                    img_original = Image.open(f)
                    largeur_disponible = parent_window.winfo_width() - 20  
                    hauteur_max = 400  

                 
                    ratio = img_original.width / img_original.height
                    nouvelle_largeur = min(largeur_disponible, int(hauteur_max * ratio))
                    nouvelle_hauteur = int(nouvelle_largeur / ratio)

                    img_resized = img_original.resize((nouvelle_largeur, nouvelle_hauteur))
                    img_tk = ImageTk.PhotoImage(img_resized)

                    if image_label is not None:
                        image_label.destroy()

                    image_label = tk.Label(parent_window, image=img_tk, bg=REDDIT_BG_COLOR)
                    image_label.image = img_tk   
                    image_label.pack(pady=10, padx=10)
            except FileNotFoundError:
                print(f"Error: Image file not found at {image_path}")
            except Exception as e:
                print(f"Error displaying image: {e}")
        else:
            print("No visualization generated or path is invalid.")

    visualisation_button = tk.Button(parent_window, text="📊 Afficher la Visualisation", command=show_visualisation,
                                     bg=REDDIT_BUTTON_BG, fg=REDDIT_BUTTON_FG, font=REDDIT_FONT_NORMAL,
                                     relief="raised", bd=3, highlightthickness=0, activebackground=REDDIT_BUTTON_ACTIVE_BG,
                                     activeforeground="white", cursor="hand2", padx=20, pady=10)
    visualisation_button.pack(pady=5, padx=10, fill="x")
 
def create_reddit_button(master, text, command):
    btn = tk.Button(master,
                    text=text,
                    command=command,
                    font=REDDIT_FONT_NORMAL,
                    bg=REDDIT_BUTTON_BG,
                    fg=REDDIT_BUTTON_FG,
                    relief="raised",
                    bd=3,
                    highlightthickness=0,
                    activebackground=REDDIT_BUTTON_ACTIVE_BG,
                    activeforeground="white",
                    cursor="hand2",
                    padx=20,
                    pady=10)
    btn.bind("<Enter>", lambda e: e.widget.config(bg=REDDIT_BUTTON_HOVER_BG))
    btn.bind("<Leave>", lambda e: e.widget.config(bg=REDDIT_BUTTON_BG))
    return btn


def main_interface(parent):
     
    analysis_window = tk.Toplevel(parent)
    analysis_window.title("Analyze Reddit Comments")
    analysis_window.configure(bg=REDDIT_BG_COLOR)

    header_frame = tk.Frame(analysis_window, bg=REDDIT_HEADER_BG, pady=10)
    header_frame.pack(fill="x")
    header_label = tk.Label(header_frame, text="Analyze Subreddit Comments", font=REDDIT_FONT_HEADER,
                             bg=REDDIT_HEADER_BG, fg=REDDIT_TEXT_COLOR)
    header_label.pack(pady=5)

    input_frame = tk.Frame(analysis_window, bg=REDDIT_BG_COLOR, pady=10, padx=10)
    input_frame.pack(fill="x")

    subreddit_label = tk.Label(input_frame, text="Enter subreddit name (e.g., python):", bg=REDDIT_BG_COLOR,
                                 fg=REDDIT_TEXT_COLOR, font=REDDIT_FONT_NORMAL)
    subreddit_label.pack(side="left")

    subreddit_entry = tk.Entry(input_frame, font=REDDIT_FONT_NORMAL)
    subreddit_entry.pack(side="left", fill="x", expand=True)
 

    def analyze():
        subreddit = subreddit_entry.get()
         
        for widget in analysis_window.winfo_children():
            if widget != input_frame and widget != header_frame:
                widget.destroy()
        reddit_comments(subreddit, analysis_window)
        update_stats(subreddits=1, comments=len(fetch_comments(subreddit)), sentiments=1)
        update_analysis_data(subreddit, "", file_name="C:/xampp/folder/htdocs/application_web/projet_python/reddit_stock.json")

    visualise_button = create_reddit_button(input_frame, "🔍 Analyze", analyze)
    visualise_button.pack(side="right", padx=5)
 
    style = ttk.Style(analysis_window)
    style.configure("RedditBack.TButton",
                    background=REDDIT_BG_COLOR,
                    foreground=REDDIT_TEXT_COLOR,
                    font=REDDIT_FONT_NORMAL,
                    relief="flat",
                    borderwidth=2,
                    highlightthickness=0)
    style.map("RedditBack.TButton",
              background=[("active", REDDIT_BUTTON_HOVER_BG)],
              foreground=[("active", "white")])

    back_button = ttk.Button(analysis_window, text="⬅ Back", command=analysis_window.destroy,
                             style="RedditBack.TButton")
    back_button.pack(pady=15, fill="x", side="bottom")

    














 
