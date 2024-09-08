import tkinter as tk
from tkinter import messagebox, ttk

def save_input():
    array = entry_array.get()
    algo = algo_menu.get()

    # Save the input to input.txt
    with open("input.txt", "w") as file:
        file.write(array + "\n")
        file.write(algo + "\n")
    
    messagebox.showinfo("Info", "Input saved successfully!")
    
    # Close the window after clicking OK
    window.destroy()

# Create a Tkinter window
window = tk.Tk()
window.title("Input Getter")

# Array input field
label_array = tk.Label(window, text="Enter Array (comma-separated):")
label_array.pack(padx=10, pady=5)

entry_array = tk.Entry(window, width=50)
entry_array.pack(padx=10, pady=5)

# Sorting algorithm dropdown
label_algo = tk.Label(window, text="Select Sorting Algorithm:")
label_algo.pack(padx=10, pady=5)

algo_menu = ttk.Combobox(window, values=["Bubble Sort", "Insertion Sort", "Selection Sort", "Heap Sort", "Quick Sort", "Merge Sort"])
algo_menu.pack(padx=10, pady=5)
algo_menu.current(0)  # Default selection

# Save button
save_button = tk.Button(window, text="Save Input", command=save_input)
save_button.pack(padx=10, pady=10)

window.mainloop()
