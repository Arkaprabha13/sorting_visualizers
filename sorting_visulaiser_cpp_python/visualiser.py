import matplotlib.pyplot as plt
import numpy as np

# Function to generate colors for bars
def generate_colors(num_bars):
    return [np.random.rand(3,) for _ in range(num_bars)]

# Function to visualize the array with consistent colors and value labels
def visualize(arr, colors):
    plt.bar(range(len(arr)), arr, color=colors)
    for i, value in enumerate(arr):
        plt.text(i, value + 0.1, str(value), ha='center', va='bottom')
    plt.pause(0.5)  # Add a small delay for visualization

# Function to read steps from file and visualize them
def visualize_sorting_steps():
    plt.figure()
    plt.title("Sorting Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")

    colors = []  # Will be populated with bar colors

    try:
        with open("steps.txt", "r") as file:
            first_line = file.readline().strip()
            if first_line:
                # Initialize colors based on the first array size
                arr = list(map(int, first_line.split()))
                colors = generate_colors(len(arr))
                plt.bar(range(len(arr)), arr, color=colors)  # Plot the initial bars

            file.seek(0)  # Move back to the beginning of the file

            for line in file:
                if line.strip() == "":
                    continue  # Skip empty lines
                arr = list(map(int, line.strip().split()))
                plt.clf()  # Clear the previous plot
                plt.title("Sorting Visualization")
                plt.xlabel("Index")
                plt.ylabel("Value")
                visualize(arr, colors)
    except FileNotFoundError:
        print("steps.txt not found. Make sure the C++ program has run successfully.")
        return

    plt.show()

if __name__ == "__main__":
    visualize_sorting_steps()
