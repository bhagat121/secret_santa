# Secret Santa Assignment Tool

📌 Overview

This Python script automates the process of assigning secret gift exchange (Secret Santa) participants while ensuring that employees do not receive the same person as their Secret Child as they did in the previous year. The assignments are stored and can be used to ensure fair and non-repetitive pairings.

🛠 Installation
Prerequisites

Python 3.x installed
pip installed
Clone this repository

🚀 How to Run the Program

Ensure the current_employee.csv file is updated with the latest employees' names and email IDs.

If available, update previous_employee.csv with last year's assignments.
Run the script
python secret_santa.py
The script will generate a new assignment

📜 Functionality

1️⃣ Read Employee Data
    Reads current_employee.csv and stores employee details in a list.

2️⃣ Read Previous Assignments
    Loads past Secret Santa assignments from previous_employee.csv to avoid duplicate pairings.

3️⃣ Generate Assignments
    Randomly assigns Secret Children while ensuring no self-assignment or repetition from the previous year.
