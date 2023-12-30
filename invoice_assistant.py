# filename: /Users/enrique/ai-experiments/invoice_assistant_autogen/invoice_assistant.py
import os
import re
import csv
from typing import List, Dict

# Define the data points to be extracted from the invoices
data_points = ["Total amount", "Hourly Rate", "Invoice number", "Project name", "Due date", "Sales Representative"]

def extract_data_from_invoice(invoice_content: str) -> Dict[str, str]:
    """
    Extracts the relevant data fields from the invoice content.
    """
    extracted_data = {}
    for field in data_points:
        # Create a regex pattern to find the data field and capture the value after it
        pattern = re.compile(rf"{field}:\s*(.+)")
        match = pattern.search(invoice_content)
        if match:
            extracted_data[field] = match.group(1).strip()
        else:
            extracted_data[field] = ""  # If the field is not found, leave it empty
    return extracted_data

def read_invoices_and_generate_csv(invoice_dir: str, output_csv: str):
    """
    Reads all invoice files from the given directory, extracts data, and writes it to a CSV file.
    """
    # Create a list to hold all extracted invoice data
    all_invoices_data = []

    # List all files in the invoice directory
    for filename in os.listdir(invoice_dir):
        if filename.startswith("invoice") and filename.endswith(".txt"):
            with open(os.path.join(invoice_dir, filename), 'r') as file:
                content = file.read()
                invoice_data = extract_data_from_invoice(content)
                all_invoices_data.append(invoice_data)

    # Write the extracted data to a CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data_points)
        writer.writeheader()
        for invoice_data in all_invoices_data:
            writer.writerow(invoice_data)

# Define the directory where the invoices are stored and the output CSV file path
invoice_directory = '/Users/enrique/ai-experiments/invoice_assistant_autogen/invoices'
output_csv_file = '/Users/enrique/ai-experiments/invoice_assistant_autogen/invoices.csv'

# Call the function to process the invoices and generate the CSV
read_invoices_and_generate_csv(invoice_directory, output_csv_file)