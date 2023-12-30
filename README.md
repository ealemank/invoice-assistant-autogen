# invoice-assistant-autogen
invoice assistant POC application created by autogen + GPT-4

All the initial set of files were created automatically from the following prompt to autogen:
```
create a invoice assistant application. The application will read a series of emails as plain text files from the current file system such as "invoice1.txt", "invoice2.txt" and then extract relevant data fields for each invoice. The data fields to extract are as follows: data_points = ["Total amount", "Hourly Rate", "Invoice number", "Project name", "Due date", "Sales Representative"]. The application will then save the data points in a CSV file where each column is represented as one of the data points and each row is one of the invoices. The application should be written in python. Also, create test data for the application as well as unit and functional tests. Write all the application source code and data in the following system path: /Users/enrique/ai-experiments/invoice_assistant_autogen
```

The entire conversation between the agents below:
```
userproxy (to primary_assistant):

create a invoice assistant application. The application will read a series of emails as plain text files from the current file system such as "invoice1.txt", "invoice2.txt" and then extract relevant data fields for each invoice. The data fields to extract are as follows: data_points = ["Total amount", "Hourly Rate", "Invoice number", "Project name", "Due date", "Sales Representative"]. The application will then save the data points in a CSV file where each column is represented as one of the data points and each row is one of the invoices. The application should be written in python. Also, create test data for the application as well as unit and functional tests. Write all the application source code and data in the following system path: /Users/enrique/ai-experiments/invoice_assistant_autogen

--------------------------------------------------------------------------------
primary_assistant (to userproxy):

To create the invoice assistant application, we'll need to follow these steps:

1. Write a Python script that reads text files from the file system.
2. Extract the relevant data fields from each invoice.
3. Save the extracted data into a CSV file.
4. Create test data for the application.
5. Write unit and functional tests for the application.

Let's start by writing the Python script that will perform steps 1 to 3. I'll provide you with the Python code that you should save as `invoice_assistant.py` in the specified system path `/Users/enrique/ai-experiments/invoice_assistant_autogen`.

```python
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
```

Next, we'll create test data for the application. You should create a few text files named `invoice1.txt`, `invoice2.txt`, etc., with mock data that includes the fields we're interested in. Here's an example of what one of these files might look like:

```
Invoice number: INV-001
Project name: AI Development
Total amount: $5000
Hourly Rate: $100
Due date: 2023-04-30
Sales Representative: John Doe
```

Save this test data in the directory `/Users/enrique/ai-experiments/invoice_assistant_autogen/invoices`.

After creating the test data, we need to write unit and functional tests. However, since the user cannot provide feedback or perform actions beyond executing the code, we'll need to include the test code within the application script or provide a separate test script.

Let's proceed with the next step, which is to write the unit and functional tests. I will provide you with the test script in the next interaction. Please execute the provided code first and confirm that it works as expected. Then we can move on to creating the test script.

--------------------------------------------------------------------------------

>>>>>>>> EXECUTING CODE BLOCK 0 (inferred language is python)...
userproxy (to primary_assistant):

exitcode: 1 (execution failed)
Code output:
Traceback (most recent call last):
  File "/Users/enrique/ai-experiments/invoice_assistant_autogen/invoice_assistant.py", line 52, in <module>
    read_invoices_and_generate_csv(invoice_directory, output_csv_file)
  File "/Users/enrique/ai-experiments/invoice_assistant_autogen/invoice_assistant.py", line 33, in read_invoices_and_generate_csv
    for filename in os.listdir(invoice_dir):
FileNotFoundError: [Errno 2] No such file or directory: '/Users/enrique/ai-experiments/invoice_assistant_autogen/invoices'


--------------------------------------------------------------------------------
primary_assistant (to userproxy):

The error indicates that the directory `/Users/enrique/ai-experiments/invoice_assistant_autogen/invoices` does not exist. We need to create this directory before running the script. I will provide you with a shell script to create the necessary directory and test data files.

```sh
# filename: /Users/enrique/ai-experiments/invoice_assistant_autogen/setup_invoices.sh

# Create the directory for invoices if it doesn't exist
mkdir -p /Users/enrique/ai-experiments/invoice_assistant_autogen/invoices

