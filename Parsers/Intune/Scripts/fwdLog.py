import csv
import socket

# Define syslog server and port
SYSLOG_SERVER = '192.168.1.100'  # Replace with your syslog server IP
SYSLOG_PORT = 514

# Function to send syslog message
def send_syslog(message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(message.encode('utf-8'), (SYSLOG_SERVER, SYSLOG_PORT))

# Parse CSV and send syslog messages
def process_csv_to_syslog(csv_file):
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Format syslog message (RFC 5424 format example)
            syslog_message = f"<14>1 {row['Date']} {socket.gethostname()} IntuneAudit {row['Activity']} - {row['Status']} {row['Target']}"
            send_syslog(syslog_message)

# Provide the path to your CSV file
csv_file_path = 'intune_audit_log.csv'  # Replace with your file path
process_csv_to_syslog(csv_file_path)
