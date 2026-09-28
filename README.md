# GRADE-GENERATOR
# Student Grade Analysis and Curve Evaluation System

A lightweight, terminal-based Python application designed to collect student test scores, evaluate performance against a dynamic class curve (mean-deviation model), and output class-level descriptive statistics.


## Overview

The **Student Grade Analysis System** automates the computation of relative academic grades. Unlike rigid absolute grading thresholds (e.g., 90% = A, 80% = B), this application grades students on a curve determined by their deviation from the class mean ($\text{diff} = \text{mark} - \text{average}$). It also outputs a statistical breakdown identifying the highest and lowest performers in the cohort.

---

## Features

- **Dynamic Curved Grading**: Evaluates performance relative to the cohort's average score.
- **Summary Metrics**: Calculates overall class aggregate and mean score.
- **Performance Outliers**: Identifies top and bottom scores alongside the corresponding students.
- **Lightweight & Dependency-Free**: Operates entirely using native Python standard libraries without requiring third-party package installations.

---


## Requirements

- Python 3.7 or higher
- Operating System: Windows, macOS, or Linux
- Terminal or command-line prompt

---

## Installation and Setup

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-username/student-grading-system.git
   cd student-grading-system
   ```

2. **Verify Python Installation**:
   ```bash
   python --version
   # or
   python3 --version
   ```

3. **Run the Script**:
   ```bash
   python grade_analyzer.py
   ```

---

## Usage Instructions

1. Launch the script via terminal.
2. When prompted, enter the total number of students ($N$) as a positive integer.
3. For each student, enter:
   - Full name (string)
   - Score/mark (floating-point number or integer)
4. View the generated report, which displays:
   - Class mean
   - Individual grade cards
   - Class-wide high and low metrics

---

## Sample Input and Output

### Input Example
```text
Enter number of students: 3
Enter student name: Alice
Enter marks: 92
Enter student name: Bob
Enter marks: 74
Enter student name: Charlie
Enter marks: 56
```

### Output Example
```text
Class Average: 74.0

Name: Alice
Marks: 92.0
Grade: A

Name: Bob
Marks: 74.0
Grade: C

Name: Charlie
Marks: 56.0
Grade: F

Class Statistics
----------------
Highest Marks: 92.0
Highest Scorer: Alice
Lowest Marks: 56.0
Lowest Scorer: Charlie
```
