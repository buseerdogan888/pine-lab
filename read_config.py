import json

# Load the configuration file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Access configuration settings
data_directory = config['data_directory']
log_level = config['log_level']
max_retries = config['max_retries']

# Print the configuration settings
print(f"Data Directory: {data_directory}")
print(f"Log Level: {log_level}")
print(f"Max Retries: {max_retries}")
