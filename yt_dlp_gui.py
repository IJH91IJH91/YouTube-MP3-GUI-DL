import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to select download path
def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder)

# Function to download audio using yt-dlp
def download_audio():
    url = url_entry.get()
    output_folder = path_entry.get()

    if not url or not output_folder:
        messagebox.showwarning("Input Error", "Please provide a URL and select an output folder.")
        return

    # yt-dlp command to download highest quality audio
    command = f'yt-dlp -f "bestaudio" --extract-audio --audio-format mp3 -o "{output_folder}/%(title)s.%(ext)s" "{url}"'
    os.system(command)
    messagebox.showinfo("Download Complete", "The audio has been downloaded successfully.")

# Create the main window
root = tk.Tk()
root.title("IJH Music Downloader and Converter")

# URL input field
tk.Label(root, text="Video URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Path selection field
tk.Label(root, text="Download Path:").pack(pady=5)
path_entry = tk.Entry(root, width=50)
path_entry.pack(pady=5)
browse_button = tk.Button(root, text="Browse", command=select_folder)
browse_button.pack(pady=5)

# Download button
download_button = tk.Button(root, text="Download Audio", command=download_audio)
download_button.pack(pady=20)

# Run the application
root.mainloop()
