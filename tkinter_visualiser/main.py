import tkinter as tk
from tkinter import messagebox, ttk
import random
import time
import numpy as np

# Sorting algorithms with delay

def bubble_sort(arr, draw_data, speed):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            draw_data(arr, ["green" if x == j or x == j + 1 else "blue" for x in range(len(arr))])
            time.sleep(speed)

def insertion_sort(arr, draw_data, speed):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        draw_data(arr, ["green" if x == j or x == i else "blue" for x in range(len(arr))])
        time.sleep(speed)

def selection_sort(arr, draw_data, speed):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_data(arr, ["green" if x == min_idx or x == i else "blue" for x in range(len(arr))])
        time.sleep(speed)

def heapify(arr, n, i, draw_data, speed):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        draw_data(arr, ["green" if x == i or x == largest else "blue" for x in range(len(arr))])
        time.sleep(speed)
        heapify(arr, n, largest, draw_data, speed)

def heap_sort(arr, draw_data, speed):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, draw_data, speed)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        draw_data(arr, ["green" if x == i or x == 0 else "blue" for x in range(len(arr))])
        time.sleep(speed)
        heapify(arr, i, 0, draw_data, speed)

def partition(arr, low, high, draw_data, speed):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        draw_data(arr, ["green" if x == i or x == high else "blue" for x in range(len(arr))])
        time.sleep(speed)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high, draw_data, speed):
    if low < high:
        pi = partition(arr, low, high, draw_data, speed)
        quick_sort(arr, low, pi - 1, draw_data, speed)
        quick_sort(arr, pi + 1, high, draw_data, speed)

def merge(arr, left, mid, right, draw_data, speed):
    left_half = arr[left:mid + 1]
    right_half = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
        draw_data(arr, ["green" if x >= left and x <= right else "blue" for x in range(len(arr))])
        time.sleep(speed)
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

def merge_sort(arr, left, right, draw_data, speed):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid, draw_data, speed)
        merge_sort(arr, mid + 1, right, draw_data, speed)
        merge(arr, left, mid, right, draw_data, speed)

# Visualization function
def draw_data(arr, color_array):
    canvas.delete("all")
    canvas_height = 400
    canvas_width = 800
    bar_width = canvas_width / (len(arr) + 1)
    spacing = 10
    for i, height in enumerate(arr):
        x0 = i * bar_width + spacing
        y0 = canvas_height - height
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
    window.update_idletasks()

# Sorting call handler
def start_sorting():
    global arr
    speed = speed_scale.get()
    if algo_menu.get() == "Bubble Sort":
        bubble_sort(arr, draw_data, speed)
    elif algo_menu.get() == "Insertion Sort":
        insertion_sort(arr, draw_data, speed)
    elif algo_menu.get() == "Selection Sort":
        selection_sort(arr, draw_data, speed)
    elif algo_menu.get() == "Heap Sort":
        heap_sort(arr, draw_data, speed)
    elif algo_menu.get() == "Quick Sort":
        quick_sort(arr, 0, len(arr) - 1, draw_data, speed)
    elif algo_menu.get() == "Merge Sort":
        merge_sort(arr, 0, len(arr) - 1, draw_data, speed)

# Input array handler
def generate_array():
    global arr
    array_size = int(size_entry.get())
    arr = [random.randint(10, 200) for _ in range(array_size)]
    draw_data(arr, ["blue" for _ in range(len(arr))])

# Tkinter UI
window = tk.Tk()
window.title("Sorting Algorithm Visualizer")
window.geometry("900x600")

# GUI layout
UI_frame = tk.Frame(window, width=800, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# Array size input
size_label = tk.Label(UI_frame, text="Array Size: ", bg='grey')
size_label.grid(row=0, column=0, padx=5, pady=5)
size_entry = tk.Entry(UI_frame)
size_entry.grid(row=0, column=1, padx=5, pady=5)

# Sorting algorithm dropdown
algo_label = tk.Label(UI_frame, text="Sorting Algorithm: ", bg='grey')
algo_label.grid(row=1, column=0, padx=5, pady=5)
algo_menu = ttk.Combobox(UI_frame, values=["Bubble Sort", "Insertion Sort", "Selection Sort", "Heap Sort", "Quick Sort", "Merge Sort"])
algo_menu.grid(row=1, column=1, padx=5, pady=5)
algo_menu.current(0)

# Speed scale
speed_scale_label = tk.Label(UI_frame, text="Sorting Speed [s]: ", bg='grey')
speed_scale_label.grid(row=2, column=0, padx=5, pady=5)
speed_scale = tk.Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.1, orient='horizontal')
speed_scale.grid(row=2, column=1, padx=5, pady=5)

# Buttons
generate_button = tk.Button(UI_frame, text="Generate Array", command=generate_array, bg='light blue')
generate_button.grid(row=0, column=2, padx=5, pady=5)

sort_button = tk.Button(UI_frame, text="Start Sorting", command=start_sorting, bg='light green')
sort_button.grid(row=1, column=2, padx=5, pady=5)

# Canvas for visualization
canvas = tk.Canvas(window, width=800, height=400, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()
