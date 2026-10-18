# Student Performance Analytics System

A simple Python script that builds a student marks dataset, calculates totals, averages, grades and pass/fail results, prints a class-level analysis, and saves the results to CSV files.

## Features

- Creates a dataset of 15 students with marks in 5 subjects plus attendance
- Saves the raw data to `student_data.csv`
- Calculates each student's **Total** and **Average**
- Assigns a **Grade** based on the average
- Determines a **Pass/Fail** result
- Prints a class analysis (average, highest, lowest, pass/fail counts)
- Saves the final report to `student_performance.csv`

## Project Structure

```
.
├── main.py                  # Main script
├── student_data.csv         # Generated: raw student marks and attendance
├── student_performance.csv  # Generated: raw data + Total, Average, Grade, Result
└── README.md
```

## Requirements

- Python 3.8+
- [pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)

Install dependencies:

```bash
pip install pandas numpy
```

## Usage

```bash
python main.py
```

Running the script (re)creates both CSV files in the current directory and prints the report to the console.

## Dataset

| Column       | Description                        |
|--------------|------------------------------------|
| Student_ID   | Unique student ID (501–515)        |
| Name         | Student name                       |
| Python       | Marks out of 100                   |
| SQL          | Marks out of 100                   |
| HTML         | Marks out of 100                   |
| CSS          | Marks out of 100                   |
| JavaScript   | Marks out of 100                   |
| Attendance   | Attendance percentage              |

`student_performance.csv` adds these calculated columns:

| Column  | Description                                      |
|---------|--------------------------------------------------|
| Total   | Sum of the five subject marks (out of 500)       |
| Average | Mean of the five subject marks, rounded to 2 dp  |
| Grade   | Letter grade based on the average                |
| Result  | `Pass` or `Fail`                                 |

## Grading Rules

**Grade (based on Average):**

| Average | Grade |
|---------|-------|
| 90+     | A+    |
| 80–89   | A     |
| 70–79   | B     |
| 60–69   | C     |
| 50–59   | D     |
| 40–49   | E     |
| Below 40| F     |

**Result:** A student **passes** only if they score **35 or more in every subject**. Scoring below 35 in any single subject results in **Fail**, regardless of the average.

## Sample Output

```
CLASS ANALYSIS
Class Average: 78.65
Highest Average: 93.0
Lowest Average: 45.6
Students Passed: 13
Students Failed: 2
```

Partial report:

```
 Student_ID       Name  Total  Average Grade Result
        501      Priya    423     84.6     A   Pass
        503   Jyothika    465     93.0    A+   Pass
        513    Shalini    286     57.2     D   Fail
        515       Janu    228     45.6     E   Fail
```

## Notes

- Shalini (513) fails because of a 34 in JavaScript, even though her average is 57.2 (Grade D).
- Janu (515) fails because of a 33 in Python.
- Attendance is stored in the dataset but is not currently used in grading or pass/fail logic.

## Possible Improvements

- Load student data from an external CSV instead of hard-coding it
- Factor attendance into the result (e.g., minimum 75% required)
- Add subject-wise statistics and topper lists
- Add charts using matplotlib or seaborn

## License

This project is for learning and educational purposes.
