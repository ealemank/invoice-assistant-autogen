# filename: /Users/enrique/ai-experiments/invoice_assistant_autogen/test_invoice_assistant.py
import unittest
import os
from invoice_assistant import extract_data_from_invoice, read_invoices_and_generate_csv

class TestInvoiceAssistant(unittest.TestCase):
    def test_extract_data_from_invoice(self):
        # Test data for a single invoice
        invoice_content = """
        Invoice number: INV-001
        Project name: AI Development
        Total amount: $5000
        Hourly Rate: $100
        Due date: 2023-04-30
        Sales Representative: John Doe
        """
        expected_data = {
            "Total amount": "$5000",
            "Hourly Rate": "$100",
            "Invoice number": "INV-001",
            "Project name": "AI Development",
            "Due date": "2023-04-30",
            "Sales Representative": "John Doe"
        }
        extracted_data = extract_data_from_invoice(invoice_content)
        self.assertEqual(extracted_data, expected_data)

    def test_read_invoices_and_generate_csv(self):
        # Define the directory where the invoices are stored and the output CSV file path
        invoice_directory = '/Users/enrique/ai-experiments/invoice_assistant_autogen/invoices'
        output_csv_file = '/Users/enrique/ai-experiments/invoice_assistant_autogen/invoices_test.csv'
        
        # Run the function to process the invoices and generate the CSV
        read_invoices_and_generate_csv(invoice_directory, output_csv_file)
        
        # Check if the CSV file was created
        self.assertTrue(os.path.exists(output_csv_file))
        
        # Check if the CSV file contains the expected number of lines (2 invoices + 1 header)
        with open(output_csv_file, 'r') as csvfile:
            lines = csvfile.readlines()
            self.assertEqual(len(lines), 3)

if __name__ == '__main__':
    unittest.main()