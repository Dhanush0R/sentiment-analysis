# Sentiment Analysis with IMDb Reviews

## Overview

This Python project performs sentiment analysis on IMDb movie reviews using natural language processing (NLP) techniques. The sentiment analysis is carried out on user-provided movie reviews or reviews extracted from IMDb using web scraping.

## Dependencies

Make sure you have the following dependencies installed before running the code:

- `nltk` (Natural Language Toolkit)
- `matplotlib`
- `selenium`
- `tkinter`
- `chromedriver` (for web scraping)

You can install these dependencies using the following command:

```bash
pip install nltk matplotlib selenium
```

## Usage

### 1. Sentiment Analysis from Text File

1. Place your text file with movie reviews in the project directory and name it `read.txt`.
2. Run the `main_nltk.py` script.

### 2. IMDb Review Extraction and Analysis

1. Make sure you have Chrome installed on your machine.
2. Run the `main_selenium.py` script, which will prompt you to enter the movie name.
3. The script will scrape IMDb reviews for the specified movie and save them to `read.txt`.
4. Run the `main_nltk.py` script for sentiment analysis.

### 3. GUI Application

1. Run the `main_gui.py` script to launch the GUI application.
2. Enter the movie name and click the "Analyse" button.
3. The sentiment analysis result will be displayed along with an emoji representing the sentiment.
4. Click the "Graph" button to visualize the distribution of emotions in the reviews.

## Files

- `main_nltk.py`: Contains the main class for sentiment analysis using NLTK.
- `main_selenium.py`: Extracts IMDb reviews using web scraping with Selenium.
- `main_gui.py`: GUI application for sentiment analysis.
- `background.png`: Background image for the GUI.
- `graph.png`: Output graph of emotion distribution.
- `emotions.txt`: Maps cleaned words to corresponding emotions.

## Credits

- This project uses the Natural Language Toolkit (NLTK) for sentiment analysis.
- Web scraping for IMDb reviews is done using Selenium.

## License

This project is licensed under the [MIT License](LICENSE).

---
