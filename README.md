# WhatsApp Message Counter
This repo provides a Python and Node scipt to count the number of messages sent by each participant in a WhatsApp chat. The tool processes a .txt file of WhatsApp chat history and outputs the total number of messages as well as a breakdown of messages sent by each participant.

## How to use
1. Go to the WhatsApp chat you wish to count the messages in. 
2. Export the chat as a .txt file (i.e. `whatsapp_chat.txt`) and save it in the same directory as this repo.
4. Run with Python or Node:

```bash
python3 wamessage-counter.py whatsapp_chat.txt
```

```bash
node wamessage-counter.py whatsapp_chat.txt
```

## Example output

```bash
❯ node wamessage-counter.js whatsapp_chat.txt

A warm welcome to the WhatsApp chat message counter.
This app processes a .txt file of WhatsApp chat history and counts the messages for each participant.

There are 425 messages in the chat history.
John Doe sent 3 messages.
Jane Smith sent 45 messages.
Alice Johnson sent 15 messages.
Bob Brown sent 52 messages.
Charlie Davis sent 40 messages.
David Evans sent 47 messages.
Eve Foster sent 33 messages.
Grace Hall sent 69 messages.
Henry King sent 20 messages.
Ivy Lewis sent 66 messages.
Jack Miller sent 22 messages.
Liam Nelson sent 6 messages.
Mia Owens sent 7 messages.
```