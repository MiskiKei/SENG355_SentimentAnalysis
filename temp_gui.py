import tkinter as tk

texts = ["This is the first text", "Here is the second one", "Another example of text", "Final text in the array"]
scores = [1, 0, 1, 0]
index = 0

def update_display():
    text_label.configure(text=texts[index])
    score_label.configure(text=f"Score: {scores[index]}")

def next_text():
    global index
    if index < len(texts) - 1:
        index += 1
        update_display()

def prev_text():
    global index
    if index > 0:
        index -= 1
        update_display()

window = tk.Tk()
window.title("Sentiment Analysis")
window.geometry("400x200")

text_label = tk.Label(window, text=texts[index], font=("Arial", 14))
text_label.pack(pady=10)

score_label = tk.Label(window, text=f"Score: {scores[index]}", font=("Arial", 12))
score_label.pack(pady=5)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

prev_button = tk.Button(button_frame, text="⬅ Prev", command=prev_text)
prev_button.pack(side=tk.LEFT, padx=10)
