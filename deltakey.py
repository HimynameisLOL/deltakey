import tkinter as tk
import random
import string

def generate_random_string():
    # Generate a random string of 20 characters with lowercase letters and numbers
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choices(characters, k=20))
    return f"KEY_{random_string}"

def on_generate():
    # When the button is clicked, update the label with the generated string
    generated_string.set(generate_random_string())

# Create the main window
root = tk.Tk()
root.title("Random String Generator")

# StringVar to hold the generated string
generated_string = tk.StringVar(root)

# Create the form elements
entry_label = tk.Label(root, text="Enter any word:")
entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate", command=on_generate)
result_label = tk.Label(root, textvariable=generated_string)

# Layout the form elements
entry_label.pack()
entry.pack()
generate_button.pack()
result_label.pack()

# Run the main loop
root.mainloop()
