Adaptive Disk Scheduling Visualizer
A visual, interactive disk scheduling algorithm simulator built with Python and Tkinter.

Overview
This application demonstrates various disk scheduling algorithms with an intuitive graphical interface. It provides real-time visualization of disk head movements and detailed performance metrics to help understand the efficiency of different scheduling strategies.

Features
Multiple Disk Scheduling Algorithms:
First-Come-First-Serve (FCFS)

Shortest Seek Time First (SSTF)

SCAN

C-SCAN

LOOK

C-LOOK

Interactive Request Management:
Add disk requests with customizable parameters (Request Sequence, Initial Head Position)

Delete or reset request entries

Dynamic request queue visualization

Visual Representation:
Graphical disk head movement visualization

Real-time animation of seek operations

Color-coded track movements for clarity

Comprehensive Performance Metrics:
Total seek time

Average seek time

Seek sequence visualization

Throughput analysis

Efficiency comparison between algorithms

Installation & Setup
Prerequisites:
Python 3.6+

tkinter

matplotlib

ttkbootstrap

Usage
Adding Requests:
Enter the sequence of disk requests.

Specify the initial head position.

Click "Add Request" to include it in the queue.

Selecting a Scheduling Algorithm:
Choose from the dropdown menu (FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK).

Click "Run Scheduler" to execute the selected algorithm.

View the head movement visualization and performance metrics below.

Managing Requests:
Select a request and click "Delete" to remove it.

Click "Reset" to clear all requests.


Performance Metrics
Total Seek Time: Sum of all seek operations performed.

Average Seek Time: Average movement required per request.

Throughput: Number of requests completed per unit time.

Efficiency: Comparison of different scheduling strategies.

Note
Currently, all code is contained in a single file. A proper code file structure will be implemented in upcoming updates.

Future Enhancements
Additional scheduling algorithms (F-SCAN, N-Step SCAN).

Export functionality for metrics and charts.

Enhanced animation of disk movements.

Real-world workload simulation.
