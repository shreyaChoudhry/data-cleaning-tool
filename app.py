import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt

print("App started...")

df = None

def load_file():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        messagebox.showinfo("Success", "File Loaded!")

# ✅ FIX: open_file OUTSIDE
def open_file():
    try:
        os.startfile("cleaned_data.csv")
    except:
        messagebox.showerror("Error", "File not found! Clean data first.")

def clean_data():
    global df
    if df is None:
        messagebox.showerror("Error", "Load file first!")
        return

    # BEFORE graph
    df.isnull().sum().plot(kind='bar')
    plt.title("Before Cleaning")
    plt.show()

    # Cleaning
    df.drop_duplicates(inplace=True)
    df.fillna(method='ffill', inplace=True)

    # AFTER graph
    df.isnull().sum().plot(kind='bar')
    plt.title("After Cleaning")
    plt.show()

    df.to_csv("cleaned_data.csv", index=False)
    messagebox.showinfo("Done", "Cleaned & Saved!")

# UI
root = tk.Tk()
root.title("Data Cleaning Tool")
root.geometry("400x300")

tk.Label(root, text="Data Cleaning Tool", font=("Arial", 16)).pack(pady=20)

tk.Button(root, text="Upload CSV", command=load_file).pack(pady=10)
tk.Button(root, text="Clean Data", command=clean_data).pack(pady=10)
tk.Button(root, text="Download / Open Cleaned File", command=open_file).pack(pady=10)

root.mainloop()