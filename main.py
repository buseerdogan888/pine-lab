import json

# Load configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Access configuration settings
data_directory = config['data_directory']
log_level = config['log_level']
max_retries = config['max_retries']

print(f"Data Directory: {data_directory}")
print(f"Log Level: {log_level}")
print(f"Max Retries: {max_retries}")

# Your application logic here
# For example, using the data_directory to read files
import os
import pandas as pd

# Process each CSV file in the data directory
for filename in os.listdir(data_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_directory, filename)
        data = pd.read_csv(file_path)
        # Process data (example: print the first few rows)
        print(f"Processing {filename}")
        print(data.head())
