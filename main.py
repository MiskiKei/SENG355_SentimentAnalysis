import tkinter as tk
from tkinter import scrolledtext, ttk
from reddit_api_connection import RedditAPI
from sentiment_analysis import SentimentAnalyzer


class SentimentAnalyzerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Reddit Sentiment Analyzer")
        self.master.geometry("1000x700")
        self.master.configure(bg="#f4f4f4")

        self.reddit_api = RedditAPI()
        self.sentiment_analyzer = SentimentAnalyzer()

        # Title
        title_label = tk.Label(master, text="Reddit Sentiment Analyzer", font=("Arial", 20, "bold"), bg="#f4f4f4")
        title_label.pack(pady=10)

        # Input
        input_frame = tk.Frame(master, bg="#f4f4f4")
        input_frame.pack(pady=5)

        self.entry_label = tk.Label(input_frame, text="Enter Subreddit:", font=("Arial", 14, "bold"), bg="#f4f4f4")
        self.entry_label.pack(side=tk.LEFT, padx=5)

        self.entry = tk.Entry(input_frame, width=35, font=("Arial", 14))
        self.entry.pack(side=tk.LEFT, padx=5)

        self.fetch_button = ttk.Button(input_frame, text="Fetch Posts", command=self.fetch_reddit_posts) # The Call Right Here
        self.fetch_button.pack(side=tk.LEFT, padx=5)

        # Text Display for Results Area
        self.text_area = scrolledtext.ScrolledText(master, width=120, height=35, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(pady=10, padx=10)

        # Analyze Button
        self.analyze_button = ttk.Button(master, text="Analyze Sentiment", command=self.analyze_sentiments) # The Call Right Here
        self.analyze_button.pack(pady=5)

        # Sentiment Results Text
        self.result_label = tk.Label(master, text="", font=("Arial", 14, "bold"), bg="#f4f4f4")
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

    def analyze_sentiments(self):
        if not hasattr(self, 'posts') or not self.posts:
            self.result_label.config(text="No posts to analyze. Fetch posts first!", fg="red")
            return

        self.result_label.config(text="Analyzing Sentiments...", fg="blue")
        self.master.update_idletasks()

        results = []
        for i, post in enumerate(self.posts, start=1):
            sentiment, scores = self.sentiment_analyzer.analyze_sentiment(post)
            results.append(f"🔍 Post {i}: {sentiment} | Scores: {scores}\n")

        self.text_area.insert(tk.END, "\nSentiment Analysis Results:\n" + "-" * 100 + "\n")
        self.text_area.insert(tk.END, "\n".join(results) + "\n", "big")
        self.result_label.config(text="Sentiment Analysis Complete!", fg="green")


if __name__ == "__main__":
    root = tk.Tk()
    app = SentimentAnalyzerGUI(root)
    root.mainloop()
