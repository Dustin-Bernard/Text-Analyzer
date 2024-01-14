import tkinter as tk
from tkinter import scrolledtext
from collections import Counter

result_label = None  # Declare result_label as a global variable

def main():
    global result_label  # Use the global variable
    # Create the main window
    root = tk.Tk()
    root.title("Text Analyzer")
    root.geometry("500x320")

    # Create and configure the text entry
    text_entry = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, font=("Arial", 12))
    text_entry.pack(pady=10)
    text_entry.bind("<KeyRelease>", lambda event: on_text_change(text_entry))

    # Create a label to display analysis results
    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

def clean_text(text):
    # Remove punctuation and convert to lowercase. 
    return ''.join(char.lower() if char.isalnum() else ' ' for char in text)

def count_characters(text):
    # Count the total number of characters. 
    text = text.replace(" ", "")
    return len(text)

def count_words(text):
    # Count the total number of words.
    words = text.split()
    return len(words)

def find_longest_word(words):
    # Find the longest word in the text. 
    return max(words, key=len)

def find_most_common_word(words):
    # Find the most common word in the list.
    word_counter = Counter(words)
    most_common_word, _ = word_counter.most_common(1)[0]
    # Only return the word without the count value
    return most_common_word

def on_text_change(text_entry):
    # Callback function to update analysis results dynamically. 
    result_label
    text = text_entry.get("1.0", tk.END)
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    analysis_result = {
        'total_characters': count_characters(cleaned_text),
        'total_words': count_words(cleaned_text),
        'longest_word': find_longest_word(words),
        'most_common_word': find_most_common_word(words)
    }

    # Update labels
    result_label.config(text=f"Total Characters: {analysis_result['total_characters']}\n"
                             f"Total Words: {analysis_result['total_words']}\n"
                             f"Longest Word: {analysis_result['longest_word']}\n"
                             f"Most Common Word: {analysis_result['most_common_word']}\n")

if __name__ == "__main__":
    main()
