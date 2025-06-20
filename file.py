import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import tkinter.font as font
from tkinter import filedialog
from model_function import resultat
from visualisation import visualisation_fct
from fct_reddit_comments import reddit_comments, main_interface
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from wordcloud import WordCloud
from tkinter import messagebox
from functools import partial
from PIL import Image, ImageTk
import os   
from fct_reddit_post import reddit_post, main_interface_post
from visualisation_post import visualisation_fct_post
 



 
BG_COLOR = "#DAE0E6"           
HEADER_BG = "#FFFFFF"           
BUTTON_BG = "#FF4500"           
BUTTON_FG = "#FFFFFF"           
TEXT_COLOR = "#222222"          
SECONDARY_TEXT = "#777777"     
LINK_COLOR = "#0079D3"           
FONT_NORMAL = ("Arial", 10)
FONT_HEADER = ("Arial", 16, "bold")
FONT_TITLE = ("Segoe UI", 18, "bold")   

 

def on_enter(e):
    e.widget['background'] = '#e03d00'   
    e.widget['relief'] = 'groove'   
    e.widget['bd'] = 2
def on_leave(e):
    e.widget['background'] = BUTTON_BG
    e.widget['relief'] = 'raised'  
    e.widget['bd'] = 2
def create_attractive_button(master, text, command):
    btn = tk.Button(master,
                    text=text,
                    command=command,
                    font=("Segoe UI", 11, "bold"),
                    bg=BUTTON_BG,
                    fg=BUTTON_FG,
                    activebackground="#e03d00",
                    activeforeground="white",
                    relief="raised",
                    bd=2,  
                    padx=15,
                    pady=8,
                    cursor="hand2")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn


 
def configure_entry_placeholder(entry, var, placeholder):
    def on_entry_click(event):
        if var.get() == placeholder:
            var.set("")
            entry.config(foreground=TEXT_COLOR)

    def on_focus_out(event):
        if not var.get():
            var.set(placeholder)
            entry.config(foreground=SECONDARY_TEXT)

    entry.bind("<FocusIn>", on_entry_click)
    entry.bind("<FocusOut>", on_focus_out)
    var.set(placeholder)
    entry.config(foreground=SECONDARY_TEXT)

    


 
def switch_window1(event=None):
    root.withdraw()
    roote = tk.Toplevel(root)
    roote.title("Text Sentiment Analysis")
    roote.geometry("600x500")
    roote.configure(bg=BG_COLOR)

 
    chat_frame = ttk.Frame(roote)
    chat_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    chat_display = scrolledtext.ScrolledText(
        chat_frame, wrap=tk.WORD, width=70, height=18,
        font=FONT_NORMAL, background="white", foreground=TEXT_COLOR,
        borderwidth=1, relief=tk.SOLID
    )
    chat_display.pack(fill=tk.BOTH, expand=True)
    chat_display.config(state=tk.DISABLED)

  
    input_frame = ttk.Frame(roote)
    input_frame.pack(side=tk.BOTTOM, fill=tk.X)

    entry_var2 = tk.StringVar()
    entry2 = ttk.Entry(input_frame, textvariable=entry_var2, width=50, font=FONT_NORMAL, foreground=SECONDARY_TEXT)
    entry2.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5, ipady=5)
    configure_entry_placeholder(entry2, entry_var2, "Enter text...")

    def send_message():
        user_message2 = entry_var2.get().strip()
        if user_message2 and user_message2 != "Enter text...":
            chat_display.config(state=tk.NORMAL)
            chat_display.insert(tk.END, f"👤 You: {user_message2}\n", "user")
            sentiment = resultat(user_message2)
            if sentiment.lower() == "negative":
                chat_display.insert(tk.END, f"🤖 Bot: Sentiment → {sentiment}\n", "negative")
            else:
                chat_display.insert(tk.END, f"🤖 Bot: Sentiment → {sentiment}\n", "bot")
            chat_display.config(state=tk.DISABLED)
            entry_var2.set("Enter text...")
            entry2.config(foreground=SECONDARY_TEXT)

    def back_to_main():
        roote.destroy()
        root.deiconify()

    back_button = create_attractive_button(roote, "⬅ Back", back_to_main)
    back_button.pack(pady=5)

    send_button = create_attractive_button(input_frame, "Send", send_message)
    send_button.pack(side=tk.RIGHT, padx=5)

    chat_display.tag_config("user", foreground=LINK_COLOR)
    chat_display.tag_config("bot", foreground="#4CAF50")
    chat_display.tag_config("negative", foreground="red")


