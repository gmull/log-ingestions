#!/user/bin/env python3

import re

# File path
file_path = "sampleLog.log"

# Regex for parsing log lines
regex = r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}-\d{4})\s+(\S+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\d+)\s+(\S+):(?:\s+\(([^)]+)\))?\s+(\S+):?\s*(.*)$'

# Read and parse the file
try:
    with open(file_path, 'r') as file:
        for line_number, log_entry in enumerate(file, start=1):
            log_entry = log_entry.strip()
            if not log_entry:  # Skip empty lines
                continue
            match = re.match(regex, log_entry)
            if match:
                print(f"Line {line_number}: Parsed successfully")
                print("  Timestamp:", match.group(1))
                print("  Hex Field 1:", match.group(2))
                print("  Log Level:", match.group(3))
                print("  Hex Field 2:", match.group(4))
                print("  PID:", match.group(5))
                print("  TID:", match.group(6))
                print("  Process Name:", match.group(7))
                print("  Subsystem:", match.group(8) or "N/A")  # Handle optional Subsystem
                print("  Category:", match.group(9))
                print("  Message:", match.group(10))
                print()
            else:
                print(f"Line {line_number}: Failed to parse")
                print("  Content:", log_entry)
                print()
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")