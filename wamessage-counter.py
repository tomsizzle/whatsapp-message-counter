import sys
import re

# Print welcome message
print("\nA warm welcome to the WhatsApp chat message counter.")
print("This app processes a .txt file of WhatsApp chat history and counts the messages for each participant.\n")

# Open the chat file
try:
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        lines = f.readlines()
except IndexError:
    print("Please provide a .txt file as an argument.")
    sys.exit(1)

# Initialize variables
messages = 0
ind_mes = {}

# Regular expression to detect messages in the WhatsApp format
message_pattern = re.compile(r'^\[\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2}\] (.*?):')

# Process each line
for line in lines:
    match = message_pattern.match(line)
    if match:
        participant = match.group(1).strip()  # Extract participant name
        if participant in ind_mes:
            ind_mes[participant] += 1
        else:
            ind_mes[participant] = 1
        messages += 1

# Output results
print(f"There are {messages} messages between you and the group.")
for participant, count in ind_mes.items():
    print(f"{participant} sent {count} messages.")
import sys
import re

# Print welcome message
print("\nA warm welcome to the WhatsApp chat message counter.")
print("This app processes a .txt file of WhatsApp chat history and counts the messages for each participant.\n")

# Open the chat file
try:
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        lines = f.readlines()
except IndexError:
    print("Please provide a .txt file as an argument.")
    sys.exit(1)

# Initialize variables
messages = 0
ind_mes = {}

# Regular expression to detect messages in the WhatsApp format
message_pattern = re.compile(r'^\[\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2}\] (.*?):')

# Process each line
for line in lines:
    match = message_pattern.match(line)
    if match:
        participant = match.group(1).strip()  # Extract participant name
        if participant in ind_mes:
            ind_mes[participant] += 1
        else:
            ind_mes[participant] = 1
        messages += 1

# Output results
print(f"There are {messages} messages between you and the group.")
for participant, count in ind_mes.items():
    print(f"{participant} sent {count} messages.")
