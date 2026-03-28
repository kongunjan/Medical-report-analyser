# Medical-report-analyser
A basic rule-based medical report analyzer built in Python that reads PDF reports, extracts common blood test values, and displays simple health insights in tabular form.
# Simple AI Medical Report Analyzer

## Project Description
This project is a **basic AI-style medical report analyzer** made using Python.  
It allows the user to **select a PDF medical report**, extracts text from the PDF, finds some common medical test values, and compares them with normal ranges.

The program then shows:
- Test name
- Your value
- Normal range
- Status (**Low / Normal / High**)
- Short explanation of the test

It also includes a **simple chatbot** where the user can ask about a specific test.

> This is a **rule-based beginner project**, not a real medical AI system.

---

## Features
- Select/upload a PDF medical report using file picker
- Extract text from PDF using `pdfplumber`
- Find medical test values using `re` (regular expressions)
- Compare values with normal ranges
- Show results in a table using `pandas`
- Simple chatbot for asking about extracted tests
- Beginner-friendly and easy to understand

---

## Technologies Used
- **Python**
- **pdfplumber** → to read text from PDF
- **pandas** → to display results in table format
- **re** → to search test values from text
- **tkinter** → to select PDF file

---

## Medical Tests Included
The current version checks these tests:
- Hemoglobin
- WBC
- Blood Sugar
- Cholesterol
- Platelets

---

## How the Project Works
1. User selects a PDF file.
2. The program extracts text from the PDF.
3. It searches for known test names and their values.
4. It compares the values with predefined normal ranges.
5. It classifies each result as:
   - **Low**
   - **Normal**
   - **High**
6. It displays the results in a pandas table.
7. The chatbot allows the user to ask about any extracted test.

---

## Installation

### Step 1: Install Python
Make sure Python is installed on your system.

### Step 2: Install required libraries
Open terminal / command prompt and run:

```bash
pip install pdfplumber pandas
