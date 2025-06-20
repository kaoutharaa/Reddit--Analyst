 
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

 
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

def on_leave(e):
    e.widget['background'] = BUTTON_BG

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

def switch_window1():
    print("Analyze Text clicked")   
def switch_window2():
    print("Analyze Data File clicked")   

def switch_window3or():
    print("Analyze Reddit clicked")   
 
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

button1_sidebar = create_attractive_button(buttons_frame, "Analyze Text", switch_window1)
button1_sidebar.pack(pady=5, fill="x")

button2_sidebar = create_attractive_button(buttons_frame, "Analyze Data File", switch_window2)
button2_sidebar.pack(pady=5, fill="x")

button3_sidebar = create_attractive_button(buttons_frame, "Analyze Reddit", switch_window3or)
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
            resized_image = bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)   
            new_photo = ImageTk.PhotoImage(resized_image)
            image_label.config(image=new_photo)
            image_label.image = new_photo  

    image_label = tk.Label(main_content_frame, bg=BG_COLOR)
    image_label.grid(row=0, column=0, sticky="nsew")

    main_content_frame.bind("<Configure>", update_image_size)
    root.after(1, lambda: main_content_frame.event_generate("<Configure>"))  # Initial resize

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