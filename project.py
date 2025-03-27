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
