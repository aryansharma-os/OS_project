import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# Disk Scheduling Algorithms

def fcfs(requests, head):
    """ First-Come-First-Serve Disk Scheduling """
    seek_sequence = [head] + requests
    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time

def sstf(requests, head):
    """ Shortest Seek Time First Disk Scheduling """
    seek_sequence = [head]
    remaining = requests.copy()
    
    while remaining:
        closest = min(remaining, key=lambda x: abs(x - seek_sequence[-1]))
        seek_sequence.append(closest)
        remaining.remove(closest)
    
    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time

def scan(requests, head, max_cylinder):
    """ SCAN Disk Scheduling (Elevator Algorithm) """
    requests.append(head)
    requests.sort()
    direction = 1  # Move towards higher values
    seek_sequence = []

    if head in requests:
        idx = requests.index(head)

    if direction == 1:  # Moving right
        seek_sequence.extend(requests[idx:])
        seek_sequence.append(max_cylinder)  # Go to max limit
        seek_sequence.extend(reversed(requests[:idx]))  # Then go back

    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time
def c_scan(requests, head, max_cylinder):
    """ C-SCAN Disk Scheduling """
    requests.append(head)
    requests.sort()
    seek_sequence = []

    idx = requests.index(head)
    seek_sequence.extend(requests[idx:])  # Move towards max cylinder
    seek_sequence.append(max_cylinder)  # Go to max limit
    seek_sequence.append(0)  # Jump to min
    seek_sequence.extend(requests[:idx])  # Serve remaining requests

    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time

# LOOK and C-LOOK similar to SCAN and C-SCAN, but don't go to disk edges.

def plot_disk_movement(seek_sequence):
    """ Function to visualize disk head movement """
    plt.figure(figsize=(8, 5))
    plt.plot(seek_sequence, range(len(seek_sequence)), marker="o", linestyle="-", color="b")
    plt.xlabel("Cylinder Number")
    plt.ylabel("Sequence Step")
    plt.title("Disk Head Movement")
    plt.grid(True)
    plt.show()


# GUI Implementation

def run_scheduler():
    try:
        requests = list(map(int, entry_requests.get().split(",")))
        head = int(entry_head.get())
        algorithm = algo_var.get()
        max_cylinder = 200  # Set disk size

        if algorithm == "FCFS":
            seek_sequence, seek_time = fcfs(requests, head)
        elif algorithm == "SSTF":
            seek_sequence, seek_time = sstf(requests, head)
        elif algorithm == "SCAN":
            seek_sequence, seek_time = scan(requests, head, max_cylinder)
        elif algorithm == "C-SCAN":
            seek_sequence, seek_time = c_scan(requests, head, max_cylinder)
        else:
            messagebox.showerror("Error", "Select a valid algorithm")
            return

        # Show results
        result_label.config(text=f"Seek Time: {seek_time}")
        plot_disk_movement(seek_sequence)

    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers for requests and head position.")


# Tkinter GUI

root = tk.Tk()
root.title("Adaptive Disk Scheduling Visualizer")

tk.Label(root, text="Request Sequence (comma-separated):").pack()
entry_requests = tk.Entry(root)
entry_requests.pack()

tk.Label(root, text="Initial Head Position:").pack()
entry_head = tk.Entry(root)
entry_head.pack()

tk.Label(root, text="Select Algorithm:").pack()
algo_var = tk.StringVar(value="FCFS")
tk.OptionMenu(root, algo_var, "FCFS", "SSTF", "SCAN", "C-SCAN").pack()

tk.Button(root, text="Run Scheduler", command=run_scheduler).pack()
result_label = tk.Label(root, text="Seek Time: ")
result_label.pack()

root.mainloop()