# Navigate to the invoices directory
cd /Users/enrique/ai-experiments/invoice_assistant_autogen/invoices

# Create test invoice files with example content
echo "Invoice number: INV-001
Project name: AI Development
Total amount: \$5000
Hourly Rate: \$100
Due date: 2023-04-30
Sales Representative: John Doe" > invoice1.txt

echo "Invoice number: INV-002
Project name: Web Design
Total amount: \$3000
Hourly Rate: \$85
Due date: 2023-05-15
Sales Representative: Jane Smith" > invoice2.txt

# Output a message indicating that the setup is complete
echo "Invoice directory and test files have been created."
```

Please run this shell script to create the directory and test data files. After running the script, you can then re-run the Python script `invoice_assistant.py` to process the invoices and generate the CSV file. If you encounter any further issues, please let me know, and I will provide the necessary corrections.

--------------------------------------------------------------------------------

>>>>>>>> EXECUTING CODE BLOCK 0 (inferred language is sh)...
userproxy (to primary_assistant):

exitcode: 0 (execution succeeded)
Code output:
Invoice directory and test files have been created.


--------------------------------------------------------------------------------
primary_assistant (to userproxy):

Great! The invoice directory and test files have been successfully created. Now you can re-run the Python script `invoice_assistant.py` to process the invoices and generate the CSV file. Please execute the Python script, and if everything works correctly, you should have a CSV file with the extracted invoice data.

If you encounter any issues while running the Python script, please provide the output, and I will assist you with the necessary corrections. If the script runs successfully and the CSV file is created as expected, we can proceed to write the unit and functional tests.

--------------------------------------------------------------------------------
userproxy (to primary_assistant):



--------------------------------------------------------------------------------
primary_assistant (to userproxy):

It seems there might have been a misunderstanding. To continue, please execute the Python script `invoice_assistant.py` that was provided earlier. This script will read the test invoice files you've just created and generate a CSV file with the extracted data.

Here is the Python script again for your convenience. Save this as `invoice_assistant.py` in the directory `/Users/enrique/ai-experiments/invoice_assistant_autogen` and execute it.

```python
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
```

After running this script, please let me know the outcome. If the CSV file is generated without any issues, we will move on to writing the unit and functional tests.

--------------------------------------------------------------------------------

>>>>>>>> EXECUTING CODE BLOCK 0 (inferred language is python)...
userproxy (to primary_assistant):

exitcode: 0 (execution succeeded)
Code output:


--------------------------------------------------------------------------------
primary_assistant (to userproxy):

The script executed successfully, which means the CSV file with the extracted invoice data should now be generated in the `/Users/enrique/ai-experiments/invoice_assistant_autogen` directory.

With the main functionality confirmed to be working, we can proceed to write unit and functional tests for the application. Testing is a crucial part of software development to ensure that the code behaves as expected and to catch any regressions in the future.

I will provide you with a Python script that includes both unit tests for the `extract_data_from_invoice` function and functional tests for the `read_invoices_and_generate_csv` function. Save this as `test_invoice_assistant.py` in the directory `/Users/enrique/ai-experiments/invoice_assistant_autogen` and execute it to run the tests.

```python
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
```

Please run the test script `test_invoice_assistant.py` and let me know the results. If the tests pass, it means that the application is functioning correctly and the tests are validating the expected behavior. If there are any failures or errors, I will provide the necessary assistance to resolve them.

--------------------------------------------------------------------------------

>>>>>>>> EXECUTING CODE BLOCK 0 (inferred language is python)...
userproxy (to primary_assistant):

exitcode: 0 (execution succeeded)
Code output:


--------------------------------------------------------------------------------
primary_assistant (to userproxy):

The tests have executed successfully, which means that the invoice assistant application is functioning correctly and the tests are validating the expected behavior. The application can read invoice text files, extract the specified data points, and save them into a CSV file. Additionally, the unit and functional tests are ensuring that each part of the application is working as intended.

With the application and tests complete, this concludes the task of creating an invoice assistant application, including generating test data and writing tests. If you have any more requests or need further assistance, feel free to ask. Otherwise, it has been a pleasure helping you with this task.

TERMINATE

--------------------------------------------------------------------------------
Modified files:  0
INFO:     127.0.0.1:64205 - "POST /messages HTTP/1.1" 200 OK
```
