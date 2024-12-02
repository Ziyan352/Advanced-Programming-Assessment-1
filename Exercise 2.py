import tkinter as tk
import random

def load_jokes(file_path):
    """Load jokes from the specified file and return as a list of tuples (setup, punchline)."""
    with open(file_path, 'r') as file:
        return [line.strip().split('?') for line in file if '?' in line]

def tell_joke():
    """Display a random joke's setup and enable punchline reveal."""
    global current_joke
    current_joke = random.choice(jokes)
    joke_label.config(text=current_joke[0] + "?", fg="blue")
    punchline_button.config(state=tk.NORMAL, text="Ready for the Punchline?")

def reveal_punchline():
    """Display the punchline with flair and disable the button afterward."""
    joke_label.config(text=current_joke[1], fg="green")
    punchline_button.config(state=tk.DISABLED, text="Ta-da!")

root = tk.Tk()
root.title("The LOL Machine")

jokes = load_jokes('randomJokes.txt')
current_joke = None

welcome_label = tk.Label(root, text="Ready for some laughs? Click below to start!", font=("Comic Sans MS", 12, "italic"))
welcome_label.pack(pady=15)

joke_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), wraplength=400, justify="center")
joke_label.pack(pady=20)

tell_joke_button = tk.Button(root, text="Tell me a joke!", command=tell_joke, font=("Arial", 12), bg="lightblue", padx=10, pady=5)
tell_joke_button.pack(pady=5)

punchline_button = tk.Button(root, text="Reveal punchline", command=reveal_punchline, font=("Arial", 12), bg="lightgreen", padx=10, pady=5, state=tk.DISABLED)
punchline_button.pack(pady=5)

root.mainloop()
