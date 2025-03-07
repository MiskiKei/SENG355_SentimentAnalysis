import tkinter as tk
from tkinter import scrolledtext, ttk
from reddit_api_connection import RedditAPI
from sentiment_analysis import SentimentAnalyzer
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class SentimentAnalyzerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Reddit Sentiment Analyzer")
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry('%dx%d+0+0' % (width, height))
        self.master.configure(bg="#1e1e1e")

        self.reddit_api = RedditAPI()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.stored_posts = []

        title_label = tk.Label(master, text="Reddit Sentiment Analyzer", font=("Arial", 20, "bold"), bg="#1e1e1e", fg="white")
        title_label.pack(pady=10)

        input_frame = tk.Frame(master, bg="#1e1e1e")
        input_frame.pack(pady=5)

        self.entry_label = tk.Label(input_frame, text="Enter Subreddit:", font=("Arial", 14, "bold"), bg="#1e1e1e", fg="white")
        self.entry_label.pack(side=tk.LEFT, padx=5)

        self.entry = tk.Entry(input_frame, width=35, font=("Arial", 14), bg="#2b2b2b", fg="white", insertbackground="white")
        self.entry.pack(side=tk.LEFT, padx=5)

        self.fetch_button = ttk.Button(input_frame, text="Fetch Posts", command=self.fetch_reddit_posts)
        self.fetch_button.pack(side=tk.LEFT, padx=5)

        self.text_area = scrolledtext.ScrolledText(master, width=120, height=35, wrap=tk.WORD, font=("Arial", 12), bg="#2b2b2b", fg="white", insertbackground="white")
        self.text_area.pack(pady=10, padx=10)

        self.analyze_button = ttk.Button(master, text="Analyze Sentiment", command=self.analyze_sentiments)
        self.analyze_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 14, "bold"), bg="#1e1e1e", fg="white")
        self.result_label.pack(pady=10)

    def fetch_reddit_posts(self):
        subreddit_name = self.entry.get().strip()
        if not subreddit_name:
            self.text_area.insert(tk.END, "Please enter a subreddit name.\n\n")
            return

        self.text_area.delete(1.0, tk.END)
        self.posts = self.reddit_api.get_posts(subreddit_name, limit=10)

        if not self.posts:
            self.text_area.insert(tk.END, "No posts found or an error occurred.\n\n")
        else:
            for i, post in enumerate(self.posts, start=1):
                self.text_area.insert(tk.END, f"Post {i}:\n{post}\n")
                self.text_area.insert(tk.END, "-" * 80 + "\n")
                self.stored_posts.append(f"Post {i}:\n{post}\n")

    def analyze_sentiments(self):
        if not hasattr(self, 'posts') or not self.posts:
            self.result_label.config(text="No posts to analyze. Fetch posts first!", fg="red")
            return

        self.result_label.config(text="Analyzing Sentiments...", fg="blue")
        self.master.update_idletasks()

        self.text_area.delete(1.0, tk.END)
        for i, post in enumerate(self.posts, start=1):
            sentiment, scores = self.sentiment_analyzer.analyze_sentiment(post)
            score = scores['compound']
            color = self.score_to_color(score)

            tag_name = f"score_{i}"
            self.text_area.tag_configure(tag_name, foreground=color)
            self.text_area.insert(tk.END, self.stored_posts[i - 1])
            self.text_area.insert(tk.END, f"{sentiment} | Score: {score}\n", tag_name)
            if i < 10:
                self.text_area.insert(tk.END, "-" * 80 + "\n")

        self.result_label.config(text="Sentiment Analysis Complete!", fg="green")

    def score_to_color(self, s):
        s = (s + 1) / 2
        cmap = plt.get_cmap("RdYlGn")
        return mcolors.to_hex(cmap(s))


if __name__ == "__main__":
    root = tk.Tk()
    app = SentimentAnalyzerGUI(root)
    root.mainloop()