def switch_window2():
    global selected_file_path
    root.withdraw()
    new_window = tk.Toplevel(root)
    new_window.title("Analyze Data File")
    new_window.configure(bg=BG_COLOR)

    header_frame = tk.Frame(new_window, bg=HEADER_BG, pady=10)
    header_frame.pack(fill="x")
    text = tk.Label(header_frame, text="Analyze your data!", font=FONT_HEADER, bg=HEADER_BG, fg=TEXT_COLOR)
    text.pack(pady=5)

    frame = tk.Frame(new_window, bg=BG_COLOR, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)

    def myfile():
        global selected_file_path
        file_path = filedialog.askopenfilename(title="Open the file that contains data")
        if file_path:
            selected_file_path = file_path
            myentry.delete(0, tk.END)
            myentry.insert(0, file_path)

    def start_analysis():
        if selected_file_path:
            path = visualisation_fct(selected_file_path)
            try:
                image = Image.open(path)
                image.show()
            except FileNotFoundError:
                messagebox.showerror("Error", f"Image file not found at: {path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open image: {e}")

    tk.Button(frame, text="Select Data File", command=myfile, bg="white", fg=TEXT_COLOR, font=FONT_NORMAL, relief=tk.FLAT).pack(pady=8, padx=10, fill="x")
    myentry = tk.Entry(frame, bg="white", fg=SECONDARY_TEXT, font=FONT_NORMAL, relief=tk.FLAT)
    myentry.pack(pady=8, padx=10, fill="x")
    myentry.config(state=tk.DISABLED)
    tk.Button(frame, text="Analyze", command=start_analysis, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT_NORMAL, relief=tk.FLAT).pack(pady=10, fill="x")
    ttk.Button(frame, text="⬅ Back", command=lambda: [new_window.destroy(), root.deiconify()], style="TButton").pack(pady=15, fill="x")

    footer = tk.Label(
        new_window,
        text="© 2023 Sentiment Analyst",
        bg=BG_COLOR,
        fg=SECONDARY_TEXT,
        font=FONT_NORMAL,
        pady=5
    )
    footer.pack(side="bottom", fill="x")
 


from functools import partial

 
REDDIT_BG_COLOR = "#DAE0E6"
REDDIT_HEADER_BG = "#FF4500"
REDDIT_TEXT_COLOR = "#222222"
REDDIT_BUTTON_BG = "#FF8C00"
REDDIT_BUTTON_FG = "white"
REDDIT_BUTTON_HOVER_BG = "#FF6347"
REDDIT_BUTTON_ACTIVE_BG = "#E64A19"
REDDIT_FONT_HEADER = ("Segoe UI", 18, "bold")
REDDIT_FONT_NORMAL = ("Segoe UI", 12, "bold") 

def create_reddit_button(master, text, command):
    btn = tk.Button(master,
                    text=text,
                    command=command,
                    font=REDDIT_FONT_NORMAL,
                    bg="white",
                    fg=REDDIT_TEXT_COLOR,
                    relief="raised",  
                    bd=3,            
                    highlightthickness=0,
                    activebackground=REDDIT_TEXT_COLOR,
                    activeforeground="white",
                    cursor="hand2",
                    padx=20,
                    pady=10)
    btn.bind("<Enter>", lambda e: e.widget.config(bg=REDDIT_BUTTON_HOVER_BG, fg="white"))
    btn.bind("<Leave>", lambda e: e.widget.config(bg="white", fg=REDDIT_TEXT_COLOR))
    return btn

