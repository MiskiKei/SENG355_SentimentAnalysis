import tkinter as tk
import random


def populate_boxes():
    user_input = entry.get()
    for i in range(10):
        labels[i].configure(text=f"{user_input} {i + 1}")


def assign_scores():
    for i in range(10):
        score_labels[i].configure(text=str(random.randint(1, 100)))


window = tk.Tk()
window.title("Sentiment Analyzer")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width,height))

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

search_button = tk.Button(window, text="Pull from Subreddit", command=populate_boxes)
search_button.pack(pady=5)

frame = tk.Frame(window)
frame.pack()

labels = []
score_labels = []

for i in range(10):
    row_frame = tk.Frame(frame)
    row_frame.pack(pady=2)

    label = tk.Label(row_frame, text="", width=20, anchor="w", relief="sunken")
    label.pack(side=tk.LEFT)
    labels.append(label)

    score_label = tk.Label(row_frame, text="")
    score_label.pack(side=tk.LEFT, padx=10)
    score_labels.append(score_label)

analyze_button = tk.Button(window, text="Analyze Sentiment", command=assign_scores)
analyze_button.pack(pady=5)

window.resizable(True, True)

window.mainloop()
