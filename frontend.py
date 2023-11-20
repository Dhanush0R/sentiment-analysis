import tkinter as tk
from tkinter import Entry, Button, Label
from imdb_review import ReviewExtraction
from main_nltk import Sentiment
BG_COLOR1 = "#B4BDFF"
FONT_NAME = "Courier"
BG_COLOR2 = "#83A2FF"
response_data = {
    -1: ["Negative Sentiment", "🙁"],
    1: ["Positive Sentiment", "🙂"],
    0: ["Neutral Sentiment", "😐"]
}
senti = Sentiment()
class SentimentAnalyzerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sentiment Analyzer")
        self.master.config(bg=BG_COLOR1)


        self.master.geometry("800x600")

        # background image
        self.bg_image = tk.PhotoImage(file="background.png")

        # a canvas to place the background image
        self.canvas = tk.Canvas(self.master, width=780, height=360, highlightthickness=0)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        self.canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # a search input and button
        self.search_entry = Entry(self.master, width=40, bg=BG_COLOR1, highlightthickness=4,
                                  highlightbackground=BG_COLOR2)
        self.search_entry.grid(row=0, column=0, columnspan=2, pady=20)

        self.analyse_button = Button(self.master, text="Analyse",font=(FONT_NAME, 10, "bold"), command=self.perform_analysis, bg=BG_COLOR2,
                                     highlightthickness=4)
        self.analyse_button.grid(row=0, column=1, pady=20)



    def perform_analysis(self):
        rev_extraction = ReviewExtraction(self.search_entry.get())
        rev_extraction.extraction()
        response = senti.sentiment_analyse(sentiment_text=senti.cleaned_text)
        response_text = response_data[response]
        analysis_label1 = Label(self.master, text=response_text[0], font=(FONT_NAME, 20, "bold"),
                                    bg=BG_COLOR1)
        analysis_label1.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        emoji_label2 = Label(self.master, text=response_text[1], font=(FONT_NAME, 50, "bold"),
                                    bg=BG_COLOR1)
        emoji_label2.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        graph_button = Button(self.master, text="Graph", font=(FONT_NAME, 15, "bold"), command=self.show_graph, bg=BG_COLOR2)
        graph_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


    def show_graph(self):
        senti.graph_rep()


if __name__ == "__main__":
    root = tk.Tk()
    app = SentimentAnalyzerGUI(root)
    root.mainloop()
