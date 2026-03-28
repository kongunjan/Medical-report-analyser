import re
import pdfplumber
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

normal_ranges = {
    "hemoglobin": (12.0, 16.0, "g/dL"),
    "wbc": (4000, 11000, "cells/mcL"),
    "blood sugar": (70, 140, "mg/dL"),
    "cholesterol": (125, 200, "mg/dL"),
    "platelets": (150000, 450000, "cells/mcL")
}
test_info = {
    "hemoglobin": "Hemoglobin carries oxygen in blood.",
    "wbc": "WBC helps fight infection.",
    "blood sugar": "Blood sugar shows glucose level in blood.",
    "cholesterol": "Cholesterol affects heart health.",
    "platelets": "Platelets help in blood clotting."
}
def select_pdf():
    root = Tk()
    root.withdraw()

    file_path = askopenfilename(
        title="Select Medical Report PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )
    return file_path
def extract_text(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text.lower()
def extract_tests(report_text):
    found_tests = {}

    for test in normal_ranges:
        pattern = test + r"\s*[:\-]?\s*([\d.]+)"
        match = re.search(pattern, report_text)

        if match:
            value = float(match.group(1))
            found_tests[test] = value

    return found_tests
def analyze_tests(found_tests):
    data = []

    for test in found_tests:
        value = found_tests[test]
        low, high, unit = normal_ranges[test]

        if value < low:
            status = "Low"
        elif value > high:
            status = "High"
        else:
            status = "Normal"

        row = {
            "Test Name": test.title(),
            "Your Value": value,
            "Unit": unit,
            "Normal Range": f"{low} - {high}",
            "Status": status,
            "Info": test_info[test]
        }

        data.append(row)

    df = pd.DataFrame(data)
    return df

def chatbot(found_tests):
    if len(found_tests) == 0:
        return

    print("\nYou can ask about a test name.")
    print("Example: hemoglobin, wbc, blood sugar")
    print("Type exit to stop.\n")

    while True:
        question = input("Ask about a test: ").lower()

        if question == "exit":
            print("Thank you! This is only a very basic AI assistant.")
            break

        if question in found_tests:
            value = found_tests[question]
            low, high, unit = normal_ranges[question]

            print("\nTest:", question.title())
            print("Your Value:", value, unit)
            print("Normal Range:", low, "-", high, unit)
            print("Info:", test_info[question])

            if value < low:
                print("Result: Low")
            elif value > high:
                print("Result: High")
            else:
                print("Result: Normal")

            print("Please consult a doctor for final diagnosis.\n")

        else:
            print("Test not found in the report.\n")

print("=== SIMPLE AI MEDICAL REPORT ANALYZER ===")

file_path = select_pdf()

if file_path == "":
    print("No PDF selected.")
else:
    report_text = extract_text(file_path)

    print("\n--- Extracted Text from PDF ---")
    print(report_text)

    found_tests = extract_tests(report_text)

    if len(found_tests) == 0:
        print("\nNo known medical tests found in the PDF.")
    else:
        df = analyze_tests(found_tests)

        print("\n=== ANALYSIS TABLE ===")
        print(df)

        chatbot(found_tests)
