import tkinter as tk
import random

# Create a list of motivational quotes
quotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "The biggest risk is not taking any risk.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "The only way to do great work is to be passionate about what you do."
]

def generate_quote():
  # Select a random quote from the list
  quote = random.choice(quotes)
  # Set the quote as the text of the label
  quote_label.config(text=quote)

# Create the main window
window = tk.Tk()
window.title("Motivational Quotes")

# Set the background color of the main window
window.configure(bg="white")

# Create a label to display the quote
quote_label = tk.Label(text="", bg="white", font=("Helvetica", 16))
quote_label.pack(pady=20)

# Create a button to generate a new quote
quote_button = tk.Button(text="Motivate Me", bg="lightblue", font=("Helvetica", 14), command=generate_quote)
quote_button.pack(pady=10)

# Run the main loop
window.mainloop()