def switch_window3or(parent):
    window = tk.Toplevel(parent)
    window.title("Reddit Analysis")
    window.geometry("400x220")
    window.configure(bg=REDDIT_BG_COLOR)
 
    header_frame = tk.Frame(window, bg=REDDIT_HEADER_BG, pady=15)
    header_frame.pack(fill="x")
    welcome_label = tk.Label(
        header_frame,
        text="Reddit Analysis",
        font=REDDIT_FONT_HEADER,
        bg=REDDIT_HEADER_BG,
        fg=REDDIT_TEXT_COLOR,
        pady=8
    )
    welcome_label.pack()

    
    buttons_frame = tk.Frame(window, bg=REDDIT_BG_COLOR, padx=30, pady=20) 
    buttons_frame.pack(expand=True)
    buttons_frame.grid_columnconfigure(0, weight=1)

 
    subreddit_button = create_reddit_button(buttons_frame, "Analyze Subreddit Comments", lambda: main_interface(window))
    subreddit_button.grid(row=0, column=0, pady=(15, 8), sticky="ew")  
 
    post_button = create_reddit_button(buttons_frame, "Analyze Post Comments", partial(main_interface_post, window))
    post_button.grid(row=1, column=0, pady=8, sticky="ew")
 
    style = ttk.Style(window)
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

    back_button = ttk.Button(window, text="⬅ Back", command=window.destroy, style="RedditBack.TButton")
    back_button.pack(pady=15, fill="x", side="bottom")




 
root = tk.Tk()
root.title("Sentiment Analyst")
root.geometry("700x450")   
root.configure(bg=BG_COLOR)

 
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TFrame", background=HEADER_BG)

 
sidebar_frame = ttk.Frame(root, width=180, style="TFrame")
sidebar_frame.pack(side="left", fill="y", padx=(10, 0), pady=10)   

 
title_label = tk.Label(
    sidebar_frame,
    text="Sentiment\nAnalyst",
    font=FONT_TITLE,   
    bg=HEADER_BG,
    fg=TEXT_COLOR,
    pady=15
)
title_label.pack(pady=(10, 20), padx=10, fill="x")   
 
buttons_frame = ttk.Frame(sidebar_frame, style="TFrame")
buttons_frame.pack(fill="x", padx=10, pady=10)

button1_sidebar = create_attractive_button(buttons_frame, "Analyze your feelings", switch_window1)
button1_sidebar.pack(pady=5, fill="x")
 
 
button3_sidebar = create_attractive_button(buttons_frame, "Analyze Reddit", lambda: switch_window3or(root))
button3_sidebar.pack(pady=5, fill="x")


 
main_content_frame = tk.Frame(root, bg=BG_COLOR)
main_content_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
main_content_frame.grid_rowconfigure(0, weight=1)
main_content_frame.grid_columnconfigure(0, weight=1)


try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "bg.jpg")  
    bg_image = Image.open(image_path)

    def update_image_size(event):
        new_width = event.width
        new_height = event.height
        if new_width > 0 and new_height > 0:
            resized_image = bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)  # High-quality resize
            new_photo = ImageTk.PhotoImage(resized_image)
            image_label.config(image=new_photo)
            image_label.image = new_photo   

    image_label = tk.Label(main_content_frame, bg=BG_COLOR)
    image_label.grid(row=0, column=0, sticky="nsew")

    main_content_frame.bind("<Configure>", update_image_size)
    root.after(1, lambda: main_content_frame.event_generate("<Configure>"))   

except FileNotFoundError:
    print("Error: 'bg.jpg' not found in the same directory as the script.")
    no_image_label = tk.Label(main_content_frame, text="Image not found", font=FONT_NORMAL, bg=BG_COLOR, fg=TEXT_COLOR)
    no_image_label.pack(expand=True, fill="both")
except Exception as e:
    print(f"Error loading image: {e}")
    error_label = tk.Label(main_content_frame, text=f"Error loading image: {e}", font=FONT_NORMAL, bg=BG_COLOR, fg="red")
    error_label.pack(expand=True, fill="both")

 
footer = tk.Label(
    root,
    text="© 2023 Sentiment Analyst",
    bg=BG_COLOR,
    fg=SECONDARY_TEXT,
    font=FONT_NORMAL,
    pady=5
)
footer.pack(side="bottom", fill="x")

root.mainloop()