# Initialize your Pyrogram client
app = Client("my_app")

# Define the source and destination chat IDs
source_chat_id = -1001234567890  # Replace with your source chat ID
destination_chat_id = -1009876543210  # Replace with your destination chat ID

# Forward messages from any chat to the destination chat
@app.on_message(filters.chat(source_chat_id))
def forward_message(client, message):
    client.forward_messages(destination_chat_id, message.chat.id, message.message_id)

# Forward messages from multiple chats to the destination chat
@app.on_message(filters.chat([source_chat_id, -1001111111111, -1002222222222]))  # Add additional chat IDs as needed
def forward_message(client, message):
    client.forward_messages(destination_chat_id, message.chat.id, message.message_id)

# Filter messages based on type or keywords
@app.on_message(filters.chat(source_chat_id) & (filters.photo | filters.document | filters.voice))
def filter_messages(client, message):
    # Add your filtering logic here
    # For example, you can check if the message contains a specific keyword
    if "keyword" in message.text:
        client.forward_messages(destination_chat_id, message.chat.id, message.message_id)

# Clone chats from source to destination
@app.on_message(filters.chat(source_chat_id))
def clone_chat(client, message):
    # Add your cloning logic here
    # For example, you can forward the entire chat history to the destination chat
    client.forward_messages(destination_chat_id, message.chat.id, message.message_id)

# Enable message duplicate filtering
@app.on_message(filters.chat(source_chat_id))
def filter_duplicates(client, message):
    # Add your duplicate filtering logic here
    # For example, you can keep track of message IDs and ignore duplicates
    if message.message_id not in processed_message_ids:
        client.forward_messages(destination_chat_id, message.chat.id, message.message_id)
        processed_message_ids.append(message.message_id)

# Start the Pyrogram client
app.run() 
