import csv
import secrets
import subprocess
from pathlib import Path

# File Paths (adjust if needed)
cwd = Path.cwd()
data_folder = cwd / "drive" / "MyDrive" / "Colab Notebooks" / "data"
input_file = data_folder / "users_in.csv"
output_file = data_folder / "users_out.csv"

with open(input_file, "r") as file_input, open(output_file, "w", newline='') as file_output:
    reader = csv.DictReader(file_input)
    writer = csv.DictWriter(file_output, fieldnames=reader.fieldnames)
    writer.writeheader()

    for user in reader:
        user["password"] = secrets.token_hex(8)

        # Useradd command (modify for your system)
        useradd_cmd = [
            "useradd",  # Adjust path if needed
            "-c", user.get("real_name", ""),  # Handle missing 'real_name'
            "-m",
            "-G", "users",
            "-p", user["password"],
            user["username"]
        ]
        subprocess.run(useradd_cmd, check=True)
        writer.writerow(user)

'''File Paths: It's generally best to construct file paths more explicitly. I've created variables for the data 
folder, input file, and output file. Adjust these paths to match your actual file structure. 
CSV Writer Initialization: You need to create a csv.DictWriter object (writer) to write dictionaries to the CSV file. 
Use fieldnames=reader.fieldnames to ensure the output CSV has the same headers as the input. 
newline='' in open(): When writing to CSV files, it's recommended to use newline='' in the open() function to prevent 
potential issues with extra blank lines (especially on Windows). 
Handling Missing 'real_name': I've added user.get("real_name", "") to handle cases where the "real_name" field might be 
missing in the input CSV. This provides an empty string as a default. 
Writing User Data: The writer.writerow(user) line was inside the subprocess.run() block, causing only the 
last user to be written. I've moved it outside the block to write each user's data after the useradd command is 
executed. 
useradd Command: The path to the useradd command might vary depending on your system. I've removed the 
leading /sbin/ – you might need to adjust this if useradd is located elsewhere. 
Important Considerations: 
File Paths: Double-check that the file paths in the code accurately point to your input CSV file and the desired 
location for the output CSV. 
useradd Command: The useradd command and its options might differ slightly based on your operating system 
(Linux/macOS). Refer to the useradd documentation for your system if needed. 
Error Handling: The code currently uses check=True in subprocess.run(), which will raise an exception if the useradd 
command fails. You might want to add more robust error handling (e.g., using try...except) to gracefully handle 
potential issues during user creation.'''
